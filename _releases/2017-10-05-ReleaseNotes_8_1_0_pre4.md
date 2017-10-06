---
layout: post
title:  "8_1_0_pre4"
date:   2017-10-05 18:46:15 +0200
categories: cmssw
relmajor: 8
relminor: 1
relsubminor: 0

relpre: _pre4
---

# CMSSW_8_1_0_pre4
#### Changes since CMSSW_8_1_0_pre3:

[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_8_1_0_pre3...CMSSW_8_1_0_pre4)



1. [14347](http://github.com/cms-sw/cmssw/pull/14347)  from @deguio: fix EDMtoMEConverter for multiRun harvesting `dqm`  created: 2016-05-03T11:36:27Z merged: 2016-05-03T14:39:31Z

1. [14345](http://github.com/cms-sw/cmssw/pull/14345)  from @JanFSchulte: Change of StoN cut in hit selection for SiPixAli in PCL + 0T configs for the same `alca`  created: 2016-05-03T10:27:35Z merged: 2016-05-04T07:05:38Z

1. [14343](http://github.com/cms-sw/cmssw/pull/14343)  from @hengne: relval matrix updates `pdmv`  created: 2016-05-03T09:51:30Z merged: 2016-05-04T07:10:18Z

1. [14337](http://github.com/cms-sw/cmssw/pull/14337)  from @schneiml: TrackerMonitorTrack: Fix side for TID so that TID/MINUS histograms appear. (8_1_X) `dqm`  created: 2016-05-03T08:10:59Z merged: 2016-05-03T14:39:43Z

1. [14332](http://github.com/cms-sw/cmssw/pull/14332)  from @lathomas: Filling the fillDescription method of CaloRecHitsBeamHaloCleaned and  `reconstruction`  created: 2016-05-02T19:59:25Z merged: 2016-05-04T07:05:53Z

1. [14330](http://github.com/cms-sw/cmssw/pull/14330)  from @Dr15Jones: Have edmStreamStallGrapher estimate time in source while finding events `core`  created: 2016-05-02T17:32:12Z merged: 2016-05-03T07:21:16Z

1. [14326](http://github.com/cms-sw/cmssw/pull/14326)  from @cms-l1t-offline: Updates to L1T packer needed to simultaneously pack GT inputs and GMT/Calo ouputs `l1`  created: 2016-05-02T14:56:43Z merged: 2016-05-02T15:26:57Z

1. [14319](http://github.com/cms-sw/cmssw/pull/14319)  from @cms-l1t-offline: Update L1TNuples to l1t-tsg-v5, and address memory management problems. `l1`  created: 2016-05-02T11:48:06Z merged: 2016-05-02T15:41:52Z

1. [14317](http://github.com/cms-sw/cmssw/pull/14317)  from @mtosi: update trajectory filters (minNumberOfHits --> minNumberOfHitsForLoopers) `hlt`  `reconstruction`  created: 2016-05-02T08:24:59Z merged: 2016-05-04T07:06:06Z

1. [14314](http://github.com/cms-sw/cmssw/pull/14314)  from @bsunanda: bsunanda:Run2-hcx79 Add 2 more methods to HcalDetId `simulation`  created: 2016-04-30T17:06:21Z merged: 2016-05-04T07:09:05Z

1. [14311](http://github.com/cms-sw/cmssw/pull/14311)  from @Dr15Jones: Make edmStreamStallGrapher properly handle unscheduled processing `core`  created: 2016-04-29T21:31:30Z merged: 2016-04-30T18:23:18Z

1. [14309](http://github.com/cms-sw/cmssw/pull/14309)  from @wddgit: Fix uninitialized variables which were causing `core`  created: 2016-04-29T19:33:01Z merged: 2016-04-30T18:23:40Z

1. [14308](http://github.com/cms-sw/cmssw/pull/14308)  from @wmtan: Fix use of std::unique_ptr in GeneratorFilter `generators`  created: 2016-04-29T19:14:37Z merged: 2016-05-01T07:46:48Z

1. [14307](http://github.com/cms-sw/cmssw/pull/14307)  from @kpedro88: define RecoFullLocal and use in Phase2 upgrade workflows `pdmv`  `reconstruction`  created: 2016-04-29T15:57:39Z merged: 2016-05-04T07:06:45Z

1. [14304](http://github.com/cms-sw/cmssw/pull/14304)  from @Dr15Jones: Properly handle the case where there are more than 10 streams `core`  created: 2016-04-29T15:13:13Z merged: 2016-04-29T17:56:20Z

1. [14302](http://github.com/cms-sw/cmssw/pull/14302)  from @ianna: Use Correct HcalTopology Record `geometry`  created: 2016-04-29T14:17:27Z merged: 2016-04-29T17:55:59Z

1. [14299](http://github.com/cms-sw/cmssw/pull/14299)  from @VinInn: Tracking Fast cleaner during pattern recognition `reconstruction`  created: 2016-04-29T12:03:43Z merged: 2016-05-02T15:20:02Z

1. [14298](http://github.com/cms-sw/cmssw/pull/14298)  from @mmusich: Update Global Tag for L1Menu_Collisions2016_v1_xml L1T menu and splitting Ecal Pedestal tags `alca`  created: 2016-04-29T10:57:12Z merged: 2016-04-30T18:24:02Z

1. [14297](http://github.com/cms-sw/cmssw/pull/14297)  from @cms-l1t-offline: Bugfix Check L1T Global Scale Range in Sums `l1`  created: 2016-04-29T10:54:17Z merged: 2016-04-29T11:54:41Z

1. [14296](http://github.com/cms-sw/cmssw/pull/14296)  from @cms-l1t-offline: Bugfix Check L1T Global Scale Range `l1`  created: 2016-04-29T07:16:54Z merged: 2016-04-29T07:50:20Z

1. [14294](http://github.com/cms-sw/cmssw/pull/14294)  from @bsunanda: bsunanda:Run2-alca40 Change the name of L1 GT seed `alca`  created: 2016-04-28T22:19:17Z merged: 2016-04-30T18:24:14Z

1. [14293](http://github.com/cms-sw/cmssw/pull/14293)  from @Dr15Jones: Fix use of std::unique_ptr in HadronizerFilter `comparison`  `generators`  created: 2016-04-28T21:23:08Z merged: 2016-04-29T09:44:07Z

1. [14292](http://github.com/cms-sw/cmssw/pull/14292)  from @cms-l1t-offline: ifstream bugfix redux `l1`  created: 2016-04-28T16:51:29Z merged: 2016-04-28T17:18:26Z

1. [14290](http://github.com/cms-sw/cmssw/pull/14290)  from @cms-l1t-offline: Update to L1T Global for 2016 Menu (80X) `dqm`  `hlt`  `l1`  created: 2016-04-28T10:41:33Z merged: 2016-05-02T05:54:14Z

1. [14289](http://github.com/cms-sw/cmssw/pull/14289)  from @civanch: Fixed SIM exception actions `simulation`  created: 2016-04-28T09:16:39Z merged: 2016-05-01T07:51:13Z

1. [14284](http://github.com/cms-sw/cmssw/pull/14284)  from @cms-l1t-offline: Updates to L1TCaloLayer1 and unpacker `l1`  created: 2016-04-27T20:47:37Z merged: 2016-05-03T07:20:42Z

1. [14282](http://github.com/cms-sw/cmssw/pull/14282)  from @cms-l1t-offline: Update to L1T Global for 2016 Menu (81X) `comparison`  `dqm`  `hlt`  `l1`  created: 2016-04-27T19:59:02Z merged: 2016-04-28T08:24:49Z

1. [14280](http://github.com/cms-sw/cmssw/pull/14280)  from @mmusich: Update HLTHI Global Tag for CMSHLT-518 `alca`  created: 2016-04-27T19:54:11Z merged: 2016-04-28T17:19:05Z

1. [14278](http://github.com/cms-sw/cmssw/pull/14278)  from @davidsheffield: Quietly return when producer fails to find input collection `hlt`  created: 2016-04-27T18:47:23Z merged: 2016-04-28T06:36:23Z

1. [14277](http://github.com/cms-sw/cmssw/pull/14277)  from @wmtan: Use unique_ptr, not auto_ptr, in CommonTools `analysis`  `reconstruction`  created: 2016-04-27T17:28:51Z merged: 2016-04-28T06:13:29Z

1. [14275](http://github.com/cms-sw/cmssw/pull/14275)  from @cms-l1t-offline: tsg-v5 L1REPACK 80x `l1`  `operations`  created: 2016-04-27T16:29:07Z merged: 2016-05-02T05:50:27Z

1. [14274](http://github.com/cms-sw/cmssw/pull/14274)  from @cms-l1t-offline: tsg-v5 L1REPACK 80x `l1`  `operations`  created: 2016-04-27T16:28:23Z merged: 2016-04-28T06:40:31Z

1. [14271](http://github.com/cms-sw/cmssw/pull/14271)  from @duanders: Jet ID and b-tag information for Scouting Calojets `core`  `hlt`  created: 2016-04-27T14:52:30Z merged: 2016-04-29T11:55:28Z

1. [14269](http://github.com/cms-sw/cmssw/pull/14269)  from @silviodonato: Pixel PU jet update `hlt`  created: 2016-04-27T12:16:10Z merged: 2016-04-28T14:43:27Z

1. [14266](http://github.com/cms-sw/cmssw/pull/14266)  from @lveldere: FastSim: clean up and simplify generator particle filtering `fastsim`  created: 2016-04-27T08:45:00Z merged: 2016-04-28T06:34:59Z

1. [14264](http://github.com/cms-sw/cmssw/pull/14264)  from @mmusich: DropBox metadata - 2016 (81X) `alca`  `db`  created: 2016-04-27T07:53:24Z merged: 2016-04-28T06:36:05Z

1. [14262](http://github.com/cms-sw/cmssw/pull/14262)  from @wddgit: Consumes migration for triggerResultsByName `analysis`  `core`  created: 2016-04-26T20:19:12Z merged: 2016-04-27T12:31:16Z

1. [14256](http://github.com/cms-sw/cmssw/pull/14256)  from @rovere: Fix axis limit for StoppingReasonPhi plot `dqm`  created: 2016-04-26T15:14:39Z merged: 2016-04-27T08:55:13Z

1. [14255](http://github.com/cms-sw/cmssw/pull/14255)  from @sdevissc: bug fix in the APV Killing procedure `simulation`  created: 2016-04-26T15:04:55Z merged: 2016-04-28T18:43:13Z

1. [14254](http://github.com/cms-sw/cmssw/pull/14254)  from @ianna: Update Validation Tests `geometry`  created: 2016-04-26T14:45:30Z merged: 2016-04-27T10:21:33Z

1. [14250](http://github.com/cms-sw/cmssw/pull/14250)  from @rovere: Fix axis limit for StoppingReasonPhi plot `dqm`  created: 2016-04-26T13:13:13Z merged: 2016-04-27T10:03:38Z

1. [14247](http://github.com/cms-sw/cmssw/pull/14247)  from @VinInn: Small improvements in Pixel track reconstruction `comparison`  `reconstruction`  created: 2016-04-26T10:20:54Z merged: 2016-04-29T07:51:56Z

1. [14246](http://github.com/cms-sw/cmssw/pull/14246)  from @cms-l1t-offline: Pr 14141 plus bxvector fix 80x `l1`  created: 2016-04-26T08:46:08Z merged: 2016-04-27T05:24:57Z

1. [14245](http://github.com/cms-sw/cmssw/pull/14245)  from @cms-l1t-offline: Fix IB crashes due to BX range set improperly `l1`  created: 2016-04-25T22:41:13Z merged: 2016-04-26T07:16:39Z

1. [14243](http://github.com/cms-sw/cmssw/pull/14243)  from @wmtan: Use unique_ptr, not auto_ptr, in HLT `hlt`  created: 2016-04-25T19:27:19Z merged: 2016-04-26T07:22:44Z

1. [14241](http://github.com/cms-sw/cmssw/pull/14241)  from @Dr15Jones: Added missing dictionaries related to BXVector `l1`  created: 2016-04-25T15:16:21Z merged: 2016-04-26T07:39:41Z

1. [14240](http://github.com/cms-sw/cmssw/pull/14240)  from @makortel: Remove (obsolete) customizations from phase1TkCustoms.py `pdmv`  `simulation`  created: 2016-04-25T15:05:23Z merged: 2016-04-26T14:32:15Z

1. [14238](http://github.com/cms-sw/cmssw/pull/14238)  from @ianna: Elliptical Tube Visualization `comparison`  `visualization`  created: 2016-04-25T13:34:10Z merged: 2016-04-26T07:23:41Z

1. [14237](http://github.com/cms-sw/cmssw/pull/14237)  from @hengne: relval matrix update, add 3 Higgs LHE basked fullsim workflows `generators`  `pdmv`  created: 2016-04-25T13:04:14Z merged: 2016-04-26T18:24:18Z

1. [14229](http://github.com/cms-sw/cmssw/pull/14229)  from @ghellwig: Declare 'seedOnlyFromAbove_' as 'int' in 'Calibration/TkAlCaRecoProdu `alca`  created: 2016-04-25T09:52:54Z merged: 2016-04-28T09:43:15Z

1. [14228](http://github.com/cms-sw/cmssw/pull/14228)  from @ghellwig: Declare 'seedOnlyFromAbove_' as 'int' in 'Calibration/TkAlCaRecoProdu `alca`  created: 2016-04-25T09:52:09Z merged: 2016-04-26T07:24:41Z

1. [14225](http://github.com/cms-sw/cmssw/pull/14225)  from @thomaslenzi: Updated Phase2TrackerClusterizer validation code `reconstruction`  created: 2016-04-25T08:08:24Z merged: 2016-04-28T14:43:40Z

1. [14223](http://github.com/cms-sw/cmssw/pull/14223)  from @davidlt: Clang warnings clean up (April 25th) `alca`  `analysis`  `reconstruction`  created: 2016-04-25T07:29:36Z merged: 2016-04-28T17:32:59Z

1. [14213](http://github.com/cms-sw/cmssw/pull/14213)  from @wddgit: Add new template class ThreadSafeAddOnlyContainer `core`  created: 2016-04-22T15:51:23Z merged: 2016-04-23T07:39:44Z

1. [14209](http://github.com/cms-sw/cmssw/pull/14209)  from @mbandrews: Add pulse max check parameter `dqm`  created: 2016-04-22T14:16:11Z merged: 2016-04-27T11:49:38Z

1. [14205](http://github.com/cms-sw/cmssw/pull/14205)  from @avetisya: Increasing number of paths in old module (81X) `hlt`  created: 2016-04-22T12:46:38Z merged: 2016-04-23T07:40:09Z

1. [14204](http://github.com/cms-sw/cmssw/pull/14204)  from @avetisya: Short term fix for number of HLT paths `hlt`  created: 2016-04-22T12:42:24Z merged: 2016-04-26T07:40:23Z

1. [14202](http://github.com/cms-sw/cmssw/pull/14202)  from @cms-l1t-offline: New CondFormats for L1T Global `alca`  `db`  `l1`  created: 2016-04-21T21:53:13Z merged: 2016-04-26T18:25:21Z

1. [14201](http://github.com/cms-sw/cmssw/pull/14201)  from @cms-l1t-offline: New CondFormats for L1T Global `alca`  `db`  `l1`  created: 2016-04-21T21:51:09Z merged: 2016-04-23T07:39:12Z

1. [14198](http://github.com/cms-sw/cmssw/pull/14198)  from @dimattia: Calibration update 80 x `alca`  created: 2016-04-21T19:51:12Z merged: 2016-04-28T06:14:59Z

1. [14196](http://github.com/cms-sw/cmssw/pull/14196)  from @alja: 80x Fireworks: Add checks for incomplete reco geometry `comparison`  `visualization`  created: 2016-04-21T19:09:41Z merged: 2016-04-22T07:16:49Z

1. [14195](http://github.com/cms-sw/cmssw/pull/14195)  from @mkirsano: fix incorrect usage of boost `generators`  created: 2016-04-21T18:04:44Z merged: 2016-04-26T07:24:56Z

1. [14193](http://github.com/cms-sw/cmssw/pull/14193)  from @diguida: Fix condition loading in Castor DQM online client `dqm`  created: 2016-04-21T15:26:07Z merged: 2016-04-23T07:40:44Z

1. [14191](http://github.com/cms-sw/cmssw/pull/14191)  from @Martin-Grunewald: Fix Unrunnable Schedule due to multiple offlineBeamSpots (80X) `fastsim`  created: 2016-04-21T14:19:03Z merged: 2016-04-22T08:12:33Z

1. [14189](http://github.com/cms-sw/cmssw/pull/14189)  from @civanch: Extended G4 geometry printouts `simulation`  created: 2016-04-21T14:14:04Z merged: 2016-04-22T07:17:29Z

1. [14187](http://github.com/cms-sw/cmssw/pull/14187)  from @vanbesien: Updating scenario to ppEra_Run2_2016 - 80X `dqm`  created: 2016-04-21T14:07:11Z merged: 2016-04-22T08:12:47Z

1. [14180](http://github.com/cms-sw/cmssw/pull/14180)  from @lgray: Update HGCal unit test to run with flat phase 2 tracker `operations`  `reconstruction`  created: 2016-04-21T10:41:48Z merged: 2016-04-29T09:23:09Z

1. [14179](http://github.com/cms-sw/cmssw/pull/14179)  from @VinInn: Speed up Jet Producer for HLT `reconstruction`  created: 2016-04-21T10:03:39Z merged: 2016-04-30T18:25:42Z

1. [14176](http://github.com/cms-sw/cmssw/pull/14176)  from @lveldere: FastSim bug fix: proper FastTrackerRecHit id `fastsim`  created: 2016-04-21T09:37:27Z merged: 2016-04-28T14:43:52Z

1. [14170](http://github.com/cms-sw/cmssw/pull/14170)  from @UMN-CMS: uMNio data skipping implemented `reconstruction`  created: 2016-04-20T19:56:05Z merged: 2016-04-22T08:12:58Z

1. [14169](http://github.com/cms-sw/cmssw/pull/14169)  from @wmtan: Use unique_ptr, not auto_ptr, in Generators `generators`  created: 2016-04-20T17:05:43Z merged: 2016-04-26T07:29:41Z

1. [14168](http://github.com/cms-sw/cmssw/pull/14168)  from @kpedro88: HGCal Eras using recommended methods `alca`  `l1`  `operations`  `reconstruction`  `simulation`  created: 2016-04-20T13:05:28Z merged: 2016-04-28T06:37:43Z

1. [14163](http://github.com/cms-sw/cmssw/pull/14163)  from @bsunanda: bsunanda:Run2-alca39 Add the GammaJetSelector which is more suitable for the AlCaReco step `alca`  created: 2016-04-20T10:58:54Z merged: 2016-05-02T05:49:08Z

1. [14159](http://github.com/cms-sw/cmssw/pull/14159)  from @makortel: Enable pixel templates for phase1 pixel `reconstruction`  created: 2016-04-20T09:15:34Z merged: 2016-04-29T09:18:53Z

1. [14151](http://github.com/cms-sw/cmssw/pull/14151)  from @VinInn: Slim down PFRecHit `core`  `db`  `geometry`  `reconstruction`  `visualization`  created: 2016-04-19T16:34:56Z merged: 2016-04-27T11:50:06Z

1. [14146](http://github.com/cms-sw/cmssw/pull/14146)  from @sarafiorendi: update muon validation plots to Stage2L1 + update HLT DQM plots `dqm`  created: 2016-04-19T13:27:16Z merged: 2016-04-23T07:44:52Z

1. [14144](http://github.com/cms-sw/cmssw/pull/14144)  from @trtomei: DQM for B2G Ele + Single Jet paths 2016 - backport 80X `dqm`  created: 2016-04-19T11:31:00Z merged: 2016-04-26T07:46:01Z

1. [14143](http://github.com/cms-sw/cmssw/pull/14143)  from @ahinzmann: Add test configuration for jet tools from MiniAOD `reconstruction`  created: 2016-04-19T11:28:53Z merged: 2016-04-27T11:55:18Z

1. [14142](http://github.com/cms-sw/cmssw/pull/14142)  from @trtomei: DQM for Express 2016 - backport 80X `dqm`  created: 2016-04-19T11:16:53Z merged: 2016-04-26T07:45:49Z

1. [14141](http://github.com/cms-sw/cmssw/pull/14141)  from @cms-l1t-offline: Bring L1T up-to-date with l1t-tsg-v5-cand (80x) `l1`  created: 2016-04-19T10:56:06Z merged: 2016-04-26T18:25:01Z

1. [14140](http://github.com/cms-sw/cmssw/pull/14140)  from @kpedro88: fix up zero suppression for QIE10 `simulation`  created: 2016-04-19T10:49:35Z merged: 2016-04-26T07:46:40Z

1. [14138](http://github.com/cms-sw/cmssw/pull/14138)  from @lgray: Use a quick union algorithm to speed up PFBlockAlgo (factor of 2-3x) `reconstruction`  created: 2016-04-19T10:42:31Z merged: 2016-04-29T07:52:14Z

1. [14135](http://github.com/cms-sw/cmssw/pull/14135)  from @sarafiorendi: modify L2MuonSeedGeneratorFromL1T to deal with possible L1 zero charge `reconstruction`  created: 2016-04-19T10:09:51Z merged: 2016-04-28T06:38:14Z

1. [14134](http://github.com/cms-sw/cmssw/pull/14134)  from @CTPPS: CTPPS: new DataFormats for local TOTEM RP reconstruction `reconstruction`  created: 2016-04-19T09:39:30Z merged: 2016-04-22T07:17:50Z

1. [14129](http://github.com/cms-sw/cmssw/pull/14129)  from @trtomei: DQM for B2G Ele + Single Jet paths 2016 `dqm`  created: 2016-04-18T23:01:27Z merged: 2016-04-22T13:01:42Z

1. [14126](http://github.com/cms-sw/cmssw/pull/14126)  from @tanmaymudholkar: Added chi-squared plots to Timing Task `dqm`  created: 2016-04-18T16:25:18Z merged: 2016-04-26T07:46:20Z

1. [14123](http://github.com/cms-sw/cmssw/pull/14123)  from @trtomei: Updated DQM for very high MET paths for Hotline/Express `dqm`  created: 2016-04-18T14:20:01Z merged: 2016-04-26T07:28:36Z

1. [14121](http://github.com/cms-sw/cmssw/pull/14121)  from @ianna: Unordered Map Serialization `alca`  `db`  created: 2016-04-18T12:55:34Z merged: 2016-04-27T11:54:46Z

1. [14118](http://github.com/cms-sw/cmssw/pull/14118)  from @tanmaymudholkar: Fix for emulator match problem and incorrect tower binning. `dqm`  created: 2016-04-18T10:57:30Z merged: 2016-04-26T09:33:41Z

1. [14117](http://github.com/cms-sw/cmssw/pull/14117)  from @hengne: relval matrix to use HLT relval2016  `pdmv`  created: 2016-04-18T10:36:56Z merged: 2016-04-26T18:27:02Z

1. [14115](http://github.com/cms-sw/cmssw/pull/14115)  from @bsunanda: bsunanda:Phase2-hgx50 Validation code for HGCal and in particular geometry validation `dqm`  `reconstruction`  `simulation`  created: 2016-04-17T14:13:51Z merged: 2016-04-22T17:46:43Z

1. [14090](http://github.com/cms-sw/cmssw/pull/14090)  from @tanmaymudholkar: Fix for emulator match problem and incorrect tower binning. `dqm`  created: 2016-04-15T13:25:10Z merged: 2016-04-26T18:25:53Z

1. [14068](http://github.com/cms-sw/cmssw/pull/14068)  from @gpetruc: Save L1 stage2 info in offline data tiers (80X) `analysis`  `l1`  `reconstruction`  created: 2016-04-14T12:24:12Z merged: 2016-04-22T08:13:13Z

1. [14066](http://github.com/cms-sw/cmssw/pull/14066)  from @jasperlauwers: Update HLTriggerOffline/Higgs paths 80X `dqm`  created: 2016-04-14T11:07:03Z merged: 2016-04-26T07:45:37Z

1. [14065](http://github.com/cms-sw/cmssw/pull/14065)  from @jasperlauwers: Update HLTriggerOffline/Higgs paths 81X `dqm`  created: 2016-04-14T11:04:07Z merged: 2016-04-25T08:13:14Z

1. [14057](http://github.com/cms-sw/cmssw/pull/14057)  from @VinInn: minimal fix to use rep, not position.eta/phi `reconstruction`  created: 2016-04-14T07:41:10Z merged: 2016-04-26T18:26:13Z

1. [14051](http://github.com/cms-sw/cmssw/pull/14051)  from @gpetruc: Save L1 stage2 info in offline data tiers (81X) `analysis`  `l1`  `reconstruction`  created: 2016-04-13T14:42:01Z merged: 2016-04-22T07:18:02Z

1. [14035](http://github.com/cms-sw/cmssw/pull/14035)  from @jruizvar: PFMET paths for Monojet EXO DQM + Remove NoHalo (80X) `dqm`  created: 2016-04-12T12:23:47Z merged: 2016-04-26T07:45:25Z

1. [14032](http://github.com/cms-sw/cmssw/pull/14032)  from @ianna: Geometry Validation `db`  `dqm`  `geometry`  created: 2016-04-12T10:04:09Z merged: 2016-04-24T08:06:16Z

1. [14027](http://github.com/cms-sw/cmssw/pull/14027)  from @dildick: More general form of valid hit in pixel function (81X) `analysis`  `dqm`  `reconstruction`  created: 2016-04-12T03:04:18Z merged: 2016-04-28T14:46:00Z

1. [14017](http://github.com/cms-sw/cmssw/pull/14017)  from @makortel: Fix era treatments for FastSim seeds in TrackValidation_cff `dqm`  created: 2016-04-11T11:29:32Z merged: 2016-04-23T07:44:38Z

1. [13988](http://github.com/cms-sw/cmssw/pull/13988)  from @makortel: Migrate customiseForRunI to era (81X) `dqm`  `operations`  `reconstruction`  created: 2016-04-07T19:08:44Z merged: 2016-04-22T12:55:49Z

1. [13987](http://github.com/cms-sw/cmssw/pull/13987)  from @makortel: Migrate the temporary 2017 DQM+validation customizations to eras `dqm`  `reconstruction`  `simulation`  created: 2016-04-07T19:07:48Z merged: 2016-04-23T07:45:36Z

1. [13976](http://github.com/cms-sw/cmssw/pull/13976)  from @vbotta: Alignment geometry upgrade 81X `alca`  created: 2016-04-07T13:45:34Z merged: 2016-04-26T13:22:00Z

1. [13967](http://github.com/cms-sw/cmssw/pull/13967)  from @depasse: Ecal Tools for new O2O machine `db`  created: 2016-04-06T17:26:05Z merged: 2016-05-02T11:58:02Z

1. [13963](http://github.com/cms-sw/cmssw/pull/13963)  from @dildick: Split up GEM and ME0 customizations `core`  `dqm`  `operations`  `reconstruction`  `simulation`  created: 2016-04-06T14:59:12Z merged: 2016-04-30T12:53:50Z

1. [13953](http://github.com/cms-sw/cmssw/pull/13953)  from @lgray: Hgcal Hit Tools `geometry`  `reconstruction`  created: 2016-04-06T11:08:30Z merged: 2016-04-22T17:42:32Z

1. [13943](http://github.com/cms-sw/cmssw/pull/13943)  from @barvic:  CSCOfflineMonitor DQM module - added timing plots  `dqm`  created: 2016-04-05T22:07:59Z merged: 2016-04-22T08:13:25Z

1. [13935](http://github.com/cms-sw/cmssw/pull/13935)  from @olivito: Susy HLT DQM updates in 81x `comparison`  `dqm`  created: 2016-04-05T14:03:49Z merged: 2016-04-26T11:51:50Z

1. [13932](http://github.com/cms-sw/cmssw/pull/13932)  from @olivito: Susy HLT DQM updates in 80x `dqm`  created: 2016-04-05T13:46:07Z merged: 2016-04-26T07:45:13Z

1. [13839](http://github.com/cms-sw/cmssw/pull/13839)  from @CTPPS: CTPPS: new EventFilter for raw-to-digi conversion of TOTEM RP data `daq`  `reconstruction`  created: 2016-03-25T15:33:39Z merged: 2016-04-25T08:20:21Z

1. [13830](http://github.com/cms-sw/cmssw/pull/13830)  from @hqucms: New codes for Strip O2O. `alca`  `db`  created: 2016-03-24T14:46:36Z merged: 2016-04-26T09:53:36Z

1. [13802](http://github.com/cms-sw/cmssw/pull/13802)  from @mtosi: drop pixel vertices (they are not available since run2 !) `dqm`  created: 2016-03-22T16:18:40Z merged: 2016-04-26T07:44:57Z

1. [13754](http://github.com/cms-sw/cmssw/pull/13754)  from @Vlandr57: FastSim HF timing from SL `fastsim`  created: 2016-03-17T13:39:51Z merged: 2016-04-25T08:17:08Z

1. [13696](http://github.com/cms-sw/cmssw/pull/13696)  from @delaere: Migration of L1 tracker primitives from SLHCDEV `l1`  created: 2016-03-11T16:45:31Z merged: 2016-05-03T14:38:00Z

1. [13659](http://github.com/cms-sw/cmssw/pull/13659)  from @mtosi: add monitoring of tracks stopping source `dqm`  created: 2016-03-09T12:46:00Z merged: 2016-04-26T07:44:41Z

1. [13595](http://github.com/cms-sw/cmssw/pull/13595)  from @fcavallo: Fraction noisy channels `dqm`  created: 2016-03-04T13:00:33Z merged: 2016-05-02T11:59:16Z

#### CMSDIST Changes between Tags REL/CMSSW_8_1_0_pre3/slc6_amd64_gcc530 and REL/CMSSW_8_1_0_pre4/slc6_amd64_gcc530:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_8_1_0_pre3/slc6_amd64_gcc530...REL/CMSSW_8_1_0_pre4/slc6_amd64_gcc530)



1. [2277](http://github.com/cms-sw/cmssw/pull/2277)  from @degano: Updata data for L1Trigger/L1TCalorimeter. created: 2014-02-03T17:24:35Z merged: 2014-02-10T11:59:56Z

1. [2276](http://github.com/cms-sw/cmssw/pull/2276)  from @degano: Upgrade frontier client to v 2.8.19. created: 2014-02-03T17:09:11Z merged: 2014-02-05T02:28:09Z

1. [2275](http://github.com/cms-sw/cmssw/pull/2275)  from @cms-sw: Update data-L1Trigger-L1TMuon.spec created: 2014-02-03T16:50:39Z merged: 2014-02-10T11:49:29Z

1. [2273](http://github.com/cms-sw/cmssw/pull/2273)  from @iahmad-khan: davix updated to 0.6.0 in 81x stable created: 2014-02-03T15:20:31Z merged: None

1. [2271](http://github.com/cms-sw/cmssw/pull/2271)  from @degano: Add data for CalibTracker/SiStripDCS. created: 2014-02-03T14:54:13Z merged: 2014-02-06T20:08:09Z

1. [2270](http://github.com/cms-sw/cmssw/pull/2270)  from @degano: Add data for CalibTracker/SiStripDCS. created: 2014-02-03T14:05:57Z merged: 2014-02-04T19:28:19Z

1. [2264](http://github.com/cms-sw/cmssw/pull/2264)  from @cms-sw: Update utm.spec created: 2014-02-02T05:49:49Z merged: 2014-02-02T09:25:17Z

1. [2263](http://github.com/cms-sw/cmssw/pull/2263)  from @degano: Add data for new package SLHCUpgradeSimulations/Geometry. created: 2014-02-01T15:44:24Z merged: 2014-02-04T08:48:56Z
