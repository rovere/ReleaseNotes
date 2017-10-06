---
layout: post
title:  "7_2_0_pre1"
date:   2017-10-06 17:36:55 +0200
categories: cmssw
relmajor: 7
relminor: 2
relsubminor: 0
relpre: _pre1
---

# CMSSW_7_2_0_pre1
#### Changes since CMSSW_7_1_0:

1. [4366](http://github.com/cms-sw/cmssw/pull/4366){:target="_blank"}  from **@ahinzmann**: Adapt edmConfigEditor for unscheduled mode. `core`  created: 2014-06-24T09:20:13Z merged: 2014-06-24T11:40:06Z

1. [4347](http://github.com/cms-sw/cmssw/pull/4347){:target="_blank"}  from **@jpavel**: Adding offset parameter to the tau isolation. `reconstruction`  created: 2014-06-23T09:52:42Z merged: 2014-06-24T11:39:09Z

1. [4368](http://github.com/cms-sw/cmssw/pull/4368){:target="_blank"}  from **@cms-sw**: Forward port CMSSW_7_1_X into CMSSW_7_2_X `operations`  `simulation`  created: 2014-06-24T09:53:45Z merged: 2014-06-24T10:52:11Z

1. [4356](http://github.com/cms-sw/cmssw/pull/4356){:target="_blank"}  from **@ktf**: Fix forward port 72x `alca`  `analysis`  `daq`  `db`  `dqm`  `fastsim`  `hlt`  `l1`  `operations`  `reconstruction`  `simulation`  `visualization`  created: 2014-06-23T15:02:11Z merged: 2014-06-24T08:37:55Z

1. [4343](http://github.com/cms-sw/cmssw/pull/4343){:target="_blank"}  from **@Martin-Grunewald**: CMSSW 710 template in ConfDb for HLT menues in 72X. `hlt`  created: 2014-06-23T08:35:13Z merged: 2014-06-24T04:55:23Z

1. [4360](http://github.com/cms-sw/cmssw/pull/4360){:target="_blank"}  from **@civanch**: cleanup generator interface as in 4306 `simulation`  created: 2014-06-23T16:50:52Z merged: 2014-06-24T04:52:39Z

1. [4232](http://github.com/cms-sw/cmssw/pull/4232){:target="_blank"}  from **@ktf**: Fix forward port from CMSSW_7_1_X to CMSSW_7_2_X `core`  `geometry`  `hlt`  `l1`  created: 2014-06-13T11:46:24Z merged: 2014-06-23T12:51:44Z

1. [4322](http://github.com/cms-sw/cmssw/pull/4322){:target="_blank"}  from **@wmtan**: Remove line breaks. They cause problems `reconstruction`  created: 2014-06-19T22:26:58Z merged: 2014-06-23T07:31:29Z

1. [4317](http://github.com/cms-sw/cmssw/pull/4317){:target="_blank"}  from **@cerati**: MultiTrackValidator remove vectors and remove unused plots. `dqm`  created: 2014-06-19T15:53:58Z merged: 2014-06-22T22:04:10Z

1. [4174](http://github.com/cms-sw/cmssw/pull/4174){:target="_blank"}  from **@Dr15Jones**: Removed unnecessary mutable from GlobalTriggerMenu `alca`  `db`  `l1`  created: 2014-06-09T22:13:14Z merged: 2014-06-22T15:28:10Z

1. [4320](http://github.com/cms-sw/cmssw/pull/4320){:target="_blank"}  from **@srimanob**: fix postLS1Customs.py `simulation`  created: 2014-06-19T21:01:26Z merged: 2014-06-22T15:26:35Z

1. [4329](http://github.com/cms-sw/cmssw/pull/4329){:target="_blank"}  from **@rcastello**: Updated GTs for 7_2_0_pre1 `alca`  created: 2014-06-20T11:18:17Z merged: 2014-06-20T18:59:38Z

1. [4259](http://github.com/cms-sw/cmssw/pull/4259){:target="_blank"}  from **@TaiSakuma**: code-cleaning in RecoMET/METProducers/python `reconstruction`  created: 2014-06-16T00:45:47Z merged: 2014-06-20T17:03:26Z

1. [4282](http://github.com/cms-sw/cmssw/pull/4282){:target="_blank"}  from **@TaiSakuma**: delete "calotoweroptmaker" `dqm`  `operations`  `reconstruction`  `simulation`  created: 2014-06-16T23:50:20Z merged: 2014-06-20T14:20:10Z

1. [4324](http://github.com/cms-sw/cmssw/pull/4324){:target="_blank"}  from **@mdhildreth**: Change DataMixer to merge CSC Strip Digis instead of adding duplicates `simulation`  created: 2014-06-20T04:15:26Z merged: 2014-06-20T12:08:52Z

1. [4308](http://github.com/cms-sw/cmssw/pull/4308){:target="_blank"}  from **@deguio**: Update the configuration of the FastTimerService used for Offline DQM: same as #4307 `dqm`  created: 2014-06-18T18:06:39Z merged: 2014-06-20T09:01:28Z

1. [4314](http://github.com/cms-sw/cmssw/pull/4314){:target="_blank"}  from **@gartung**: Remove unused declaration `core`  created: 2014-06-19T14:20:30Z merged: 2014-06-19T14:24:16Z

1. [4293](http://github.com/cms-sw/cmssw/pull/4293){:target="_blank"}  from **@VinInn**: TLS cleanup `alca`  `db`  `reconstruction`  created: 2014-06-17T13:34:13Z merged: 2014-06-19T14:08:31Z

1. [4285](http://github.com/cms-sw/cmssw/pull/4285){:target="_blank"}  from **@apfeiffer1**: explicitly convert Time_t to RunNumber to avoid compiler warning `alca`  created: 2014-06-17T08:20:02Z merged: 2014-06-19T09:19:43Z

1. [4299](http://github.com/cms-sw/cmssw/pull/4299){:target="_blank"}  from **@HuguesBrun**: Fix in Higgs HLT validation DQM for multithreading `dqm`  created: 2014-06-18T07:54:53Z merged: 2014-06-19T06:55:05Z

1. [4303](http://github.com/cms-sw/cmssw/pull/4303){:target="_blank"}  from **@deguio**: Handle correctly the ME which are not TH1 [int,string,float] `dqm`  created: 2014-06-18T12:45:55Z merged: 2014-06-18T16:38:03Z

1. [4291](http://github.com/cms-sw/cmssw/pull/4291){:target="_blank"}  from **@thuer**: Sherpa 2.1.1 API changes. `generators`  created: 2014-06-17T12:53:10Z merged: 2014-06-18T08:07:15Z

1. [4298](http://github.com/cms-sw/cmssw/pull/4298){:target="_blank"}  from **@threus**: Thread safety fixes for DQM/SiStripMonitorHardware `dqm`  created: 2014-06-17T17:38:16Z merged: 2014-06-18T08:05:34Z

1. [4260](http://github.com/cms-sw/cmssw/pull/4260){:target="_blank"}  from **@barvic**: CSC DDU IDs fix for post-LS1 configuration `dqm`  `reconstruction`  created: 2014-06-16T01:32:15Z merged: 2014-06-18T06:42:04Z

1. [4297](http://github.com/cms-sw/cmssw/pull/4297){:target="_blank"}  from **@deguio**: move L1TFED to DQMEDAnalyzer interface `dqm`  created: 2014-06-17T17:10:10Z merged: 2014-06-18T06:41:17Z

1. [4239](http://github.com/cms-sw/cmssw/pull/4239){:target="_blank"}  from **@cerati**: MultiTrackValidator: add efficiency and fakerate vs deltaR `dqm`  created: 2014-06-13T14:41:42Z merged: 2014-06-17T19:22:09Z

1. [4269](http://github.com/cms-sw/cmssw/pull/4269){:target="_blank"}  from **@perrotta**: HLT run2 updates `hlt`  created: 2014-06-16T12:09:40Z merged: 2014-06-17T13:49:25Z

1. [4253](http://github.com/cms-sw/cmssw/pull/4253){:target="_blank"}  from **@davidlange6**: clear map before each event is processed in PhotonMCTruthFinder `dqm`  `reconstruction`  created: 2014-06-15T17:12:22Z merged: 2014-06-17T05:44:59Z

1. [4248](http://github.com/cms-sw/cmssw/pull/4248){:target="_blank"}  from **@gartung**: Virtual function calls of the for Foo::bar() are not linked to their override `core`  created: 2014-06-14T16:15:37Z merged: 2014-06-16T21:18:23Z

1. [4182](http://github.com/cms-sw/cmssw/pull/4182){:target="_blank"}  from **@perrotta**: HLT run2 menu `alca`  `fastsim`  `hlt`  created: 2014-06-10T12:51:44Z merged: 2014-06-16T09:09:36Z

1. [4236](http://github.com/cms-sw/cmssw/pull/4236){:target="_blank"}  from **@deguio**: Fix a static variable which was removed by mistake in DQM/BeamMonitor `dqm`  created: 2014-06-13T14:15:19Z merged: 2014-06-16T07:35:54Z

1. [4045](http://github.com/cms-sw/cmssw/pull/4045){:target="_blank"}  from **@TaiSakuma**: Use new implementation of MET corrections in PAT jetTools and start refactoring the MET uncertainty tool `analysis`  created: 2014-05-28T23:11:11Z merged: 2014-06-16T06:14:07Z

1. [4043](http://github.com/cms-sw/cmssw/pull/4043){:target="_blank"}  from **@Dr15Jones**: Fixed incorrect virtual function overload in TSelectorAnalyzer `analysis`  created: 2014-05-28T19:53:40Z merged: 2014-06-16T06:13:30Z

1. [4090](http://github.com/cms-sw/cmssw/pull/4090){:target="_blank"}  from **@sethcooper**: Update to sourcing data format and unpacker `reconstruction`  created: 2014-06-02T17:13:25Z merged: 2014-06-16T06:13:11Z

1. [4091](http://github.com/cms-sw/cmssw/pull/4091){:target="_blank"}  from **@Dr15Jones**: Changed TrackWithVertexRefSelector to a stream module. `analysis`  `reconstruction`  created: 2014-06-02T17:36:43Z merged: 2014-06-15T19:57:58Z

1. [4252](http://github.com/cms-sw/cmssw/pull/4252){:target="_blank"}  from **@davidlange6**: fix memory leak Validation/EventGenerator created: 2014-06-15T17:06:19Z merged: 2014-06-15T17:06:32Z

1. [4250](http://github.com/cms-sw/cmssw/pull/4250){:target="_blank"}  from **@Dr15Jones**: Removed old Timing plugin declaration `core`  created: 2014-06-15T00:55:42Z merged: 2014-06-15T06:47:26Z

1. [4064](http://github.com/cms-sw/cmssw/pull/4064){:target="_blank"}  from **@ericvaandering**: Improve LumiList `core`  created: 2014-05-30T19:03:03Z merged: 2014-06-14T05:55:49Z

1. [4096](http://github.com/cms-sw/cmssw/pull/4096){:target="_blank"}  from **@ktf**: Final clang fix. `analysis`  `core`  created: 2014-06-03T09:34:11Z merged: 2014-06-13T20:17:31Z

1. [4227](http://github.com/cms-sw/cmssw/pull/4227){:target="_blank"}  from **@wmtan**: Use std::shared_ptr, not boost::shared_ptr `analysis`  `core`  `daq`  `dqm`  `generators`  `geometry`  `reconstruction`  `simulation`  `visualization`  created: 2014-06-12T21:07:30Z merged: 2014-06-13T11:58:43Z

1. [4230](http://github.com/cms-sw/cmssw/pull/4230){:target="_blank"}  from **@ktf**: Drop unused variable. `core`  created: 2014-06-13T10:02:15Z merged: 2014-06-13T10:30:13Z

1. [4213](http://github.com/cms-sw/cmssw/pull/4213){:target="_blank"}  from **@Dr15Jones**: Add ability to account for additional CPU time per event. `core`  created: 2014-06-11T19:49:36Z merged: 2014-06-13T09:10:28Z

1. [4173](http://github.com/cms-sw/cmssw/pull/4173){:target="_blank"}  from **@Dr15Jones**: Removed unneeded const_cast from TrackAssociatorByHits `simulation`  created: 2014-06-09T21:52:17Z merged: 2014-06-13T08:58:15Z

1. [4162](http://github.com/cms-sw/cmssw/pull/4162){:target="_blank"}  from **@cerati**: Jet core step from710pre8 fixed `dqm`  `reconstruction`  created: 2014-06-09T15:17:10Z merged: 2014-06-13T07:21:09Z

1. [4220](http://github.com/cms-sw/cmssw/pull/4220){:target="_blank"}  from **@jpavel**: Removed duplicated definitions of EDProducers. `reconstruction`  created: 2014-06-12T12:36:23Z merged: 2014-06-13T07:19:24Z

1. [4034](http://github.com/cms-sw/cmssw/pull/4034){:target="_blank"}  from **@barvic**: Post-LS1 CSC integration - updated to new data format CSC packer / unpacker `analysis`  `dqm`  `reconstruction`  created: 2014-05-28T13:33:23Z merged: 2014-06-13T07:18:52Z

1. [4106](http://github.com/cms-sw/cmssw/pull/4106){:target="_blank"}  from **@deguio**: Move the Vx3DHLTAnalyzer class to the DQMEDAnalyzer interface `dqm`  created: 2014-06-04T11:47:08Z merged: 2014-06-12T18:42:02Z

1. [4114](http://github.com/cms-sw/cmssw/pull/4114){:target="_blank"}  from **@TaiSakuma**: Change the naming convention of CaloMETs `reconstruction`  created: 2014-06-05T02:25:46Z merged: 2014-06-12T17:50:25Z

1. [4112](http://github.com/cms-sw/cmssw/pull/4112){:target="_blank"}  from **@ptcox**: Multithreading for CSCOfflineMonitor `dqm`  created: 2014-06-04T17:42:12Z merged: 2014-06-12T17:49:41Z

1. [4196](http://github.com/cms-sw/cmssw/pull/4196){:target="_blank"}  from **@leggat**: Multithread pixel update - raw data error fix. `dqm`  created: 2014-06-10T18:36:41Z merged: 2014-06-12T12:15:04Z

1. [4193](http://github.com/cms-sw/cmssw/pull/4193){:target="_blank"}  from **@wmtan**: Add missing includes. `core`  `daq`  `reconstruction`  created: 2014-06-10T17:12:56Z merged: 2014-06-12T07:28:54Z

1. [4007](http://github.com/cms-sw/cmssw/pull/4007){:target="_blank"}  from **@TaiSakuma**: Remove unused files in RecoMET. `reconstruction`  created: 2014-05-26T04:28:06Z merged: 2014-06-12T07:27:12Z

1. [4129](http://github.com/cms-sw/cmssw/pull/4129){:target="_blank"}  from **@Dr15Jones**: Removed unused variable to avoid valgrind error in SoftElectronMVAEstimator `reconstruction`  created: 2014-06-05T18:57:26Z merged: 2014-06-12T07:25:48Z

1. [4104](http://github.com/cms-sw/cmssw/pull/4104){:target="_blank"}  from **@gartung**: Check the bodies of FunctionDecl's too. `core`  created: 2014-06-03T18:46:29Z merged: 2014-06-11T09:20:43Z

1. [4158](http://github.com/cms-sw/cmssw/pull/4158){:target="_blank"}  from **@ktf**: Forward port CMSSW_7_1_X into CMSSW_7_2_X (corrected by hand) `alca`  `dqm`  created: 2014-06-07T13:30:03Z merged: 2014-06-11T08:07:35Z

1. [4016](http://github.com/cms-sw/cmssw/pull/4016){:target="_blank"}  from **@gpetruc**: miniAOD part4 (7.2.X, only PatAlgos and cmsDriver) `analysis`  `operations`  created: 2014-05-27T11:37:11Z merged: 2014-06-10T16:00:59Z

1. [4018](http://github.com/cms-sw/cmssw/pull/4018){:target="_blank"}  from **@ptraczyk**: RecoLocalMuon/DTSegment -- DT meantimer tune `reconstruction`  created: 2014-05-27T13:07:03Z merged: 2014-06-10T14:46:49Z

1. [4166](http://github.com/cms-sw/cmssw/pull/4166){:target="_blank"}  from **@Dr15Jones**: Mark as thread safe classes from Geometry/EcalAlgo created: 2014-06-09T20:47:43Z merged: 2014-06-09T20:50:42Z

1. [4156](http://github.com/cms-sw/cmssw/pull/4156){:target="_blank"}  from **@ktf**: Fix a bunch of clang warnings. `analysis`  `reconstruction`  created: 2014-06-07T13:08:18Z merged: 2014-06-07T13:10:12Z

1. [4130](http://github.com/cms-sw/cmssw/pull/4130){:target="_blank"}  from **@civanch**: Multithreading fixes in simulation `simulation`  created: 2014-06-05T19:14:09Z merged: 2014-06-06T19:21:28Z

1. [4128](http://github.com/cms-sw/cmssw/pull/4128){:target="_blank"}  from **@Dr15Jones**: Fixed a read of uninitialized memory in CastorMonitorModule `dqm`  created: 2014-06-05T18:56:56Z merged: 2014-06-05T20:27:15Z

1. [4120](http://github.com/cms-sw/cmssw/pull/4120){:target="_blank"}  from **@degano**: Update RivetInterface to use Rivet 2.0.0 `generators`  created: 2014-06-05T09:33:20Z merged: 2014-06-05T09:44:14Z

1. [4035](http://github.com/cms-sw/cmssw/pull/4035){:target="_blank"}  from **@wddgit**: Event setup exceptions. `analysis`  `core`  `geometry`  `reconstruction`  created: 2014-05-28T14:08:07Z merged: 2014-06-03T23:15:59Z

1. [4075](http://github.com/cms-sw/cmssw/pull/4075){:target="_blank"}  from **@ktf**: Make sure files are at CERN also when specifying multiple runs. `operations`  created: 2014-06-02T11:59:26Z merged: 2014-06-03T08:47:49Z

1. [4040](http://github.com/cms-sw/cmssw/pull/4040){:target="_blank"}  from **@ktf**: Drop tertiary vertex `reconstruction`  created: 2014-05-28T15:35:37Z merged: 2014-06-03T06:11:09Z

1. [4071](http://github.com/cms-sw/cmssw/pull/4071){:target="_blank"}  from **@nclopezo**: Removed duplicate line in DataFormats/TauReco/BuildFile.xml `reconstruction`  created: 2014-06-02T08:18:14Z merged: 2014-06-03T06:10:38Z

1. [4053](http://github.com/cms-sw/cmssw/pull/4053){:target="_blank"}  from **@davidlt**: Good seed producer dtor segfault. `reconstruction`  created: 2014-05-30T09:48:05Z merged: 2014-06-03T06:10:01Z

1. [4006](http://github.com/cms-sw/cmssw/pull/4006){:target="_blank"}  from **@TaiSakuma**: Make "alias" optional in *METProducer. `reconstruction`  created: 2014-05-25T23:16:06Z merged: 2014-06-03T06:09:23Z

1. [4005](http://github.com/cms-sw/cmssw/pull/4005){:target="_blank"}  from **@TaiSakuma**: Remove unused cfi file in RecoMET. `reconstruction`  created: 2014-05-25T21:30:19Z merged: 2014-06-03T06:04:07Z

1. [4044](http://github.com/cms-sw/cmssw/pull/4044){:target="_blank"}  from **@Dr15Jones**: Clang fixes for RecoMuon/MuonSeedGenerator `reconstruction`  created: 2014-05-28T20:13:14Z merged: 2014-06-03T05:46:27Z

1. [4068](http://github.com/cms-sw/cmssw/pull/4068){:target="_blank"}  from **@apfeiffer1**: Update serialisation generator script. `db`  created: 2014-05-31T14:14:10Z merged: 2014-06-02T09:31:19Z

1. [4057](http://github.com/cms-sw/cmssw/pull/4057){:target="_blank"}  from **@nclopezo**: Static Analyser -- Changed the configuration for the static analyser `core`  created: 2014-05-30T14:52:14Z merged: 2014-06-02T08:03:59Z

1. [3971](http://github.com/cms-sw/cmssw/pull/3971){:target="_blank"}  from **@cms-tau-pog**: Tau quality cuts update. `reconstruction`  created: 2014-05-22T16:40:12Z merged: 2014-06-02T06:25:46Z

1. [3993](http://github.com/cms-sw/cmssw/pull/3993){:target="_blank"}  from **@jpavel**: Saving tau decay mode inside PFTau and patTau. `analysis`  `reconstruction`  created: 2014-05-23T17:00:56Z merged: 2014-05-30T18:50:40Z

1. [4019](http://github.com/cms-sw/cmssw/pull/4019){:target="_blank"}  from **@deguio**: Enhancing the igetter functionalities: addint DQMStore::IGetter::removeElement `dqm`  created: 2014-05-27T14:02:23Z merged: 2014-05-30T18:49:04Z

1. [4046](http://github.com/cms-sw/cmssw/pull/4046){:target="_blank"}  from **@ktf**: Fix clang bug `analysis`  created: 2014-05-29T09:06:55Z merged: 2014-05-30T11:23:42Z

1. [4042](http://github.com/cms-sw/cmssw/pull/4042){:target="_blank"}  from **@Dr15Jones**: Added tryToGet method to EventSetup and EventSetupRecord. `core`  created: 2014-05-28T18:20:00Z merged: 2014-05-29T16:29:59Z

1. [3966](http://github.com/cms-sw/cmssw/pull/3966){:target="_blank"}  from **@VinInn**: SingleObjectSelector as stream module. `analysis`  `dqm`  `reconstruction`  created: 2014-05-22T14:43:15Z merged: 2014-05-29T12:09:28Z

1. [4020](http://github.com/cms-sw/cmssw/pull/4020){:target="_blank"}  from **@VinInn**: Tau discrimination producers (not yet) stream `reconstruction`  created: 2014-05-27T16:29:05Z merged: 2014-05-28T14:32:04Z

1. [4015](http://github.com/cms-sw/cmssw/pull/4015){:target="_blank"}  from **@ktf**: More clang fixes. `alca`  `analysis`  `db`  `dqm`  `generators`  `geometry`  `l1`  `reconstruction`  `simulation`  created: 2014-05-27T06:57:16Z merged: 2014-05-28T13:43:37Z

1. [4033](http://github.com/cms-sw/cmssw/pull/4033){:target="_blank"}  from **@smuzaffar**: Fix duplicate reflex library search for patch releases created: 2014-05-28T12:59:46Z merged: 2014-05-28T12:59:52Z

1. [4023](http://github.com/cms-sw/cmssw/pull/4023){:target="_blank"}  from **@Dr15Jones**: Have the command line arg -n override numberOfThreads in config `core`  created: 2014-05-27T21:46:03Z merged: 2014-05-28T01:09:15Z

1. [4014](http://github.com/cms-sw/cmssw/pull/4014){:target="_blank"}  from **@TaiSakuma**: Prepare to delete old definitions of corrected CaloMETs `analysis`  created: 2014-05-26T23:30:51Z merged: 2014-05-27T19:11:01Z

1. [3965](http://github.com/cms-sw/cmssw/pull/3965){:target="_blank"}  from **@vadler**: Update test input RelVal RecoMET/METProducers `reconstruction`  created: 2014-05-22T14:32:43Z merged: 2014-05-27T13:50:26Z

1. [3989](http://github.com/cms-sw/cmssw/pull/3989){:target="_blank"}  from **@lveldere**: FastSim -- Switch to Pythia 8 for FastSim decays  `fastsim`  created: 2014-05-23T13:14:46Z merged: 2014-05-26T07:48:51Z

1. [3988](http://github.com/cms-sw/cmssw/pull/3988){:target="_blank"}  from **@apfeiffer1**: Fix missing qg likelihood 72x `db`  created: 2014-05-23T13:14:35Z merged: 2014-05-23T13:27:33Z

1. [3948](http://github.com/cms-sw/cmssw/pull/3948){:target="_blank"}  from **@davidlt**: ARM64 -- condformats_serialization_generate.py: support for aarch64 `db`  created: 2014-05-21T14:08:50Z merged: 2014-05-22T15:09:00Z

1. [3951](http://github.com/cms-sw/cmssw/pull/3951){:target="_blank"}  from **@davidlt**: ARM64 -- DataFormats/Math: rdtscp.h disable on aarch64 `reconstruction`  created: 2014-05-21T15:33:33Z merged: 2014-05-22T13:12:14Z

1. [3942](http://github.com/cms-sw/cmssw/pull/3942){:target="_blank"}  from **@TaiSakuma**: Reco -- Change the naming convention of CaloMETs `analysis`  `dqm`  `reconstruction`  created: 2014-05-20T18:17:10Z merged: 2014-05-22T07:49:24Z

1. [3946](http://github.com/cms-sw/cmssw/pull/3946){:target="_blank"}  from **@gpetruc**: MiniAOD part 3 (7.2.X clone of the 7.1.X PR) `analysis`  `core`  `operations`  `reconstruction`  created: 2014-05-21T11:54:26Z merged: 2014-05-21T19:34:05Z
