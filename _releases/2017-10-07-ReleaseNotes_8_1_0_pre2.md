---
layout: post
title:  "8_1_0_pre2"
date:   2017-10-07 22:24:56 +0200
categories: cmssw
relmajor: 8
relminor: 1
relsubminor: 0
relpre: _pre2
---

# CMSSW_8_1_0_pre2
#### Changes since CMSSW_8_1_0_pre1:

[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_8_1_0_pre1...CMSSW_8_1_0_pre2)



1. [13941](http://github.com/cms-sw/cmssw/pull/13941){:target="_blank"}  from **@davidlange6**: more era migration in relval matrix  `comparison`  `pdmv`  created: 2016-04-05T18:36:15Z merged: 2016-04-05T18:50:07Z

1. [13939](http://github.com/cms-sw/cmssw/pull/13939){:target="_blank"}  from **@mdhildreth**: PreMixing era switch for Stage 2 L1 configuration `comparison`  `operations`  created: 2016-04-05T17:58:11Z merged: 2016-04-05T18:50:26Z

1. [13919](http://github.com/cms-sw/cmssw/pull/13919){:target="_blank"}  from **@davidlange6**: move to 2016 era and 2016 hlt where it is working in relvals `alca`  `core`  `hlt`  `l1`  `pdmv`  created: 2016-04-04T17:36:29Z merged: 2016-04-04T20:35:31Z

1. [13913](http://github.com/cms-sw/cmssw/pull/13913){:target="_blank"}  from **@ianna**: Remove Obsolete Customizations `geometry`  created: 2016-04-04T13:09:22Z merged: 2016-04-05T14:28:50Z

1. [13903](http://github.com/cms-sw/cmssw/pull/13903){:target="_blank"}  from **@cms-l1t-offline**: HLT L1T interface updates - trhow exceptions and L1GlobalDecision  80x `hlt`  created: 2016-04-03T19:04:46Z merged: 2016-04-04T17:51:34Z

1. [13901](http://github.com/cms-sw/cmssw/pull/13901){:target="_blank"}  from **@wmtan**: use std::make_shared in framework (again) `core`  created: 2016-04-02T19:21:35Z merged: 2016-04-04T19:56:59Z

1. [13899](http://github.com/cms-sw/cmssw/pull/13899){:target="_blank"}  from **@wmtan**: Use std::shared_ptr and std::make_shared (EventSetup in Simulation) `reconstruction`  `simulation`  created: 2016-04-02T15:38:12Z merged: 2016-04-04T21:54:39Z

1. [13898](http://github.com/cms-sw/cmssw/pull/13898){:target="_blank"}  from **@wmtan**: use std::shared_ptr and std::make_shared (EventSetup in Reco) `alca`  `reconstruction`  created: 2016-04-02T15:34:12Z merged: 2016-04-04T21:54:56Z

1. [13897](http://github.com/cms-sw/cmssw/pull/13897){:target="_blank"}  from **@wmtan**: use std::shared_ptr and std::make_shared (EventSetup in Geometry/Alignment/Visualization) `alca`  `geometry`  `visualization`  created: 2016-04-02T15:27:34Z merged: 2016-04-04T17:49:46Z

1. [13896](http://github.com/cms-sw/cmssw/pull/13896){:target="_blank"}  from **@wmtan**: Use std::shared_ptr and std::make_shared (EventSetup in FastSim) `fastsim`  created: 2016-04-02T15:23:08Z merged: 2016-04-04T17:50:08Z

1. [13895](http://github.com/cms-sw/cmssw/pull/13895){:target="_blank"}  from **@wmtan**: use std::shared_ptr and std::make_shared (EventSetup in Calibration) `alca`  `l1`  created: 2016-04-02T15:19:58Z merged: 2016-04-05T14:29:11Z

1. [13891](http://github.com/cms-sw/cmssw/pull/13891){:target="_blank"}  from **@cms-l1t-offline**: L1Trigger DQM Combo PR 13800 fixed merge conflict `dqm`  `l1`  created: 2016-04-02T11:33:26Z merged: 2016-04-05T14:41:15Z

1. [13885](http://github.com/cms-sw/cmssw/pull/13885){:target="_blank"}  from **@makortel**: Fix compilation under EDM_ML_DEBUG `analysis`  `reconstruction`  created: 2016-04-01T15:01:04Z merged: 2016-04-02T06:38:16Z

1. [13873](http://github.com/cms-sw/cmssw/pull/13873){:target="_blank"}  from **@Sam-Harper**: Bug fix for Electron Tracker Isolation used by HEEP   `reconstruction`  created: 2016-03-31T11:37:47Z merged: 2016-04-02T06:38:32Z

1. [13872](http://github.com/cms-sw/cmssw/pull/13872){:target="_blank"}  from **@bsunanda**: bsunanda:Phase2-hgx47 Update the ganging for BH as discussed in the simulation meeting `geometry`  created: 2016-03-30T16:21:22Z merged: 2016-04-02T06:38:47Z

1. [13870](http://github.com/cms-sw/cmssw/pull/13870){:target="_blank"}  from **@smuzaffar**: remove unused testRandomNumberGenerators binary `core`  created: 2016-03-30T14:37:31Z merged: 2016-03-31T07:46:17Z

1. [13869](http://github.com/cms-sw/cmssw/pull/13869){:target="_blank"}  from **@Sam-Harper**: Eg HLT PM module fixes for the auto->unique ptr central migration `hlt`  created: 2016-03-30T13:37:26Z merged: 2016-03-30T16:25:37Z

1. [13868](http://github.com/cms-sw/cmssw/pull/13868){:target="_blank"}  from **@akhukhun**: fix HF TP transcoder crash. `alca`  `l1`  created: 2016-03-30T12:39:11Z merged: 2016-04-02T08:13:03Z

1. [13867](http://github.com/cms-sw/cmssw/pull/13867){:target="_blank"}  from **@davidlange6**: add some phase2 (sim only) workflows to the default matrix `pdmv`  created: 2016-03-30T12:01:55Z merged: 2016-04-02T08:12:23Z

1. [13866](http://github.com/cms-sw/cmssw/pull/13866){:target="_blank"}  from **@smuzaffar**: Move L1Trigger/CSCTrackFinder/src/core_ files to external package `l1`  created: 2016-03-30T10:59:32Z merged: 2016-04-04T17:50:27Z

1. [13860](http://github.com/cms-sw/cmssw/pull/13860){:target="_blank"}  from **@alja**: 80x Fireworks: Set classic root gui style `comparison`  `visualization`  created: 2016-03-29T21:16:34Z merged: 2016-03-30T07:49:46Z

1. [13859](http://github.com/cms-sw/cmssw/pull/13859){:target="_blank"}  from **@Dr15Jones**: mv test record.cppunit.cpp from DataFormats/FWLite to PhysicsTools/Co `analysis`  `core`  created: 2016-03-29T19:32:14Z merged: 2016-03-30T07:45:48Z

1. [13857](http://github.com/cms-sw/cmssw/pull/13857){:target="_blank"}  from **@jruizvar**: Adding double-electron triggers to EXO DQM (81X) `dqm`  created: 2016-03-29T17:38:42Z merged: 2016-03-31T07:50:42Z

1. [13855](http://github.com/cms-sw/cmssw/pull/13855){:target="_blank"}  from **@wmtan**: Change auto_ptr to unique_ptr in text `core`  created: 2016-03-29T16:38:56Z merged: 2016-03-30T07:46:04Z

1. [13852](http://github.com/cms-sw/cmssw/pull/13852){:target="_blank"}  from **@Martin-Grunewald**: Less verbose HLTPrescaleProvider (81X) `hlt`  created: 2016-03-29T12:14:12Z merged: 2016-03-30T07:46:41Z

1. [13850](http://github.com/cms-sw/cmssw/pull/13850){:target="_blank"}  from **@alja**: 8x Fireworks: move clipping cone apex in 3D region view  `comparison`  `visualization`  created: 2016-03-28T21:38:50Z merged: 2016-03-29T08:33:03Z

1. [13848](http://github.com/cms-sw/cmssw/pull/13848){:target="_blank"}  from **@bsunanda**: bsunanda:Phase2-gem12 Get geometry information of GEM detector `geometry`  created: 2016-03-28T15:36:51Z merged: 2016-03-30T07:46:58Z

1. [13846](http://github.com/cms-sw/cmssw/pull/13846){:target="_blank"}  from **@Sam-Harper**: E/g HLT Pixel Match Variable Producer `hlt`  created: 2016-03-27T08:04:24Z merged: 2016-03-30T07:54:44Z

1. [13834](http://github.com/cms-sw/cmssw/pull/13834){:target="_blank"}  from **@bsunanda**: bsunanda:Phase2-gem11 More realistic ME0 geometry and extended GE21 geometry `geometry`  created: 2016-03-24T19:35:01Z merged: 2016-04-02T08:11:27Z

1. [13831](http://github.com/cms-sw/cmssw/pull/13831){:target="_blank"}  from **@VinInn**: Speedup Gsf component merging, return components by const reference `analysis`  `reconstruction`  created: 2016-03-24T15:17:07Z merged: 2016-04-04T17:50:49Z

1. [13823](http://github.com/cms-sw/cmssw/pull/13823){:target="_blank"}  from **@lihux25**: Fix crash in HcalDumpConditions.cc  `comparison`  `db`  created: 2016-03-24T05:11:19Z merged: 2016-03-26T08:13:23Z

1. [13822](http://github.com/cms-sw/cmssw/pull/13822){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-hcx76 Remove obsolete parameter definitions for relabelling at DIGI step `geometry`  `simulation`  created: 2016-03-23T22:28:22Z merged: 2016-03-30T07:54:39Z

1. [13821](http://github.com/cms-sw/cmssw/pull/13821){:target="_blank"}  from **@mmusich**: Introducing realistic phase-I simuation key `alca`  `pdmv`  `simulation`  created: 2016-03-23T21:59:44Z merged: 2016-03-28T10:18:18Z

1. [13820](http://github.com/cms-sw/cmssw/pull/13820){:target="_blank"}  from **@wmtan**: Use unique_ptr, not auto_ptr `analysis`  `core`  `reconstruction`  created: 2016-03-23T20:03:30Z merged: 2016-03-28T20:44:27Z

1. [13819](http://github.com/cms-sw/cmssw/pull/13819){:target="_blank"}  from **@VinInn**: Speed seeding for HLT `geometry`  `reconstruction`  `simulation`  created: 2016-03-23T15:08:10Z merged: 2016-04-04T17:51:02Z

1. [13814](http://github.com/cms-sw/cmssw/pull/13814){:target="_blank"}  from **@hroskes**: Fix consumes for alignment validations `alca`  `reconstruction`  created: 2016-03-23T13:43:41Z merged: 2016-03-28T10:17:56Z

1. [13809](http://github.com/cms-sw/cmssw/pull/13809){:target="_blank"}  from **@cms-l1t-offline**: Fix crash in CorrelationConditions uGT emulator `l1`  created: 2016-03-23T07:23:50Z merged: 2016-03-24T08:36:17Z

1. [13808](http://github.com/cms-sw/cmssw/pull/13808){:target="_blank"}  from **@cms-l1t-offline**: Fix crash in CorrelationConditions uGT emulator  `l1`  created: 2016-03-23T07:22:12Z merged: 2016-03-23T18:09:14Z

1. [13803](http://github.com/cms-sw/cmssw/pull/13803){:target="_blank"}  from **@akhukhun**: Adjusting 1x1 HF output LUTs `alca`  `comparison`  `l1`  created: 2016-03-22T16:49:16Z merged: 2016-03-24T10:47:20Z

1. [13801](http://github.com/cms-sw/cmssw/pull/13801){:target="_blank"}  from **@mtosi**: drop pixel vertices (they are not available since run2 !) `dqm`  created: 2016-03-22T16:18:37Z merged: 2016-03-25T06:33:21Z

1. [13799](http://github.com/cms-sw/cmssw/pull/13799){:target="_blank"}  from **@bsunanda**: bsunanda:Phase2-hgx46 Update a test cfi file for testing finer segmentation of BH `geometry`  created: 2016-03-22T14:04:20Z merged: 2016-03-28T20:41:15Z

1. [13797](http://github.com/cms-sw/cmssw/pull/13797){:target="_blank"}  from **@hengne**: relval matrix updates  `pdmv`  created: 2016-03-22T10:49:25Z merged: 2016-03-28T10:22:17Z

1. [13793](http://github.com/cms-sw/cmssw/pull/13793){:target="_blank"}  from **@jdolen**: Update miniAOD AK8 userFloat content. Add PUPPI substructure. Remove CMSTT. `analysis`  `comparison`  `reconstruction`  created: 2016-03-21T18:26:25Z merged: 2016-03-28T10:20:16Z

1. [13792](http://github.com/cms-sw/cmssw/pull/13792){:target="_blank"}  from **@Martin-Grunewald**: Fix forgotten saveTags default switchover (81X) `hlt`  created: 2016-03-21T15:32:00Z merged: 2016-03-22T16:52:15Z

1. [13791](http://github.com/cms-sw/cmssw/pull/13791){:target="_blank"}  from **@Martin-Grunewald**: Fix forgotten saveTags default switchover `hlt`  created: 2016-03-21T15:28:26Z merged: 2016-03-22T16:40:46Z

1. [13790](http://github.com/cms-sw/cmssw/pull/13790){:target="_blank"}  from **@mmusich**: Adding the Stage-II L1 menu to phase-I upgrade simulation `alca`  created: 2016-03-21T13:53:50Z merged: 2016-03-22T16:40:59Z

1. [13787](http://github.com/cms-sw/cmssw/pull/13787){:target="_blank"}  from **@cms-l1t-offline**: Fixes in L1T Calo packers - useful for data taking - 81x `l1`  created: 2016-03-21T12:34:24Z merged: 2016-03-22T16:51:52Z

1. [13786](http://github.com/cms-sw/cmssw/pull/13786){:target="_blank"}  from **@cms-l1t-offline**: Fixes in L1T Calo packers - useful for data taking - 80x `l1`  created: 2016-03-21T10:53:18Z merged: 2016-03-22T16:40:21Z

1. [13784](http://github.com/cms-sw/cmssw/pull/13784){:target="_blank"}  from **@mmusich**: Adding the Stage-II L1 menu to phase-I upgrade simulation `alca`  created: 2016-03-21T08:55:57Z merged: 2016-03-21T18:33:58Z

1. [13782](http://github.com/cms-sw/cmssw/pull/13782){:target="_blank"}  from **@cms-l1t-offline**: Change LogWarning to LogTrace `hlt`  created: 2016-03-20T13:26:18Z merged: 2016-03-21T07:35:31Z

1. [13781](http://github.com/cms-sw/cmssw/pull/13781){:target="_blank"}  from **@cms-l1t-offline**: Change LogWarning to LogTrace `hlt`  created: 2016-03-20T13:25:40Z merged: 2016-03-21T07:36:36Z

1. [13780](http://github.com/cms-sw/cmssw/pull/13780){:target="_blank"}  from **@cms-l1t-offline**: Fix TriggerObjectMap filling with a long L1T menu. `l1`  created: 2016-03-19T02:52:13Z merged: 2016-03-22T16:40:35Z

1. [13779](http://github.com/cms-sw/cmssw/pull/13779){:target="_blank"}  from **@cms-l1t-offline**: Fix TriggerObjectMap filling with a long L1T menu. `l1`  created: 2016-03-19T02:48:20Z merged: 2016-03-22T16:52:32Z

1. [13778](http://github.com/cms-sw/cmssw/pull/13778){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-hcx75 Backport the changes from PR 13683 (2016 Geometry of Hcal) needed to work on updating constants to Hcal DB `geometry`  created: 2016-03-18T21:58:15Z merged: 2016-03-22T16:42:16Z

1. [13774](http://github.com/cms-sw/cmssw/pull/13774){:target="_blank"}  from **@civanch**: cleanup of the TestBeam `simulation`  created: 2016-03-18T16:16:35Z merged: 2016-03-19T07:39:20Z

1. [13773](http://github.com/cms-sw/cmssw/pull/13773){:target="_blank"}  from **@mandrenguyen**: Filter to select HLT paths corresponding to peripheral HI events `reconstruction`  created: 2016-03-18T16:04:20Z merged: 2016-03-23T10:51:04Z

1. [13772](http://github.com/cms-sw/cmssw/pull/13772){:target="_blank"}  from **@jpazzini**: FEDid-wheel mapping fixed for +1 and +2 `comparison`  `l1`  created: 2016-03-18T11:22:20Z merged: 2016-03-22T16:54:18Z

1. [13770](http://github.com/cms-sw/cmssw/pull/13770){:target="_blank"}  from **@ggovi**: Allow empty user text in tag log entries `db`  created: 2016-03-18T09:36:08Z merged: 2016-03-25T06:32:48Z

1. [13769](http://github.com/cms-sw/cmssw/pull/13769){:target="_blank"}  from **@wmtan**: Deep const correctness for edm::value_ptr `core`  created: 2016-03-18T03:35:14Z merged: 2016-03-21T18:33:41Z

1. [13768](http://github.com/cms-sw/cmssw/pull/13768){:target="_blank"}  from **@cms-l1t-offline**: Bring L1T emulation up to date with l1t-tsg-v4 tag `alca`  `db`  `l1`  created: 2016-03-18T03:13:08Z merged: 2016-04-01T08:28:51Z

1. [13766](http://github.com/cms-sw/cmssw/pull/13766){:target="_blank"}  from **@CTPPS**: Adding new detectors - integration of RomanPot detectors for CTPPS project `comparison`  `simulation`  created: 2016-03-17T19:39:27Z merged: 2016-03-21T08:54:07Z

1. [13765](http://github.com/cms-sw/cmssw/pull/13765){:target="_blank"}  from **@wmtan**: Remove duplicated functions in Provenance.h `core`  `dqm`  `hlt`  created: 2016-03-17T19:22:59Z merged: 2016-03-18T08:29:58Z

1. [13762](http://github.com/cms-sw/cmssw/pull/13762){:target="_blank"}  from **@mplaner**: updated DQM module for Higgs->diphoton 2016 trigger `dqm`  created: 2016-03-17T19:04:28Z merged: 2016-03-22T16:59:40Z

1. [13756](http://github.com/cms-sw/cmssw/pull/13756){:target="_blank"}  from **@thuer**: Cmssw 81 x sherpa weights `generators`  created: 2016-03-17T15:00:50Z merged: 2016-03-22T17:32:21Z

1. [13755](http://github.com/cms-sw/cmssw/pull/13755){:target="_blank"}  from **@boudoul**: Revert "updating  TrackerGeometry in Geometry/TrackerGeometryBuilder to accom" `geometry`  `simulation`  created: 2016-03-17T14:12:03Z merged: 2016-03-19T07:39:35Z

1. [13753](http://github.com/cms-sw/cmssw/pull/13753){:target="_blank"}  from **@makortel**: Quadruplet seeding by propagating triplet to 4th layer `alca`  `hlt`  `reconstruction`  created: 2016-03-17T12:10:02Z merged: 2016-03-29T08:37:52Z

1. [13751](http://github.com/cms-sw/cmssw/pull/13751){:target="_blank"}  from **@cms-btv-pog**: Bugfix in the BoostedDoubleSV tagger (80X) `reconstruction`  created: 2016-03-17T11:06:48Z merged: 2016-03-21T07:29:46Z

1. [13749](http://github.com/cms-sw/cmssw/pull/13749){:target="_blank"}  from **@cms-btv-pog**: Bugfix in the BoostedDoubleSV tagger (81X) `reconstruction`  created: 2016-03-17T11:04:44Z merged: 2016-03-19T07:39:46Z

1. [13748](http://github.com/cms-sw/cmssw/pull/13748){:target="_blank"}  from **@lgray**: Fix non-linearity from C++ in HGCDigitizer `simulation`  created: 2016-03-17T09:26:00Z merged: 2016-03-18T13:16:31Z

1. [13747](http://github.com/cms-sw/cmssw/pull/13747){:target="_blank"}  from **@slava77**: locally named load of FEVT in hotlineSkims (same as #13746) `alca`  created: 2016-03-17T07:44:06Z merged: 2016-03-17T09:03:20Z

1. [13746](http://github.com/cms-sw/cmssw/pull/13746){:target="_blank"}  from **@slava77**: locally named load of FEVT in hotlineSkims `alca`  created: 2016-03-17T07:42:41Z merged: 2016-03-17T09:02:18Z

1. [13745](http://github.com/cms-sw/cmssw/pull/13745){:target="_blank"}  from **@wmtan**: Remove Obsolete Header HideStdUniquePtrFromRoot.h `core`  `reconstruction`  created: 2016-03-16T22:26:48Z merged: 2016-03-18T08:30:12Z

1. [13742](http://github.com/cms-sw/cmssw/pull/13742){:target="_blank"}  from **@jpazzini**: FEDid-wheel mapping fixed for +1 and +2 `l1`  created: 2016-03-16T15:39:26Z merged: 2016-03-22T16:53:41Z

1. [13741](http://github.com/cms-sw/cmssw/pull/13741){:target="_blank"}  from **@alja**: 80x Fireworks: Port change in FWSiPixelClusterPB from 71 `comparison`  `visualization`  created: 2016-03-16T14:02:44Z merged: 2016-03-17T09:04:16Z

1. [13740](http://github.com/cms-sw/cmssw/pull/13740){:target="_blank"}  from **@mmusich**: Global Tag updates for 80x: introducing new L1 uGT stage-II menu and MC updates for Digi-Reco `alca`  `pdmv`  created: 2016-03-16T13:55:36Z merged: 2016-03-21T08:33:32Z

1. [13739](http://github.com/cms-sw/cmssw/pull/13739){:target="_blank"}  from **@jsalfeld**: 80 x add 2016 spring mc pileup scenario v1 `comparison`  `operations`  `simulation`  created: 2016-03-16T13:40:13Z merged: 2016-03-16T13:41:03Z

1. [13738](http://github.com/cms-sw/cmssw/pull/13738){:target="_blank"}  from **@makortel**: Fix typo in Types.py `core`  created: 2016-03-16T12:02:35Z merged: 2016-03-17T09:01:59Z

1. [13737](http://github.com/cms-sw/cmssw/pull/13737){:target="_blank"}  from **@ianna**: Add 2023 Scenarios `comparison`  `visualization`  created: 2016-03-16T09:55:11Z merged: 2016-03-17T09:01:45Z

1. [13736](http://github.com/cms-sw/cmssw/pull/13736){:target="_blank"}  from **@makortel**: Introduce new tracking sequence for phase1 (2017) `dqm`  `operations`  `reconstruction`  created: 2016-03-16T07:55:18Z merged: 2016-03-22T17:32:52Z

1. [13735](http://github.com/cms-sw/cmssw/pull/13735){:target="_blank"}  from **@wmtan**: Remove unneeded selector `core`  created: 2016-03-15T21:17:23Z merged: 2016-03-16T16:47:04Z

1. [13732](http://github.com/cms-sw/cmssw/pull/13732){:target="_blank"}  from **@Martin-Grunewald**: Need unqiue cfi file names in fillDescription to avoid overwriting in HLT (81X) `alca`  `hlt`  created: 2016-03-15T16:38:21Z merged: 2016-03-16T12:42:52Z

1. [13730](http://github.com/cms-sw/cmssw/pull/13730){:target="_blank"}  from **@makortel**: Fix RectangularEtaPhiTrackingRegion (80X) `reconstruction`  created: 2016-03-15T16:38:09Z merged: 2016-03-17T09:03:35Z

1. [13729](http://github.com/cms-sw/cmssw/pull/13729){:target="_blank"}  from **@makortel**: Fix RectangularEtaPhiTrackingRegion `reconstruction`  created: 2016-03-15T16:37:50Z merged: 2016-03-17T09:01:31Z

1. [13728](http://github.com/cms-sw/cmssw/pull/13728){:target="_blank"}  from **@Martin-Grunewald**: Need unqiue cfi file names in fillDescription to avoid overwriting in HLT (80X) `alca`  `hlt`  created: 2016-03-15T16:34:12Z merged: 2016-03-16T13:17:38Z

1. [13727](http://github.com/cms-sw/cmssw/pull/13727){:target="_blank"}  from **@Dr15Jones**: Made EarlyDeleteHelper thread-safe `core`  created: 2016-03-15T13:57:31Z merged: 2016-03-15T16:47:38Z

1. [13724](http://github.com/cms-sw/cmssw/pull/13724){:target="_blank"}  from **@dimattia**: Implementation of the new gain Calibration paradigma in 8_1_X `alca`  `dqm`  `operations`  `pdmv`  created: 2016-03-15T11:12:16Z merged: 2016-03-24T08:45:26Z

1. [13722](http://github.com/cms-sw/cmssw/pull/13722){:target="_blank"}  from **@wmtan**: Avoid unneeded retrievel of per event provenance `alca`  `analysis`  `core`  `dqm`  `reconstruction`  `visualization`  created: 2016-03-15T03:33:56Z merged: 2016-03-16T12:48:57Z

1. [13720](http://github.com/cms-sw/cmssw/pull/13720){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-alca37 Fix bug to avoid run-time error for Pythia8 `generators`  created: 2016-03-14T19:23:29Z merged: 2016-03-15T14:43:56Z

1. [13719](http://github.com/cms-sw/cmssw/pull/13719){:target="_blank"}  from **@bsunanda**: bsunanda"Phase2-hgx44 Complete the example of TB for HGCal `reconstruction`  `simulation`  created: 2016-03-14T18:44:57Z merged: 2016-03-17T09:01:17Z

1. [13718](http://github.com/cms-sw/cmssw/pull/13718){:target="_blank"}  from **@Dr15Jones**: Pass non nullptr to std::unique_ptr guard `core`  created: 2016-03-14T17:06:05Z merged: 2016-03-15T08:41:57Z

1. [13716](http://github.com/cms-sw/cmssw/pull/13716){:target="_blank"}  from **@hengne**: Fix re-reco golden json, adding 50ns lumi blocks coverage `pdmv`  created: 2016-03-14T15:12:49Z merged: 2016-03-15T08:43:57Z

1. [13715](http://github.com/cms-sw/cmssw/pull/13715){:target="_blank"}  from **@hengne**: Fix re-reco golden json, adding 50ns lumi blocks coverage `pdmv`  created: 2016-03-14T15:08:08Z merged: 2016-03-16T13:10:34Z

1. [13714](http://github.com/cms-sw/cmssw/pull/13714){:target="_blank"}  from **@ianna**: Sync Materials in 2015 Dev Scenario `geometry`  created: 2016-03-14T14:12:22Z merged: 2016-03-15T11:08:58Z

1. [13711](http://github.com/cms-sw/cmssw/pull/13711){:target="_blank"}  from **@ghellwig**: Multi-IOV weak mode constraints (Backport of #13710) `alca`  created: 2016-03-14T13:13:12Z merged: 2016-03-22T16:41:20Z

1. [13710](http://github.com/cms-sw/cmssw/pull/13710){:target="_blank"}  from **@ghellwig**: Multi-IOV weak mode constraints `alca`  created: 2016-03-14T13:11:41Z merged: 2016-03-17T08:59:21Z

1. [13709](http://github.com/cms-sw/cmssw/pull/13709){:target="_blank"}  from **@mmusich**: Global Tag updates for 81x: introducing new L1 uGT stage-II menu and MC updates for Digi-Reco  `alca`  `pdmv`  created: 2016-03-14T13:01:00Z merged: 2016-03-18T12:13:32Z

1. [13708](http://github.com/cms-sw/cmssw/pull/13708){:target="_blank"}  from **@lgray**: Picosecond stepping for HGC and FastTimer SDs `simulation`  created: 2016-03-14T12:57:12Z merged: 2016-03-19T07:39:56Z

1. [13707](http://github.com/cms-sw/cmssw/pull/13707){:target="_blank"}  from **@cms-l1t-offline**: Rekovic hlt 802 seed unpacked gt (pruning on top of PR 13703) `hlt`  created: 2016-03-14T10:54:36Z merged: 2016-03-15T08:42:18Z

1. [13706](http://github.com/cms-sw/cmssw/pull/13706){:target="_blank"}  from **@suchandradutta**: updating  TrackerGeometry in Geometry/TrackerGeometryBuilder to accom `geometry`  `simulation`  created: 2016-03-14T10:47:40Z merged: 2016-03-15T09:39:19Z

1. [13705](http://github.com/cms-sw/cmssw/pull/13705){:target="_blank"}  from **@ianna**: Fix Validation Script `db`  `dqm`  `geometry`  created: 2016-03-14T10:46:21Z merged: 2016-03-15T16:48:01Z

1. [13703](http://github.com/cms-sw/cmssw/pull/13703){:target="_blank"}  from **@cms-l1t-offline**: Rekovic hlt 802 seed unpacked gt `hlt`  created: 2016-03-12T15:53:41Z merged: 2016-03-14T08:46:49Z

1. [13702](http://github.com/cms-sw/cmssw/pull/13702){:target="_blank"}  from **@cms-l1t-offline**: Rekovic hlt 802 seed unpacked gt `hlt`  created: 2016-03-12T15:52:13Z merged: 2016-03-15T09:32:39Z

1. [13698](http://github.com/cms-sw/cmssw/pull/13698){:target="_blank"}  from **@Dr15Jones**: Refactored ProductHolders `core`  created: 2016-03-11T20:30:03Z merged: 2016-03-14T08:40:00Z

1. [13695](http://github.com/cms-sw/cmssw/pull/13695){:target="_blank"}  from **@jsalfeld**: 80 x add 2016 spring mc pileup scenario v1 `operations`  `simulation`  created: 2016-03-11T14:36:04Z merged: 2016-03-16T13:40:22Z

1. [13693](http://github.com/cms-sw/cmssw/pull/13693){:target="_blank"}  from **@Martin-Grunewald**:  Fix: 50ns used legacy L1 (backport of #13692) `operations`  created: 2016-03-11T13:25:29Z merged: 2016-03-15T17:04:45Z

1. [13691](http://github.com/cms-sw/cmssw/pull/13691){:target="_blank"}  from **@dmitrijus**: Fix DQM/L1TMonitor BuildFile `dqm`  created: 2016-03-11T11:42:36Z merged: 2016-03-15T08:42:38Z

1. [13688](http://github.com/cms-sw/cmssw/pull/13688){:target="_blank"}  from **@slava77**: cleanup unnamed sequences in TrackingDQMSourceTier0\* `dqm`  created: 2016-03-11T08:31:25Z merged: 2016-03-15T08:43:00Z

1. [13687](http://github.com/cms-sw/cmssw/pull/13687){:target="_blank"}  from **@bsunanda**: bsunanda:Phase2-hgx43 Takes care of half cell positions `geometry`  created: 2016-03-11T02:52:02Z merged: 2016-03-15T08:43:11Z

1. [13686](http://github.com/cms-sw/cmssw/pull/13686){:target="_blank"}  from **@cms-btv-pog**: PAT btag update (80X) `analysis`  `reconstruction`  created: 2016-03-11T02:13:44Z merged: 2016-03-17T09:05:38Z

1. [13685](http://github.com/cms-sw/cmssw/pull/13685){:target="_blank"}  from **@cms-btv-pog**: PAT btag update (81X) `analysis`  `reconstruction`  created: 2016-03-11T02:05:31Z merged: 2016-03-17T08:57:58Z

1. [13684](http://github.com/cms-sw/cmssw/pull/13684){:target="_blank"}  from **@bendavid**: Changes needed for SUSY parameter scans (80x) `analysis`  `generators`  `reconstruction`  created: 2016-03-10T21:41:32Z merged: 2016-03-17T09:05:12Z

1. [13683](http://github.com/cms-sw/cmssw/pull/13683){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-hcx74 Add scenario to help testing 2016 HCAL setup `geometry`  created: 2016-03-10T19:13:30Z merged: 2016-03-17T18:45:49Z

1. [13682](http://github.com/cms-sw/cmssw/pull/13682){:target="_blank"}  from **@slava77**:  delete loaded cleanPatJets after the temporary load if it was not around already (same as #13681 ) `analysis`  created: 2016-03-10T19:02:45Z merged: 2016-03-17T09:07:25Z

1. [13681](http://github.com/cms-sw/cmssw/pull/13681){:target="_blank"}  from **@slava77**: delete loaded cleanPatJets after the temporary load if it was not around already `analysis`  created: 2016-03-10T19:00:30Z merged: 2016-03-12T07:13:59Z

1. [13680](http://github.com/cms-sw/cmssw/pull/13680){:target="_blank"}  from **@ianna**: Migrate to CondDB Configuration `db`  created: 2016-03-10T15:42:41Z merged: 2016-03-15T09:37:35Z

1. [13679](http://github.com/cms-sw/cmssw/pull/13679){:target="_blank"}  from **@vanbesien**: Fixed the missing linking between plot and refplot (8_1_X) `dqm`  created: 2016-03-10T15:14:06Z merged: 2016-03-12T07:13:42Z

1. [13678](http://github.com/cms-sw/cmssw/pull/13678){:target="_blank"}  from **@vanbesien**: Fixed the missing linking between plot and refplot (8_0_X) `dqm`  created: 2016-03-10T15:14:03Z merged: 2016-03-15T17:05:21Z

1. [13677](http://github.com/cms-sw/cmssw/pull/13677){:target="_blank"}  from **@lgray**: Add accessor to HGCalDDDConstants `geometry`  created: 2016-03-10T14:41:25Z merged: 2016-03-11T09:54:51Z

1. [13676](http://github.com/cms-sw/cmssw/pull/13676){:target="_blank"}  from **@mbandrews**: Fix binning in ZS filter SRTask plots `dqm`  created: 2016-03-10T12:03:00Z merged: 2016-03-15T17:06:13Z

1. [13675](http://github.com/cms-sw/cmssw/pull/13675){:target="_blank"}  from **@mbandrews**: Add channel status (with fixed desc). Add laser threshold. `dqm`  created: 2016-03-10T11:50:45Z merged: 2016-03-15T17:06:00Z

1. [13672](http://github.com/cms-sw/cmssw/pull/13672){:target="_blank"}  from **@bouril**: Changed the struct Count to avoid thread safety warnings `simulation`  created: 2016-03-09T22:22:19Z merged: 2016-03-14T08:46:31Z

1. [13671](http://github.com/cms-sw/cmssw/pull/13671){:target="_blank"}  from **@boudoul**: Workflows for 2023 including Phase2 Tracker (gensim step) `geometry`  `operations`  `pdmv`  `simulation`  created: 2016-03-09T18:03:03Z merged: 2016-03-10T19:45:35Z

1. [13668](http://github.com/cms-sw/cmssw/pull/13668){:target="_blank"}  from **@mdhildreth**: Add automatic turn-off of tracker digiSimLink production in standard production mode `simulation`  created: 2016-03-09T16:12:09Z merged: 2016-03-15T17:06:58Z

1. [13666](http://github.com/cms-sw/cmssw/pull/13666){:target="_blank"}  from **@makortel**: Migrate remaining 2017 reco customizations to era `operations`  `reconstruction`  `simulation`  created: 2016-03-09T15:17:06Z merged: 2016-03-15T09:36:25Z

1. [13665](http://github.com/cms-sw/cmssw/pull/13665){:target="_blank"}  from **@pargali**: Top dqm singletopbtagfix `dqm`  created: 2016-03-09T15:09:26Z merged: 2016-03-24T08:33:47Z

1. [13663](http://github.com/cms-sw/cmssw/pull/13663){:target="_blank"}  from **@deguio**: add protection for T0 configuration query `dqm`  created: 2016-03-09T13:33:00Z merged: 2016-03-15T17:05:32Z

1. [13654](http://github.com/cms-sw/cmssw/pull/13654){:target="_blank"}  from **@bsunanda**: bsunanda:Phase2-hgx42 Making an application for TB simulation of HGCal `geometry`  `simulation`  created: 2016-03-08T21:57:07Z merged: 2016-03-10T19:46:46Z

1. [13644](http://github.com/cms-sw/cmssw/pull/13644){:target="_blank"}  from **@ghellwig**: Declare 'seedOnlyFromAbove_' as 'int' (Backport of #13643). `alca`  created: 2016-03-08T16:25:34Z merged: 2016-03-17T09:13:12Z

1. [13641](http://github.com/cms-sw/cmssw/pull/13641){:target="_blank"}  from **@ahinzmann**: Add PU id working points to MiniAOD `analysis`  `reconstruction`  created: 2016-03-08T14:16:02Z merged: 2016-03-17T09:05:56Z

1. [13626](http://github.com/cms-sw/cmssw/pull/13626){:target="_blank"}  from **@bsunanda**: bsunanda:Phase2 hgx41Validation code due to Maksat `dqm`  `simulation`  created: 2016-03-07T15:50:10Z merged: 2016-03-18T16:23:28Z

1. [13623](http://github.com/cms-sw/cmssw/pull/13623){:target="_blank"}  from **@gpetruc**: Trigger matching with tracker muons (80X) `analysis`  `comparison`  created: 2016-03-07T14:57:39Z merged: 2016-03-17T09:08:22Z

1. [13621](http://github.com/cms-sw/cmssw/pull/13621){:target="_blank"}  from **@Martin-Grunewald**: Remove extra parameter from HLTL1TSeed module `hlt`  created: 2016-03-07T13:35:50Z merged: 2016-03-15T09:39:54Z

1. [13606](http://github.com/cms-sw/cmssw/pull/13606){:target="_blank"}  from **@ferencek**: Protect default PAT jet configuration (81X) `analysis`  `reconstruction`  created: 2016-03-04T23:59:23Z merged: 2016-03-14T08:41:53Z

1. [13605](http://github.com/cms-sw/cmssw/pull/13605){:target="_blank"}  from **@ferencek**: Protect default PAT jet configuration (80X) `analysis`  `reconstruction`  created: 2016-03-04T22:26:48Z merged: 2016-03-17T11:12:28Z

1. [13603](http://github.com/cms-sw/cmssw/pull/13603){:target="_blank"}  from **@mandrenguyen**: Added customizations to run pp reco on peripheral HI events `reconstruction`  created: 2016-03-04T18:51:39Z merged: 2016-03-12T07:17:38Z

1. [13596](http://github.com/cms-sw/cmssw/pull/13596){:target="_blank"}  from **@ssekmen**: Hlt hcal movemodulestol1t `alca`  `hlt`  `reconstruction`  created: 2016-03-04T13:50:28Z merged: 2016-03-15T09:31:09Z

1. [13590](http://github.com/cms-sw/cmssw/pull/13590){:target="_blank"}  from **@makortel**: Enable all working DQM and validation modules for 2017 `dqm`  `simulation`  created: 2016-03-04T09:23:16Z merged: 2016-03-17T18:50:41Z

1. [13577](http://github.com/cms-sw/cmssw/pull/13577){:target="_blank"}  from **@degano**: [CondFormats/SiPixelObjects] Solve warning found by gcc 5.3.0 `alca`  `db`  created: 2016-03-03T11:15:07Z merged: 2016-03-25T06:29:08Z

1. [13572](http://github.com/cms-sw/cmssw/pull/13572){:target="_blank"}  from **@sarafiorendi**: migration to stage-2 L1 for muon modules `hlt`  `reconstruction`  created: 2016-03-03T10:55:08Z merged: 2016-03-15T09:30:56Z

1. [13566](http://github.com/cms-sw/cmssw/pull/13566){:target="_blank"}  from **@jasperlauwers**: Correct QuadPFJet pathnames `dqm`  created: 2016-03-03T09:47:23Z merged: 2016-03-15T14:50:15Z

1. [13558](http://github.com/cms-sw/cmssw/pull/13558){:target="_blank"}  from **@Sam-Harper**: EG L1S1 to L1S2 migration `hlt`  created: 2016-03-02T17:31:43Z merged: 2016-03-15T09:23:46Z

1. [13520](http://github.com/cms-sw/cmssw/pull/13520){:target="_blank"}  from **@ianna**: 2016 Geometry Scenario Scripts `db`  created: 2016-02-29T15:26:28Z merged: 2016-03-11T09:55:45Z

1. [13496](http://github.com/cms-sw/cmssw/pull/13496){:target="_blank"}  from **@mmusich**: Fixing 80X relval alcareco in express test `pdmv`  created: 2016-02-26T15:25:07Z merged: 2016-03-17T09:17:37Z

1. [13484](http://github.com/cms-sw/cmssw/pull/13484){:target="_blank"}  from **@alberto-sanchez**: Adding tracks from V0, and fixing bug in photon conversion producer for 80x `analysis`  `comparison`  created: 2016-02-25T19:56:13Z merged: 2016-03-17T09:08:50Z

1. [13460](http://github.com/cms-sw/cmssw/pull/13460){:target="_blank"}  from **@jruizvar**: Remove obsolete files in the HLT SUSY Validation package `dqm`  created: 2016-02-24T16:52:27Z merged: 2016-03-17T09:16:18Z

1. [13413](http://github.com/cms-sw/cmssw/pull/13413){:target="_blank"}  from **@rrabadan**: StoNCorrOnTrack in  modules with the highest values `dqm`  created: 2016-02-20T21:29:53Z merged: 2016-03-17T09:16:42Z

1. [13404](http://github.com/cms-sw/cmssw/pull/13404){:target="_blank"}  from **@schneiml**: DQM TrackerMonitorTrack improvements (80X version) `alca`  `dqm`  created: 2016-02-19T09:35:10Z merged: 2016-03-17T09:18:33Z

1. [13398](http://github.com/cms-sw/cmssw/pull/13398){:target="_blank"}  from **@schneiml**: Add cuts to SiStripMonitorTrack `dqm`  created: 2016-02-18T17:14:20Z merged: 2016-03-17T09:18:45Z

1. [13393](http://github.com/cms-sw/cmssw/pull/13393){:target="_blank"}  from **@schneiml**: DQM TrackerMonitorTrack improvements `alca`  `dqm`  created: 2016-02-18T14:23:44Z merged: 2016-03-15T08:43:40Z

1. [13373](http://github.com/cms-sw/cmssw/pull/13373){:target="_blank"}  from **@alexeybaskakov**: CompHEP interface to Pythia8 `comparison`  `generators`  created: 2016-02-18T10:06:40Z merged: 2016-03-17T13:22:39Z

1. [13361](http://github.com/cms-sw/cmssw/pull/13361){:target="_blank"}  from **@matz-e**: Fix the hcaletValue function. `alca`  `db`  `dqm`  `l1`  created: 2016-02-18T10:03:24Z merged: 2016-03-17T14:22:49Z

1. [13347](http://github.com/cms-sw/cmssw/pull/13347){:target="_blank"}  from **@clacaputo**: Validation module for ME0 Detector (Phase2 Upgrade) `dqm`  created: 2016-02-18T09:59:38Z merged: 2016-03-28T10:08:38Z

1. [13295](http://github.com/cms-sw/cmssw/pull/13295){:target="_blank"}  from **@mbandrews**: ECALbyLumi+Timing `dqm`  created: 2016-02-15T23:57:42Z merged: 2016-03-17T09:20:17Z

1. [13115](http://github.com/cms-sw/cmssw/pull/13115){:target="_blank"}  from **@cms-met**: MET PAT tool update + update of MET significance `analysis`  `reconstruction`  created: 2016-01-28T19:16:06Z merged: 2016-03-17T09:07:07Z

1. [12985](http://github.com/cms-sw/cmssw/pull/12985){:target="_blank"}  from **@jfernan2**: Added DaqSource emulator using DaqFakeReader `alca`  created: 2016-01-19T10:09:06Z merged: 2016-03-22T16:42:03Z

#### CMSDIST Changes between Tags REL/CMSSW_8_1_0_pre1/slc6_amd64_gcc530 and REL/CMSSW_8_1_0_pre2/slc6_amd64_gcc530:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_8_1_0_pre1/slc6_amd64_gcc530...REL/CMSSW_8_1_0_pre2/slc6_amd64_gcc530)



1. [2219](http://github.com/cms-sw/cmssw/pull/2219){:target="_blank"}  from **@smuzaffar**: Move L1Trigger/CSCTrackFinder/src/core_ files to external package created: 2014-01-29T09:38:23Z merged: None

1. [2215](http://github.com/cms-sw/cmssw/pull/2215){:target="_blank"}  from **@smuzaffar**: back-port cmsswdata changes from next to stable branch created: 2014-01-29T04:09:44Z merged: 2014-01-31T14:33:15Z

1. [2214](http://github.com/cms-sw/cmssw/pull/2214){:target="_blank"}  from **@smuzaffar**: Updated root to tip of 39e926b created: 2014-01-29T03:26:15Z merged: None

1. [2208](http://github.com/cms-sw/cmssw/pull/2208){:target="_blank"}  from **@degano**: Add data files for L1Trigger/L1THGCal. created: 2014-01-28T18:26:47Z merged: 2014-01-30T15:04:47Z

1. [2206](http://github.com/cms-sw/cmssw/pull/2206){:target="_blank"}  from **@degano**: Advance data for L1Trigger/ L1TCalorimeter, L1TGlobal and L1TMuon. created: 2014-01-28T15:29:55Z merged: 2014-02-13T15:58:28Z

1. [2204](http://github.com/cms-sw/cmssw/pull/2204){:target="_blank"}  from **@smuzaffar**: Updated root to tip of 3abd13e created: 2014-01-28T15:18:53Z merged: 2014-01-28T15:19:14Z

1. [2202](http://github.com/cms-sw/cmssw/pull/2202){:target="_blank"}  from **@degano**: Advance data for L1Trigger/ L1TCalorimeter, L1TGlobal and L1TMuon. created: 2014-01-28T14:25:25Z merged: 2014-01-30T08:25:22Z

1. [2197](http://github.com/cms-sw/cmssw/pull/2197){:target="_blank"}  from **@degano**: New release for GeneratorInterface/EvtGenInterface. created: 2014-01-28T13:17:51Z merged: 2014-01-30T11:59:11Z

1. [2194](http://github.com/cms-sw/cmssw/pull/2194){:target="_blank"}  from **@smuzaffar**: properly update buildfile dependency information for patch releases

1. [2193](http://github.com/cms-sw/cmssw/pull/2193){:target="_blank"}  from **@smuzaffar**: Update tkonline 80x created: 2014-01-28T09:30:28Z merged: 2014-01-28T11:12:48Z

1. [2181](http://github.com/cms-sw/cmssw/pull/2181){:target="_blank"}  from **@degano**: Advance data for Fireworks/Geometry. created: 2014-01-27T16:05:41Z merged: None

1. [2161](http://github.com/cms-sw/cmssw/pull/2161){:target="_blank"}  from **@TaiSakuma**: update pandas version to 0.17.1 for 8_0_X created: 2014-01-24T14:19:24Z merged: None
