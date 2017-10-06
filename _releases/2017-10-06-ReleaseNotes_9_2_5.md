---
layout: post
title:  "9_2_5"
date:   2017-10-06 10:52:06 +0200
categories: cmssw
relmajor: 9
relminor: 2
relsubminor: 5
---

# CMSSW_9_2_5
#### Changes since CMSSW_9_2_4:
[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_9_2_4...CMSSW_9_2_5)



1. [19581](http://github.com/cms-sw/cmssw/pull/19581){:target="_blank"}  from **@Martin-Grunewald**: HLTPrescaler work (92X) `hlt`  created: 2017-07-06T08:44:17Z merged: 2017-07-06T20:58:39Z

1. [19545](http://github.com/cms-sw/cmssw/pull/19545){:target="_blank"}  from **@JanFSchulte**: Allow TrackClusterRemover to work on either pixel or strip clusters alone (92X backport) `reconstruction`  created: 2017-07-04T14:44:55Z merged: 2017-07-06T16:03:37Z

1. [19540](http://github.com/cms-sw/cmssw/pull/19540){:target="_blank"}  from **@hroskes**: Tracker alignment validation das client `alca`  created: 2017-07-04T12:32:47Z merged: 2017-07-06T20:58:50Z

1. [19516](http://github.com/cms-sw/cmssw/pull/19516){:target="_blank"}  from **@ggovi**: IOV range returned ordered by since `db`  created: 2017-07-03T09:57:57Z merged: 2017-07-06T16:04:57Z

1. [19511](http://github.com/cms-sw/cmssw/pull/19511){:target="_blank"}  from **@Martin-Grunewald**: Do not throw on non-matching triggers in ecalTrgHLT (92X) `alca`  created: 2017-07-03T08:35:20Z merged: 2017-07-06T16:04:04Z

1. [19497](http://github.com/cms-sw/cmssw/pull/19497){:target="_blank"}  from **@mschrode**: Add scripts to read and write APE from/to ASCII and db files `alca`  created: 2017-06-30T16:24:09Z merged: 2017-07-06T16:02:22Z

1. [19494](http://github.com/cms-sw/cmssw/pull/19494){:target="_blank"}  from **@apana**: pr92x L1T fix L1T_ZeroBias not firing in RelVal MC. `l1`  created: 2017-06-30T12:47:25Z merged: 2017-07-06T16:12:48Z

1. [19482](http://github.com/cms-sw/cmssw/pull/19482){:target="_blank"}  from **@makortel**: Add track selection MVA plots to tracking DQM (92X) `dqm`  `reconstruction`  created: 2017-06-29T14:46:09Z merged: 2017-07-06T20:55:39Z

1. [19473](http://github.com/cms-sw/cmssw/pull/19473){:target="_blank"}  from **@cms-sw**: make sure that workflow commands are written with all the quotes `pdmv`  `upgrade`  created: 2017-06-29T11:24:04Z merged: 2017-07-06T16:01:58Z

1. [19464](http://github.com/cms-sw/cmssw/pull/19464){:target="_blank"}  from **@apana**: pr92/93x L1T allow correlations from other than bx=0 (backport of #19453) `l1`  created: 2017-06-28T17:45:58Z merged: 2017-07-06T16:09:28Z

1. [19448](http://github.com/cms-sw/cmssw/pull/19448){:target="_blank"}  from **@kmcdermo**: Combined backport of PR #19205 and #19404: ootPhotons in miniAOD from AOD from either 92X or 80X inputs `analysis`  `reconstruction`  created: 2017-06-27T14:42:22Z merged: 2017-07-06T20:55:55Z

1. [19438](http://github.com/cms-sw/cmssw/pull/19438){:target="_blank"}  from **@makortel**: Update online beamspot to quadruplet-only and rescale track uncertainties (92X) `dqm`  `reconstruction`  created: 2017-06-27T07:49:36Z merged: 2017-07-06T16:01:48Z

1. [19434](http://github.com/cms-sw/cmssw/pull/19434){:target="_blank"}  from **@forthommel**:  CTPPS: fixes for 2017 diamond data taking operations (backport to 9_2_X) `dqm`  `reconstruction`  created: 2017-06-27T07:05:23Z merged: 2017-07-06T16:00:32Z

1. [19433](http://github.com/cms-sw/cmssw/pull/19433){:target="_blank"}  from **@mmusich**: [92X] add SiStripCalMinBias to the upgrade phase-I samples (backport of #19430) `pdmv`  `upgrade`  created: 2017-06-27T06:42:54Z merged: 2017-07-06T16:00:45Z

1. [19416](http://github.com/cms-sw/cmssw/pull/19416){:target="_blank"}  from **@ianna**: Move Geometry Aligner Header `alca`  `geometry`  created: 2017-06-23T14:44:48Z merged: 2017-06-26T08:26:51Z

1. [19375](http://github.com/cms-sw/cmssw/pull/19375){:target="_blank"}  from **@Sam-Harper**: Adding Cross Trigger Support to E/gamma TnP DQM `dqm`  created: 2017-06-19T20:58:58Z merged: 2017-06-26T08:28:36Z

#### CMSDIST Changes between Tags REL/CMSSW_9_2_4/slc6_amd64_gcc530 and REL/CMSSW_9_2_5/slc6_amd64_gcc530:
[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_9_2_4/slc6_amd64_gcc530...REL/CMSSW_9_2_5/slc6_amd64_gcc530)



1. [3142](http://github.com/cms-sw/cmssw/pull/3142){:target="_blank"}  from **@vkuznet**: New version fixed acess to RunRegistry data-service created: 2014-04-01T15:46:47Z merged: None

1. [3137](http://github.com/cms-sw/cmssw/pull/3137){:target="_blank"}  from **@vkuznet**: New version of dasgoclient to fix run splitting from DBS output created: 2014-04-01T13:46:21Z merged: 2014-04-02T12:03:47Z

1. [3124](http://github.com/cms-sw/cmssw/pull/3124){:target="_blank"}  from **@davidlange6**: adding hyperas and hyper opt python tools created: 2014-03-31T20:24:28Z merged: 2014-03-31T20:28:09Z
