#!/usr/bin/env python

import json
import StringIO
import pycurl
import re
import fire
from glob import glob
from githubAPI import github_api_token
from datetime import datetime as dt
from collections import namedtuple
import pytz

RX_LINKS = re.compile('^Link: <(.*?)>; rel="next", <(.*?)>; rel="last"')
RX_RELEASE = re.compile('CMSSW_(\d+)_(\d+)_(\d+)(_pre[0-9]+)*(_cand[0-9]+)*(_patch[0-9]+)*')
RX_COMMIT = re.compile(".*\#(\d{0,5})( from.*)")
RX_SINGLECOMMIT = re.compile(".*cmssw/pull/(\d{0,5})")
RX_AUTHOR = re.compile("(.*)(@[a-zA-Z-_0-9]+)")
RX_COMPARE = re.compile("(https://github.*compare.*\.\.\..*)")

Release = namedtuple("Release", ["major", "minor", "subminor", "pre", "cand", "patch"])

DEBUG = True

class tcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def head(title, release):
    ret = "---\n"
    ret += "layout: post\n"
    ret += 'title:  "{title}"\n'.format(title=title)
    ret += "date:   {now}\n".format(now=dt.now(tz=pytz.timezone('Europe/Zurich')).strftime("%Y-%m-%d %H:%M:%S %z"))
    ret += "categories: cmssw\n"
    ret += "relmajor: {major}\n".format(major=release.major)
    ret += "relminor: {minor}\n".format(minor=release.minor)
    ret += "relsubminor: {subminor}\n".format(subminor=release.subminor)
    if release.pre:
        ret += "relpre: {pre}\n".format(pre=release.pre)
    if release.cand:
        ret += "relcand: {cand}\n".format(cand=release.cand)
    if release.patch:
        ret += "relpatch: {patch}\n".format(patch=release.patch)
    ret += "---\n\n"
    return ret

def extractPRnumbers(release_notes):
    prs = [re.match(RX_SINGLECOMMIT, l).group(1) for l in release_notes.split('\n') if re.match(RX_SINGLECOMMIT, l)]
    if DEBUG:
       for pr in prs:
          print "PR: ", pr
    return prs

def checkRateLimits(header):
    head = {}
    hh = [h.split(':') for h in header.split('\n')]
    for o in hh:
        if len(o) > 1:
            head.setdefault(o[0],o[1].replace('\r', ''))
    if DEBUG:
        print head
    if int(head['X-RateLimit-Remaining']) == 0:
        print "Rate Limits exceeded"
        print "X-RateLimit-Limit", head['X-RateLimit-Limit']
        print "X-RateLimit-Reset", head['X-RateLimit-Reset']
        print "X-RateLimit-Remaining", head['X-RateLimit-Remaining']
        import sys
        sys.exit(1)

def getReleasesNotes(selected_releases_regexp):
  next_link = 'first'
  last_link = 'last'
  current_link = "https://api.github.com/repos/cms-sw/cmssw/releases"
  pr_current_link = "https://api.github.com/repos/cms-sw/cmssw/pulls"
  response = StringIO.StringIO()
  pr_response = StringIO.StringIO()
  header   = StringIO.StringIO()
  pr_header   = StringIO.StringIO()
  c = pycurl.Curl()
  c.setopt(pycurl.URL, current_link)
  c.setopt(pycurl.WRITEFUNCTION, response.write)
  c.setopt(pycurl.HEADERFUNCTION, header.write)
  c.setopt(pycurl.HTTPHEADER, ['Authorization: token %s' % github_api_token])
  cpr = pycurl.Curl()
  cpr.setopt(pycurl.URL, pr_current_link)
  cpr.setopt(pycurl.WRITEFUNCTION, pr_response.write)
  cpr.setopt(pycurl.WRITEFUNCTION, pr_response.write)
  cpr.setopt(pycurl.HEADERFUNCTION, pr_header.write)
  counter = -1
  notes = []

  while next_link != last_link:
    c.perform()

    releases = json.loads(response.getvalue())
    headers = header.getvalue()
    checkRateLimits(headers)
    for line in headers.split('\n'):
       m = re.match(RX_LINKS, line)
       if m:
          next_link = m.group(1)
          last_link = m.group(2)
          c.setopt(pycurl.URL, next_link)
          print '%s, [%s,%s]' % (line, next_link, last_link)

    for i in range(len(releases)):
      counter += 1
      rel_numbers = re.match(RX_RELEASE, releases[i]['name'])
      if rel_numbers and re.match(selected_releases_regexp, releases[i]['name']):
        # Check if we locally already have release notes for this specific release. If so, ignore it to avoid duplication.
        if len(glob("*{release}*".format(release=releases[i]['name'].replace('CMSSW_', '')))):
            print tcolors.BOLD + tcolors.WARNING + "Skipping release {release}".format(release=releases[i]['name']) + tcolors.ENDC
            continue
        release_notes = re.sub(RX_COMMIT, '\\n1. [\\1](http://github.com/cms-sw/cmssw/pull/\\1){:target="_blank"} \\2', releases[i]['body'])
        release_notes = re.sub(RX_COMPARE, '[compare to previous](\\1)\n\n', release_notes)
        release_notes = re.sub(RX_AUTHOR, '\\1**\\2**', release_notes)
        if DEBUG:
            print release_notes.encode('ascii', 'replace')
        prs = extractPRnumbers(release_notes)
        for pr in prs:
            cpr.setopt(pycurl.URL, pr_current_link + "/%s" % pr)
            cpr.setopt(pycurl.HTTPHEADER, ['Authorization: token %s' % github_api_token])
            cpr.perform()
            checkRateLimits(pr_header.getvalue())
            commit = json.loads(pr_response.getvalue())
            if commit.has_key('created_at') and commit.has_key('merged_at'):
                release_notes = re.sub('\[%s\](.*)' % pr, '[%s]\\1 created: %s merged: %s' % (pr, commit['created_at'], commit['merged_at']), release_notes)
            pr_response.seek(0)
            pr_response.truncate()
            pr_header.seek(0)
            pr_header.truncate()
        notes.append([Release(int(rel_numbers.group(1)),
                              int(rel_numbers.group(2)),
                              int(rel_numbers.group(3)),
                              rel_numbers.group(4),
                              rel_numbers.group(5),
                              rel_numbers.group(6)),
                              releases[i]['name'],
                              release_notes
                     ])
    response.seek(0)
    response.truncate()
    header.seek(0)
    header.truncate()

  current = ""
  out_rel = None
  notes = sorted(notes, key = lambda x: (x[0].major, x[0].minor, x[0].subminor, x[0].pre, x[0].patch), reverse=True)
  for r, release_name, release_notes in notes:
    new_current = "{major}_{minor}_{subminor}{pre}{cand}{patch}".format(major=r.major,
                                                                        minor=r.minor,
                                                                        subminor=r.subminor,
                                                                        pre=r.pre if r.pre else '',
                                                                        cand=r.cand if r.cand else '',
                                                                        patch=r.patch if r.patch else '')
    if new_current != current:
      if out_rel:
        out_rel.close()
      out_rel = open("{date}-ReleaseNotes_{release}.md".format(date=dt.now().strftime('%Y-%m-%d'),release=new_current), 'w')
      out_rel.write(head(new_current, r))
      current = new_current
    try:
      out_rel.write('# %s\n%s' % (release_name.encode('ascii', 'replace'), release_notes.encode('ascii', 'replace')))
    except:
      pass

if __name__ == '__main__':
  fire.Fire(getReleasesNotes)
