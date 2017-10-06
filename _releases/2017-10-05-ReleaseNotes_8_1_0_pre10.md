---
layout: post
title:  "8_1_0_pre10"
date:   2017-10-05 18:46:15 +0200
categories: cmssw
relmajor: 8
relminor: 1
relsubminor: 0

relpre: _pre10
---

# CMSSW_8_1_0_pre10
#### Changes since CMSSW_8_1_0_pre9:

[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_8_1_0_pre9...CMSSW_8_1_0_pre10)



1. [15456](http://github.com/cms-sw/cmssw/pull/15456)  from @Dr15Jones: Small modifications based on code review of asynchronous prefetching `core`  created: 2016-08-12T16:37:54Z merged: 2016-08-13T06:33:15Z

1. [15452](http://github.com/cms-sw/cmssw/pull/15452)  from @mmusich: Adding vtx smearing parameters for 2015 Beta*=90m for FSQ analyses `operations`  `simulation`  created: 2016-08-12T13:58:57Z merged: 2016-08-13T06:34:20Z

1. [15443](http://github.com/cms-sw/cmssw/pull/15443)  from @davidlange6: fix bug that led to double inclusion of customise from command line in cmsDriver `operations`  created: 2016-08-12T08:10:15Z merged: 2016-08-12T08:49:28Z

1. [15438](http://github.com/cms-sw/cmssw/pull/15438)  from @Dr15Jones: Minor maintenance improvements to WaitingTaskList `core`  created: 2016-08-11T21:38:29Z merged: 2016-08-12T07:01:35Z

1. [15436](http://github.com/cms-sw/cmssw/pull/15436)  from @mdhildreth: HIP Killing and PreMixing for 81X `core`  `simulation`  created: 2016-08-11T19:31:58Z merged: 2016-08-13T06:34:47Z

1. [15435](http://github.com/cms-sw/cmssw/pull/15435)  from @Dr15Jones: Added missing header files needed for gcc 6 `analysis`  `simulation`  created: 2016-08-11T18:54:11Z merged: 2016-08-11T19:00:23Z

1. [15433](http://github.com/cms-sw/cmssw/pull/15433)  from @Dr15Jones: Prefetch data products from Event concurrently `core`  created: 2016-08-11T15:00:59Z merged: 2016-08-11T19:01:00Z

1. [15432](http://github.com/cms-sw/cmssw/pull/15432)  from @cms-AlCaDB: MC updates for trancheIV `alca`  created: 2016-08-11T14:51:11Z merged: 2016-08-12T07:55:47Z

1. [15420](http://github.com/cms-sw/cmssw/pull/15420)  from @Dr15Jones: Downgrade ROOT error from "Inverter::Dinv" `core`  created: 2016-08-10T20:37:28Z merged: 2016-08-11T08:07:50Z

1. [15414](http://github.com/cms-sw/cmssw/pull/15414)  from @makortel: Remove DataFormats/TrackingSeed as obsolete `core`  `hlt`  `reconstruction`  created: 2016-08-10T13:44:55Z merged: 2016-08-11T08:07:16Z

1. [15412](http://github.com/cms-sw/cmssw/pull/15412)  from @mbandrews: Fix LS reports: only use RawData. `dqm`  created: 2016-08-10T10:18:14Z merged: 2016-08-12T08:49:39Z

1. [15406](http://github.com/cms-sw/cmssw/pull/15406)  from @igv4321: Updating HBHEPulseShapeFlag and HBHEStatusBitSetter for Phase 1 `reconstruction`  created: 2016-08-10T00:09:04Z merged: 2016-08-11T15:04:59Z

1. [15405](http://github.com/cms-sw/cmssw/pull/15405)  from @wmtan: Use unique_ptr, not auto_ptr, in DataFormats/Math `reconstruction`  created: 2016-08-09T22:01:15Z merged: 2016-08-11T08:06:52Z

1. [15404](http://github.com/cms-sw/cmssw/pull/15404)  from @wmtan: Use unique_ptr, not auto_ptr, in 2 L1 packages `l1`  created: 2016-08-09T21:50:29Z merged: 2016-08-11T08:06:18Z

1. [15393](http://github.com/cms-sw/cmssw/pull/15393)  from @kpedro88: Phase2 workflow revamp `alca`  `db`  `dqm`  `geometry`  `operations`  `pdmv`  `reconstruction`  `simulation`  created: 2016-08-08T21:25:23Z merged: 2016-08-11T19:01:43Z

1. [15386](http://github.com/cms-sw/cmssw/pull/15386)  from @uhussain: Replacing unreliable array initialization in SiPixelTemplateReco.cc `reconstruction`  created: 2016-08-08T11:45:25Z merged: 2016-08-09T08:51:21Z

1. [15385](http://github.com/cms-sw/cmssw/pull/15385)  from @mmusich: 81x: fix SiPixelAli PCL update logic `alca`  created: 2016-08-08T11:10:13Z merged: 2016-08-09T12:39:44Z

1. [15379](http://github.com/cms-sw/cmssw/pull/15379)  from @bsunanda: bsunanda:Run2-TB04 Update all codes for HGCal TB till July 2016 `simulation`  created: 2016-08-05T16:49:44Z merged: 2016-08-08T07:58:54Z

1. [15377](http://github.com/cms-sw/cmssw/pull/15377)  from @bsunanda: bsunanda:Run2-TB03 Complete the analyzer and correct the configuration file for production `simulation`  created: 2016-08-05T14:22:50Z merged: 2016-08-08T07:59:33Z

1. [15371](http://github.com/cms-sw/cmssw/pull/15371)  from @makortel: Add possibility to weigh pixel hits in QuickTrackAssociatorByHits `simulation`  created: 2016-08-05T10:12:23Z merged: 2016-08-09T06:36:29Z

1. [15370](http://github.com/cms-sw/cmssw/pull/15370)  from @davidlange6: remove failing relval from short matrix (temporarily) `pdmv`  created: 2016-08-05T08:33:15Z merged: 2016-08-05T08:58:33Z

1. [15364](http://github.com/cms-sw/cmssw/pull/15364)  from @bsunanda: Run2-hcx87 Fix a bug for Hcal geometry which affeted Phase2 operation `geometry`  created: 2016-08-03T17:29:00Z merged: 2016-08-09T15:48:51Z

1. [15363](http://github.com/cms-sw/cmssw/pull/15363)  from @kpedro88: remove HcalCovarianceMatrix object entirely `alca`  `db`  created: 2016-08-03T15:28:20Z merged: 2016-08-07T08:40:28Z

1. [15361](http://github.com/cms-sw/cmssw/pull/15361)  from @fioriNTU: Update cfg files for offline analysis `analysis`  `comparison`  created: 2016-08-03T14:23:34Z merged: 2016-08-05T07:46:21Z

1. [15359](http://github.com/cms-sw/cmssw/pull/15359)  from @makortel: Two technical fixes to SeedingLayerSetsHits `reconstruction`  created: 2016-08-03T11:46:14Z merged: 2016-08-06T08:02:58Z

1. [15357](http://github.com/cms-sw/cmssw/pull/15357)  from @bsunanda: bsunanda:Run2-alca57 Add 2 new condition objects for HCAL: SiPMParameter and SiPMCharacteristics `alca`  `db`  created: 2016-08-03T02:33:32Z merged: 2016-08-10T07:45:16Z

1. [15354](http://github.com/cms-sw/cmssw/pull/15354)  from @bsunanda: bsunanda:Run2-alca56 Correct code for IsoTrack and PhiSymmetry calibration `alca`  created: 2016-08-02T17:17:59Z merged: 2016-08-11T08:57:00Z

1. [15352](http://github.com/cms-sw/cmssw/pull/15352)  from @bsunanda: bsunanda:Run2-alca55 Correct G4 validation code using isolated particles `alca`  `comparison`  created: 2016-08-02T15:54:47Z merged: 2016-08-05T13:34:51Z

1. [15348](http://github.com/cms-sw/cmssw/pull/15348)  from @jalimena: Update muon timing analyzer 81x `comparison`  `reconstruction`  created: 2016-08-02T11:37:27Z merged: 2016-08-04T14:30:47Z

1. [15347](http://github.com/cms-sw/cmssw/pull/15347)  from @ianna: Cylindrical Cut Section or Cut Tube Implementation `comparison`  `geometry`  `simulation`  `visualization`  created: 2016-08-02T09:16:38Z merged: 2016-08-05T08:58:49Z

1. [15345](http://github.com/cms-sw/cmssw/pull/15345)  from @fioriNTU: IsolatedBunchesMonitor81X `comparison`  `dqm`  created: 2016-08-01T16:19:51Z merged: 2016-08-03T08:51:39Z

1. [15343](http://github.com/cms-sw/cmssw/pull/15343)  from @archiron: New PF iso recomputation from miniAOD histos 81X V2 `dqm`  created: 2016-08-01T15:55:46Z merged: 2016-08-11T08:04:02Z

1. [15341](http://github.com/cms-sw/cmssw/pull/15341)  from @boudoul: fixing typo in geometry in Strip hit efficiency tool  `alca`  `comparison`  created: 2016-08-01T15:22:33Z merged: 2016-08-03T08:48:17Z

1. [15339](http://github.com/cms-sw/cmssw/pull/15339)  from @dntaylor: Remove SET muon from constructed `reconstruction`  created: 2016-08-01T13:29:17Z merged: 2016-08-03T08:06:28Z

1. [15337](http://github.com/cms-sw/cmssw/pull/15337)  from @diguida: Fix http proxy setting in curl for Tier0 DataService query of the Event Display online application `comparison`  `dqm`  created: 2016-08-01T10:11:34Z merged: 2016-08-03T08:06:10Z

1. [15336](http://github.com/cms-sw/cmssw/pull/15336)  from @fabozzi: new BPH MC relvals `pdmv`  created: 2016-08-01T09:09:23Z merged: 2016-08-01T16:32:29Z

1. [15335](http://github.com/cms-sw/cmssw/pull/15335)  from @mmusich: Update Hcal MC pulse shapes in all Global Tags `alca`  created: 2016-07-31T21:21:43Z merged: 2016-08-11T08:03:41Z

1. [15334](http://github.com/cms-sw/cmssw/pull/15334)  from @uhussain: Fixed variable names in PFBlockAlgo to abide by CMS coding rules  `reconstruction`  created: 2016-07-31T16:18:29Z merged: 2016-08-03T08:07:26Z

1. [15332](http://github.com/cms-sw/cmssw/pull/15332)  from @venturia: New macro for occupancy trend plots and new analyzer for common mode studies `analysis`  `comparison`  created: 2016-07-31T10:12:43Z merged: 2016-08-04T19:14:01Z

1. [15331](http://github.com/cms-sw/cmssw/pull/15331)  from @cms-btv-pog: Subjet TagInfo updates `analysis`  `reconstruction`  created: 2016-07-30T22:44:33Z merged: 2016-08-09T12:36:23Z

1. [15330](http://github.com/cms-sw/cmssw/pull/15330)  from @barvic: 81X - Added CSC Unpacker check for FED/DDU<->chamber mapping inconsistencies `reconstruction`  created: 2016-07-30T21:58:17Z merged: 2016-08-02T18:52:36Z

1. [15327](http://github.com/cms-sw/cmssw/pull/15327)  from @cms-tsg-storm: 81X HLT July 29th train `alca`  `hlt`  created: 2016-07-30T13:14:50Z merged: 2016-08-01T16:33:13Z

1. [15325](http://github.com/cms-sw/cmssw/pull/15325)  from @dildick: Don't produce GEMCoPadDigi in 2016 WFs `l1`  created: 2016-07-28T20:00:06Z merged: 2016-08-09T06:42:19Z

1. [15322](http://github.com/cms-sw/cmssw/pull/15322)  from @kpedro88: New pulse shape for HE 2017 SiPM `alca`  `simulation`  created: 2016-07-28T16:53:43Z merged: 2016-08-02T18:52:47Z

1. [15320](http://github.com/cms-sw/cmssw/pull/15320)  from @kpedro88: remove HcalCholeskyMatrix object entirely `alca`  `db`  created: 2016-07-28T16:16:30Z merged: 2016-08-03T08:52:33Z

1. [15318](http://github.com/cms-sw/cmssw/pull/15318)  from @VinInn: Update pixelCluster to support PhaseII `reconstruction`  created: 2016-07-28T14:03:25Z merged: 2016-08-06T08:05:20Z

1. [15311](http://github.com/cms-sw/cmssw/pull/15311)  from @CTPPS: CTPPS: directory rename Totem -> CTPPS `dqm`  `geometry`  `operations`  `reconstruction`  created: 2016-07-27T17:26:47Z merged: 2016-08-03T17:25:21Z

1. [15309](http://github.com/cms-sw/cmssw/pull/15309)  from @wddgit: Fix checking for duplicate process names `core`  created: 2016-07-27T16:52:40Z merged: 2016-07-28T07:25:28Z

1. [15307](http://github.com/cms-sw/cmssw/pull/15307)  from @jasperlauwers: 81X Adding Mu12_Ele23 path `comparison`  `dqm`  created: 2016-07-27T16:30:19Z merged: 2016-08-04T19:04:14Z

1. [15305](http://github.com/cms-sw/cmssw/pull/15305)  from @cms-sw: Revert "Replacing C-style arrays with std::array" `reconstruction`  created: 2016-07-27T15:46:50Z merged: 2016-07-28T07:25:40Z

1. [15303](http://github.com/cms-sw/cmssw/pull/15303)  from @smuzaffar: avoid ambiguous option --s error for workflow 136.735 `pdmv`  created: 2016-07-27T10:50:15Z merged: 2016-07-27T13:12:51Z

1. [15301](http://github.com/cms-sw/cmssw/pull/15301)  from @Andrej-CMS: TTHFGenFilter `analysis`  created: 2016-07-27T09:59:36Z merged: 2016-08-08T09:48:25Z

1. [15300](http://github.com/cms-sw/cmssw/pull/15300)  from @jaylawhorn: fix SUSY Razor HLT DQM module `dqm`  created: 2016-07-27T09:54:59Z merged: 2016-07-28T09:58:54Z

1. [15297](http://github.com/cms-sw/cmssw/pull/15297)  from @rockybala: Bugfix for hlt iso mu24 eta2p1 `dqm`  created: 2016-07-27T09:02:58Z merged: 2016-08-11T08:03:27Z

1. [15296](http://github.com/cms-sw/cmssw/pull/15296)  from @diguida: Remove host-based override and printout in CondDBESource and add back connection string override in the online DQM config `alca`  `db`  `dqm`  created: 2016-07-27T08:22:03Z merged: 2016-07-28T09:57:25Z

1. [15293](http://github.com/cms-sw/cmssw/pull/15293)  from @lgray: SimClustering for HGCal `geometry`  `reconstruction`  `simulation`  `visualization`  created: 2016-07-26T20:16:06Z merged: 2016-08-11T08:55:19Z

1. [15290](http://github.com/cms-sw/cmssw/pull/15290)  from @mmusich: Update Run-I Global Tags with FEMapRcd and Phase-I reconstruction Geometry `alca`  created: 2016-07-26T14:31:03Z merged: 2016-07-27T12:08:35Z

1. [15284](http://github.com/cms-sw/cmssw/pull/15284)  from @bsunanda: bsunanda:Run2-alca53 Change output part for HcalIsolatedBunchFilter `alca`  `operations`  created: 2016-07-26T13:24:48Z merged: 2016-08-02T18:53:54Z

1. [15283](http://github.com/cms-sw/cmssw/pull/15283)  from @HeinerTholen: fix: eval_auto_bounds returns good value for pt==pt_low `comparison`  `db`  created: 2016-07-26T11:28:40Z merged: 2016-07-29T16:08:58Z

1. [15275](http://github.com/cms-sw/cmssw/pull/15275)  from @schneiml: Phase1 Pixel DQM Plot Changes `comparison`  `dqm`  created: 2016-07-25T11:42:55Z merged: 2016-08-04T19:07:54Z

1. [15273](http://github.com/cms-sw/cmssw/pull/15273)  from @fioriNTU: retuning FPix nclusters limit `dqm`  created: 2016-07-25T09:41:55Z merged: 2016-07-26T16:10:21Z

1. [15272](http://github.com/cms-sw/cmssw/pull/15272)  from @davidlt: Remove BsToMuMu_13INPUT `pdmv`  created: 2016-07-25T08:03:30Z merged: 2016-07-26T14:06:40Z

1. [15267](http://github.com/cms-sw/cmssw/pull/15267)  from @jingyucms: fix the path of input histograms used in comparison `dqm`  created: 2016-07-22T23:32:14Z merged: 2016-07-26T14:07:05Z

1. [15263](http://github.com/cms-sw/cmssw/pull/15263)  from @jhgoh: RPCRecHit with timing and y-coordinate information for iRPC `reconstruction`  created: 2016-07-22T14:17:12Z merged: 2016-08-11T08:58:04Z

1. [15261](http://github.com/cms-sw/cmssw/pull/15261)  from @UMN-CMS: uMNio data unpacking `reconstruction`  `simulation`  created: 2016-07-22T13:08:21Z merged: 2016-08-03T08:55:48Z

1. [15260](http://github.com/cms-sw/cmssw/pull/15260)  from @makortel: Switch FastCircleFit to use Eigen, generalize FastCircleFit and RZLine interfaces `analysis`  `dqm`  `reconstruction`  created: 2016-07-22T12:51:07Z merged: 2016-07-29T08:39:47Z

1. [15258](http://github.com/cms-sw/cmssw/pull/15258)  from @bsunanda: bsunanda:Run2-alca51 Add AlCaReco and DQM code for HcalIsolatedBunch `alca`  `dqm`  `operations`  created: 2016-07-22T11:19:36Z merged: 2016-07-29T14:15:20Z

1. [15257](http://github.com/cms-sw/cmssw/pull/15257)  from @civanch: Switch G4 Physics List for Geant4 10.2 `comparison`  `simulation`  created: 2016-07-22T11:11:41Z merged: 2016-07-22T17:08:42Z

1. [15256](http://github.com/cms-sw/cmssw/pull/15256)  from @ianna: LHE Reader Comment Added `generators`  created: 2016-07-22T06:57:06Z merged: 2016-07-28T09:55:33Z

1. [15254](http://github.com/cms-sw/cmssw/pull/15254)  from @kpedro88: separate amplifier for HcalUpgradeDataFrames `simulation`  created: 2016-07-21T17:19:35Z merged: 2016-07-23T05:49:39Z

1. [15253](http://github.com/cms-sw/cmssw/pull/15253)  from @mkirsano: Fix External decays: code formatting, fix, fix examples `generators`  created: 2016-07-21T16:30:44Z merged: 2016-07-28T07:26:15Z

1. [15249](http://github.com/cms-sw/cmssw/pull/15249)  from @blinkseb: [8.1.X] Prevent negative jet smearing factor `analysis`  `reconstruction`  created: 2016-07-21T13:14:34Z merged: 2016-07-23T05:53:53Z

1. [15245](http://github.com/cms-sw/cmssw/pull/15245)  from @bsunanda: bsunanda:Run2-TB02 HGCal Test Beam `geometry`  `simulation`  created: 2016-07-20T21:03:22Z merged: 2016-07-26T15:42:38Z

1. [15244](http://github.com/cms-sw/cmssw/pull/15244)  from @bsunanda: bsunanda:Run2-TB01 Test beam analysis code `simulation`  created: 2016-07-20T14:55:49Z merged: 2016-07-27T12:09:45Z

1. [15243](http://github.com/cms-sw/cmssw/pull/15243)  from @kkotov: Extended o2o for81x `alca`  `db`  `l1`  created: 2016-07-20T13:51:32Z merged: 2016-08-09T12:50:24Z

1. [15238](http://github.com/cms-sw/cmssw/pull/15238)  from @jkarancs: Enable pixel inefficiency for Phase I `simulation`  created: 2016-07-19T21:07:41Z merged: 2016-07-28T07:51:13Z

1. [15237](http://github.com/cms-sw/cmssw/pull/15237)  from @gouskos: dqm plot, pixel endcap roc occupancy in 81x `dqm`  created: 2016-07-19T20:28:30Z merged: 2016-08-08T08:03:43Z

1. [15233](http://github.com/cms-sw/cmssw/pull/15233)  from @dgulhan: rho analyzer `reconstruction`  created: 2016-07-19T15:42:23Z merged: 2016-08-12T07:56:51Z

1. [15215](http://github.com/cms-sw/cmssw/pull/15215)  from @calabria: Phase2 muon validation `dqm`  `pdmv`  `reconstruction`  `simulation`  created: 2016-07-17T09:04:24Z merged: 2016-07-27T12:10:47Z

1. [15205](http://github.com/cms-sw/cmssw/pull/15205)  from @civanch: Fixed static analyser warnings 5 `simulation`  created: 2016-07-14T16:18:02Z merged: 2016-07-27T12:10:19Z

1. [15199](http://github.com/cms-sw/cmssw/pull/15199)  from @joshhdawes: New release of Conditions Miniframework `comparison`  `db`  created: 2016-07-14T07:43:47Z merged: 2016-07-27T12:18:41Z

1. [15198](http://github.com/cms-sw/cmssw/pull/15198)  from @wddgit: Fix bugs in code that detects missing ROOT dictionaries `alca`  `analysis`  `core`  `db`  `l1`  `reconstruction`  `simulation`  created: 2016-07-13T22:17:36Z merged: 2016-07-27T06:39:05Z

1. [15195](http://github.com/cms-sw/cmssw/pull/15195)  from @civanch: Fixed static analyser warnings in sim-packages 4 `alca`  `simulation`  created: 2016-07-13T18:40:39Z merged: 2016-07-27T08:24:18Z

1. [15192](http://github.com/cms-sw/cmssw/pull/15192)  from @jlagram: update of Strip hit efficiency code `alca`  created: 2016-07-13T13:36:12Z merged: 2016-07-26T15:44:25Z

1. [15180](http://github.com/cms-sw/cmssw/pull/15180)  from @bsunanda: bsunanda:Run2-alca50 Modify HcalDbHardcode for non-empty filler of logical map `alca`  created: 2016-07-12T20:14:34Z merged: 2016-07-26T15:44:06Z

1. [15175](http://github.com/cms-sw/cmssw/pull/15175)  from @mandrenguyen: Point to 50ns vtx smearing for boosted pPb and clean up `generators`  `operations`  created: 2016-07-12T14:13:13Z merged: 2016-08-04T19:39:14Z

1. [15146](http://github.com/cms-sw/cmssw/pull/15146)  from @uhussain: Fixed all static analyzer warnings in MatacqRawEvent.cc, MatacqRawEvent.h & HcalUnpacker.cc `reconstruction`  created: 2016-07-07T16:54:40Z merged: 2016-07-29T08:24:18Z

1. [15130](http://github.com/cms-sw/cmssw/pull/15130)  from @juztas: Change current curl fork/exec with libdavix plugin for read operations `core`  created: 2016-07-06T08:31:46Z merged: 2016-07-29T16:05:38Z

1. [15072](http://github.com/cms-sw/cmssw/pull/15072)  from @gartung: SimCalorimetry/EcalTrigPrimProducers fix for bug flagged by gcc 6.0 misleading-indentation warning `comparison`  `l1`  created: 2016-06-30T02:23:34Z merged: 2016-08-05T13:54:39Z

1. [15070](http://github.com/cms-sw/cmssw/pull/15070)  from @gartung: Validation/RecoEgamma fix for bug flagged by gcc 6.0 misleading-indentation warning `dqm`  created: 2016-06-30T02:08:38Z merged: 2016-07-25T09:10:16Z

1. [15065](http://github.com/cms-sw/cmssw/pull/15065)  from @gartung: GeneratorInterface/LHEInterface : formatting fix for statements flagged by gcc 6.0 indentation warning `generators`  created: 2016-06-29T19:32:38Z merged: 2016-08-09T13:34:58Z

1. [15034](http://github.com/cms-sw/cmssw/pull/15034)  from @gartung: DQM/SiPixelMonitorClient : formatting fix for gcc 6.0 misleading-indentation warning `dqm`  created: 2016-06-28T19:21:44Z merged: 2016-08-05T13:53:53Z

1. [14998](http://github.com/cms-sw/cmssw/pull/14998)  from @gartung: PhysicsTools/MVATrainer : formatting fix for gcc 6.0 misleading-indentation warning `analysis`  `comparison`  created: 2016-06-27T17:33:45Z merged: 2016-08-05T13:50:09Z

1. [14963](http://github.com/cms-sw/cmssw/pull/14963)  from @dan131riley: protect RawTask::_process from processing bad HcalHTRData `dqm`  created: 2016-06-23T17:26:15Z merged: 2016-08-06T13:42:55Z

#### CMSDIST Changes between Tags REL/CMSSW_8_1_0_pre9/slc6_amd64_gcc530 and REL/CMSSW_8_1_0_pre10/slc6_amd64_gcc530:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_8_1_0_pre9/slc6_amd64_gcc530...REL/CMSSW_8_1_0_pre10/slc6_amd64_gcc530)



1. [2444](http://github.com/cms-sw/cmssw/pull/2444)  from @smuzaffar: das_client.py symlink in CMS_PATH/share/overrides/bin created: 2014-02-13T07:23:25Z merged: 2014-02-13T11:09:36Z

1. [2441](http://github.com/cms-sw/cmssw/pull/2441)  from @iahmad-khan: updates RecoBTag-SecondaryVertex spec created: 2014-02-13T00:23:48Z merged: 2014-02-13T10:03:04Z

1. [2431](http://github.com/cms-sw/cmssw/pull/2431)  from @iahmad-khan: updates das-client to 02.17.04 created: 2014-02-12T19:59:16Z merged: 2014-02-13T11:09:08Z

1. [2422](http://github.com/cms-sw/cmssw/pull/2422)  from @iahmad-khan: updates jemalloc to 4.2.0 created: 2014-02-12T12:56:57Z merged: 2014-02-13T10:57:50Z

1. [2417](http://github.com/cms-sw/cmssw/pull/2417)  from @smuzaffar: Updated root to tip of 3e3caaf created: 2014-02-12T10:05:03Z merged: 2014-02-16T14:27:57Z

1. [2415](http://github.com/cms-sw/cmssw/pull/2415)  from @iahmad-khan: updates sherpa to 2.2.1 in 81x stable created: 2014-02-12T00:07:18Z merged: 2014-02-12T06:31:26Z

1. [2412](http://github.com/cms-sw/cmssw/pull/2412)  from @mkirsano: upgrade evtgen to 1.6.0 created: 2014-02-11T21:29:39Z merged: 2014-02-13T15:56:15Z

1. [2408](http://github.com/cms-sw/cmssw/pull/2408)  from @civanch: Update clhep and geant4 for G4 10.2 created: 2014-02-11T19:18:35Z merged: 2014-03-05T08:32:01Z
