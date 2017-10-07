---
layout: post
title:  "7_6_0_pre5"
date:   2017-10-07 19:52:18 +0200
categories: cmssw
relmajor: 7
relminor: 6
relsubminor: 0
relpre: _pre5
---

# CMSSW_7_6_0_pre5
#### Changes since CMSSW_7_6_0_pre4:

[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_7_6_0_pre4...CMSSW_7_6_0_pre5)



1. [11132](http://github.com/cms-sw/cmssw/pull/11132){:target="_blank"}  from **@davidsheffield**: Add scouting electron, photon, and muon classes and producers `hlt`  created: 2015-09-04T14:55:13Z merged: 2015-09-11T09:31:46Z

1. [11135](http://github.com/cms-sw/cmssw/pull/11135){:target="_blank"}  from **@Dr15Jones**: Made MaterialAccountingTrack const correct `simulation`  created: 2015-09-04T15:55:33Z merged: 2015-09-11T09:30:24Z

1. [11043](http://github.com/cms-sw/cmssw/pull/11043){:target="_blank"}  from **@cms-tsg-storm**: 76X 25ns HLT round three `hlt`  created: 2015-08-31T13:32:57Z merged: 2015-09-11T07:56:32Z

1. [11183](http://github.com/cms-sw/cmssw/pull/11183){:target="_blank"}  from **@makortel**: Fix MeasurementTrackerEvent configuration of some TrackingRegionProducers `fastsim`  `hlt`  `reconstruction`  created: 2015-09-08T07:32:48Z merged: 2015-09-11T07:51:10Z

1. [11140](http://github.com/cms-sw/cmssw/pull/11140){:target="_blank"}  from **@cvuosalo**: Convert remaining legacy modules in RECO to support multi-threading `analysis`  `reconstruction`  created: 2015-09-04T17:14:42Z merged: 2015-09-11T07:05:08Z

1. [11146](http://github.com/cms-sw/cmssw/pull/11146){:target="_blank"}  from **@Dr15Jones**: Use iorule to remove mutables from CandKinResolution `analysis`  created: 2015-09-04T21:03:14Z merged: 2015-09-11T07:03:53Z

1. [11158](http://github.com/cms-sw/cmssw/pull/11158){:target="_blank"}  from **@smorovic**: Fix premature end of run in DAQ (76X) `daq`  `reconstruction`  created: 2015-09-05T21:38:25Z merged: 2015-09-11T07:02:35Z

1. [11219](http://github.com/cms-sw/cmssw/pull/11219){:target="_blank"}  from **@ndaci**:  Updated paths (DiPhoton, HighPtPhoton). `dqm`  created: 2015-09-10T10:39:37Z merged: 2015-09-11T06:59:47Z

1. [11145](http://github.com/cms-sw/cmssw/pull/11145){:target="_blank"}  from **@Dr15Jones**: Made PFTau const thread-safe `reconstruction`  created: 2015-09-04T19:50:16Z merged: 2015-09-10T09:01:26Z

1. [11173](http://github.com/cms-sw/cmssw/pull/11173){:target="_blank"}  from **@slava77**: cleanup of uninitialized reads reported by valgrind `analysis`  `dqm`  `reconstruction`  created: 2015-09-07T19:30:16Z merged: 2015-09-10T08:57:19Z

1. [11201](http://github.com/cms-sw/cmssw/pull/11201){:target="_blank"}  from **@lveldere**: FastSim, use cms::Exception rather than logError + exit `fastsim`  created: 2015-09-09T12:57:42Z merged: 2015-09-10T08:31:14Z

1. [11202](http://github.com/cms-sw/cmssw/pull/11202){:target="_blank"}  from **@smuzaffar**: fixed typo: RecoEGamma/Examples -> RecoEgamma/Examples `core`  created: 2015-09-09T13:17:28Z merged: 2015-09-09T13:23:02Z

1. [11139](http://github.com/cms-sw/cmssw/pull/11139){:target="_blank"}  from **@matteosan1**: Roll-back to old configuration to fix issue in VID `reconstruction`  created: 2015-09-04T16:19:24Z merged: 2015-09-09T12:21:21Z

1. [11121](http://github.com/cms-sw/cmssw/pull/11121){:target="_blank"}  from **@lveldere**: Fastsim newrechits rebase sep4 `analysis`  `fastsim`  `geometry`  `reconstruction`  `simulation`  created: 2015-09-04T09:44:33Z merged: 2015-09-09T10:20:17Z

1. [11063](http://github.com/cms-sw/cmssw/pull/11063){:target="_blank"}  from **@ndaci**: Added a new path in DiPhoton category. `dqm`  created: 2015-09-01T15:24:51Z merged: 2015-09-09T05:25:38Z

1. [11192](http://github.com/cms-sw/cmssw/pull/11192){:target="_blank"}  from **@Dr15Jones**: Marked DataProxy as thread safe `core`  created: 2015-09-08T19:53:07Z merged: 2015-09-09T05:23:31Z

1. [11089](http://github.com/cms-sw/cmssw/pull/11089){:target="_blank"}  from **@VinInn**: fix inner outer for OutIn `reconstruction`  created: 2015-09-02T16:01:35Z merged: 2015-09-09T05:23:12Z

1. [11079](http://github.com/cms-sw/cmssw/pull/11079){:target="_blank"}  from **@pietverwilligen**: Update test gem rec hit analyzer `reconstruction`  created: 2015-09-02T10:37:23Z merged: 2015-09-08T12:35:47Z

1. [11035](http://github.com/cms-sw/cmssw/pull/11035){:target="_blank"}  from **@ebouvier**: Top trigger names for 25 ns 76X `dqm`  created: 2015-08-31T08:20:02Z merged: 2015-09-08T12:35:14Z

1. [11083](http://github.com/cms-sw/cmssw/pull/11083){:target="_blank"}  from **@wulsin**: Add customize configuration file to produce/keep a collection of part? `simulation`  created: 2015-09-02T13:05:42Z merged: 2015-09-08T05:31:09Z

1. [11161](http://github.com/cms-sw/cmssw/pull/11161){:target="_blank"}  from **@Sam-Harper**: DiEle25 dqm update `dqm`  created: 2015-09-06T15:42:43Z merged: 2015-09-08T05:26:09Z

1. [11115](http://github.com/cms-sw/cmssw/pull/11115){:target="_blank"}  from **@smorovic**: Streamer output modules ported to one::OutputModule (76X) `core`  `daq`  `dqm`  `reconstruction`  created: 2015-09-03T21:05:11Z merged: 2015-09-08T05:21:29Z

1. [11142](http://github.com/cms-sw/cmssw/pull/11142){:target="_blank"}  from **@Dr15Jones**: Made BeamCurrentInfo thread-safe via use of iorules `reconstruction`  created: 2015-09-04T18:14:35Z merged: 2015-09-08T05:21:25Z

1. [11170](http://github.com/cms-sw/cmssw/pull/11170){:target="_blank"}  from **@dmitrijus**: Fix a 'kNoTypesStored' bug in DQMRootSource (76x) `dqm`  created: 2015-09-07T09:02:06Z merged: 2015-09-08T05:21:09Z

1. [11167](http://github.com/cms-sw/cmssw/pull/11167){:target="_blank"}  from **@alja**: 75x Fireworks: auto-detect configuration after opening first file -- git reattempt 2 `visualization`  created: 2015-09-06T21:51:56Z merged: 2015-09-07T10:01:22Z

1. [11144](http://github.com/cms-sw/cmssw/pull/11144){:target="_blank"}  from **@Dr15Jones**: Release shared resources when use mayConsumes `core`  `simulation`  created: 2015-09-04T19:35:23Z merged: 2015-09-07T05:54:27Z

1. [11112](http://github.com/cms-sw/cmssw/pull/11112){:target="_blank"}  from **@makortel**: Forward originalAlgo and algoMask in TrackRefitter `reconstruction`  created: 2015-09-03T14:31:03Z merged: 2015-09-05T06:56:14Z

1. [11143](http://github.com/cms-sw/cmssw/pull/11143){:target="_blank"}  from **@wmtan**: Maintainability cleanup for EventSelector `core`  created: 2015-09-04T18:24:31Z merged: 2015-09-05T06:56:09Z

1. [11147](http://github.com/cms-sw/cmssw/pull/11147){:target="_blank"}  from **@gartung**: Only check const cast away in CStyle casts and const_cast<> expresssions `core`  created: 2015-09-04T21:44:46Z merged: 2015-09-05T06:51:10Z

1. [10904](http://github.com/cms-sw/cmssw/pull/10904){:target="_blank"}  from **@ggovi**: Prototype of payload inspector modules for V2 `alca`  `db`  created: 2015-08-21T14:32:37Z merged: 2015-09-04T15:51:45Z

1. [10821](http://github.com/cms-sw/cmssw/pull/10821){:target="_blank"}  from **@slehti**: Hlt tau validation update76X `dqm`  created: 2015-08-17T15:11:43Z merged: 2015-09-04T15:46:43Z

1. [11125](http://github.com/cms-sw/cmssw/pull/11125){:target="_blank"}  from **@vasile-ghete**: Cmssw 7 6 x L1 gt utils update `l1`  created: 2015-09-04T12:46:03Z merged: 2015-09-04T15:43:59Z

1. [11097](http://github.com/cms-sw/cmssw/pull/11097){:target="_blank"}  from **@civanch**: Fixed static analyzer warnings `simulation`  created: 2015-09-03T08:54:18Z merged: 2015-09-04T13:31:36Z

1. [11106](http://github.com/cms-sw/cmssw/pull/11106){:target="_blank"}  from **@istaslis**: Added dummy parameters to HIMultiTrackSelector `reconstruction`  created: 2015-09-03T11:52:46Z merged: 2015-09-04T09:51:29Z

1. [10972](http://github.com/cms-sw/cmssw/pull/10972){:target="_blank"}  from **@degano**: Fix EvtGenInterface report instruction to comply with evtgen 1.4. `generators`  created: 2015-08-27T08:08:57Z merged: 2015-09-04T09:01:37Z

1. [10911](http://github.com/cms-sw/cmssw/pull/10911){:target="_blank"}  from **@makortel**: Transform RecoTrackRefSelector to stream::EDProducer `hlt`  `reconstruction`  created: 2015-08-24T07:15:34Z merged: 2015-09-04T07:21:37Z

1. [11099](http://github.com/cms-sw/cmssw/pull/11099){:target="_blank"}  from **@heppye**: Create Create Bd_JpsiKPi.dec `generators`  created: 2015-09-03T09:01:21Z merged: 2015-09-03T14:01:51Z

1. [10242](http://github.com/cms-sw/cmssw/pull/10242){:target="_blank"}  from **@hdelanno**: Addition of histograms for SiStrip : Cluster widths vs amplitudes `dqm`  created: 2015-07-16T12:21:05Z merged: 2015-09-03T10:52:09Z

1. [11050](http://github.com/cms-sw/cmssw/pull/11050){:target="_blank"}  from **@fwyzard**: DQMStore::removeElement: do not remove non-existing MEs `dqm`  created: 2015-08-31T20:51:58Z merged: 2015-09-03T10:51:45Z

1. [10907](http://github.com/cms-sw/cmssw/pull/10907){:target="_blank"}  from **@ndaci**: Fixed path names. Removed pt2 and pt3 in unnecessary cases. Added deb? `dqm`  created: 2015-08-22T13:11:33Z merged: 2015-09-03T07:56:30Z

1. [11072](http://github.com/cms-sw/cmssw/pull/11072){:target="_blank"}  from **@fwyzard**: migrate modules used by the HLT menu to multithreading (L1) (76x) `l1`  created: 2015-09-02T07:18:28Z merged: 2015-09-03T07:53:41Z

1. [10974](http://github.com/cms-sw/cmssw/pull/10974){:target="_blank"}  from **@ndaci**: Update paths. `dqm`  created: 2015-08-27T08:44:46Z merged: 2015-09-03T07:51:45Z

1. [10989](http://github.com/cms-sw/cmssw/pull/10989){:target="_blank"}  from **@ianna**: Update Validation to Use Default GT `db`  `dqm`  `geometry`  created: 2015-08-27T14:56:27Z merged: 2015-09-03T07:51:39Z

1. [11001](http://github.com/cms-sw/cmssw/pull/11001){:target="_blank"}  from **@lveldere**: Introduce slim track validation sequences  `dqm`  created: 2015-08-28T10:03:49Z merged: 2015-09-03T07:51:33Z

1. [11040](http://github.com/cms-sw/cmssw/pull/11040){:target="_blank"}  from **@danduggan**: Patching to better handle LS based histos during LS transitions in 76x `dqm`  created: 2015-08-31T11:34:59Z merged: 2015-09-03T07:51:23Z

1. [11090](http://github.com/cms-sw/cmssw/pull/11090){:target="_blank"}  from **@gartung**: add edm::serviceregistry::ServicesManager::MakerHolder::add() to skip? `core`  created: 2015-09-02T17:27:29Z merged: 2015-09-03T07:51:18Z

1. [11029](http://github.com/cms-sw/cmssw/pull/11029){:target="_blank"}  from **@davidsheffield**: Add index to primary vertex in scouting particle collection `hlt`  created: 2015-08-31T00:04:45Z merged: 2015-09-03T07:48:11Z

1. [11073](http://github.com/cms-sw/cmssw/pull/11073){:target="_blank"}  from **@cms-sw**: Revert "adding David Lange's comments built on rebase of ValidationDo? `dqm`  `generators`  created: 2015-09-02T07:32:31Z merged: 2015-09-02T07:41:14Z

1. [10695](http://github.com/cms-sw/cmssw/pull/10695){:target="_blank"}  from **@cms-l1t-offline**: Add HF Minimum Bias algorithm to Stage1 Emulator `l1`  created: 2015-08-11T18:02:24Z merged: 2015-09-02T06:31:29Z

1. [10963](http://github.com/cms-sw/cmssw/pull/10963){:target="_blank"}  from **@ngrenz**: ngrenz: testing of stereo optimization `reconstruction`  `simulation`  created: 2015-08-27T04:44:22Z merged: 2015-09-02T06:26:48Z

1. [10984](http://github.com/cms-sw/cmssw/pull/10984){:target="_blank"}  from **@davidlt**: runTheMatrix.py: misc cleanups; make --showMatrix consistent `pdmv`  created: 2015-08-27T13:21:49Z merged: 2015-09-02T06:26:30Z

1. [11028](http://github.com/cms-sw/cmssw/pull/11028){:target="_blank"}  from **@ahinzmann**: Add energy correlation functions to jet tools `reconstruction`  created: 2015-08-29T21:44:28Z merged: 2015-09-02T06:26:25Z

1. [10917](http://github.com/cms-sw/cmssw/pull/10917){:target="_blank"}  from **@gpetruc**: Add L1 prescales to the miniAOD (76X port of #10895) `analysis`  created: 2015-08-24T09:47:36Z merged: 2015-09-02T06:26:17Z

1. [11045](http://github.com/cms-sw/cmssw/pull/11045){:target="_blank"}  from **@kkiesel**: Fastsim ECAL response correction (2) `fastsim`  created: 2015-08-31T14:54:02Z merged: 2015-09-02T06:26:11Z

1. [11066](http://github.com/cms-sw/cmssw/pull/11066){:target="_blank"}  from **@wmtan**: Use anonymous namespaces to avoid duplicate symbols `reconstruction`  created: 2015-09-01T18:37:52Z merged: 2015-09-02T06:21:10Z

1. [11053](http://github.com/cms-sw/cmssw/pull/11053){:target="_blank"}  from **@fwyzard**: migrate L1 and HLT summary modules to one::EDAnalyzer `hlt`  `l1`  created: 2015-08-31T20:58:25Z merged: 2015-09-01T16:16:42Z

1. [10958](http://github.com/cms-sw/cmssw/pull/10958){:target="_blank"}  from **@fwyzard**: migrate modules used by the HLT menu to multithreading (various) `analysis`  `db`  `dqm`  `hlt`  `l1`  created: 2015-08-26T15:43:19Z merged: 2015-09-01T16:12:49Z

1. [10842](http://github.com/cms-sw/cmssw/pull/10842){:target="_blank"}  from **@apfeiffer1**: update of the XML conversion in C++  `db`  created: 2015-08-18T14:48:32Z merged: 2015-09-01T16:12:39Z

1. [10971](http://github.com/cms-sw/cmssw/pull/10971){:target="_blank"}  from **@cerminar**: First integration of Pixel Alignment of large structures in PCL - updated (76X)  `alca`  `db`  `operations`  `pdmv`  created: 2015-08-27T07:35:07Z merged: 2015-09-01T05:21:43Z

1. [10977](http://github.com/cms-sw/cmssw/pull/10977){:target="_blank"}  from **@kodolova**: Fix bug in JetPlusTrackCorrections_cff.py: add JetVertexExtender `reconstruction`  created: 2015-08-27T09:37:37Z merged: 2015-09-01T05:21:35Z

1. [11051](http://github.com/cms-sw/cmssw/pull/11051){:target="_blank"}  from **@fwyzard**: ThroughputServiceClient: add more throughput plots `hlt`  created: 2015-08-31T20:54:47Z merged: 2015-09-01T05:21:10Z

1. [10836](http://github.com/cms-sw/cmssw/pull/10836){:target="_blank"}  from **@cms-tsg-storm**: Round Two 25ns HLT updates (76X) `hlt`  created: 2015-08-18T08:06:32Z merged: 2015-08-31T09:51:54Z

1. [10979](http://github.com/cms-sw/cmssw/pull/10979){:target="_blank"}  from **@lveldere**: FastSim: remove import of non-existing cfg from START geometry `fastsim`  created: 2015-08-27T12:09:58Z merged: 2015-08-31T09:46:47Z

1. [10988](http://github.com/cms-sw/cmssw/pull/10988){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `alca`  created: 2015-08-27T14:52:47Z merged: 2015-08-30T14:18:36Z

1. [11018](http://github.com/cms-sw/cmssw/pull/11018){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `l1`  created: 2015-08-28T17:45:01Z merged: 2015-08-30T14:17:17Z

1. [11017](http://github.com/cms-sw/cmssw/pull/11017){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `l1`  created: 2015-08-28T17:25:34Z merged: 2015-08-30T14:17:00Z

1. [11016](http://github.com/cms-sw/cmssw/pull/11016){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `dqm`  created: 2015-08-28T16:55:10Z merged: 2015-08-30T14:16:40Z

1. [11015](http://github.com/cms-sw/cmssw/pull/11015){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `dqm`  created: 2015-08-28T15:55:31Z merged: 2015-08-30T14:16:22Z

1. [11014](http://github.com/cms-sw/cmssw/pull/11014){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `generators`  created: 2015-08-28T15:29:42Z merged: 2015-08-30T14:16:04Z

1. [11006](http://github.com/cms-sw/cmssw/pull/11006){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `analysis`  created: 2015-08-28T14:16:57Z merged: 2015-08-30T14:15:46Z

1. [11005](http://github.com/cms-sw/cmssw/pull/11005){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `dqm`  `l1`  created: 2015-08-28T14:10:30Z merged: 2015-08-30T14:15:28Z

1. [11003](http://github.com/cms-sw/cmssw/pull/11003){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `dqm`  created: 2015-08-28T14:04:23Z merged: 2015-08-30T14:15:07Z

1. [10997](http://github.com/cms-sw/cmssw/pull/10997){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `dqm`  created: 2015-08-28T02:42:46Z merged: 2015-08-30T14:14:49Z

1. [10990](http://github.com/cms-sw/cmssw/pull/10990){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `alca`  `l1`  created: 2015-08-27T15:30:29Z merged: 2015-08-30T14:14:30Z

1. [10653](http://github.com/cms-sw/cmssw/pull/10653){:target="_blank"}  from **@echapon**: New track algorithm names for HI muon RegIt `reconstruction`  created: 2015-08-10T15:15:48Z merged: 2015-08-30T07:16:17Z

1. [10947](http://github.com/cms-sw/cmssw/pull/10947){:target="_blank"}  from **@ssanders50**: boundary check `reconstruction`  created: 2015-08-26T09:26:12Z merged: 2015-08-30T07:16:09Z

1. [10873](http://github.com/cms-sw/cmssw/pull/10873){:target="_blank"}  from **@lgray**: Important-> EDM IDs update, Fixed typo in effective areas. `analysis`  `reconstruction`  created: 2015-08-20T10:29:32Z merged: 2015-08-30T07:11:29Z

1. [10923](http://github.com/cms-sw/cmssw/pull/10923){:target="_blank"}  from **@ahinzmann**: Switch to latest pileup jet id in DQM `dqm`  created: 2015-08-24T15:02:38Z merged: 2015-08-30T07:11:22Z

1. [10951](http://github.com/cms-sw/cmssw/pull/10951){:target="_blank"}  from **@wmtan**: Thread Safety: Remove unneeded state from TriggerResultsBasedEventSelector `core`  created: 2015-08-26T14:57:04Z merged: 2015-08-30T07:11:10Z

1. [10995](http://github.com/cms-sw/cmssw/pull/10995){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `dqm`  created: 2015-08-28T02:09:42Z merged: 2015-08-30T07:07:36Z

1. [10996](http://github.com/cms-sw/cmssw/pull/10996){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `dqm`  created: 2015-08-28T02:28:31Z merged: 2015-08-30T07:07:13Z

1. [11000](http://github.com/cms-sw/cmssw/pull/11000){:target="_blank"}  from **@fwyzard**: more cleanup of RecoLocalMuon/RPCRecHit `reconstruction`  created: 2015-08-28T08:39:18Z merged: 2015-08-30T07:06:55Z

1. [11011](http://github.com/cms-sw/cmssw/pull/11011){:target="_blank"}  from **@Dr15Jones**: Fix bug preventing the use of a local cache `core`  created: 2015-08-28T14:41:22Z merged: 2015-08-30T07:06:49Z

1. [11020](http://github.com/cms-sw/cmssw/pull/11020){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `reconstruction`  created: 2015-08-28T18:41:02Z merged: 2015-08-30T07:06:44Z

1. [11021](http://github.com/cms-sw/cmssw/pull/11021){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `simulation`  created: 2015-08-28T18:41:52Z merged: 2015-08-30T07:06:38Z

1. [10998](http://github.com/cms-sw/cmssw/pull/10998){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `dqm`  created: 2015-08-28T02:52:59Z merged: 2015-08-30T07:06:06Z

1. [11008](http://github.com/cms-sw/cmssw/pull/11008){:target="_blank"}  from **@gartung**: Event filter utilities fix clang warning `daq`  `hlt`  `reconstruction`  created: 2015-08-28T14:36:34Z merged: 2015-08-30T07:05:10Z

1. [11019](http://github.com/cms-sw/cmssw/pull/11019){:target="_blank"}  from **@gartung**: fix clang static analyzer warning using namespace in header `analysis`  created: 2015-08-28T18:16:06Z merged: 2015-08-30T07:04:05Z

#### CMSDIST Changes between Tags REL/CMSSW_7_6_0_pre4/slc6_amd64_gcc493 and REL/CMSSW_7_6_0_pre5/slc6_amd64_gcc493:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_7_6_0_pre4/slc6_amd64_gcc493...REL/CMSSW_7_6_0_pre5/slc6_amd64_gcc493)



1. [1803](http://github.com/cms-sw/cmssw/pull/1803){:target="_blank"}  from **@degano**: Update geant4 to version 10.01.p02. created: 2013-12-13T12:37:06Z merged: 2013-12-14T18:06:43Z

1. [1802](http://github.com/cms-sw/cmssw/pull/1802){:target="_blank"}  from **@smuzaffar**: move to latest config tag V05-05-03 created: 2013-12-13T12:26:52Z merged: 2013-12-14T18:06:09Z

1. [1800](http://github.com/cms-sw/cmssw/pull/1800){:target="_blank"}  from **@degano**: Update data for Configuration/Generator. created: 2013-12-13T11:12:46Z merged: 2013-12-13T11:13:00Z

1. [1777](http://github.com/cms-sw/cmssw/pull/1777){:target="_blank"}  from **@cms-sw**: Revert "Revert "upgrade to evtgen 1.4.0p1"" created: 2013-12-11T20:20:31Z merged: 2013-12-12T12:58:45Z

1. [1795](http://github.com/cms-sw/cmssw/pull/1795){:target="_blank"}  from **@degano**: Create new data for RecoBTag/CTagging from repository. created: 2013-12-12T20:18:11Z merged: None

1. [1791](http://github.com/cms-sw/cmssw/pull/1791){:target="_blank"}  from **@degano**: Update Root to the tip of the branch 6.02.00-patches. created: 2013-12-12T18:03:06Z merged: 2013-12-15T08:59:33Z

1. [1775](http://github.com/cms-sw/cmssw/pull/1775){:target="_blank"}  from **@davidlt**: GDB, SQLite, CMake, CGAL, libxslt updates created: 2013-12-11T18:46:58Z merged: 2013-12-12T21:36:05Z

1. [1786](http://github.com/cms-sw/cmssw/pull/1786){:target="_blank"}  from **@degano**: Add python modules: PyYAML, docopt, prettytable, schema. created: 2013-12-12T15:36:40Z merged: 2013-12-16T09:20:57Z

1. [1781](http://github.com/cms-sw/cmssw/pull/1781){:target="_blank"}  from **@degano**: Update to latest CondFormats/JetMETObjects created: 2013-12-12T09:38:53Z merged: 2013-12-13T14:57:43Z
