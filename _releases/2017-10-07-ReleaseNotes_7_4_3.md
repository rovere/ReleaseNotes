---
layout: post
title:  "7_4_3"
date:   2017-10-07 19:13:38 +0200
categories: cmssw
relmajor: 7
relminor: 4
relsubminor: 3
---

# CMSSW_7_4_3
#### Changes since CMSSW_7_4_2_patch1:

[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_7_4_2_patch1...CMSSW_7_4_3)



1. [9247](http://github.com/cms-sw/cmssw/pull/9247){:target="_blank"}  from **@davidlange6**: protect against a missing L1 GT `dqm`  created: 2015-05-23T12:30:18Z merged: 2015-05-23T15:50:16Z

1. [9240](http://github.com/cms-sw/cmssw/pull/9240){:target="_blank"}  from **@slava77**:  Put some order in old MF configs; asymptotic default will be MagneticField_cff.py (same as #9239 ) `operations`  created: 2015-05-22T16:13:15Z merged: 2015-05-23T15:50:01Z

1. [9212](http://github.com/cms-sw/cmssw/pull/9212){:target="_blank"}  from **@dmitrijus**: Minor improvement for DQM/PhysicsHWW. `dqm`  created: 2015-05-21T18:05:20Z merged: 2015-05-22T14:17:44Z

1. [9176](http://github.com/cms-sw/cmssw/pull/9176){:target="_blank"}  from **@cms-tsg-storm**: HLT updates on top of what is in CMSSW742 `hlt`  created: 2015-05-20T14:52:25Z merged: 2015-05-22T14:13:07Z

1. [9220](http://github.com/cms-sw/cmssw/pull/9220){:target="_blank"}  from **@lveldere**: Bug fix: undo fix of ConversionTracks in case of gen-mixing (74X) `fastsim`  created: 2015-05-22T07:58:35Z merged: 2015-05-22T14:12:22Z

1. [9229](http://github.com/cms-sw/cmssw/pull/9229){:target="_blank"}  from **@davidlange6**: Option to remove hwwdqm `dqm`  `operations`  created: 2015-05-22T10:15:54Z merged: 2015-05-22T14:11:53Z

1. [8953](http://github.com/cms-sw/cmssw/pull/8953){:target="_blank"}  from **@cms-tsg-storm**: HLT updates on top of 741 with FastSim for 74X `fastsim`  `hlt`  `operations`  created: 2015-05-04T17:53:29Z merged: 2015-05-22T06:35:38Z

1. [9181](http://github.com/cms-sw/cmssw/pull/9181){:target="_blank"}  from **@wmtan**: Backport secondary input source improvements from 7_5_X `core`  created: 2015-05-20T19:20:36Z merged: 2015-05-22T06:34:37Z

1. [8653](http://github.com/cms-sw/cmssw/pull/8653){:target="_blank"}  from **@lveldere**: Fastsim 74X: fix truth matching for recoTracks from PU events `reconstruction`  `simulation`  created: 2015-04-03T12:44:57Z merged: 2015-05-22T06:33:32Z

1. [9090](http://github.com/cms-sw/cmssw/pull/9090){:target="_blank"}  from **@cfmcginn**: Moved *_cff.py to *_cfi.py for inclusion into HLT and confdb (backport from 75 pr) `reconstruction`  created: 2015-05-14T16:22:19Z merged: 2015-05-21T20:22:04Z

1. [9211](http://github.com/cms-sw/cmssw/pull/9211){:target="_blank"}  from **@lveldere**: FastSim 74X: remove FastSim specific collections from AODSIM  `fastsim`  created: 2015-05-21T17:54:41Z merged: 2015-05-21T20:18:57Z

1. [9108](http://github.com/cms-sw/cmssw/pull/9108){:target="_blank"}  from **@fcavallo**: fix FEDIDmin/max initialization `dqm`  created: 2015-05-15T14:33:56Z merged: 2015-05-21T14:43:30Z

1. [9187](http://github.com/cms-sw/cmssw/pull/9187){:target="_blank"}  from **@cms-btv-pog**: Protection for pt=0 ghost candidates in jet flavor clustering (74X) `analysis`  created: 2015-05-21T00:09:42Z merged: 2015-05-21T14:38:49Z

1. [9205](http://github.com/cms-sw/cmssw/pull/9205){:target="_blank"}  from **@Dr15Jones**: Make 10MB the default stack size for additional threads `core`  created: 2015-05-21T14:25:08Z merged: 2015-05-21T14:38:37Z

1. [9151](http://github.com/cms-sw/cmssw/pull/9151){:target="_blank"}  from **@HuguesBrun**: fix muon HLT DQM for tk muon (backport in 74X) `dqm`  created: 2015-05-19T12:14:52Z merged: 2015-05-20T18:37:18Z

1. [9164](http://github.com/cms-sw/cmssw/pull/9164){:target="_blank"}  from **@mengleisun**: fix the calibration DQM configuration `dqm`  created: 2015-05-19T21:22:22Z merged: 2015-05-20T18:36:57Z

1. [9006](http://github.com/cms-sw/cmssw/pull/9006){:target="_blank"}  from **@emanueledimarco**: Use of full5x5 cluster shapes to compute the MVA, read gzipped xml files `analysis`  created: 2015-05-08T13:19:39Z merged: 2015-05-20T15:12:49Z

1. [8677](http://github.com/cms-sw/cmssw/pull/8677){:target="_blank"}  from **@bmarzocc**: 7_4_X_alcarecostream_nophisym `alca`  `operations`  `pdmv`  created: 2015-04-08T06:53:57Z merged: 2015-05-20T15:05:38Z

1. [8056](http://github.com/cms-sw/cmssw/pull/8056){:target="_blank"}  from **@cms-btv-pog**: Switch by default to new flavour tool based on Hadrons. Update of exampl... `dqm`  created: 2015-03-04T08:58:52Z merged: 2015-05-20T15:03:20Z

1. [8124](http://github.com/cms-sw/cmssw/pull/8124){:target="_blank"}  from **@rjwang**: add plots of wire group and strip numbers for all chambers `dqm`  created: 2015-03-06T18:12:05Z merged: 2015-05-20T15:03:06Z

1. [8152](http://github.com/cms-sw/cmssw/pull/8152){:target="_blank"}  from **@fruboes**: DQM plots for jet triggers in lowPU runs `dqm`  created: 2015-03-09T12:25:38Z merged: 2015-05-20T15:02:53Z

1. [8210](http://github.com/cms-sw/cmssw/pull/8210){:target="_blank"}  from **@ndaci**:   Added Dxy plots (only for electron/muon at this moment) (Backport from 75X) `dqm`  created: 2015-03-11T19:45:08Z merged: 2015-05-20T15:02:42Z

1. [8573](http://github.com/cms-sw/cmssw/pull/8573){:target="_blank"}  from **@jingyucms**: Histograms for L1T Stage1 `dqm`  created: 2015-03-27T17:29:13Z merged: 2015-05-20T15:02:32Z

1. [8730](http://github.com/cms-sw/cmssw/pull/8730){:target="_blank"}  from **@acimmino**: RPC DQM Fix for summary plots and DCS bit in 74X `dqm`  created: 2015-04-14T15:19:03Z merged: 2015-05-20T15:01:58Z

1. [8904](http://github.com/cms-sw/cmssw/pull/8904){:target="_blank"}  from **@lveldere**: Fastsim: 74X premixing `fastsim`  `operations`  `pdmv`  `simulation`  created: 2015-04-28T19:39:35Z merged: 2015-05-20T15:01:42Z

1. [8937](http://github.com/cms-sw/cmssw/pull/8937){:target="_blank"}  from **@aelwood**: Updated the alphaT paths for the DQM modules `dqm`  created: 2015-05-01T21:15:48Z merged: 2015-05-20T15:01:26Z

1. [8972](http://github.com/cms-sw/cmssw/pull/8972){:target="_blank"}  from **@hdelanno**: Cleaned unused config parameters in Strip DQM for 7_4_X `dqm`  created: 2015-05-06T14:45:39Z merged: 2015-05-20T15:01:15Z

1. [9021](http://github.com/cms-sw/cmssw/pull/9021){:target="_blank"}  from **@jmduarte**: updating razor HLT paths for SUSY DQM in 74X `dqm`  created: 2015-05-08T23:11:12Z merged: 2015-05-20T15:00:57Z

1. [9029](http://github.com/cms-sw/cmssw/pull/9029){:target="_blank"}  from **@cbernet**: Heppy 74X integration `analysis`  created: 2015-05-11T07:49:26Z merged: 2015-05-20T15:00:46Z

#### CMSDIST Changes between Tags REL/CMSSW_7_4_2_patch1/slc6_amd64_gcc491 and REL/CMSSW_7_4_3/slc6_amd64_gcc491:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_7_4_2_patch1/slc6_amd64_gcc491...REL/CMSSW_7_4_3/slc6_amd64_gcc491)



1. [1570](http://github.com/cms-sw/cmssw/pull/1570){:target="_blank"}  from **@smuzaffar**: updated root commit to include the LorentzVector fix 09b7416ea111be6651790d346294572b82c59a24 created: 2013-11-23T13:29:22Z merged: 2013-11-25T12:32:59Z

1. [1568](http://github.com/cms-sw/cmssw/pull/1568){:target="_blank"}  from @cms-sw: Update root to commit cms-sw/root**@8fdd98** 7_4_X created: 2013-11-23T09:15:23Z merged: 2013-11-23T09:16:02Z
