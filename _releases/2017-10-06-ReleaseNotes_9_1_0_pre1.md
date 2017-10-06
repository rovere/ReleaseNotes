---
layout: post
title:  "9_1_0_pre1"
date:   2017-10-06 10:52:06 +0200
categories: cmssw
relmajor: 9
relminor: 1
relsubminor: 0
relpre: _pre1
---

# CMSSW_9_1_0_pre1
#### Changes since CMSSW_9_0_0:
[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_9_0_0...CMSSW_9_1_0_pre1)



1. [18036](http://github.com/cms-sw/cmssw/pull/18036){:target="_blank"}  from **@cms-sw**: Revert "Bin lookup in the JetCorrectorParameters class" `analysis`  `comparison`  `db`  created: 2017-03-22T15:59:04Z merged: 2017-03-22T15:59:30Z

1. [18034](http://github.com/cms-sw/cmssw/pull/18034){:target="_blank"}  from **@cerminar**: Fix the handling of ALCARECO output for steps which don't require the creation of a combined stream (i.e. all cases but the Tier0 one) `operations`  created: 2017-03-22T13:03:01Z merged: 2017-03-22T16:03:34Z

1. [18029](http://github.com/cms-sw/cmssw/pull/18029){:target="_blank"}  from @cms-sw: Revert "add PV monitoring **@HLT**" `comparison`  `dqm`  `hlt`  `operations`  `pdmv`  `reconstruction`  `simulation`  `upgrade`  created: 2017-03-22T08:26:26Z merged: 2017-03-22T08:37:41Z

1. [18027](http://github.com/cms-sw/cmssw/pull/18027){:target="_blank"}  from **@fioriNTU**: Phase1 Geometry in Online `dqm`  created: 2017-03-22T06:58:15Z merged: 2017-03-22T12:51:30Z

1. [18022](http://github.com/cms-sw/cmssw/pull/18022){:target="_blank"}  from **@wddgit**: Fix problem introduced by recent PR #17950 related to dropOnInput `core`  created: 2017-03-21T20:31:00Z merged: 2017-03-22T06:51:07Z

1. [18008](http://github.com/cms-sw/cmssw/pull/18008){:target="_blank"}  from **@ianna**: Zero Material 2017 Plan1 Scenario `geometry`  `upgrade`  created: 2017-03-21T11:37:26Z merged: 2017-03-22T09:02:05Z

1. [18003](http://github.com/cms-sw/cmssw/pull/18003){:target="_blank"}  from **@rovere**: Material in color `simulation`  created: 2017-03-20T20:51:04Z merged: 2017-03-21T16:48:21Z

1. [18000](http://github.com/cms-sw/cmssw/pull/18000){:target="_blank"}  from **@civanch**: Removed time cut in calorimeters for neutron background simulation `core`  `simulation`  created: 2017-03-20T18:54:07Z merged: 2017-03-21T17:04:13Z

1. [17999](http://github.com/cms-sw/cmssw/pull/17999){:target="_blank"}  from **@gartung**: Enable ROOT ImplicitMT through config `comparison`  `core`  created: 2017-03-20T18:49:12Z merged: 2017-03-21T16:49:00Z

1. [17998](http://github.com/cms-sw/cmssw/pull/17998){:target="_blank"}  from **@bsunanda**: bsunanda:Phase2-gem25 Correct the gap between eta section of GE21 `geometry`  created: 2017-03-20T16:54:05Z merged: 2017-03-21T08:28:32Z

1. [17997](http://github.com/cms-sw/cmssw/pull/17997){:target="_blank"}  from **@gartung**: Fix gcc6 misleading-indentation warning `reconstruction`  created: 2017-03-20T16:40:56Z merged: 2017-03-22T16:02:27Z

1. [17996](http://github.com/cms-sw/cmssw/pull/17996){:target="_blank"}  from @mtosi: add PV monitoring **@HLT** `dqm`  `hlt`  `operations`  `pdmv`  `reconstruction`  `simulation`  `upgrade`  created: 2017-03-20T16:28:02Z merged: 2017-03-21T16:51:52Z

1. [17994](http://github.com/cms-sw/cmssw/pull/17994){:target="_blank"}  from **@imKuehlschrank**: add plot params to individual histograms created in the geometry hierarchy `dqm`  created: 2017-03-20T14:41:19Z merged: 2017-03-22T06:53:53Z

1. [17993](http://github.com/cms-sw/cmssw/pull/17993){:target="_blank"}  from **@suchandradutta**: TrackerMap creation script updated  `dqm`  created: 2017-03-20T12:01:18Z merged: 2017-03-21T08:29:05Z

1. [17991](http://github.com/cms-sw/cmssw/pull/17991){:target="_blank"}  from **@silviodonato**: Minor bug fix in hltGetConfiguration (91X) `hlt`  created: 2017-03-20T10:51:39Z merged: 2017-03-20T20:31:51Z

1. [17989](http://github.com/cms-sw/cmssw/pull/17989){:target="_blank"}  from **@anorkus**: Removed CouchURL param from injection dict in 91X `pdmv`  `upgrade`  created: 2017-03-20T09:51:41Z merged: 2017-03-20T20:31:59Z

1. [17985](http://github.com/cms-sw/cmssw/pull/17985){:target="_blank"}  from **@civanch**: Fixed new cavern description `geometry`  `upgrade`  created: 2017-03-19T21:48:03Z merged: 2017-03-20T09:21:57Z

1. [17983](http://github.com/cms-sw/cmssw/pull/17983){:target="_blank"}  from **@mariadalfonso**: HBHE M3 = fix M3  `alca`  `reconstruction`  created: 2017-03-19T09:39:02Z merged: 2017-03-21T19:49:04Z

1. [17982](http://github.com/cms-sw/cmssw/pull/17982){:target="_blank"}  from **@Dr15Jones**: Task based stream begin transitions `core`  created: 2017-03-18T19:53:37Z merged: 2017-03-20T09:23:23Z

1. [17981](http://github.com/cms-sw/cmssw/pull/17981){:target="_blank"}  from **@mmusich**: [91X] fix ShallowEventDataProducer to allow running SiStripGain PCL producers from 2016 ALCARECO   `alca`  created: 2017-03-18T10:20:54Z merged: 2017-03-21T16:50:05Z

protects SiStripGains PCL algorithm when analyzing ALCARECO data produced with versions not containing #17419



1. [17980](http://github.com/cms-sw/cmssw/pull/17980){:target="_blank"}  from **@mmusich**: [91X] Modernize configuration of SiStripDetVOffReader and add SiStripApvGainReader `db`  created: 2017-03-18T10:09:12Z merged: 2017-03-22T06:54:17Z

1. [17976](http://github.com/cms-sw/cmssw/pull/17976){:target="_blank"}  from **@deguio**: removed HCAL DQM from the offline sequences `dqm`  created: 2017-03-17T20:33:22Z merged: 2017-03-18T19:27:22Z

1. [17975](http://github.com/cms-sw/cmssw/pull/17975){:target="_blank"}  from **@arunhep**: 2017 and 2018 GTs updated with HCAL LUTs Bug fix and Resp Corr Update for Plan1 `alca`  created: 2017-03-17T20:03:42Z merged: 2017-03-20T09:23:08Z

1. [17972](http://github.com/cms-sw/cmssw/pull/17972){:target="_blank"}  from **@gartung**: SimCalorimetry/EcalEBTrigPrimAlgos : Comment out unused variables to remove gcc warning. `l1`  `upgrade`  created: 2017-03-17T16:22:28Z merged: 2017-03-22T09:08:15Z

1. [17966](http://github.com/cms-sw/cmssw/pull/17966){:target="_blank"}  from **@pietverwilligen**: from 768 to 512 strips for ME0 geometry `geometry`  `upgrade`  created: 2017-03-17T14:13:00Z merged: 2017-03-20T20:32:12Z

1. [17962](http://github.com/cms-sw/cmssw/pull/17962){:target="_blank"}  from **@gartung**: IOMC/RandomEngine/test fix bug in initialization of sleep timer. `core`  created: 2017-03-16T19:55:07Z merged: 2017-03-18T19:28:08Z

1. [17961](http://github.com/cms-sw/cmssw/pull/17961){:target="_blank"}  from **@gartung**: CalibCalorimetry/HcalPlugins fix bug found from clang warning `alca`  created: 2017-03-16T19:29:31Z merged: 2017-03-21T17:22:44Z

1. [17960](http://github.com/cms-sw/cmssw/pull/17960){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-TB24 Fix the crash with TB170 geometry `geometry`  `upgrade`  created: 2017-03-16T15:49:21Z merged: 2017-03-17T17:16:04Z

1. [17955](http://github.com/cms-sw/cmssw/pull/17955){:target="_blank"}  from **@shervin86**: removed assert `alca`  created: 2017-03-16T10:56:28Z merged: 2017-03-20T20:32:27Z

1. [17953](http://github.com/cms-sw/cmssw/pull/17953){:target="_blank"}  from **@matz-e**: Fix HCAL trigger mode in 2018 geometry `geometry`  created: 2017-03-16T08:38:48Z merged: 2017-03-16T18:19:06Z

1. [17951](http://github.com/cms-sw/cmssw/pull/17951){:target="_blank"}  from **@cms-tsg-storm**: Bugfix and clean-up of frozen HLT menus (91X) `hlt`  created: 2017-03-16T08:11:05Z merged: 2017-03-16T17:20:11Z

1. [17950](http://github.com/cms-sw/cmssw/pull/17950){:target="_blank"}  from **@wddgit**: Fix BranchChildren/Parentage problems that occur with SubProcess and EDAlias `core`  created: 2017-03-15T22:04:14Z merged: 2017-03-20T20:32:42Z

1. [17948](http://github.com/cms-sw/cmssw/pull/17948){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-hcx117 Make right treatment of neutral filter `geometry`  `simulation`  created: 2017-03-15T21:54:45Z merged: 2017-03-18T19:28:54Z

1. [17946](http://github.com/cms-sw/cmssw/pull/17946){:target="_blank"}  from **@Dr15Jones**: Use tbb::spawn instead of tbb::enqueue for stream 0 begin transitions `core`  created: 2017-03-15T19:05:22Z merged: 2017-03-16T07:25:55Z

1. [17945](http://github.com/cms-sw/cmssw/pull/17945){:target="_blank"}  from **@Dr15Jones**: Do not reset info for the stack trace helper `core`  created: 2017-03-15T16:36:38Z merged: 2017-03-16T07:25:45Z

1. [17944](http://github.com/cms-sw/cmssw/pull/17944){:target="_blank"}  from **@ianna**: 2023 Scenario and Workflow with Detailed Cavern `geometry`  `operations`  `pdmv`  `simulation`  `upgrade`  created: 2017-03-15T14:09:37Z merged: 2017-03-17T17:07:09Z

1. [17939](http://github.com/cms-sw/cmssw/pull/17939){:target="_blank"}  from **@fioriNTU**: OnlineClients `dqm`  created: 2017-03-15T08:04:54Z merged: 2017-03-16T11:54:07Z

1. [17937](http://github.com/cms-sw/cmssw/pull/17937){:target="_blank"}  from **@Dr15Jones**: Fix comparisons used for unit tests `core`  created: 2017-03-14T19:23:36Z merged: 2017-03-15T08:26:40Z

1. [17936](http://github.com/cms-sw/cmssw/pull/17936){:target="_blank"}  from **@franzoni**: fix for ECAL selective readout `alca`  created: 2017-03-14T18:22:21Z merged: 2017-03-16T07:25:36Z

1. [17935](http://github.com/cms-sw/cmssw/pull/17935){:target="_blank"}  from **@ianna**: Remove Beam-pipe from CTPPS Configuration `geometry`  created: 2017-03-14T18:19:08Z merged: 2017-03-15T08:27:55Z

1. [17932](http://github.com/cms-sw/cmssw/pull/17932){:target="_blank"}  from **@ndaci**: Fix the access to PU info in HLT Ntuples (91X, master branch) `hlt`  created: 2017-03-14T17:33:32Z merged: 2017-03-15T08:25:38Z

1. [17925](http://github.com/cms-sw/cmssw/pull/17925){:target="_blank"}  from **@folguera**: Muon HLT for IterL3: porting to new seeding  `hlt`  `reconstruction`  created: 2017-03-14T15:45:16Z merged: 2017-03-16T17:21:49Z

1. [17918](http://github.com/cms-sw/cmssw/pull/17918){:target="_blank"}  from **@makortel**: Add CA hit ntuplets for early deletion `reconstruction`  created: 2017-03-14T13:28:50Z merged: 2017-03-16T17:22:04Z

1. [17917](http://github.com/cms-sw/cmssw/pull/17917){:target="_blank"}  from **@folguera**: Muon HLT - fix in TSGForOI `reconstruction`  created: 2017-03-14T12:29:05Z merged: 2017-03-17T17:24:14Z

1. [17916](http://github.com/cms-sw/cmssw/pull/17916){:target="_blank"}  from **@fioriNTU**: removing double call to the RAW data plugin `dqm`  created: 2017-03-14T11:11:38Z merged: 2017-03-15T15:13:30Z

1. [17915](http://github.com/cms-sw/cmssw/pull/17915){:target="_blank"}  from **@cms-sw**: Revert "Revert "Update 2017 Beam-pipe Middle Section"" `geometry`  `upgrade`  created: 2017-03-14T11:06:30Z merged: 2017-03-14T14:17:48Z

1. [17914](http://github.com/cms-sw/cmssw/pull/17914){:target="_blank"}  from **@ianna**: Update All Locations of Phase 1 Beampipe `geometry`  `upgrade`  created: 2017-03-14T10:52:36Z merged: 2017-03-14T14:17:15Z

1. [17913](http://github.com/cms-sw/cmssw/pull/17913){:target="_blank"}  from **@cms-sw**: Revert "Update 2017 Beam-pipe Middle Section" `comparison`  `geometry`  `upgrade`  created: 2017-03-14T09:57:37Z merged: 2017-03-14T09:57:43Z

1. [17912](http://github.com/cms-sw/cmssw/pull/17912){:target="_blank"}  from **@Dr15Jones**: Report # events per Lumi for output files in framework job report `core`  created: 2017-03-13T20:21:41Z merged: 2017-03-14T08:29:10Z

1. [17906](http://github.com/cms-sw/cmssw/pull/17906){:target="_blank"}  from **@cms-tsg-storm**: Cleanup of HLT customization files moved into ConfDB menus (91X) `hlt`  created: 2017-03-13T15:19:56Z merged: 2017-03-14T12:29:30Z

1. [17905](http://github.com/cms-sw/cmssw/pull/17905){:target="_blank"}  from **@franzoni**: fix GEM geometry - HCAL emap - HCAL resoCorr HEP17 - SiStrip bad channels [91x version] `alca`  created: 2017-03-13T14:29:25Z merged: 2017-03-14T14:18:47Z

1. [17903](http://github.com/cms-sw/cmssw/pull/17903){:target="_blank"}  from **@makortel**: Add README for adding/reordering iterations `reconstruction`  created: 2017-03-13T12:43:05Z merged: 2017-03-14T08:29:21Z

1. [17901](http://github.com/cms-sw/cmssw/pull/17901){:target="_blank"}  from **@fabozzi**: Migration of workflow injection to Unified `pdmv`  `upgrade`  created: 2017-03-13T11:46:55Z merged: 2017-03-14T12:28:53Z

1. [17895](http://github.com/cms-sw/cmssw/pull/17895){:target="_blank"}  from **@christopheralanwest**: Fix eta range for HCAL LUT metadata `alca`  created: 2017-03-12T15:46:26Z merged: 2017-03-15T08:23:02Z

1. [17891](http://github.com/cms-sw/cmssw/pull/17891){:target="_blank"}  from **@VinInn**: New cluster shape filter for phase2 + adding PixelPair `reconstruction`  `upgrade`  created: 2017-03-11T13:33:59Z merged: 2017-03-16T19:46:46Z

1. [17889](http://github.com/cms-sw/cmssw/pull/17889){:target="_blank"}  from **@bsunanda**: bsunanda:Phase2-gem24 Fix the issue of GE21 with staggered gap `geometry`  `upgrade`  created: 2017-03-10T23:03:24Z merged: 2017-03-18T19:29:15Z

1. [17888](http://github.com/cms-sw/cmssw/pull/17888){:target="_blank"}  from **@pmillet**: Bugfix for MakeSherpaLibs and update of example cards `generators`  created: 2017-03-10T16:31:47Z merged: 2017-03-12T18:42:10Z

1. [17880](http://github.com/cms-sw/cmssw/pull/17880){:target="_blank"}  from **@leggat**: Pixel Phase 1 summary maps `dqm`  created: 2017-03-10T14:55:22Z merged: 2017-03-16T17:53:36Z

1. [17879](http://github.com/cms-sw/cmssw/pull/17879){:target="_blank"}  from **@ggovi**: Added RunInfo quick access in Condition DB `alca`  `db`  created: 2017-03-10T14:54:06Z merged: 2017-03-21T16:53:36Z

1. [17877](http://github.com/cms-sw/cmssw/pull/17877){:target="_blank"}  from **@bendavid**: Minor improvements to Multifit handling of max sample fallback (91x) `reconstruction`  created: 2017-03-10T13:52:47Z merged: 2017-03-18T19:29:44Z

1. [17874](http://github.com/cms-sw/cmssw/pull/17874){:target="_blank"}  from **@smuzaffar**: updated/bug fix duplicateReflexLibrarySearch.py  `core`  created: 2017-03-10T10:06:34Z merged: 2017-03-10T18:20:11Z

1. [17873](http://github.com/cms-sw/cmssw/pull/17873){:target="_blank"}  from **@fabozzi**: update 2017 wf in IB: replace TenMuE with ZMM (91X) `pdmv`  `upgrade`  created: 2017-03-10T09:36:20Z merged: 2017-03-10T12:05:59Z

1. [17872](http://github.com/cms-sw/cmssw/pull/17872){:target="_blank"}  from **@fwyzard**: Set HCAL method 3 respons to 1.0 for data and MC. `hlt`  `reconstruction`  created: 2017-03-09T22:31:47Z merged: 2017-03-14T08:29:35Z

1. [17870](http://github.com/cms-sw/cmssw/pull/17870){:target="_blank"}  from **@Dr15Jones**: Fixed a clang warning in View.cc `core`  created: 2017-03-09T21:42:30Z merged: 2017-03-10T07:52:06Z

1. [17869](http://github.com/cms-sw/cmssw/pull/17869){:target="_blank"}  from **@grasph**: MatacqProduce: added support for multiple matacq files per run `alca`  `reconstruction`  created: 2017-03-09T21:16:12Z merged: 2017-03-21T08:37:07Z

1. [17865](http://github.com/cms-sw/cmssw/pull/17865){:target="_blank"}  from **@enochnotsocool**: Sistrip cluster gain/raw cluster charge update - 91X `dqm`  created: 2017-03-09T20:40:02Z merged: 2017-03-15T08:16:48Z

1. [17864](http://github.com/cms-sw/cmssw/pull/17864){:target="_blank"}  from **@Dr15Jones**: Fix memory leaks associated with Muon Digi histogramming `dqm`  `simulation`  created: 2017-03-09T20:37:15Z merged: 2017-03-11T07:06:18Z

1. [17863](http://github.com/cms-sw/cmssw/pull/17863){:target="_blank"}  from **@Dr15Jones**: Use std::unique_ptr to manage memory in PileupJetIdProducer `reconstruction`  created: 2017-03-09T19:26:12Z merged: 2017-03-16T07:19:36Z

1. [17861](http://github.com/cms-sw/cmssw/pull/17861){:target="_blank"}  from **@Dr15Jones**: Fix memory leak in BasicHepMCValidation `dqm`  `generators`  created: 2017-03-09T17:19:32Z merged: 2017-03-14T14:21:58Z

1. [17855](http://github.com/cms-sw/cmssw/pull/17855){:target="_blank"}  from **@boudoul**: Cleaning  pixel certification to prevent crash at Tier0 `dqm`  created: 2017-03-09T14:57:24Z merged: 2017-03-10T07:52:31Z

1. [17854](http://github.com/cms-sw/cmssw/pull/17854){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-alca75 Changes in view of Plan1 and 2017 running `alca`  created: 2017-03-09T14:48:41Z merged: 2017-03-21T16:51:06Z

1. [17852](http://github.com/cms-sw/cmssw/pull/17852){:target="_blank"}  from **@cms-tsg-storm**: Update HLT STORM validation to Phase1 (91X) `core`  `hlt`  `pdmv`  `upgrade`  created: 2017-03-09T12:49:29Z merged: 2017-03-11T07:06:46Z

1. [17851](http://github.com/cms-sw/cmssw/pull/17851){:target="_blank"}  from **@ggovi**: Various fixes: conddb core, conddb tools, runinfo o2o `db`  created: 2017-03-09T11:32:35Z merged: 2017-03-09T19:45:35Z

1. [17844](http://github.com/cms-sw/cmssw/pull/17844){:target="_blank"}  from **@ianna**: Restructure XML Data Directories by Year and Version Step 2 `geometry`  `upgrade`  created: 2017-03-09T10:14:40Z merged: 2017-03-13T09:05:18Z

1. [17837](http://github.com/cms-sw/cmssw/pull/17837){:target="_blank"}  from **@Dr15Jones**: Added ModuloEventIDFilter and ModuloStreamIDFilter `core`  created: 2017-03-08T21:58:53Z merged: 2017-03-09T08:43:00Z

1. [17833](http://github.com/cms-sw/cmssw/pull/17833){:target="_blank"}  from **@civanch**: Extention of neutron background simulation `simulation`  created: 2017-03-08T17:41:53Z merged: 2017-03-10T08:10:38Z

1. [17831](http://github.com/cms-sw/cmssw/pull/17831){:target="_blank"}  from **@ianna**: Restructure XML Data Directories by Year and Version `geometry`  `upgrade`  created: 2017-03-08T17:08:54Z merged: 2017-03-10T12:10:54Z

1. [17828](http://github.com/cms-sw/cmssw/pull/17828){:target="_blank"}  from **@boudoul**: Setting up properly peak and deco (strip tracker config) 2017 cosmic WFs  `pdmv`  `upgrade`  created: 2017-03-08T16:47:21Z merged: 2017-03-17T17:41:41Z

1. [17825](http://github.com/cms-sw/cmssw/pull/17825){:target="_blank"}  from **@rekovic**: pr91x Configure TTStubAlgorithm from L1TrackTrigger sequence for TiltedTracker  `geometry`  `operations`  created: 2017-03-08T13:50:39Z merged: 2017-03-09T08:46:16Z

1. [17823](http://github.com/cms-sw/cmssw/pull/17823){:target="_blank"}  from **@davidlange6**: revert change to CaloCluster in warning cleanup `comparison`  `reconstruction`  created: 2017-03-08T09:41:52Z merged: 2017-03-08T09:42:20Z

1. [17821](http://github.com/cms-sw/cmssw/pull/17821){:target="_blank"}  from **@mariadalfonso**: HBHE M2 = fix Memory Leak `reconstruction`  created: 2017-03-08T09:02:48Z merged: 2017-03-10T14:33:07Z

1. [17820](http://github.com/cms-sw/cmssw/pull/17820){:target="_blank"}  from **@fcouderc**: Update tag&probe package for egm [91X PR] `analysis`  `reconstruction`  created: 2017-03-08T08:40:59Z merged: 2017-03-11T06:52:30Z

1. [17818](http://github.com/cms-sw/cmssw/pull/17818){:target="_blank"}  from **@EsmaeelEskandari**: L1T legacy app is turned off and L1T2016 is renamed to L1T `dqm`  created: 2017-03-08T08:26:54Z merged: 2017-03-16T19:46:22Z

1. [17813](http://github.com/cms-sw/cmssw/pull/17813){:target="_blank"}  from **@Dr15Jones**: Converted BaseEvtVtxGenerator to stream module `generators`  `simulation`  created: 2017-03-07T22:04:39Z merged: 2017-03-14T17:38:29Z

1. [17812](http://github.com/cms-sw/cmssw/pull/17812){:target="_blank"}  from **@aperloff**: Bin lookup in the JetCorrectorParameters class `analysis`  `db`  created: 2017-03-07T20:57:00Z merged: 2017-03-22T06:59:40Z

1. [17808](http://github.com/cms-sw/cmssw/pull/17808){:target="_blank"}  from **@Dr15Jones**: Make GenParticleProducer a global module `analysis`  created: 2017-03-07T16:53:19Z merged: 2017-03-17T08:21:09Z

1. [17807](http://github.com/cms-sw/cmssw/pull/17807){:target="_blank"}  from **@gpetruc**: customizeHitRecoveryInGluedDetTkSeedsOnly `reconstruction`  created: 2017-03-07T16:44:56Z merged: 2017-03-16T07:23:51Z

1. [17806](http://github.com/cms-sw/cmssw/pull/17806){:target="_blank"}  from **@ianna**: Update 2017 Beam-pipe Middle Section `geometry`  `upgrade`  created: 2017-03-07T15:00:52Z merged: 2017-03-13T14:28:06Z

1. [17804](http://github.com/cms-sw/cmssw/pull/17804){:target="_blank"}  from **@kandrosov**: Code for ClusterShapeHitFilter calibration `reconstruction`  created: 2017-03-07T07:28:04Z merged: 2017-03-18T19:31:06Z

1. [17803](http://github.com/cms-sw/cmssw/pull/17803){:target="_blank"}  from **@igv4321**: Proper memory cleanup `reconstruction`  created: 2017-03-07T00:53:53Z merged: 2017-03-14T08:29:55Z

1. [17801](http://github.com/cms-sw/cmssw/pull/17801){:target="_blank"}  from **@wddgit**: Initial Implementation of Tasks in CMS Configurations  `analysis`  `core`  `dqm`  `hlt`  `operations`  `reconstruction`  created: 2017-03-06T18:55:39Z merged: 2017-03-21T19:44:29Z

1. [17800](http://github.com/cms-sw/cmssw/pull/17800){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-sim04 Adding a dumping analyzer to diagnose if o/p is created using TestNumbering or not for HCAL `simulation`  created: 2017-03-06T17:45:57Z merged: 2017-03-09T08:44:16Z

1. [17798](http://github.com/cms-sw/cmssw/pull/17798){:target="_blank"}  from **@smuzaffar**: Regenerate DQMServices/Core/src/ROOTFilePB.pb files for ptotocol buffer 3.2.0 `dqm`  created: 2017-03-06T16:27:50Z merged: 2017-03-06T20:31:00Z

1. [17796](http://github.com/cms-sw/cmssw/pull/17796){:target="_blank"}  from **@cms-tsg-storm**: Bug fixes and adding a Fake2 HLT menu (91X) `hlt`  created: 2017-03-06T15:22:06Z merged: 2017-03-07T15:56:58Z

1. [17792](http://github.com/cms-sw/cmssw/pull/17792){:target="_blank"}  from **@makortel**: Improve TrackingNtuple, add optional SeedStopReason to CkfTrackCandidateMaker `alca`  `dqm`  `hlt`  `reconstruction`  created: 2017-03-06T14:09:06Z merged: 2017-03-20T20:33:24Z

1. [17789](http://github.com/cms-sw/cmssw/pull/17789){:target="_blank"}  from **@matz-e**: Fix HCAL TP compression LUTs by populating plan 1 TP list first `alca`  `l1`  created: 2017-03-06T12:51:40Z merged: 2017-03-13T09:05:55Z

1. [17788](http://github.com/cms-sw/cmssw/pull/17788){:target="_blank"}  from **@makortel**: Fix MultiTrackValidator sim dxy/dz wrt. PV histograms `dqm`  `reconstruction`  `simulation`  created: 2017-03-06T10:46:06Z merged: 2017-03-07T20:49:41Z

1. [17787](http://github.com/cms-sw/cmssw/pull/17787){:target="_blank"}  from **@makortel**: Add differential pulls, and resolutions+pulls for PV to vertex validation `dqm`  created: 2017-03-06T09:54:54Z merged: 2017-03-07T15:57:17Z

1. [17782](http://github.com/cms-sw/cmssw/pull/17782){:target="_blank"}  from **@kpedro88**: include hcalRecAlgos ES producer in cosmic workflow `reconstruction`  created: 2017-03-05T22:48:32Z merged: 2017-03-06T19:49:37Z

1. [17778](http://github.com/cms-sw/cmssw/pull/17778){:target="_blank"}  from **@Dr15Jones**: Speed up the use of DDFilteredViews `alca`  `dqm`  `geometry`  `simulation`  `upgrade`  created: 2017-03-05T19:25:28Z merged: 2017-03-10T07:52:52Z

1. [17777](http://github.com/cms-sw/cmssw/pull/17777){:target="_blank"}  from **@igv4321**: Ignoring calibration channels in the dataframes `reconstruction`  created: 2017-03-05T17:01:06Z merged: 2017-03-07T21:21:32Z

1. [17773](http://github.com/cms-sw/cmssw/pull/17773){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-hcx115 Correct the issue of ieta=29 for higher depths in the Phase1 mode `geometry`  created: 2017-03-03T22:09:07Z merged: 2017-03-07T08:34:22Z

1. [17772](http://github.com/cms-sw/cmssw/pull/17772){:target="_blank"}  from **@slava77**: Revert "narrower anode time window switched to True" (91X fwd port of #17741) `reconstruction`  created: 2017-03-03T19:02:19Z merged: 2017-03-05T16:19:23Z

1. [17771](http://github.com/cms-sw/cmssw/pull/17771){:target="_blank"}  from **@makortel**: Make track algo priority order dynamic `dqm`  `fastsim`  `hlt`  `reconstruction`  created: 2017-03-03T17:56:54Z merged: 2017-03-11T06:46:30Z

1. [17767](http://github.com/cms-sw/cmssw/pull/17767){:target="_blank"}  from **@cms-tau-pog**: Switching off reconstruction of so called "NullTaus" `reconstruction`  created: 2017-03-03T14:06:28Z merged: 2017-03-13T09:06:30Z

1. [17766](http://github.com/cms-sw/cmssw/pull/17766){:target="_blank"}  from **@makortel**: Switch phase1 tracking to use CA seeding by default `operations`  `pdmv`  `reconstruction`  `upgrade`  created: 2017-03-03T13:33:44Z merged: 2017-03-14T08:30:21Z

1. [17765](http://github.com/cms-sw/cmssw/pull/17765){:target="_blank"}  from **@mmusich**: [91X] fix spurious tickmark gain change warnings in SiStripChannelGain calibration `alca`  created: 2017-03-03T12:55:52Z merged: 2017-03-07T15:57:53Z

1. [17761](http://github.com/cms-sw/cmssw/pull/17761){:target="_blank"}  from **@enochnotsocool**: SiPixelPhase1 - Filter update `dqm`  created: 2017-03-03T10:39:35Z merged: 2017-03-07T16:01:07Z

1. [17758](http://github.com/cms-sw/cmssw/pull/17758){:target="_blank"}  from **@slava77**: increase cosmics MC step1 nevents `pdmv`  `upgrade`  created: 2017-03-02T22:15:21Z merged: 2017-03-07T08:13:36Z

1. [17755](http://github.com/cms-sw/cmssw/pull/17755){:target="_blank"}  from **@jshlee**: fix rotation in me0geometry `geometry`  `upgrade`  created: 2017-03-02T16:31:49Z merged: 2017-03-07T21:00:12Z

1. [17752](http://github.com/cms-sw/cmssw/pull/17752){:target="_blank"}  from **@wddgit**: Fix parentage provenance in corner case `core`  created: 2017-03-02T15:26:53Z merged: 2017-03-07T08:12:20Z

1. [17751](http://github.com/cms-sw/cmssw/pull/17751){:target="_blank"}  from **@kpedro88**: fix sequences for HE plan1 `operations`  `reconstruction`  created: 2017-03-02T15:25:09Z merged: 2017-03-03T20:20:33Z

1. [17749](http://github.com/cms-sw/cmssw/pull/17749){:target="_blank"}  from **@Dr15Jones**: Begin stream transitions use multiple tbb tasks `core`  `fastsim`  created: 2017-03-02T14:45:17Z merged: 2017-03-07T16:01:29Z

1. [17748](http://github.com/cms-sw/cmssw/pull/17748){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-alca74 Make IsoTrack AlCaReco as well as tree makers to be equally useful for all possible isolation strategy `alca`  created: 2017-03-02T14:43:49Z merged: 2017-03-02T14:57:45Z

1. [17747](http://github.com/cms-sw/cmssw/pull/17747){:target="_blank"}  from **@fwyzard**: implement "plan 1" and sum SiPM rechits over all depths `comparison`  `hlt`  created: 2017-03-02T14:43:31Z merged: 2017-03-02T14:58:02Z

1. [17746](http://github.com/cms-sw/cmssw/pull/17746){:target="_blank"}  from **@usarica**: Cumulative updates to HipPy scripting, TwoBodyDecay, Alignment/OfflineValidation and MuonAnalysis/MuscleFit macros created: 2017-03-02T14:43:14Z merged: 2017-03-02T14:59:49Z

1. [17745](http://github.com/cms-sw/cmssw/pull/17745){:target="_blank"}  from **@makortel**: Add IfLogDebug and IfLogTrace to MessageLogger.h `core`  `reconstruction`  created: 2017-03-02T14:06:45Z merged: 2017-03-05T16:21:13Z

1. [17744](http://github.com/cms-sw/cmssw/pull/17744){:target="_blank"}  from **@makortel**: Remove TrackerSeedValidator as obsolete `dqm`  `fastsim`  created: 2017-03-02T13:53:31Z merged: 2017-03-05T16:26:10Z

1. [17743](http://github.com/cms-sw/cmssw/pull/17743){:target="_blank"}  from **@civanch**: Some cleanup for SIM `comparison`  `simulation`  created: 2017-03-02T13:52:43Z merged: 2017-03-02T14:58:23Z

1. [17740](http://github.com/cms-sw/cmssw/pull/17740){:target="_blank"}  from **@sviret**: Porting the TTTrack classes in 81X `l1`  `simulation`  `upgrade`  created: 2017-03-02T12:39:24Z merged: 2017-03-08T11:02:49Z

1. [17734](http://github.com/cms-sw/cmssw/pull/17734){:target="_blank"}  from **@kreczko**: [90X] Offline DQM modules for L1Trigger (stage2 calo layer2) `dqm`  `l1`  created: 2017-03-02T12:37:43Z merged: 2017-03-15T09:57:13Z

1. [17724](http://github.com/cms-sw/cmssw/pull/17724){:target="_blank"}  from **@ghellwig**: [90X] Allow multi-IOV input for Millepede alignment framework `alca`  created: 2017-03-02T12:34:56Z merged: 2017-03-08T10:45:22Z

1. [17723](http://github.com/cms-sw/cmssw/pull/17723){:target="_blank"}  from **@abbiendi**: Improved muon track validation (new code + customization) `dqm`  `simulation`  created: 2017-03-02T12:34:40Z merged: 2017-03-16T07:32:07Z

1. [17718](http://github.com/cms-sw/cmssw/pull/17718){:target="_blank"}  from **@dmitrijus**: Make MonitorElement to emit LogWarning instead of writing to std::cout `dqm`  created: 2017-03-02T12:33:18Z merged: 2017-03-07T16:01:48Z

1. [17717](http://github.com/cms-sw/cmssw/pull/17717){:target="_blank"}  from **@davidlt**: Resolve segfault in MuonGEMHitsHarvestor::dqmEndJob `dqm`  created: 2017-03-02T12:33:07Z merged: 2017-03-03T12:44:21Z

1. [17716](http://github.com/cms-sw/cmssw/pull/17716){:target="_blank"}  from **@ianna**: Extended 2017 Plan1 Scenario Scripts `db`  created: 2017-03-02T12:33:01Z merged: 2017-03-11T06:54:40Z

1. [17715](http://github.com/cms-sw/cmssw/pull/17715){:target="_blank"}  from **@knoepfel**: Convert ObjectViewCleaner from legacy producer to stream producer `dqm`  created: 2017-03-02T12:32:45Z merged: 2017-03-07T16:01:58Z

1. [17713](http://github.com/cms-sw/cmssw/pull/17713){:target="_blank"}  from **@lgray**: Fix numerical precision issue in 2D vertexing and wrong normalization. `reconstruction`  `upgrade`  created: 2017-03-02T12:32:10Z merged: 2017-03-08T23:22:16Z

1. [17710](http://github.com/cms-sw/cmssw/pull/17710){:target="_blank"}  from **@cms-btv-pog**: Reject 0 pt Puppi candidates in jet-track association `reconstruction`  created: 2017-03-02T12:31:21Z merged: 2017-03-05T16:21:21Z

1. [17709](http://github.com/cms-sw/cmssw/pull/17709){:target="_blank"}  from **@rekovic**: pr90x Add stage2L1Trigger to Era_Phase2C2. `l1`  `operations`  `pdmv`  `upgrade`  created: 2017-03-02T12:31:04Z merged: 2017-03-11T06:45:53Z

1. [17708](http://github.com/cms-sw/cmssw/pull/17708){:target="_blank"}  from **@davidlange6**: Fix some of the gcc620 warnings including possibly important changes to CondTools/Ecal and RecoJets/JetAlgorithms `alca`  `analysis`  `db`  `dqm`  `l1`  `reconstruction`  created: 2017-03-02T12:30:48Z merged: 2017-03-07T21:25:11Z

1. [17705](http://github.com/cms-sw/cmssw/pull/17705){:target="_blank"}  from **@aspiezia**: residual plots for DQM `dqm`  created: 2017-03-02T12:29:57Z merged: 2017-03-17T08:20:27Z

1. [17704](http://github.com/cms-sw/cmssw/pull/17704){:target="_blank"}  from **@nfilipov**: Pcc 90 x `reconstruction`  created: 2017-03-02T12:29:40Z merged: 2017-03-05T16:22:23Z

1. [17703](http://github.com/cms-sw/cmssw/pull/17703){:target="_blank"}  from **@jshlee**: Pfmuon fix 90x `reconstruction`  `upgrade`  created: 2017-03-02T12:29:24Z merged: 2017-03-22T06:57:33Z

recover PF muon efficiency in workflows with HGCAL



1. [17702](http://github.com/cms-sw/cmssw/pull/17702){:target="_blank"}  from **@arunhep**: GT updates for 900pre5 with Summer16 JECs, GEM reco geometry and ESEE Intercalib `alca`  created: 2017-03-02T12:29:07Z merged: 2017-03-07T16:26:16Z

1. [17701](http://github.com/cms-sw/cmssw/pull/17701){:target="_blank"}  from **@CTPPS**: CTPPS: miniAOD (second resubmission) `analysis`  `dqm`  `reconstruction`  created: 2017-03-02T12:28:51Z merged: 2017-03-05T16:25:09Z

1. [17700](http://github.com/cms-sw/cmssw/pull/17700){:target="_blank"}  from **@cms-btv-pog**: Update to input collection tokens in PATJetProducer `analysis`  `reconstruction`  created: 2017-03-02T12:28:34Z merged: 2017-03-09T08:51:52Z

1. [17699](http://github.com/cms-sw/cmssw/pull/17699){:target="_blank"}  from **@knoepfel**: Convert Validation/RecoTau modules from legacy to global producers `dqm`  created: 2017-03-02T12:28:18Z merged: 2017-03-08T22:50:32Z

1. [17697](http://github.com/cms-sw/cmssw/pull/17697){:target="_blank"}  from **@kpedro88**: remove photoelectronsToAnalog python parameter (now taken from DB) `comparison`  `simulation`  created: 2017-03-02T12:27:45Z merged: 2017-03-02T15:11:06Z

1. [17696](http://github.com/cms-sw/cmssw/pull/17696){:target="_blank"}  from **@dmitrijus**: Online DQM changes for MWGR#2 `dqm`  created: 2017-03-02T12:27:29Z merged: 2017-03-18T19:32:10Z

1. [17692](http://github.com/cms-sw/cmssw/pull/17692){:target="_blank"}  from **@nancymarinelli**: Update the dataformat for the TP per crystal. It now follows what pre `l1`  `simulation`  `upgrade`  created: 2017-03-02T12:26:23Z merged: 2017-03-13T09:08:03Z

1. [17691](http://github.com/cms-sw/cmssw/pull/17691){:target="_blank"}  from **@PFCal-dev**: HGCAL trigger sim clustering `l1`  `upgrade`  created: 2017-03-02T12:26:07Z merged: 2017-03-09T13:45:49Z

1. [17690](http://github.com/cms-sw/cmssw/pull/17690){:target="_blank"}  from **@archiron**: nbOfDaughters_electrons_correction_Histos_90X_V2 `dqm`  created: 2017-03-02T12:25:50Z merged: 2017-03-18T19:34:05Z

1. [17688](http://github.com/cms-sw/cmssw/pull/17688){:target="_blank"}  from **@kpedro88**: use HBHE Phase1 reco for Run2/legacy, unify M0 parameters `dqm`  `reconstruction`  `simulation`  created: 2017-03-02T12:25:16Z merged: 2017-03-20T09:24:41Z

1. [17687](http://github.com/cms-sw/cmssw/pull/17687){:target="_blank"}  from **@nickmccoll**: CSC RU segment algorithm tuned for ME0 `reconstruction`  `upgrade`  created: 2017-03-02T12:25:00Z merged: 2017-03-18T19:34:21Z

1. [17686](http://github.com/cms-sw/cmssw/pull/17686){:target="_blank"}  from **@davidlt**: Initialize theModMEs.ClusterGain `dqm`  created: 2017-03-02T11:34:36Z merged: 2017-03-02T13:45:13Z

1. [17685](http://github.com/cms-sw/cmssw/pull/17685){:target="_blank"}  from **@fabozzi**: Relval updates `comparison`  `pdmv`  `upgrade`  created: 2017-03-02T11:31:54Z merged: 2017-03-02T15:09:27Z

1. [17684](http://github.com/cms-sw/cmssw/pull/17684){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-TB23 Add the new AHCal for 2017 HGCal TB `geometry`  `simulation`  `upgrade`  created: 2017-03-02T11:27:33Z merged: 2017-03-05T16:24:43Z

1. [17680](http://github.com/cms-sw/cmssw/pull/17680){:target="_blank"}  from **@mariadalfonso**: HBHE M2 = HPD old code cleanup `reconstruction`  created: 2017-03-02T10:55:21Z merged: 2017-03-21T16:51:22Z

#### CMSDIST Changes between Tags REL/CMSSW_9_0_0/slc6_amd64_gcc530 and REL/CMSSW_9_1_0_pre1/slc6_amd64_gcc530:
[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_9_0_0/slc6_amd64_gcc530...REL/CMSSW_9_1_0_pre1/slc6_amd64_gcc530)



1. [2907](http://github.com/cms-sw/cmssw/pull/2907){:target="_blank"}  from **@smuzaffar**: Fix scipy numpy created: 2014-03-17T22:07:00Z merged: 2014-03-17T22:12:41Z

1. [2906](http://github.com/cms-sw/cmssw/pull/2906){:target="_blank"}  from **@davidlange6**: remove /bin/perl from memprobe in root created: 2014-03-17T20:11:01Z merged: None

1. [2900](http://github.com/cms-sw/cmssw/pull/2900){:target="_blank"}  from **@smuzaffar**: Updated root to tip of branch v6-08-00-patches n 91X created: 2014-03-17T19:01:12Z merged: 2014-03-17T21:52:38Z

1. [2898](http://github.com/cms-sw/cmssw/pull/2898){:target="_blank"}  from **@vkuznet**: To avoid latency disable uniq sorting by default and made it optional created: 2014-03-17T18:53:08Z merged: None

1. [2897](http://github.com/cms-sw/cmssw/pull/2897){:target="_blank"}  from **@vkuznet**: New version of dasgoclient: fixed expired proxy and nevents in DBS output created: 2014-03-17T17:45:08Z merged: 2014-03-26T21:28:57Z

1. [2895](http://github.com/cms-sw/cmssw/pull/2895){:target="_blank"}  from **@cms-sw**: move to root 6.08.06 in 91X created: 2014-03-17T16:38:32Z merged: 2014-03-18T12:17:49Z

1. [2894](http://github.com/cms-sw/cmssw/pull/2894){:target="_blank"}  from **@cms-sw**: Update py2-tensorflow.spec created: 2014-03-17T16:36:24Z merged: 2014-03-23T21:02:55Z

1. [2891](http://github.com/cms-sw/cmssw/pull/2891){:target="_blank"}  from **@mkirsano**: Add professor2 created: 2014-03-17T13:41:16Z merged: None

1. [2888](http://github.com/cms-sw/cmssw/pull/2888){:target="_blank"}  from **@smuzaffar**: New standalone dasgoclient  created: 2014-03-17T12:18:42Z merged: 2014-03-28T22:05:00Z

1. [2887](http://github.com/cms-sw/cmssw/pull/2887){:target="_blank"}  from **@cms-sw**: Update protobuf.spec created: 2014-03-17T12:05:44Z merged: None

1. [2882](http://github.com/cms-sw/cmssw/pull/2882){:target="_blank"}  from **@davidlange6**: protobuf update created: 2014-03-16T16:40:51Z merged: 2014-03-17T16:18:43Z

1. [2881](http://github.com/cms-sw/cmssw/pull/2881){:target="_blank"}  from **@davidlange6**: Tqdm python package created: 2014-03-16T16:11:06Z merged: 2014-03-17T16:19:11Z
