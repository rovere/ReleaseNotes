---
layout: post
title:  "7_1_0"
date:   2017-10-06 17:17:31 +0200
categories: cmssw
relmajor: 7
relminor: 1
relsubminor: 0
---

# CMSSW_7_1_0
#### Changes since CMSSW_7_1_0_pre9:

1. [4335](http://github.com/cms-sw/cmssw/pull/4335){:target="_blank"}  from **@ktf**: Revert classversion. `analysis`  created: 2014-06-21T13:17:43Z merged: 2014-06-21T13:18:47Z

1. [4334](http://github.com/cms-sw/cmssw/pull/4334){:target="_blank"}  from **@ktf**: Fix cout. created: 2014-06-21T09:38:32Z merged: 2014-06-21T09:39:10Z

1. [4316](http://github.com/cms-sw/cmssw/pull/4316){:target="_blank"}  from **@ktf**: Fix forward port 71x `analysis`  `core`  `operations`  `reconstruction`  `simulation`  created: 2014-06-19T15:53:25Z merged: 2014-06-20T21:13:21Z

1. [4333](http://github.com/cms-sw/cmssw/pull/4333){:target="_blank"}  from **@civanch**: Fix hf sl sampling factor `simulation`  created: 2014-06-20T15:32:51Z merged: 2014-06-20T15:48:01Z

1. [4305](http://github.com/cms-sw/cmssw/pull/4305){:target="_blank"}  from **@diguida**: GTs in autoCond for 710 `alca`  created: 2014-06-18T13:55:01Z merged: 2014-06-20T12:07:33Z

1. [4327](http://github.com/cms-sw/cmssw/pull/4327){:target="_blank"}  from **@ktf**: Backport TLS fixes from #4293 to CMSSW_7_1_X `alca`  `db`  `reconstruction`  created: 2014-06-20T07:52:04Z merged: 2014-06-20T09:52:16Z

1. [4302](http://github.com/cms-sw/cmssw/pull/4302){:target="_blank"}  from **@civanch**: Alternative EM physics for heavy exotics  `simulation`  created: 2014-06-18T10:42:44Z merged: 2014-06-19T07:32:01Z

1. [4304](http://github.com/cms-sw/cmssw/pull/4304){:target="_blank"}  from **@deguio**: handle correctly the ME which are not TH1 [int,string,float] `dqm`  created: 2014-06-18T12:52:32Z merged: 2014-06-19T07:27:11Z

1. [4160](http://github.com/cms-sw/cmssw/pull/4160){:target="_blank"}  from **@Dr15Jones**: removed unnecessary mutables from CondFormats/L1TObjects `alca`  `db`  `l1`  created: 2014-06-07T22:24:17Z merged: 2014-06-18T16:27:38Z

1. [4264](http://github.com/cms-sw/cmssw/pull/4264){:target="_blank"}  from **@cms-l1t-offline**: L1t global bugfixes for 7 1 x `alca`  `db`  `l1`  created: 2014-06-16T09:04:15Z merged: 2014-06-18T12:45:46Z

1. [4221](http://github.com/cms-sw/cmssw/pull/4221){:target="_blank"}  from **@jpavel**: removed duplicated definitions of EDProducers (for 71x) `reconstruction`  created: 2014-06-12T13:57:32Z merged: 2014-06-18T06:36:44Z

1. [4245](http://github.com/cms-sw/cmssw/pull/4245){:target="_blank"}  from **@srimanob**: Fast sim for mixing71 x fix1 `fastsim`  `operations`  created: 2014-06-14T14:41:04Z merged: 2014-06-17T16:50:15Z

1. [4266](http://github.com/cms-sw/cmssw/pull/4266){:target="_blank"}  from **@cms-l1t-offline**: L1t calorimeter bugfixes for 7 1 x created: 2014-06-16T10:18:02Z merged: 2014-06-17T16:49:41Z

1. [4288](http://github.com/cms-sw/cmssw/pull/4288){:target="_blank"}  from **@civanch**: Fix for inf loop neutron bgr sim `simulation`  created: 2014-06-17T10:27:43Z merged: 2014-06-17T16:48:41Z

1. [4280](http://github.com/cms-sw/cmssw/pull/4280){:target="_blank"}  from **@mileva**: Unused maps and lines removed from RPCDidisValid `dqm`  created: 2014-06-16T20:14:31Z merged: 2014-06-17T16:48:29Z

1. [4272](http://github.com/cms-sw/cmssw/pull/4272){:target="_blank"}  from **@mgalanti**: Bugfix: assign correct FED IDs if some FEDs are not in the DAQ `dqm`  created: 2014-06-16T15:28:46Z merged: 2014-06-17T16:48:16Z

1. [4270](http://github.com/cms-sw/cmssw/pull/4270){:target="_blank"}  from **@civanch**: New hf sl 2011 2012 `simulation`  created: 2014-06-16T13:13:29Z merged: 2014-06-17T16:47:59Z

1. [4268](http://github.com/cms-sw/cmssw/pull/4268){:target="_blank"}  from **@mommsen**: Add new FED IDs for future uTCA FEDs `daq`  created: 2014-06-16T11:25:11Z merged: 2014-06-17T16:47:20Z

1. [4224](http://github.com/cms-sw/cmssw/pull/4224){:target="_blank"}  from **@sarafiorendi**: Split old mmtkfilter in a vertex producer and a filter `hlt`  created: 2014-06-12T17:09:27Z merged: 2014-06-17T16:47:04Z

1. [4254](http://github.com/cms-sw/cmssw/pull/4254){:target="_blank"}  from **@davidlange6**: Remove hoarding of sim tracks `dqm`  `generators`  `reconstruction`  created: 2014-06-15T18:53:22Z merged: 2014-06-16T17:11:09Z

1. [4263](http://github.com/cms-sw/cmssw/pull/4263){:target="_blank"}  from **@battibass**: Trivial Fix for VertexFromTrackProducer `hlt`  created: 2014-06-16T08:43:05Z merged: 2014-06-16T11:42:25Z

1. [4257](http://github.com/cms-sw/cmssw/pull/4257){:target="_blank"}  from **@fwyzard**: FastTimerService: avoid race condition across different threads when updating summary information `hlt`  created: 2014-06-15T21:11:48Z merged: 2014-06-16T11:41:55Z

1. [4223](http://github.com/cms-sw/cmssw/pull/4223){:target="_blank"}  from **@Dr15Jones**: Removed depricated KfComponentsHolder::setup function `alca`  `reconstruction`  created: 2014-06-12T15:13:23Z merged: 2014-06-16T11:41:15Z

1. [4261](http://github.com/cms-sw/cmssw/pull/4261){:target="_blank"}  from **@ktf**: Make sure files are at CERN also when specifying multiple runs. `operations`  created: 2014-06-16T07:57:19Z merged: 2014-06-16T08:16:10Z

1. [4244](http://github.com/cms-sw/cmssw/pull/4244){:target="_blank"}  from **@alja**: cmsShow script: fix warning about missing version.txt `visualization`  created: 2014-06-14T14:27:49Z merged: 2014-06-16T06:12:48Z

1. [4209](http://github.com/cms-sw/cmssw/pull/4209){:target="_blank"}  from **@lgray**: demote message status of gap-region linking bug `reconstruction`  created: 2014-06-11T12:58:25Z merged: 2014-06-15T14:30:14Z

1. [4233](http://github.com/cms-sw/cmssw/pull/4233){:target="_blank"}  from **@mbluj**: Bug fix to an "OR" logic in tau discrimination `reconstruction`  created: 2014-06-13T11:49:40Z merged: 2014-06-15T14:29:22Z

1. [4226](http://github.com/cms-sw/cmssw/pull/4226){:target="_blank"}  from **@ericvaandering**: 71x improve lumilist `core`  created: 2014-06-12T21:05:33Z merged: 2014-06-15T14:28:45Z

1. [4216](http://github.com/cms-sw/cmssw/pull/4216){:target="_blank"}  from **@ahinzmann**: Make the magnetic field record for the PixelCPEGeneric configurable `reconstruction`  created: 2014-06-12T08:31:05Z merged: 2014-06-15T14:27:56Z

1. [4210](http://github.com/cms-sw/cmssw/pull/4210){:target="_blank"}  from **@smorovic**: EvF updates `daq`  `dqm`  created: 2014-06-11T15:28:20Z merged: 2014-06-15T14:27:05Z

1. [4207](http://github.com/cms-sw/cmssw/pull/4207){:target="_blank"}  from **@nclopezo**: Forward port CMSSW_7_0_X into CMSSW_7_1_X (Fixed Conflicts) `operations`  created: 2014-06-11T11:55:37Z merged: 2014-06-15T14:25:46Z

1. [4197](http://github.com/cms-sw/cmssw/pull/4197){:target="_blank"}  from **@giamman**: New fastsim event content for pileup `fastsim`  created: 2014-06-10T19:43:15Z merged: 2014-06-15T14:24:53Z

1. [4179](http://github.com/cms-sw/cmssw/pull/4179){:target="_blank"}  from **@VinInn**: Global muon refitter and TrackTransformer `reconstruction`  created: 2014-06-10T10:10:47Z merged: 2014-06-15T14:23:34Z

1. [4140](http://github.com/cms-sw/cmssw/pull/4140){:target="_blank"}  from **@cms-btv-pog**: remove unused variable `reconstruction`  created: 2014-06-06T10:07:39Z merged: 2014-06-15T14:23:14Z

1. [3991](http://github.com/cms-sw/cmssw/pull/3991){:target="_blank"}  from **@Dr15Jones**: Make GctRawToDigi thread safe `l1`  created: 2014-05-23T16:11:11Z merged: 2014-06-15T14:22:18Z

1. [4198](http://github.com/cms-sw/cmssw/pull/4198){:target="_blank"}  from **@wmtan**: Avoid thread locals. `core`  created: 2014-06-10T19:55:36Z merged: 2014-06-11T09:19:19Z

1. [4177](http://github.com/cms-sw/cmssw/pull/4177){:target="_blank"}  from **@Martin-Grunewald**: 710pre9 hlt `hlt`  created: 2014-06-10T07:48:10Z merged: 2014-06-10T15:46:15Z

1. [4167](http://github.com/cms-sw/cmssw/pull/4167){:target="_blank"}  from **@Dr15Jones**: Make HcalDDDGeometry thread-safe `geometry`  created: 2014-06-09T20:56:27Z merged: 2014-06-10T15:45:04Z

1. [4163](http://github.com/cms-sw/cmssw/pull/4163){:target="_blank"}  from **@civanch**: T rugg ribbon `geometry`  created: 2014-06-09T16:12:03Z merged: 2014-06-10T15:44:45Z

1. [4138](http://github.com/cms-sw/cmssw/pull/4138){:target="_blank"}  from **@perrotta**: allow using the developing HLT menu for run2 in CMSSW_7_1_X `fastsim`  `hlt`  created: 2014-06-06T09:03:15Z merged: 2014-06-10T15:43:59Z

1. [4109](http://github.com/cms-sw/cmssw/pull/4109){:target="_blank"}  from **@fwyzard**: hltGetConfiguration cleanup `hlt`  created: 2014-06-04T15:12:13Z merged: 2014-06-10T15:42:50Z

1. [4116](http://github.com/cms-sw/cmssw/pull/4116){:target="_blank"}  from **@ktf**: Add missing header. `analysis`  created: 2014-06-05T06:18:44Z merged: 2014-06-09T17:59:04Z
# CMSSW_7_1_0_THREADED_pre2
#### Changes since CMSSW_7_1_0_THREADED_pre1:

fatal: ambiguous argument 'CMSSW_7_1_0_THREADED_pre1..CMSSW_7_1_0_THREADED_pre2': unknown revision or path not in the working tree.
Use '--' to separate paths from revisions
