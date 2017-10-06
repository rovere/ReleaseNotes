---
layout: post
title:  "8_1_0_pre1"
date:   2017-10-05 18:46:15 +0200
categories: cmssw
relmajor: 8
relminor: 1
relsubminor: 0

relpre: _pre1
---

# CMSSW_8_1_0_pre1
#### Changes since CMSSW_8_0_2:

[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_8_0_2...CMSSW_8_1_0_pre1)



1. [13667](http://github.com/cms-sw/cmssw/pull/13667)  from @mdhildreth: Add automatic turn-off of tracker digiSimLink production in standard production mode `simulation`  created: 2016-03-09T16:07:55Z merged: 2016-03-10T09:41:50Z

1. [13662](http://github.com/cms-sw/cmssw/pull/13662)  from @deguio: add protection for T0 configuration query `dqm`  created: 2016-03-09T13:32:49Z merged: 2016-03-09T17:01:47Z

1. [13658](http://github.com/cms-sw/cmssw/pull/13658)  from @davidlt: Do not use constexpr with std::log in C++14 for ICC `reconstruction`  created: 2016-03-09T10:28:21Z merged: 2016-03-10T09:42:12Z

1. [13651](http://github.com/cms-sw/cmssw/pull/13651)  from @davidlt: Regenerate DQMServices/Core/src/ROOTFilePB.proto `comparison`  `dqm`  created: 2016-03-08T18:51:11Z merged: 2016-03-08T18:58:19Z

1. [13645](http://github.com/cms-sw/cmssw/pull/13645)  from @cms-tsg-storm: Cummulative 80X PRs for 81X: (#13558 #13572 #13588 #13596 #13602 #13607 #13621) `alca`  `hlt`  `l1`  `reconstruction`  created: 2016-03-08T16:26:28Z merged: 2016-03-10T09:56:01Z

1. [13643](http://github.com/cms-sw/cmssw/pull/13643)  from @ghellwig: Declare 'seedOnlyFromAbove_' as 'int'. `alca`  created: 2016-03-08T16:23:59Z merged: 2016-03-09T13:08:04Z

1. [13642](http://github.com/cms-sw/cmssw/pull/13642)  from @ahinzmann: Add PU id working points to MiniAOD 8_1_X `analysis`  `reconstruction`  created: 2016-03-08T14:18:01Z merged: 2016-03-09T16:28:12Z

1. [13638](http://github.com/cms-sw/cmssw/pull/13638)  from @cms-sw: Revert "Fix a minor error in DQM/L1TMonitor BuildFile" `comparison`  `dqm`  created: 2016-03-08T09:49:56Z merged: 2016-03-08T09:50:01Z

1. [13634](http://github.com/cms-sw/cmssw/pull/13634)  from @davidlt: Misc cleanup for GCC 6 (missing header, integer overflow, wrong address usage, ..) `analysis`  `reconstruction`  created: 2016-03-08T08:56:38Z merged: 2016-03-09T13:11:22Z

1. [13632](http://github.com/cms-sw/cmssw/pull/13632)  from @davidlt: Clean up ElectroWeakAnalysis (GCC 6) `analysis`  created: 2016-03-07T18:13:18Z merged: 2016-03-07T19:20:05Z

1. [13631](http://github.com/cms-sw/cmssw/pull/13631)  from @davidlt: Clean up for GCC 6 (<cmath> header, std::, __afs cache files) `l1`  created: 2016-03-07T17:42:29Z merged: 2016-03-08T08:55:29Z

1. [13630](http://github.com/cms-sw/cmssw/pull/13630)  from @swang373: EMTF DQM Module for CMSSW_8_1_X `dqm`  `l1`  created: 2016-03-07T17:09:04Z merged: 2016-03-09T13:13:14Z

1. [13627](http://github.com/cms-sw/cmssw/pull/13627)  from @mbandrews: Fix binning in ZS filter SRTask plots `dqm`  created: 2016-03-07T15:54:16Z merged: 2016-03-08T08:35:41Z

1. [13619](http://github.com/cms-sw/cmssw/pull/13619)  from @dmitrijus: Fix a minor error in DQM/L1TMonitor BuildFile `dqm`  created: 2016-03-07T09:19:51Z merged: 2016-03-07T19:19:36Z

1. [13617](http://github.com/cms-sw/cmssw/pull/13617)  from @dmitrijus: Fix a small bug in an online DQM input source `dqm`  created: 2016-03-07T08:22:01Z merged: 2016-03-07T19:19:20Z

1. [13616](http://github.com/cms-sw/cmssw/pull/13616)  from @davidlt: Use std::abs for enum (tauImpactParameter::PDGInfo::PDGMCNumbering) `reconstruction`  created: 2016-03-07T06:36:22Z merged: 2016-03-07T10:13:23Z

1. [13615](http://github.com/cms-sw/cmssw/pull/13615)  from @davidlt: Add missing <vector> header `generators`  created: 2016-03-06T22:42:32Z merged: 2016-03-07T09:10:46Z

1. [13614](http://github.com/cms-sw/cmssw/pull/13614)  from @davidlt: Add missing <cmath> header and remove <string.h> header `core`  created: 2016-03-06T22:35:32Z merged: 2016-03-07T09:11:01Z

1. [13613](http://github.com/cms-sw/cmssw/pull/13613)  from @davidlt: Add missing <cassert> header `simulation`  created: 2016-03-06T22:27:51Z merged: 2016-03-07T09:11:22Z

1. [13611](http://github.com/cms-sw/cmssw/pull/13611)  from @davidlt: Add missing <numeric> include for std::accumulate `reconstruction`  created: 2016-03-06T21:57:15Z merged: 2016-03-08T08:55:54Z

1. [13610](http://github.com/cms-sw/cmssw/pull/13610)  from @davidlt: Add missing headers (GCC 6.0.0) `hlt`  created: 2016-03-06T21:44:53Z merged: 2016-03-07T09:10:29Z

1. [13601](http://github.com/cms-sw/cmssw/pull/13601)  from @makortel: Remove 2017 fake conditions `geometry`  `simulation`  created: 2016-03-04T15:48:15Z merged: 2016-03-07T09:12:38Z

1. [13600](http://github.com/cms-sw/cmssw/pull/13600)  from @wmtan: Enforce consumes interface in output modules `core`  `daq`  `dqm`  `reconstruction`  `simulation`  created: 2016-03-04T15:47:27Z merged: 2016-03-10T10:09:09Z

1. [13594](http://github.com/cms-sw/cmssw/pull/13594)  from @VinInn: Gsf cleanup and debug `reconstruction`  created: 2016-03-04T11:07:54Z merged: 2016-03-08T08:36:27Z

1. [13591](http://github.com/cms-sw/cmssw/pull/13591)  from @makortel: Enable castor digis for 2017 `operations`  created: 2016-03-04T09:58:43Z merged: 2016-03-06T21:32:52Z

1. [13585](http://github.com/cms-sw/cmssw/pull/13585)  from @tmrhombus: cleaning static analyzer warnings `reconstruction`  created: 2016-03-03T16:56:44Z merged: 2016-03-06T08:35:13Z

1. [13583](http://github.com/cms-sw/cmssw/pull/13583)  from @ianna: Remove Extra Plane in Pixel Service Cylinder Polycone `geometry`  created: 2016-03-03T13:49:24Z merged: 2016-03-06T08:35:30Z

1. [13579](http://github.com/cms-sw/cmssw/pull/13579)  from @makortel: Fix track validation for heavy ions `dqm`  created: 2016-03-03T11:21:41Z merged: 2016-03-08T16:50:39Z

1. [13571](http://github.com/cms-sw/cmssw/pull/13571)  from @degano: [SimCalorimetry/EcalElectronicsEmulation] Solve warning found by gcc 5.3.0. `simulation`  created: 2016-03-03T10:50:30Z merged: 2016-03-10T09:57:38Z

1. [13570](http://github.com/cms-sw/cmssw/pull/13570)  from @makortel: Fix QuickTrackAssociatorByHits for empty TrackingParticleRefVector `simulation`  created: 2016-03-03T10:32:36Z merged: 2016-03-03T13:22:41Z

1. [13567](http://github.com/cms-sw/cmssw/pull/13567)  from @lihux25: Fix "withTopo" issue `alca`  created: 2016-03-03T09:51:11Z merged: 2016-03-08T18:13:29Z

1. [13564](http://github.com/cms-sw/cmssw/pull/13564)  from @lveldere: Fastsim: Muon HLT: refactor seeding configuration `fastsim`  `hlt`  created: 2016-03-03T08:24:37Z merged: 2016-03-06T21:32:28Z

1. [13560](http://github.com/cms-sw/cmssw/pull/13560)  from @rrabadan: StoN in module highest values `dqm`  created: 2016-03-02T20:05:33Z merged: 2016-03-08T08:53:41Z

1. [13559](http://github.com/cms-sw/cmssw/pull/13559)  from @civanch: Hcal tb2006 update `simulation`  created: 2016-03-02T18:46:23Z merged: 2016-03-03T12:39:46Z

1. [13557](http://github.com/cms-sw/cmssw/pull/13557)  from @bsunanda: bsunada:Run2-hcx73 Correct hcal customization code `simulation`  created: 2016-03-02T16:42:23Z merged: 2016-03-03T10:13:01Z

1. [13555](http://github.com/cms-sw/cmssw/pull/13555)  from @ggovi: popcon2dropbox tool moved to condition uploader `db`  created: 2016-03-02T15:29:02Z merged: 2016-03-03T12:35:30Z

1. [13554](http://github.com/cms-sw/cmssw/pull/13554)  from @davidlange6: Printout reduction (81x) `dqm`  `l1`  created: 2016-03-02T11:30:32Z merged: 2016-03-03T10:16:27Z

1. [13552](http://github.com/cms-sw/cmssw/pull/13552)  from @ianna: DD Regression Test for All Scenarios `geometry`  created: 2016-03-02T11:00:20Z merged: 2016-03-02T16:20:47Z

1. [13551](http://github.com/cms-sw/cmssw/pull/13551)  from @makortel: Update tracking MC validation scripts `dqm`  created: 2016-03-02T10:42:38Z merged: 2016-03-08T08:37:27Z

1. [13550](http://github.com/cms-sw/cmssw/pull/13550)  from @lveldere: Fastsim: muon hlt cleanup `fastsim`  created: 2016-03-02T09:46:47Z merged: 2016-03-02T16:20:27Z

1. [13544](http://github.com/cms-sw/cmssw/pull/13544)  from @vkhristenko: HCAL DQM small fixed `dqm`  created: 2016-03-01T18:34:25Z merged: 2016-03-08T08:38:06Z

1. [13539](http://github.com/cms-sw/cmssw/pull/13539)  from @jfernan2: Fixes to DT*Trigger classes to make them compatible with the DT PoA `dqm`  created: 2016-03-01T16:42:40Z merged: 2016-03-08T08:39:41Z

1. [13530](http://github.com/cms-sw/cmssw/pull/13530)  from @bendavid: Changes needed for SUSY parameter scans `analysis`  `generators`  `reconstruction`  created: 2016-03-01T00:37:39Z merged: 2016-03-10T09:56:40Z

1. [13529](http://github.com/cms-sw/cmssw/pull/13529)  from @bsunanda: bsunanda:Run2-hcx72 Modify the code/xml files to define BH `geometry`  created: 2016-02-29T22:30:01Z merged: 2016-03-01T11:23:29Z

1. [13527](http://github.com/cms-sw/cmssw/pull/13527)  from @smrenna: Modifications to guns to allow finite decay length for mothers `generators`  created: 2016-02-29T17:38:33Z merged: 2016-03-02T16:20:16Z

1. [13526](http://github.com/cms-sw/cmssw/pull/13526)  from @Dr15Jones: PSet.clone now works like module clone `core`  created: 2016-02-29T16:45:30Z merged: 2016-03-01T11:23:43Z

1. [13525](http://github.com/cms-sw/cmssw/pull/13525)  from @ianna: Enable Partial Sim/Reco Geometry Dump `visualization`  created: 2016-02-29T16:44:49Z merged: 2016-03-01T11:48:11Z

1. [13524](http://github.com/cms-sw/cmssw/pull/13524)  from @hengne: relval matrix updates, PR#13516 port to 81x `alca`  `pdmv`  created: 2016-02-29T16:39:09Z merged: 2016-03-07T09:12:12Z

1. [13522](http://github.com/cms-sw/cmssw/pull/13522)  from @bsunanda: bsunanda:Run2-hcx71 Try to sort out some geometry issue of HGCal `geometry`  created: 2016-02-29T15:55:27Z merged: 2016-03-01T11:48:34Z

1. [13521](http://github.com/cms-sw/cmssw/pull/13521)  from @Dr15Jones: Improve exception message for missing produces call `core`  created: 2016-02-29T15:45:20Z merged: 2016-03-01T11:51:11Z

1. [13519](http://github.com/cms-sw/cmssw/pull/13519)  from @lveldere: FastSim: run btag DQM `fastsim`  created: 2016-02-29T15:18:52Z merged: 2016-03-03T08:35:44Z

1. [13518](http://github.com/cms-sw/cmssw/pull/13518)  from @lveldere: FastSim: never run DQM in endPath for FastSim `operations`  created: 2016-02-29T14:25:10Z merged: 2016-03-01T17:32:17Z

1. [13517](http://github.com/cms-sw/cmssw/pull/13517)  from @makortel: Fix trackingOnly DQM `dqm`  created: 2016-02-29T11:07:22Z merged: 2016-03-08T08:39:06Z

1. [13515](http://github.com/cms-sw/cmssw/pull/13515)  from @davidlt: Fix all [-Wheader-guard] warnings `alca`  `analysis`  `core`  `db`  `dqm`  `fastsim`  `generators`  `geometry`  `hlt`  `l1`  `reconstruction`  `simulation`  `visualization`  created: 2016-02-28T08:42:56Z merged: 2016-02-29T15:09:48Z

1. [13511](http://github.com/cms-sw/cmssw/pull/13511)  from @kpedro88: add QIE10 product to DataMixingModule (one-line fix) `comparison`  `simulation`  created: 2016-02-27T19:24:11Z merged: 2016-02-28T08:16:09Z

1. [13509](http://github.com/cms-sw/cmssw/pull/13509)  from @Martin-Grunewald: Add protection against 0-element uGtAlgoBlocks in HLTL1TSeed module `hlt`  created: 2016-02-27T06:23:40Z merged: 2016-02-29T17:49:54Z

1. [13506](http://github.com/cms-sw/cmssw/pull/13506)  from @slava77: add missing initialization in CaloCluster `reconstruction`  created: 2016-02-26T21:31:06Z merged: 2016-03-01T11:49:23Z

1. [13503](http://github.com/cms-sw/cmssw/pull/13503)  from @makortel: Print deprecation warning if anybody uses phase1TkCustoms without phase1Pixel era `simulation`  created: 2016-02-26T17:53:16Z merged: 2016-03-02T21:26:08Z

1. [13502](http://github.com/cms-sw/cmssw/pull/13502)  from @tanmaymudholkar: New chi-squared plots `dqm`  created: 2016-02-26T17:45:29Z merged: 2016-03-08T08:38:49Z

1. [13501](http://github.com/cms-sw/cmssw/pull/13501)  from @lveldere: FastSim: fix layer definition of hltPixelPairSeeds `fastsim`  created: 2016-02-26T17:36:51Z merged: 2016-02-27T18:05:41Z

1. [13500](http://github.com/cms-sw/cmssw/pull/13500)  from @mbandrews: Add channel status + laser threshold `dqm`  created: 2016-02-26T17:12:42Z merged: 2016-03-08T18:18:15Z

1. [13494](http://github.com/cms-sw/cmssw/pull/13494)  from @mmusich: Fixing 81X relval alcareco in express test `pdmv`  created: 2016-02-26T14:57:18Z merged: 2016-03-02T21:56:17Z

1. [13493](http://github.com/cms-sw/cmssw/pull/13493)  from @lveldere: FastSim: disable btag DQM cause it depends on product not available in FastSim `fastsim`  created: 2016-02-26T13:19:22Z merged: 2016-02-26T16:06:02Z

1. [13491](http://github.com/cms-sw/cmssw/pull/13491)  from @bsunanda: bsunanda:Run2-hcx69 Create scenario to run with new HCAL TP `geometry`  created: 2016-02-26T11:38:15Z merged: 2016-03-06T08:36:19Z

1. [13486](http://github.com/cms-sw/cmssw/pull/13486)  from @fioriNTU: correct raw data collection to be used `alca`  created: 2016-02-26T10:40:21Z merged: 2016-02-27T18:26:24Z

1. [13485](http://github.com/cms-sw/cmssw/pull/13485)  from @schneiml: Add cuts to SiStripMonitorTrack (8_1_X version) `dqm`  created: 2016-02-26T09:31:30Z merged: 2016-03-03T10:19:16Z

1. [13483](http://github.com/cms-sw/cmssw/pull/13483)  from @alberto-sanchez: Adding tracks from V0, and fixing bug in photon conversion producer `analysis`  created: 2016-02-25T19:55:04Z merged: 2016-03-06T21:34:57Z

1. [13482](http://github.com/cms-sw/cmssw/pull/13482)  from @lveldere: FastSim : Tracking: fix bad import `fastsim`  created: 2016-02-25T18:52:44Z merged: 2016-02-26T06:16:31Z

1. [13481](http://github.com/cms-sw/cmssw/pull/13481)  from @Dr15Jones: Principal::getForOutput now always retrieves the product `comparison`  `core`  created: 2016-02-25T16:17:32Z merged: 2016-02-29T16:56:14Z

1. [13478](http://github.com/cms-sw/cmssw/pull/13478)  from @pietverwilligen: Me0 digitizer constand phi smearing 800 `simulation`  created: 2016-02-25T12:35:53Z merged: 2016-02-27T07:27:18Z

1. [13477](http://github.com/cms-sw/cmssw/pull/13477)  from @makortel: Migrate 2017 tracking to eras `dqm`  `reconstruction`  `simulation`  created: 2016-02-25T10:41:17Z merged: 2016-03-08T18:16:26Z

1. [13475](http://github.com/cms-sw/cmssw/pull/13475)  from @schneiml: Improve print_trace in DQMStore `dqm`  created: 2016-02-25T10:20:24Z merged: 2016-03-08T18:15:48Z

1. [13472](http://github.com/cms-sw/cmssw/pull/13472)  from @jbrands: including the 76X pileup Jet Id training  `reconstruction`  created: 2016-02-25T09:05:21Z merged: 2016-03-06T08:37:24Z

1. [13470](http://github.com/cms-sw/cmssw/pull/13470)  from @kirschen: remove unused L1 includes and members of the class `hlt`  created: 2016-02-25T08:30:55Z merged: 2016-02-27T18:06:25Z

1. [13468](http://github.com/cms-sw/cmssw/pull/13468)  from @kirschen: add HLTJetL1TMatchProducer as simplified stage2L1-version with corres `hlt`  created: 2016-02-24T21:53:30Z merged: 2016-02-27T18:07:15Z

1. [13467](http://github.com/cms-sw/cmssw/pull/13467)  from @Dr15Jones: Testing OutputModules only get products they consume `core`  created: 2016-02-24T20:40:49Z merged: 2016-02-26T08:08:19Z

1. [13466](http://github.com/cms-sw/cmssw/pull/13466)  from @mmusich: Updated Photon regressions, added e/gamma regressions for online, updated JECs with L2L3 residuals and other fixes `alca`  created: 2016-02-24T20:32:49Z merged: 2016-02-29T15:26:46Z

1. [13465](http://github.com/cms-sw/cmssw/pull/13465)  from @wmtan: Better way to disable rootlogon `core`  created: 2016-02-24T17:51:35Z merged: 2016-02-26T08:08:32Z

1. [13464](http://github.com/cms-sw/cmssw/pull/13464)  from @lveldere: FastSim bug fix 8_1_X: fastSim era for Validation sequence, define DQM sequence for FastSim => *run physicsDQM8 `fastsim`  `operations`  `pdmv`  created: 2016-02-24T17:33:56Z merged: 2016-02-25T09:19:35Z

1. [13462](http://github.com/cms-sw/cmssw/pull/13462)  from @Vlandr57: FastSim: New correction coefficients for HF 81X `fastsim`  created: 2016-02-24T17:20:28Z merged: 2016-02-26T08:09:00Z

1. [13459](http://github.com/cms-sw/cmssw/pull/13459)  from @lveldere: FastSim: apply fastsim customs on L1Reco via fastsim era `fastsim`  `l1`  `operations`  created: 2016-02-24T16:19:59Z merged: 2016-03-03T10:14:48Z

1. [13458](http://github.com/cms-sw/cmssw/pull/13458)  from @lveldere: Fastsim tracking remove obs files `fastsim`  created: 2016-02-24T15:54:12Z merged: 2016-02-27T07:26:41Z

1. [13456](http://github.com/cms-sw/cmssw/pull/13456)  from @lveldere: FastSim: fix L1 muons `fastsim`  created: 2016-02-24T15:36:57Z merged: 2016-02-26T08:09:14Z

1. [13451](http://github.com/cms-sw/cmssw/pull/13451)  from @kirschen: change selector to stream for multithreading `analysis`  `reconstruction`  created: 2016-02-24T12:47:18Z merged: 2016-02-25T09:18:47Z

1. [13448](http://github.com/cms-sw/cmssw/pull/13448)  from @VinInn: Small performance improvement in Tracking `reconstruction`  `simulation`  created: 2016-02-24T06:29:52Z merged: 2016-03-02T11:15:33Z

1. [13446](http://github.com/cms-sw/cmssw/pull/13446)  from @aysent: Fix AssociationMap in TrackRefitter (81X) `reconstruction`  created: 2016-02-24T05:14:24Z merged: 2016-02-26T08:09:53Z

1. [13444](http://github.com/cms-sw/cmssw/pull/13444)  from @wmtan: Support ESProducrs returning std::unique_ptr. `comparison`  `core`  created: 2016-02-23T22:29:35Z merged: 2016-02-27T18:08:11Z

1. [13442](http://github.com/cms-sw/cmssw/pull/13442)  from @wmtan: Use correct python version `alca`  `core`  `db`  `dqm`  `hlt`  `reconstruction`  created: 2016-02-23T19:52:07Z merged: 2016-02-26T08:11:37Z

1. [13440](http://github.com/cms-sw/cmssw/pull/13440)  from @civanch: Fixed static anal warnings in SIM `simulation`  created: 2016-02-23T17:18:47Z merged: 2016-02-29T15:47:08Z

1. [13439](http://github.com/cms-sw/cmssw/pull/13439)  from @dmitrijus: Further improve memory tracking (for DQM PR tests) `dqm`  created: 2016-02-23T14:08:24Z merged: 2016-03-02T11:08:49Z

1. [13437](http://github.com/cms-sw/cmssw/pull/13437)  from @lveldere: Fastsim trackrefactor `fastsim`  created: 2016-02-23T12:31:33Z merged: 2016-02-24T09:52:14Z

1. [13434](http://github.com/cms-sw/cmssw/pull/13434)  from @friccita: debugged MaterialBudgetAction and runP_*_cfg.py `dqm`  `geometry`  created: 2016-02-23T00:53:52Z merged: 2016-03-06T08:37:48Z

1. [13432](http://github.com/cms-sw/cmssw/pull/13432)  from @wmtan: Fix incorrect exception message `core`  created: 2016-02-22T20:28:50Z merged: 2016-02-24T09:36:18Z

1. [13430](http://github.com/cms-sw/cmssw/pull/13430)  from @wmtan: Use consumes info to populate lookup tables `core`  created: 2016-02-22T17:07:41Z merged: 2016-02-24T09:36:37Z

1. [13429](http://github.com/cms-sw/cmssw/pull/13429)  from @kencall: Adds option to EcalDeadCellTriggerPrimitiveFilter to consider kTPSaturated flag `analysis`  `reconstruction`  created: 2016-02-22T16:02:35Z merged: 2016-02-27T18:10:19Z

1. [13428](http://github.com/cms-sw/cmssw/pull/13428)  from @ericvaandering: Fix regressions of python 2 modernization features `core`  `docs`  `dqm`  `l1`  created: 2016-02-22T15:58:33Z merged: 2016-02-26T08:10:42Z

1. [13427](http://github.com/cms-sw/cmssw/pull/13427)  from @Dr15Jones: Clean EndPaths as well when going unscheduled `core`  created: 2016-02-22T14:07:28Z merged: 2016-02-24T09:37:57Z

1. [13426](http://github.com/cms-sw/cmssw/pull/13426)  from @slehti: HLTTauRefProducer: bugfix `dqm`  created: 2016-02-22T13:14:57Z merged: 2016-03-02T11:41:39Z

1. [13424](http://github.com/cms-sw/cmssw/pull/13424)  from @makortel: Make TrackExtra::setSeedRef() to take RefToBase<TrajectorySeed> via const reference `reconstruction`  created: 2016-02-22T11:21:09Z merged: 2016-02-25T09:18:22Z

1. [13423](http://github.com/cms-sw/cmssw/pull/13423)  from @makortel: Remove remaining PixelCPEGeneric customizations for phase1 `simulation`  created: 2016-02-22T10:48:12Z merged: 2016-02-24T18:30:35Z

1. [13419](http://github.com/cms-sw/cmssw/pull/13419)  from @IHEP-CMS: Adding 1D Flightdistance tagging variables from cmssw 8_0_0_pre6 `comparison`  `reconstruction`  created: 2016-02-22T00:12:14Z merged: 2016-02-27T18:22:21Z

1. [13410](http://github.com/cms-sw/cmssw/pull/13410)  from @bsunanda: bsunanda:Phase2-hgx01 Remove a few bugs in HGC code and add example for TB `geometry`  created: 2016-02-19T16:28:19Z merged: 2016-02-21T15:46:51Z

1. [13408](http://github.com/cms-sw/cmssw/pull/13408)  from @VinInn: fix non const static and obsolete avx code `reconstruction`  created: 2016-02-19T14:00:51Z merged: 2016-02-21T15:46:06Z

1. [13400](http://github.com/cms-sw/cmssw/pull/13400)  from @cmsdqm: migrate to consumes `dqm`  `l1`  `pdmv`  created: 2016-02-18T20:36:03Z merged: 2016-02-24T09:37:42Z

1. [13386](http://github.com/cms-sw/cmssw/pull/13386)  from @VinInn: Code cleanup, debug improvements, bug fixes in Tracking code `alca`  `db`  `reconstruction`  created: 2016-02-18T10:18:16Z merged: 2016-02-27T07:26:26Z

1. [13385](http://github.com/cms-sw/cmssw/pull/13385)  from @heppye: add DQM Validation plots for MSSM Hbb Trigger Paths `dqm`  created: 2016-02-18T10:18:02Z merged: 2016-02-23T10:00:06Z

1. [13383](http://github.com/cms-sw/cmssw/pull/13383)  from @makortel: Add eras to select tracking configuration for 2017 detector `operations`  created: 2016-02-18T10:13:45Z merged: 2016-02-23T10:00:44Z

1. [13372](http://github.com/cms-sw/cmssw/pull/13372)  from @cms-met: MET PAT tool update + update of MET significance `analysis`  `reconstruction`  created: 2016-02-18T10:06:23Z merged: 2016-03-10T09:56:26Z

1. [13370](http://github.com/cms-sw/cmssw/pull/13370)  from @diguida: Further cleanup of Condition access in AlCaDB, online DQM, Geometry, HLT, Simulation, and standard configuration `alca`  `db`  `dqm`  `geometry`  `hlt`  `operations`  `simulation`  created: 2016-02-18T10:05:50Z merged: 2016-03-10T10:05:26Z

1. [13368](http://github.com/cms-sw/cmssw/pull/13368)  from @suchandradutta: Porting Phase2Tracker Digitizer from 62X_SLHC release. Updated also T `geometry`  `simulation`  created: 2016-02-18T10:05:17Z merged: 2016-03-03T09:45:01Z

1. [13365](http://github.com/cms-sw/cmssw/pull/13365)  from @lveldere: FastSim : HLT SUSYBSM validation : remove dependence on non-existing collection 'conversions' `dqm`  created: 2016-02-18T10:04:29Z merged: 2016-02-23T10:04:46Z

1. [13362](http://github.com/cms-sw/cmssw/pull/13362)  from @bsunanda: bsunanda:Run2-alca34 Update Pythia Isolated Track Filter `generators`  `reconstruction`  created: 2016-02-18T10:03:40Z merged: 2016-02-19T10:35:09Z

1. [13360](http://github.com/cms-sw/cmssw/pull/13360)  from @gpasztor: HLTElectronMuonInvMassFilter update `comparison`  `hlt`  created: 2016-02-18T10:03:08Z merged: 2016-02-19T10:32:07Z

1. [13358](http://github.com/cms-sw/cmssw/pull/13358)  from @mbandrews: ECALbyLumi+Timing `dqm`  created: 2016-02-18T10:02:36Z merged: 2016-03-08T18:24:24Z

1. [13357](http://github.com/cms-sw/cmssw/pull/13357)  from @dkotlins: Phase1 customs `db`  `geometry`  `simulation`  created: 2016-02-18T10:02:20Z merged: 2016-03-02T16:35:45Z

1. [13350](http://github.com/cms-sw/cmssw/pull/13350)  from @makortel: Fix NavigationSchoolAnalyzer for "ByGeom" `comparison`  `reconstruction`  created: 2016-02-18T10:00:27Z merged: 2016-02-19T10:33:03Z

1. [13348](http://github.com/cms-sw/cmssw/pull/13348)  from @makortel: Add GsfTracks to tracking validation `dqm`  `reconstruction`  `simulation`  created: 2016-02-18T09:59:55Z merged: 2016-03-02T11:07:11Z

1. [13346](http://github.com/cms-sw/cmssw/pull/13346)  from @bsunanda: bsunanda:Run2-hcx68 Add xml files for BH (HGCal) `geometry`  created: 2016-02-18T09:59:22Z merged: 2016-02-21T15:47:47Z

1. [13344](http://github.com/cms-sw/cmssw/pull/13344)  from @kpedro88: SIM/DIGI/RECO changes for HF QIE10 (part B) `alca`  `operations`  `reconstruction`  `simulation`  created: 2016-02-18T09:58:50Z merged: 2016-02-26T16:06:42Z

1. [13341](http://github.com/cms-sw/cmssw/pull/13341)  from @cms-l1t-offline: L1t hlt wseeds presc mask 80x `comparison`  `hlt`  created: 2016-02-18T09:58:01Z merged: 2016-02-19T10:34:03Z

#### CMSDIST Changes between Tags REL/CMSSW_8_0_2/slc6_amd64_gcc530 and REL/CMSSW_8_1_0_pre1/slc6_amd64_gcc530:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_8_0_2/slc6_amd64_gcc530...REL/CMSSW_8_1_0_pre1/slc6_amd64_gcc530)



1. [2187](http://github.com/cms-sw/cmssw/pull/2187)  from @smuzaffar: updated root from 81x next branch created: 2014-01-27T21:38:58Z merged: None

1. [2180](http://github.com/cms-sw/cmssw/pull/2180)  from @degano: Advance data for Fireworks/Geometry. created: 2014-01-27T15:23:34Z merged: 2014-01-29T11:00:14Z

1. [2176](http://github.com/cms-sw/cmssw/pull/2176)  from @degano: Advance data for L1Trigger/L1TGlobal. created: 2014-01-27T10:10:09Z merged: None

1. [2174](http://github.com/cms-sw/cmssw/pull/2174)  from @degano: Update frontier client to 2.8.18. created: 2014-01-26T13:54:10Z merged: 2014-01-27T00:53:02Z

1. [2171](http://github.com/cms-sw/cmssw/pull/2171)  from @degano: Update python to 2.7.11 created: 2014-01-24T22:00:16Z merged: None

1. [2170](http://github.com/cms-sw/cmssw/pull/2170)  from @degano: Add external generator Starlight. created: 2014-01-24T18:53:05Z merged: 2014-01-25T11:32:59Z

1. [2169](http://github.com/cms-sw/cmssw/pull/2169)  from @degano: Upgrade Froniter client to 2.8.16 and pacparser to 1.3.5. created: 2014-01-24T18:45:48Z merged: 2014-01-24T19:03:46Z

1. [2168](http://github.com/cms-sw/cmssw/pull/2168)  from @degano: Update xrootd to 4.2.3.

1. [2166](http://github.com/cms-sw/cmssw/pull/2166)  from @degano: Advance data for RecoJets/JetProducers. created: 2014-01-24T16:41:26Z merged: 2014-01-27T13:48:36Z

1. [2159](http://github.com/cms-sw/cmssw/pull/2159)  from @TaiSakuma: update pandas version to 0.17.1 for 8_1_X created: 2014-01-24T11:32:33Z merged: 2014-01-24T12:43:52Z

1. [2158](http://github.com/cms-sw/cmssw/pull/2158)  from @degano: Advance data for FastSimulation/TrackingRecHitProducer. created: 2014-01-24T11:18:58Z merged: 2014-01-24T14:30:39Z

1. [2152](http://github.com/cms-sw/cmssw/pull/2152)  from @davidlt: cmsos.file: add a proper shebang created: 2014-01-23T17:52:48Z merged: None
