---
layout: post
title:  "9_2_1"
date:   2017-10-06 10:52:06 +0200
categories: cmssw
relmajor: 9
relminor: 2
relsubminor: 1
---

# CMSSW_9_2_1
#### Changes since CMSSW_9_2_0_patch5:
[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_9_2_0_patch5...CMSSW_9_2_1)



1. [19067](http://github.com/cms-sw/cmssw/pull/19067){:target="_blank"}  from **@rekovic**: pr92 L1T parser compatible utm-0.6.0 and later `l1`  created: 2017-06-01T15:24:21Z merged: 2017-06-01T17:46:47Z

1. [19059](http://github.com/cms-sw/cmssw/pull/19059){:target="_blank"}  from **@mtosi**: fix pixel DQM `dqm`  created: 2017-06-01T11:57:28Z merged: 2017-06-01T18:27:44Z

1. [19047](http://github.com/cms-sw/cmssw/pull/19047){:target="_blank"}  from **@kpedro88**: Fix HCAL premixing with QIE8 and uHTR `operations`  `reconstruction`  created: 2017-05-31T18:27:03Z merged: 2017-06-01T18:20:16Z

1. [19045](http://github.com/cms-sw/cmssw/pull/19045){:target="_blank"}  from **@fwyzard**: recover original behaviour: do not write .jsndata files for empty lumisections `hlt`  created: 2017-05-31T15:49:38Z merged: 2017-06-01T06:51:45Z

1. [19037](http://github.com/cms-sw/cmssw/pull/19037){:target="_blank"}  from **@BenjaminRS**: Fixing a bug to not try to take a L2 track when no L2 is available `hlt`  created: 2017-05-31T13:58:19Z merged: 2017-06-01T13:54:31Z

1. [19035](http://github.com/cms-sw/cmssw/pull/19035){:target="_blank"}  from **@dmitrijus**: Online DQM fix for ML applications. `dqm`  created: 2017-05-31T13:47:21Z merged: 2017-06-01T10:15:13Z

1. [19022](http://github.com/cms-sw/cmssw/pull/19022){:target="_blank"}  from **@davidlange6**: quieter harvesting step `dqm`  `operations`  created: 2017-05-30T16:44:31Z merged: 2017-06-01T07:50:29Z

1. [19021](http://github.com/cms-sw/cmssw/pull/19021){:target="_blank"}  from **@gartung**: Geometry : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `geometry`  created: 2017-05-30T15:42:17Z merged: 2017-06-01T06:57:49Z

1. [19016](http://github.com/cms-sw/cmssw/pull/19016){:target="_blank"}  from **@Dr15Jones**: Avoid making three copies of a large PSet in TrackingMonitor `dqm`  created: 2017-05-30T14:35:41Z merged: 2017-06-01T06:57:37Z

1. [19015](http://github.com/cms-sw/cmssw/pull/19015){:target="_blank"}  from **@cerminar**: [92X] RelVal tests for new alca workflows `pdmv`  `upgrade`  created: 2017-05-30T14:18:05Z merged: 2017-06-01T17:51:49Z

1. [19006](http://github.com/cms-sw/cmssw/pull/19006){:target="_blank"}  from **@boudoul**: Use non-deprecated phase2 scenario in detector description unit tests `geometry`  created: 2017-05-30T08:07:17Z merged: 2017-05-30T10:58:22Z

1. [18998](http://github.com/cms-sw/cmssw/pull/18998){:target="_blank"}  from **@Dr15Jones**: Avoid TClass::GetClass calls when data product missing `core`  created: 2017-05-29T20:38:05Z merged: 2017-05-30T07:42:56Z

1. [18996](http://github.com/cms-sw/cmssw/pull/18996){:target="_blank"}  from **@igv4321**: Adding anode DB suppression status to the rechits `reconstruction`  created: 2017-05-29T16:47:13Z merged: 2017-06-01T18:22:58Z

1. [18993](http://github.com/cms-sw/cmssw/pull/18993){:target="_blank"}  from **@leggat**: Updates to pixel phase 1 summary class `dqm`  created: 2017-05-29T10:23:08Z merged: 2017-06-01T07:53:38Z

1. [18991](http://github.com/cms-sw/cmssw/pull/18991){:target="_blank"}  from **@Dr15Jones**: Fix memory leaks in DQMOffline/Trigger `dqm`  created: 2017-05-29T02:54:59Z merged: 2017-05-30T20:22:41Z

1. [18990](http://github.com/cms-sw/cmssw/pull/18990){:target="_blank"}  from **@Dr15Jones**: Fix memory leak in ConversionLikelihoodCalculator `reconstruction`  created: 2017-05-28T22:45:50Z merged: 2017-06-01T06:57:27Z

1. [18989](http://github.com/cms-sw/cmssw/pull/18989){:target="_blank"}  from **@Dr15Jones**: Fixed memory leak in L1TMuonEndCapForestESProducer `l1`  created: 2017-05-28T22:17:56Z merged: 2017-06-01T07:54:15Z

1. [18988](http://github.com/cms-sw/cmssw/pull/18988){:target="_blank"}  from **@Dr15Jones**: Fix thread local memory leak in EgammaTowerIsolation `reconstruction`  created: 2017-05-28T21:17:36Z merged: 2017-06-01T06:57:15Z

1. [18987](http://github.com/cms-sw/cmssw/pull/18987){:target="_blank"}  from **@smuzaffar**: added missing header numeric to fix gcc6/7 compilation errors about std::iota `comparison`  `reconstruction`  `upgrade`  created: 2017-05-28T16:46:00Z merged: 2017-05-28T16:46:12Z

1. [18985](http://github.com/cms-sw/cmssw/pull/18985){:target="_blank"}  from **@Dr15Jones**: Fixed memory leak in MultipleScatteringX0Data `reconstruction`  created: 2017-05-28T14:02:31Z merged: 2017-06-01T14:50:28Z

1. [18982](http://github.com/cms-sw/cmssw/pull/18982){:target="_blank"}  from **@smuzaffar**: Fix geners cdump test `alca`  created: 2017-05-27T08:55:11Z merged: 2017-05-27T10:33:08Z

1. [18980](http://github.com/cms-sw/cmssw/pull/18980){:target="_blank"}  from **@fwyzard**: fix HLT rate monitoring for CMSSW 9.2.x `hlt`  created: 2017-05-27T08:29:38Z merged: 2017-05-28T08:02:47Z

1. [18973](http://github.com/cms-sw/cmssw/pull/18973){:target="_blank"}  from **@gartung**: DataFormats/PatCandidates : missing #include <array> found compiling on macos with clang `analysis`  `reconstruction`  created: 2017-05-26T18:31:19Z merged: 2017-05-27T07:33:52Z

1. [18972](http://github.com/cms-sw/cmssw/pull/18972){:target="_blank"}  from **@gartung**: FWCore/Framework : missing #include <array> found compiling on macOS with clang `core`  created: 2017-05-26T18:30:21Z merged: 2017-05-27T07:34:26Z

1. [18966](http://github.com/cms-sw/cmssw/pull/18966){:target="_blank"}  from **@forthommel**: CTPPS: small corrections in the diamond DQM `dqm`  created: 2017-05-26T15:10:45Z merged: 2017-05-30T20:26:25Z

1. [18962](http://github.com/cms-sw/cmssw/pull/18962){:target="_blank"}  from **@thomreis**: L1 muon online DQM uprades `dqm`  created: 2017-05-26T14:15:34Z merged: 2017-06-01T11:02:54Z

1. [18959](http://github.com/cms-sw/cmssw/pull/18959){:target="_blank"}  from **@jalimena**: update EXO NoBPTX trigger paths validation for 2017 pp collisions `dqm`  created: 2017-05-26T12:14:32Z merged: 2017-06-01T08:16:44Z

1. [18957](http://github.com/cms-sw/cmssw/pull/18957){:target="_blank"}  from **@folguera**: MuonHLT IterL3 reconstruction:  bug fix to avoid running twice on the same L1  `hlt`  created: 2017-05-26T08:44:54Z merged: 2017-05-27T07:37:56Z

1. [18955](http://github.com/cms-sw/cmssw/pull/18955){:target="_blank"}  from **@jhgoh**: RPCRecHits nan protection `reconstruction`  created: 2017-05-26T01:26:20Z merged: 2017-05-31T11:08:25Z

1. [18952](http://github.com/cms-sw/cmssw/pull/18952){:target="_blank"}  from **@cms-sw**: fix fwlite build by removing dependency on TrackingTools/PatternTools/interface/Trajectory.h `comparison`  `reconstruction`  created: 2017-05-25T19:39:39Z merged: 2017-05-25T19:39:52Z

1. [18947](http://github.com/cms-sw/cmssw/pull/18947){:target="_blank"}  from **@gartung**: RecoTracker: fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `reconstruction`  created: 2017-05-25T15:30:22Z merged: 2017-05-27T07:41:20Z

1. [18946](http://github.com/cms-sw/cmssw/pull/18946){:target="_blank"}  from **@gartung**: RecoParticleFlow : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `reconstruction`  created: 2017-05-25T15:26:15Z merged: 2017-05-27T07:41:35Z

1. [18945](http://github.com/cms-sw/cmssw/pull/18945){:target="_blank"}  from **@gartung**: RecoMuon : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `reconstruction`  created: 2017-05-25T15:24:09Z merged: 2017-05-27T07:41:47Z

1. [18944](http://github.com/cms-sw/cmssw/pull/18944){:target="_blank"}  from **@gartung**: RecoLocalCalo : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `reconstruction`  created: 2017-05-25T15:22:06Z merged: 2017-05-27T07:41:59Z

1. [18943](http://github.com/cms-sw/cmssw/pull/18943){:target="_blank"}  from **@gartung**: RecoBTag : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `reconstruction`  created: 2017-05-25T15:19:33Z merged: 2017-05-27T07:42:10Z

1. [18942](http://github.com/cms-sw/cmssw/pull/18942){:target="_blank"}  from **@gartung**: PhysicsTools : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `analysis`  `reconstruction`  created: 2017-05-25T15:17:34Z merged: 2017-05-27T07:42:18Z

1. [18941](http://github.com/cms-sw/cmssw/pull/18941){:target="_blank"}  from **@gartung**: L1Trigger : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `l1`  created: 2017-05-25T15:14:45Z merged: 2017-05-30T20:27:06Z

1. [18940](http://github.com/cms-sw/cmssw/pull/18940){:target="_blank"}  from **@gartung**: HLTrigger : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `hlt`  created: 2017-05-25T15:11:07Z merged: 2017-05-27T07:42:45Z

1. [18939](http://github.com/cms-sw/cmssw/pull/18939){:target="_blank"}  from **@gartung**: GeneratorInterface : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `generators`  created: 2017-05-25T15:09:02Z merged: 2017-05-30T14:12:12Z

1. [18938](http://github.com/cms-sw/cmssw/pull/18938){:target="_blank"}  from **@gartung**: EventFilter : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `l1`  created: 2017-05-25T15:06:56Z merged: 2017-05-30T20:27:16Z

1. [18937](http://github.com/cms-sw/cmssw/pull/18937){:target="_blank"}  from **@gartung**: DQMServices : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `dqm`  created: 2017-05-25T15:04:49Z merged: 2017-05-27T07:42:56Z

1. [18936](http://github.com/cms-sw/cmssw/pull/18936){:target="_blank"}  from **@gartung**: DQM + DQMOffline : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `dqm`  created: 2017-05-25T15:03:25Z merged: 2017-05-27T07:43:07Z

1. [18935](http://github.com/cms-sw/cmssw/pull/18935){:target="_blank"}  from **@gartung**: CondCore : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `db`  created: 2017-05-25T15:00:40Z merged: 2017-05-30T14:12:23Z

1. [18934](http://github.com/cms-sw/cmssw/pull/18934){:target="_blank"}  from **@gartung**: CalibCalorimetry + CaloOnlineTools : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `alca`  `db`  created: 2017-05-25T14:39:09Z merged: 2017-05-30T08:42:28Z

1. [18933](http://github.com/cms-sw/cmssw/pull/18933){:target="_blank"}  from **@gartung**: Alignment : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `alca`  created: 2017-05-25T14:36:05Z merged: 2017-05-30T07:43:13Z

1. [18931](http://github.com/cms-sw/cmssw/pull/18931){:target="_blank"}  from **@Dr15Jones**: Removed class ELdestControl `core`  created: 2017-05-25T13:43:33Z merged: 2017-05-27T07:43:28Z

1. [18930](http://github.com/cms-sw/cmssw/pull/18930){:target="_blank"}  from **@VinInn**: VertexDQM: recenter y_vtx, increase range for nvtx `dqm`  created: 2017-05-25T11:27:33Z merged: 2017-05-27T07:43:52Z

1. [18928](http://github.com/cms-sw/cmssw/pull/18928){:target="_blank"}  from **@gartung**: CalibFormats : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `alca`  created: 2017-05-25T01:40:32Z merged: 2017-05-30T08:21:35Z

1. [18927](http://github.com/cms-sw/cmssw/pull/18927){:target="_blank"}  from **@gartung**: DataFormats/TrackerRecHit2D: Fix warning warning: 'class TkCloner' has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `reconstruction`  created: 2017-05-25T01:32:37Z merged: 2017-05-27T07:44:02Z

1. [18926](http://github.com/cms-sw/cmssw/pull/18926){:target="_blank"}  from **@gartung**: SimCalorimetry : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `simulation`  `upgrade`  created: 2017-05-24T23:45:33Z merged: 2017-05-27T07:44:22Z

1. [18924](http://github.com/cms-sw/cmssw/pull/18924){:target="_blank"}  from **@gartung**: SimG4 : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `simulation`  created: 2017-05-24T22:19:38Z merged: 2017-05-27T07:44:31Z

1. [18923](http://github.com/cms-sw/cmssw/pull/18923){:target="_blank"}  from **@gartung**: SimTracker : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `simulation`  `upgrade`  created: 2017-05-24T22:16:39Z merged: 2017-05-27T07:44:43Z

1. [18922](http://github.com/cms-sw/cmssw/pull/18922){:target="_blank"}  from **@gartung**: fix Utilities/XrdAdapter : gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `core`  created: 2017-05-24T22:12:33Z merged: 2017-05-27T07:44:52Z

1. [18921](http://github.com/cms-sw/cmssw/pull/18921){:target="_blank"}  from **@gartung**: TrackingTools : fix gcc700 warning: class  has virtual functions and accessible non-virtual destructor [-Wnon-virtual-dtor] `reconstruction`  created: 2017-05-24T22:08:08Z merged: 2017-05-27T07:45:11Z

1. [18916](http://github.com/cms-sw/cmssw/pull/18916){:target="_blank"}  from **@hroskes**: fix mistake in all in one tool configuration `alca`  created: 2017-05-24T16:17:45Z merged: 2017-05-25T08:11:01Z

1. [18910](http://github.com/cms-sw/cmssw/pull/18910){:target="_blank"}  from **@smuzaffar**: Fixing rootcling warning about missing dependencies `reconstruction`  created: 2017-05-24T09:53:10Z merged: 2017-05-25T08:10:50Z

1. [18909](http://github.com/cms-sw/cmssw/pull/18909){:target="_blank"}  from **@cms-sw**: run condTestRegression test only on slc/amd64 archs. `db`  created: 2017-05-24T05:38:50Z merged: 2017-05-25T08:10:23Z

1. [18908](http://github.com/cms-sw/cmssw/pull/18908){:target="_blank"}  from **@cfmcginn**: Added offline dqm for HI triggers to be used in LowPU datataking in 2017 `dqm`  created: 2017-05-24T05:30:13Z merged: 2017-05-25T08:10:32Z

1. [18905](http://github.com/cms-sw/cmssw/pull/18905){:target="_blank"}  from **@franzoni**: [9_2_X] fix name of input collection in pathALCARECOHcalCalMinBias `alca`  created: 2017-05-23T20:06:09Z merged: 2017-05-27T07:48:11Z

1. [18900](http://github.com/cms-sw/cmssw/pull/18900){:target="_blank"}  from **@hroskes**: convenient interface for HipPy and MP alignments `alca`  created: 2017-05-23T15:13:42Z merged: 2017-05-24T07:26:36Z

1. [18898](http://github.com/cms-sw/cmssw/pull/18898){:target="_blank"}  from **@davidlt**: Implement HRRealTime for AArch64 `core`  created: 2017-05-23T14:39:00Z merged: 2017-05-24T07:26:14Z

1. [18897](http://github.com/cms-sw/cmssw/pull/18897){:target="_blank"}  from **@ianna**: DD Agorithm Cleanup `geometry`  created: 2017-05-23T14:29:20Z merged: 2017-05-24T14:02:26Z

1. [18896](http://github.com/cms-sw/cmssw/pull/18896){:target="_blank"}  from **@VinInn**: fix bug about lambda error + small cleanup `reconstruction`  created: 2017-05-23T12:57:56Z merged: 2017-05-27T07:48:28Z

1. [18894](http://github.com/cms-sw/cmssw/pull/18894){:target="_blank"}  from **@threus**: update GT in online DQM and EventDisplay `dqm`  created: 2017-05-23T08:59:01Z merged: 2017-05-23T16:04:27Z

1. [18893](http://github.com/cms-sw/cmssw/pull/18893){:target="_blank"}  from **@Teemperor**: Comment out commentary behind #endif in Constants.h `alca`  `comparison`  `db`  created: 2017-05-23T07:01:27Z merged: 2017-05-23T07:10:32Z

1. [18891](http://github.com/cms-sw/cmssw/pull/18891){:target="_blank"}  from **@ianna**: DDQuery Remove Unused Class `geometry`  created: 2017-05-22T17:18:26Z merged: 2017-05-23T05:59:09Z

1. [18890](http://github.com/cms-sw/cmssw/pull/18890){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-hcx126 Correct the name of collection in 3 cfi files of HCAL AlCaReco's `alca`  created: 2017-05-22T17:12:18Z merged: 2017-05-24T07:27:04Z

1. [18889](http://github.com/cms-sw/cmssw/pull/18889){:target="_blank"}  from **@Dr15Jones**: Added edmScanValgrind.py to discard false positives `core`  created: 2017-05-22T16:32:41Z merged: 2017-05-23T07:12:23Z

1. [18888](http://github.com/cms-sw/cmssw/pull/18888){:target="_blank"}  from **@jfernan2**: Small fix to DT DQM configuration `dqm`  created: 2017-05-22T15:21:12Z merged: 2017-05-25T08:09:57Z

1. [18887](http://github.com/cms-sw/cmssw/pull/18887){:target="_blank"}  from **@Teemperor**: Remove the dead headers ColumnPacker.hh/ColumnPackerHelper.hh `alca`  created: 2017-05-22T15:00:54Z merged: 2017-05-23T09:48:25Z

1. [18886](http://github.com/cms-sw/cmssw/pull/18886){:target="_blank"}  from **@Teemperor**: Added missing include for <utility> to collectTupleNames.hh `alca`  created: 2017-05-22T15:00:46Z merged: 2017-05-23T05:59:21Z

1. [18885](http://github.com/cms-sw/cmssw/pull/18885){:target="_blank"}  from **@Teemperor**: Add missing includes to BoundaryInformation.h `reconstruction`  created: 2017-05-22T15:00:39Z merged: 2017-05-25T08:09:38Z

1. [18884](http://github.com/cms-sw/cmssw/pull/18884){:target="_blank"}  from **@Teemperor**: Added missing <vector> include to PattRecoTree.h `reconstruction`  created: 2017-05-22T15:00:33Z merged: 2017-05-25T08:09:27Z

1. [18882](http://github.com/cms-sw/cmssw/pull/18882){:target="_blank"}  from **@smuzaffar**: Fixed unit test to use TAxis `core`  `dqm`  created: 2017-05-22T13:36:02Z merged: 2017-05-23T09:48:40Z

1. [18881](http://github.com/cms-sw/cmssw/pull/18881){:target="_blank"}  from **@smuzaffar**: fixed unit test to work in IB env `alca`  created: 2017-05-22T13:21:45Z merged: 2017-05-23T05:59:33Z

1. [18876](http://github.com/cms-sw/cmssw/pull/18876){:target="_blank"}  from **@cms-sw**: Fix unittest: avoid using shared /tmp/PixelBaryCentreTool directory `alca`  created: 2017-05-22T07:47:10Z merged: 2017-05-22T10:25:10Z

1. [18874](http://github.com/cms-sw/cmssw/pull/18874){:target="_blank"}  from **@Dr15Jones**: Removed unused variable `core`  created: 2017-05-21T15:28:23Z merged: 2017-05-22T06:15:40Z

1. [18870](http://github.com/cms-sw/cmssw/pull/18870){:target="_blank"}  from **@Dr15Jones**: Fix code indention in CTPPSPixelDQMSource `dqm`  created: 2017-05-20T15:45:37Z merged: 2017-05-22T09:11:48Z

1. [18869](http://github.com/cms-sw/cmssw/pull/18869){:target="_blank"}  from **@fwyzard**: update L1REPACK configuration to use unpacked digis also for HCAL upgrades `l1`  `operations`  created: 2017-05-20T08:55:29Z merged: 2017-05-21T08:14:17Z

1. [18867](http://github.com/cms-sw/cmssw/pull/18867){:target="_blank"}  from **@Dr15Jones**: Moved functions from anonymous namespace in CondCore/CondDB `db`  created: 2017-05-20T02:28:06Z merged: 2017-05-24T07:42:49Z

1. [18865](http://github.com/cms-sw/cmssw/pull/18865){:target="_blank"}  from **@franzoni**: Drop-box metadata management: updates and introduce AAG, BSHP, EcalPed `alca`  `db`  created: 2017-05-19T18:31:12Z merged: 2017-05-23T09:49:31Z

1. [18864](http://github.com/cms-sw/cmssw/pull/18864){:target="_blank"}  from **@bsunanda**: Phase2-hgx83 Bug fixes to two codes `dqm`  created: 2017-05-19T18:02:26Z merged: 2017-05-24T14:03:22Z

1. [18862](http://github.com/cms-sw/cmssw/pull/18862){:target="_blank"}  from **@fioriNTU**: Disabling a plot making the GUI unstable  `dqm`  created: 2017-05-19T15:44:55Z merged: 2017-05-25T08:06:44Z

1. [18861](http://github.com/cms-sw/cmssw/pull/18861){:target="_blank"}  from **@PFCal-dev**: HGCAL trigger fixes, optimizations and cleaning `l1`  `upgrade`  created: 2017-05-19T15:29:50Z merged: 2017-05-23T07:19:26Z

1. [18860](http://github.com/cms-sw/cmssw/pull/18860){:target="_blank"}  from **@thomreis**: Add zero suppression mask for L1T uGMT capId3. `dqm`  created: 2017-05-19T14:58:49Z merged: 2017-05-25T08:06:28Z

1. [18858](http://github.com/cms-sw/cmssw/pull/18858){:target="_blank"}  from **@mrodozov**: Importing missing piece of das_client `core`  created: 2017-05-19T14:25:26Z merged: 2017-05-20T07:24:19Z

1. [18853](http://github.com/cms-sw/cmssw/pull/18853){:target="_blank"}  from **@kpedro88**: temporarily disable setNoiseFlagsQIE11 for AlCa `alca`  created: 2017-05-19T13:34:36Z merged: 2017-05-23T06:00:29Z

1. [18852](http://github.com/cms-sw/cmssw/pull/18852){:target="_blank"}  from **@boudoul**: Deprecating Phase2 Tracker T3 and corresp. scenarios + Adding D18 (= D8 but with the non deprec. Tracker)  `geometry`  `operations`  `pdmv`  `upgrade`  created: 2017-05-19T13:30:33Z merged: 2017-05-29T12:26:11Z

1. [18851](http://github.com/cms-sw/cmssw/pull/18851){:target="_blank"}  from **@mrodozov**: Fixing rootcling warning about missing dependencies  `analysis`  `reconstruction`  `upgrade`  created: 2017-05-19T10:36:30Z merged: 2017-05-23T09:13:46Z

1. [18849](http://github.com/cms-sw/cmssw/pull/18849){:target="_blank"}  from **@mrodozov**: Fixing rootcling warning about missing dependencies `fastsim`  created: 2017-05-19T10:17:59Z merged: 2017-05-21T08:14:42Z

1. [18848](http://github.com/cms-sw/cmssw/pull/18848){:target="_blank"}  from **@mrodozov**: Fixing rootcling warning about missing dependencies  `simulation`  created: 2017-05-19T10:17:16Z merged: 2017-05-21T08:14:52Z

1. [18847](http://github.com/cms-sw/cmssw/pull/18847){:target="_blank"}  from **@mrodozov**: Fixing rootcling warning about missing dependencies `l1`  `upgrade`  created: 2017-05-19T10:16:36Z merged: 2017-05-22T09:09:02Z

1. [18846](http://github.com/cms-sw/cmssw/pull/18846){:target="_blank"}  from **@perrozzi**: fix LHERunInfoProduct duplication `generators`  created: 2017-05-19T06:11:53Z merged: 2017-05-28T08:03:02Z

1. [18842](http://github.com/cms-sw/cmssw/pull/18842){:target="_blank"}  from **@Dr15Jones**: Set a maximum number of waiting messages `core`  created: 2017-05-19T01:11:25Z merged: 2017-05-20T12:04:59Z

1. [18840](http://github.com/cms-sw/cmssw/pull/18840){:target="_blank"}  from **@slava77**: optimize ECAL uncalibRecHit multifit (follow up to #18600) `reconstruction`  created: 2017-05-18T22:17:46Z merged: 2017-05-20T12:05:20Z

1. [18837](http://github.com/cms-sw/cmssw/pull/18837){:target="_blank"}  from **@ianna**: Remove Legacy Code `geometry`  created: 2017-05-18T15:25:44Z merged: 2017-05-19T07:24:25Z

1. [18833](http://github.com/cms-sw/cmssw/pull/18833){:target="_blank"}  from **@Dr15Jones**: Consolidate stream and thread printout `core`  created: 2017-05-18T14:09:40Z merged: 2017-05-19T07:14:54Z

1. [18830](http://github.com/cms-sw/cmssw/pull/18830){:target="_blank"}  from **@folguera**: HLTL1MuonNoL2Selector fix to avoid the need of duplicating the class `hlt`  created: 2017-05-18T10:11:36Z merged: 2017-05-19T07:16:10Z

1. [18829](http://github.com/cms-sw/cmssw/pull/18829){:target="_blank"}  from **@calabria**: Fix for the GEM validation: fix histogram folder `dqm`  created: 2017-05-18T10:01:09Z merged: 2017-05-25T08:06:07Z

1. [18826](http://github.com/cms-sw/cmssw/pull/18826){:target="_blank"}  from **@ggovi**: Fix for PopCon BTransition module  `db`  created: 2017-05-18T07:46:04Z merged: 2017-05-19T07:16:31Z

1. [18824](http://github.com/cms-sw/cmssw/pull/18824){:target="_blank"}  from **@rovere**: Full reco-material tuninig after PR 18651 `geometry`  created: 2017-05-18T07:06:00Z merged: 2017-05-19T10:50:38Z

1. [18819](http://github.com/cms-sw/cmssw/pull/18819){:target="_blank"}  from **@Sam-Harper**: fillDescriptions fix for E/gamma Pixel Matching Modules `hlt`  `reconstruction`  created: 2017-05-17T22:40:22Z merged: 2017-05-18T09:25:10Z

1. [18817](http://github.com/cms-sw/cmssw/pull/18817){:target="_blank"}  from **@JanFSchulte**: Update of PointSeededTrackingRegionsProducer to work in CMSSW 9 `reconstruction`  created: 2017-05-17T21:53:00Z merged: 2017-05-24T08:05:40Z

1. [18816](http://github.com/cms-sw/cmssw/pull/18816){:target="_blank"}  from **@JanFSchulte**: Add fake trajectory to PixelTracks `reconstruction`  created: 2017-05-17T21:50:13Z merged: 2017-05-25T08:05:52Z

1. [18815](http://github.com/cms-sw/cmssw/pull/18815){:target="_blank"}  from **@forthommel**: CTPPS: Small memory footprint reduction for the channels mapping handler `alca`  `db`  created: 2017-05-17T21:10:17Z merged: 2017-05-29T20:29:56Z

1. [18813](http://github.com/cms-sw/cmssw/pull/18813){:target="_blank"}  from **@capalmer85**: Pcc producer phase1 rebase 92 x `alca`  `operations`  `reconstruction`  created: 2017-05-17T18:33:34Z merged: 2017-05-18T09:46:51Z

1. [18808](http://github.com/cms-sw/cmssw/pull/18808){:target="_blank"}  from **@davidlange6**: speed up earlyDeleteSettings_cff.py by avoiding function calls `operations`  created: 2017-05-17T14:57:24Z merged: 2017-05-31T09:16:29Z

1. [18807](http://github.com/cms-sw/cmssw/pull/18807){:target="_blank"}  from **@mandrenguyen**: Also store crossing frame in heavy-ion event overlay workflow `simulation`  created: 2017-05-17T14:44:39Z merged: 2017-05-19T07:14:15Z

1. [18806](http://github.com/cms-sw/cmssw/pull/18806){:target="_blank"}  from **@Teemperor**: Remove dead header TrackingDataPrint.h `simulation`  created: 2017-05-17T14:42:11Z merged: 2017-05-24T14:03:52Z

1. [18804](http://github.com/cms-sw/cmssw/pull/18804){:target="_blank"}  from **@Teemperor**: Remove compability header normalizedPhi.h `analysis`  `reconstruction`  created: 2017-05-17T14:07:49Z merged: 2017-05-19T07:16:50Z

1. [18803](http://github.com/cms-sw/cmssw/pull/18803){:target="_blank"}  from **@Teemperor**: Added missing includes to Instantiate.h. `db`  created: 2017-05-17T13:56:16Z merged: 2017-05-31T11:25:06Z

1. [18799](http://github.com/cms-sw/cmssw/pull/18799){:target="_blank"}  from **@Teemperor**: Add missing #include to DeDxHitInfo.h `reconstruction`  created: 2017-05-17T09:58:31Z merged: 2017-05-18T07:54:36Z

1. [18796](http://github.com/cms-sw/cmssw/pull/18796){:target="_blank"}  from **@Teemperor**: Add missing includes to HGCRecHitComparison.h. `reconstruction`  `upgrade`  created: 2017-05-17T09:58:04Z merged: 2017-05-18T09:25:20Z

1. [18795](http://github.com/cms-sw/cmssw/pull/18795){:target="_blank"}  from **@Teemperor**: Add missing include to LocalErrorBaseExtended.h `simulation`  created: 2017-05-17T09:57:53Z merged: 2017-05-18T07:54:23Z

1. [18788](http://github.com/cms-sw/cmssw/pull/18788){:target="_blank"}  from **@Teemperor**: Make PythiaDecays.h a standalone header. `fastsim`  created: 2017-05-17T09:56:41Z merged: 2017-05-18T07:54:09Z

1. [18787](http://github.com/cms-sw/cmssw/pull/18787){:target="_blank"}  from **@Teemperor**: Add missing includes to Phase2TrackerCOmmisioningDigi.h `reconstruction`  `upgrade`  created: 2017-05-17T09:56:30Z merged: 2017-05-18T09:24:58Z

1. [18786](http://github.com/cms-sw/cmssw/pull/18786){:target="_blank"}  from **@Teemperor**: Fix clashes between translator function in PythonModule.h/.cc `core`  created: 2017-05-17T09:56:18Z merged: 2017-05-18T09:30:29Z

1. [18785](http://github.com/cms-sw/cmssw/pull/18785){:target="_blank"}  from **@Teemperor**: Add missing includes to TrajectoryStopReasons.h `reconstruction`  created: 2017-05-17T09:56:05Z merged: 2017-05-18T07:53:06Z

1. [18784](http://github.com/cms-sw/cmssw/pull/18784){:target="_blank"}  from **@Teemperor**: Add missing includes to SerializationManual.h `alca`  `db`  created: 2017-05-17T09:55:50Z merged: 2017-05-18T09:25:41Z

1. [18779](http://github.com/cms-sw/cmssw/pull/18779){:target="_blank"}  from **@slava77**: recover multi-thread reproducibility in CTPPS diamond local track y position `reconstruction`  created: 2017-05-17T00:54:46Z merged: 2017-05-18T07:52:54Z

1. [18778](http://github.com/cms-sw/cmssw/pull/18778){:target="_blank"}  from **@igv4321**: Turning on channel quality fetching from db `reconstruction`  created: 2017-05-16T22:46:19Z merged: 2017-05-19T12:26:09Z

1. [18773](http://github.com/cms-sw/cmssw/pull/18773){:target="_blank"}  from **@slava77**:  lower pt cut on dedxhitinfo to 10 GeV and add dedx harmonic2 for pixel hits `reconstruction`  created: 2017-05-16T15:51:55Z merged: 2017-05-21T08:15:00Z

1. [18768](http://github.com/cms-sw/cmssw/pull/18768){:target="_blank"}  from **@bsunanda**: Phase2-hgx81 Add ROOT scripts to study harvested plots `dqm`  created: 2017-05-16T13:23:31Z merged: 2017-05-24T07:29:10Z

1. [18766](http://github.com/cms-sw/cmssw/pull/18766){:target="_blank"}  from **@mrodozov**: There is a missing dependency that is causing a build error `reconstruction`  created: 2017-05-16T13:04:42Z merged: 2017-05-18T07:52:23Z

1. [18765](http://github.com/cms-sw/cmssw/pull/18765){:target="_blank"}  from **@civanch**: Added CPU benchmark `simulation`  created: 2017-05-16T12:24:15Z merged: 2017-05-18T14:05:19Z

1. [18764](http://github.com/cms-sw/cmssw/pull/18764){:target="_blank"}  from **@Teemperor**: Add missing #include to DeDxHit.h. `reconstruction`  created: 2017-05-16T11:46:54Z merged: 2017-05-18T09:36:20Z

1. [18763](http://github.com/cms-sw/cmssw/pull/18763){:target="_blank"}  from **@Teemperor**: Add missing Candidate.h/LeafCandidate.h includes to CandidateWithRef.h. `analysis`  `reconstruction`  created: 2017-05-16T11:46:30Z merged: 2017-05-18T07:57:32Z

1. [18755](http://github.com/cms-sw/cmssw/pull/18755){:target="_blank"}  from **@MilanoBicocca-pix**: CMSSW 92X - Adding the possibility to select the PVs before the BeamSpot fit `alca`  `dqm`  `reconstruction`  created: 2017-05-15T23:04:34Z merged: 2017-05-24T15:17:52Z

1. [18751](http://github.com/cms-sw/cmssw/pull/18751){:target="_blank"}  from **@gartung**: DQMServices/Core: Change DQMEDHarvester to an edm::one::EDProducer and add alias to EDProducer from DQMEDHarvester `alca`  `dqm`  `fastsim`  `generators`  `geometry`  `l1`  `upgrade`  created: 2017-05-15T18:25:20Z merged: 2017-05-27T07:54:11Z

1. [18743](http://github.com/cms-sw/cmssw/pull/18743){:target="_blank"}  from **@dildick**: CSC TP bugfixes for high PU running `dqm`  `l1`  `upgrade`  created: 2017-05-15T16:21:24Z merged: 2017-05-18T14:46:26Z

1. [18739](http://github.com/cms-sw/cmssw/pull/18739){:target="_blank"}  from **@arizzi**: Pack triggerobject standalone and photons/muon updated packing for miniaod `analysis`  `operations`  `reconstruction`  created: 2017-05-15T14:50:08Z merged: 2017-06-01T10:09:38Z

1. [18728](http://github.com/cms-sw/cmssw/pull/18728){:target="_blank"}  from **@VinInn**: CA for Phase2 tracking + few more smaller-impact optimizations `reconstruction`  `upgrade`  created: 2017-05-14T16:48:09Z merged: 2017-05-23T06:03:51Z

1. [18724](http://github.com/cms-sw/cmssw/pull/18724){:target="_blank"}  from **@VinInn**: make const correct muon seeding in tracking `reconstruction`  created: 2017-05-13T10:12:27Z merged: 2017-05-22T11:57:29Z

1. [18718](http://github.com/cms-sw/cmssw/pull/18718){:target="_blank"}  from **@CTPPS**: CTPPS: DQM configuration fix `dqm`  created: 2017-05-12T18:57:18Z merged: 2017-05-28T08:03:38Z

1. [18711](http://github.com/cms-sw/cmssw/pull/18711){:target="_blank"}  from **@akhukhun**: adjust HF TP emulator and compression LUTs `l1`  created: 2017-05-12T13:15:13Z merged: 2017-05-31T06:42:46Z

1. [18696](http://github.com/cms-sw/cmssw/pull/18696){:target="_blank"}  from **@jhgoh**: MuonCaloCompatibility fix to reduce number of file handle `reconstruction`  created: 2017-05-11T14:27:39Z merged: 2017-05-22T10:24:54Z

1. [18689](http://github.com/cms-sw/cmssw/pull/18689){:target="_blank"}  from **@archiron**: miniAODIsolation_91X_V2 `dqm`  created: 2017-05-11T12:15:18Z merged: 2017-05-27T07:53:56Z

1. [18684](http://github.com/cms-sw/cmssw/pull/18684){:target="_blank"}  from **@mandrenguyen**: Remove HF/Voronoi subtraction for jets in heavy ions and disable centrality bin producer `dqm`  `reconstruction`  created: 2017-05-10T22:30:43Z merged: 2017-05-20T12:05:48Z

1. [18646](http://github.com/cms-sw/cmssw/pull/18646){:target="_blank"}  from **@abaty**: First Round of Phase 1 Tracking changes for Heavy Ions `reconstruction`  created: 2017-05-09T18:54:04Z merged: 2017-05-30T20:40:36Z

1. [18638](http://github.com/cms-sw/cmssw/pull/18638){:target="_blank"}  from **@mtosi**: add NumberOfEventsPerLS EDFilter `analysis`  created: 2017-05-09T15:26:19Z merged: 2017-05-30T10:36:19Z

1. [18634](http://github.com/cms-sw/cmssw/pull/18634){:target="_blank"}  from **@smuzaffar**: preparing for dasgoclient: implement get_value in cmssw_das_client `core`  created: 2017-05-09T14:28:40Z merged: 2017-05-18T09:37:50Z

1. [18548](http://github.com/cms-sw/cmssw/pull/18548){:target="_blank"}  from **@bjmarsh**: Add mini-isolation for leptons and a new collection of Isolated Tracks in MiniAOD `analysis`  `reconstruction`  created: 2017-05-02T20:17:14Z merged: 2017-05-23T09:44:46Z

1. [18540](http://github.com/cms-sw/cmssw/pull/18540){:target="_blank"}  from **@enochnotsocool**: Raw ADC value computation efficiency fix `dqm`  created: 2017-05-02T13:19:37Z merged: 2017-05-24T14:25:20Z

1. [18531](http://github.com/cms-sw/cmssw/pull/18531){:target="_blank"}  from **@dimattia**: DQM quality monitor for SiStrip Gain (G2) from Multi Run Harvesting  `alca`  created: 2017-05-01T14:20:02Z merged: 2017-06-01T12:43:22Z

1. [18517](http://github.com/cms-sw/cmssw/pull/18517){:target="_blank"}  from **@kkotov**: Moving the Prescale ES producer to the new parser and deleting old XML parser `l1`  created: 2017-04-28T14:28:46Z merged: 2017-05-31T08:15:10Z

1. [18447](http://github.com/cms-sw/cmssw/pull/18447){:target="_blank"}  from **@enochnotsocool**: Digi occupancy plot rotated + FED range adjusted (91X) `dqm`  created: 2017-04-24T09:51:29Z merged: 2017-05-31T10:50:22Z

1. [18364](http://github.com/cms-sw/cmssw/pull/18364){:target="_blank"}  from **@mtosi**: add HLT HCAL DQM/Validation `dqm`  `hlt`  created: 2017-04-14T14:37:24Z merged: 2017-05-31T10:52:20Z

1. [18236](http://github.com/cms-sw/cmssw/pull/18236){:target="_blank"}  from **@CMS-HGCAL**: Collected HGCal reconstruction changes `reconstruction`  `upgrade`  created: 2017-04-06T07:54:26Z merged: 2017-05-28T08:05:01Z

#### CMSDIST Changes between Tags REL/CMSSW_9_2_0_patch5/slc6_amd64_gcc530 and REL/CMSSW_9_2_1/slc6_amd64_gcc530:
[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_9_2_0_patch5/slc6_amd64_gcc530...REL/CMSSW_9_2_1/slc6_amd64_gcc530)



1. [3081](http://github.com/cms-sw/cmssw/pull/3081){:target="_blank"}  from **@cms-sw**: Use new build rule tag V05-05-24 created: 2014-03-28T18:09:14Z merged: 2014-03-28T19:01:29Z

1. [3077](http://github.com/cms-sw/cmssw/pull/3077){:target="_blank"}  from **@davidlange6**: Adding hep_ml, rep, uncertainties tools - fixing python path for xrootd created: 2014-03-28T16:23:26Z merged: 2014-03-28T16:32:08Z

1. [3072](http://github.com/cms-sw/cmssw/pull/3072){:target="_blank"}  from **@mrodozov**: Updating utm.spec for new tag usage created: 2014-03-28T15:19:15Z merged: 2014-03-31T11:49:45Z

1. [3068](http://github.com/cms-sw/cmssw/pull/3068){:target="_blank"}  from **@TaiSakuma**: update pandas version to 0.20.1 for 9_2_X created: 2014-03-28T12:39:13Z merged: 2014-03-29T10:58:16Z

1. [3064](http://github.com/cms-sw/cmssw/pull/3064){:target="_blank"}  from **@smuzaffar**: updated cms-git-tools which contains new git-cms-checkout-topic created: 2014-03-28T08:47:51Z merged: 2014-03-28T12:43:31Z

1. [3055](http://github.com/cms-sw/cmssw/pull/3055){:target="_blank"}  from **@cms-sw**: Update data-L1Trigger-L1TCalorimeter.spec created: 2014-03-27T16:40:14Z merged: 2014-03-27T16:42:36Z

1. [3040](http://github.com/cms-sw/cmssw/pull/3040){:target="_blank"}  from **@davidlange6**: add prwlock tool created: 2014-03-26T19:18:03Z merged: 2014-03-27T15:03:11Z

1. [3013](http://github.com/cms-sw/cmssw/pull/3013){:target="_blank"}  from **@mkirsano**: Upgrade pythia8 to 226 created: 2014-03-25T13:14:50Z merged: 2014-03-25T20:25:35Z
