---
layout: post
title:  "9_4_0_pre3"
date:   2017-11-01 14:35:22 +0100
categories: cmssw
relmajor: 9
relminor: 4
relsubminor: 0
relpre: _pre3
---

# CMSSW_9_4_0_pre3
#### Changes since CMSSW_9_4_0_pre2:
[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_9_4_0_pre2...CMSSW_9_4_0_pre3)



1. [20993](http://github.com/cms-sw/cmssw/pull/20993){:target="_blank"}  from **@davidlange6**: remove plugins from lib `dqm`  created: 2017-10-23T17:01:13Z merged: 2017-10-23T17:04:44Z

1. [20992](http://github.com/cms-sw/cmssw/pull/20992){:target="_blank"}  from **@davidlange6**: protect against non-stage2 eras in DigiToRawDM `operations`  created: 2017-10-23T15:03:12Z merged: 2017-10-24T05:51:25Z

1. [20991](http://github.com/cms-sw/cmssw/pull/20991){:target="_blank"}  from **@davidlange6**: Add needed changes to L1 digi to raw for premixing `operations`  created: 2017-10-23T09:12:30Z merged: 2017-10-23T09:13:07Z

1. [20981](http://github.com/cms-sw/cmssw/pull/20981){:target="_blank"}  from **@rappoccio**: Adding "else" clause to jet tokens `reconstruction`  created: 2017-10-20T16:16:49Z merged: 2017-10-23T15:30:51Z

1. [20975](http://github.com/cms-sw/cmssw/pull/20975){:target="_blank"}  from **@alberto-sanchez**: converting filters to global `generators`  created: 2017-10-19T18:44:37Z merged: 2017-10-23T15:31:05Z

1. [20968](http://github.com/cms-sw/cmssw/pull/20968){:target="_blank"}  from **@perrotta**: Solve an issue spot by the Static Analyzer in PixelCPETemplateReco.cc `reconstruction`  created: 2017-10-18T22:01:34Z merged: 2017-10-19T14:12:36Z

1. [20965](http://github.com/cms-sw/cmssw/pull/20965){:target="_blank"}  from **@capalmer85**: add smeared, projected PU for 2017 data `comparison`  `operations`  `simulation`  created: 2017-10-18T16:07:23Z merged: 2017-10-21T17:25:24Z

1. [20957](http://github.com/cms-sw/cmssw/pull/20957){:target="_blank"}  from **@rekovic**: Revert "Revert "[94X] L1 no hack conditions - cleaned"" `alca`  `core`  `dqm`  `l1`  `operations`  created: 2017-10-18T12:55:37Z merged: 2017-10-20T18:51:53Z

1. [20956](http://github.com/cms-sw/cmssw/pull/20956){:target="_blank"}  from **@hroskes**: Fix compiling PlotAlignmentValidation `alca`  created: 2017-10-18T12:20:04Z merged: 2017-10-23T15:38:00Z

1. [20954](http://github.com/cms-sw/cmssw/pull/20954){:target="_blank"}  from **@fabozzi**: fixing statistics of 2017 QCD flat_pT relval `pdmv`  `upgrade`  created: 2017-10-18T10:29:01Z merged: 2017-10-19T09:19:12Z

1. [20953](http://github.com/cms-sw/cmssw/pull/20953){:target="_blank"}  from **@slehti**: HLTTauDQM: updated t&p probe single muon trigger for mu+tau40 monitoring `dqm`  created: 2017-10-18T10:24:55Z merged: 2017-10-19T09:26:04Z

1. [20952](http://github.com/cms-sw/cmssw/pull/20952){:target="_blank"}  from **@efeyazgan**: Update GenXSecAnalyzer.cc `generators`  created: 2017-10-18T09:18:09Z merged: 2017-10-19T09:19:51Z

1. [20951](http://github.com/cms-sw/cmssw/pull/20951){:target="_blank"}  from **@ashtipliyski**: Add DQM event by event comparison plots summarising CALOL2 outputs and uGT inputs `dqm`  created: 2017-10-18T09:06:36Z merged: 2017-10-19T09:23:46Z

1. [20949](http://github.com/cms-sw/cmssw/pull/20949){:target="_blank"}  from **@slava77**: disable ecorr computations in phase-2 because they are too slow for high-PU `analysis`  `reconstruction`  `upgrade`  created: 2017-10-18T05:48:42Z merged: 2017-10-19T09:24:00Z

1. [20944](http://github.com/cms-sw/cmssw/pull/20944){:target="_blank"}  from **@thomreis**: L1T RegionalMuonCand constructor upgrade `l1`  created: 2017-10-17T14:40:48Z merged: 2017-10-18T07:10:48Z

1. [20943](http://github.com/cms-sw/cmssw/pull/20943){:target="_blank"}  from **@jfernan2**: Extended DT DQM selection for HI runs `dqm`  created: 2017-10-17T14:17:47Z merged: 2017-10-18T18:34:20Z

1. [20942](http://github.com/cms-sw/cmssw/pull/20942){:target="_blank"}  from **@crovelli**: ECAL containment in simulation update `simulation`  created: 2017-10-17T14:07:01Z merged: 2017-10-18T18:34:34Z

1. [20941](http://github.com/cms-sw/cmssw/pull/20941){:target="_blank"}  from **@Dr15Jones**: Add TotalLoopTime to framework job report `core`  created: 2017-10-17T14:03:27Z merged: 2017-10-18T07:10:05Z

1. [20938](http://github.com/cms-sw/cmssw/pull/20938){:target="_blank"}  from **@VinInn**: Introducing "Inactive" inner/outer hits... `alca`  `analysis`  `dqm`  `hlt`  `pdmv`  `reconstruction`  `visualization`  created: 2017-10-17T10:17:27Z merged: 2017-10-21T17:13:15Z

after introduction of inactive hits to inner and outer parts of the HitPattern, the HitPattern interface was updated, including removal of an existing [now ambiguous] method in order to avoid incorrect result. See PR description for details.



1. [20935](http://github.com/cms-sw/cmssw/pull/20935){:target="_blank"}  from **@thomreis**: L1T online DQM - set efficiency flags `dqm`  created: 2017-10-17T08:42:53Z merged: 2017-10-19T09:24:12Z

1. [20928](http://github.com/cms-sw/cmssw/pull/20928){:target="_blank"}  from **@bsunanda**: Run2-alca101 Make the codes and macros updated with the current versions used for calibration `alca`  created: 2017-10-16T14:16:02Z merged: 2017-10-24T05:53:26Z

1. [20926](http://github.com/cms-sw/cmssw/pull/20926){:target="_blank"}  from **@thomreis**: L1T online DQM uGMT zero suppression plot axis range change `dqm`  created: 2017-10-16T11:07:08Z merged: 2017-10-18T09:04:20Z

1. [20925](http://github.com/cms-sw/cmssw/pull/20925){:target="_blank"}  from **@natalia-korneeva**: Moving to Clopper-Pearson uncertainties in efficiency histograms `dqm`  created: 2017-10-16T10:02:06Z merged: 2017-10-18T09:03:45Z

1. [20923](http://github.com/cms-sw/cmssw/pull/20923){:target="_blank"}  from **@thomreis**: L1TOffline DQM - add efficiency flag to efficiency ME `dqm`  `l1`  created: 2017-10-16T07:48:40Z merged: 2017-10-18T09:04:00Z

1. [20922](http://github.com/cms-sw/cmssw/pull/20922){:target="_blank"}  from **@arunhep**: GT Updates with Pixel Local Reco conditions for V2 MC `alca`  created: 2017-10-16T06:16:31Z merged: 2017-10-18T07:09:53Z

1. [20921](http://github.com/cms-sw/cmssw/pull/20921){:target="_blank"}  from **@cms-sw**: Revert "[94X] L1 no hack conditions - cleaned" `comparison`  `core`  `dqm`  `l1`  `operations`  created: 2017-10-14T19:25:09Z merged: 2017-10-15T07:14:07Z

1. [20919](http://github.com/cms-sw/cmssw/pull/20919){:target="_blank"}  from **@dinardo**: Fixed HI tracking sequence `dqm`  created: 2017-10-13T20:58:42Z merged: 2017-10-18T18:36:41Z

1. [20914](http://github.com/cms-sw/cmssw/pull/20914){:target="_blank"}  from **@rekovic**: [94x] L1T Calo Layer1 packer unpacker `l1`  created: 2017-10-13T09:00:06Z merged: 2017-10-17T08:24:50Z

1. [20911](http://github.com/cms-sw/cmssw/pull/20911){:target="_blank"}  from **@lgray**: Fill time and uncertainties for slimmed primary vertices `analysis`  `reconstruction`  `upgrade`  created: 2017-10-12T23:24:27Z merged: 2017-10-19T10:07:06Z

1. [20908](http://github.com/cms-sw/cmssw/pull/20908){:target="_blank"}  from **@Dr15Jones**: Converted GenFilters to be edm::global modules `generators`  created: 2017-10-12T18:51:57Z merged: 2017-10-13T09:21:57Z

1. [20907](http://github.com/cms-sw/cmssw/pull/20907){:target="_blank"}  from **@mrodozov**: Add test for Theano `analysis`  created: 2017-10-12T16:45:17Z merged: 2017-10-13T10:16:34Z

1. [20906](http://github.com/cms-sw/cmssw/pull/20906){:target="_blank"}  from **@mrodozov**: Remove unused variables to fix warnings `analysis`  created: 2017-10-12T14:49:49Z merged: 2017-10-13T16:16:18Z

1. [20905](http://github.com/cms-sw/cmssw/pull/20905){:target="_blank"}  from **@arizzi**: NanoAOD: runTheMatrix and cmsDriver support `operations`  `pdmv`  `upgrade`  created: 2017-10-12T12:18:21Z merged: 2017-10-14T09:44:25Z

1. [20904](http://github.com/cms-sw/cmssw/pull/20904){:target="_blank"}  from **@ahinzmann**: Fix negative error cases `reconstruction`  created: 2017-10-12T11:37:36Z merged: 2017-10-19T06:40:00Z

1. [20903](http://github.com/cms-sw/cmssw/pull/20903){:target="_blank"}  from **@Sam-Harper**: adding good e/gamma flag to PackedCandidate for MiniAOD `analysis`  `reconstruction`  created: 2017-10-11T23:10:34Z merged: 2017-10-14T13:01:06Z

1. [20900](http://github.com/cms-sw/cmssw/pull/20900){:target="_blank"}  from **@cms-tau-pog**: increase of pT threshold for photons to be considered for tau reconstruction and ID `reconstruction`  created: 2017-10-11T19:43:55Z merged: 2017-10-17T07:07:16Z

1. [20899](http://github.com/cms-sw/cmssw/pull/20899){:target="_blank"}  from **@rvenditti**: Repair Zmu skim muon selector `pdmv`  created: 2017-10-11T19:28:01Z merged: 2017-10-11T19:32:35Z

1. [20898](http://github.com/cms-sw/cmssw/pull/20898){:target="_blank"}  from **@Michael-Krohn**: DQM for AK8 btag HLT  `dqm`  created: 2017-10-11T19:27:59Z merged: 2017-10-18T07:16:00Z

1. [20896](http://github.com/cms-sw/cmssw/pull/20896){:target="_blank"}  from **@slava77**: reduce max errors/warnings selected for LogError skim per kind to at most 1 per LS `core`  created: 2017-10-11T16:28:01Z merged: 2017-10-12T08:17:35Z

1. [20895](http://github.com/cms-sw/cmssw/pull/20895){:target="_blank"}  from **@Wilsker**: Aesthetic changes to off-track cluster histograms `dqm`  created: 2017-10-11T15:44:37Z merged: 2017-10-18T07:16:58Z

1. [20893](http://github.com/cms-sw/cmssw/pull/20893){:target="_blank"}  from **@bsunanda**: Run2-hcx158 Remove casting of some collections which was causing memory leaks `reconstruction`  created: 2017-10-11T13:56:08Z merged: 2017-10-12T14:46:26Z

1. [20891](http://github.com/cms-sw/cmssw/pull/20891){:target="_blank"}  from **@makortel**: Add fillDescriptions to MeasurementTrackerEventProducer `reconstruction`  created: 2017-10-11T10:19:45Z merged: 2017-10-13T09:23:06Z

1. [20887](http://github.com/cms-sw/cmssw/pull/20887){:target="_blank"}  from **@gpetruc**: Support Comp2RefEqualH DQM quality test also on TProfile `dqm`  created: 2017-10-10T21:12:26Z merged: 2017-10-18T07:09:32Z

1. [20885](http://github.com/cms-sw/cmssw/pull/20885){:target="_blank"}  from **@Dr15Jones**: TableExaminer usage `core`  created: 2017-10-10T20:45:25Z merged: 2017-10-11T07:39:12Z

1. [20883](http://github.com/cms-sw/cmssw/pull/20883){:target="_blank"}  from **@wddgit**: Bug fix. Add 2 overrides to LHESource `core`  `generators`  created: 2017-10-10T19:52:51Z merged: 2017-10-13T09:23:19Z

1. [20878](http://github.com/cms-sw/cmssw/pull/20878){:target="_blank"}  from **@gpetruc**: introduce semi-deterministic smearing for e/gamma objects `analysis`  created: 2017-10-10T14:36:30Z merged: 2017-10-12T13:54:15Z

1. [20876](http://github.com/cms-sw/cmssw/pull/20876){:target="_blank"}  from **@mrodozov**: Fix unused vars warnings in Reco pkgs `reconstruction`  created: 2017-10-10T13:02:21Z merged: 2017-10-11T19:37:11Z

1. [20875](http://github.com/cms-sw/cmssw/pull/20875){:target="_blank"}  from **@mrodozov**: Fix DataFormats/HeavyIonEvent pkg comp warnings after clang-tidy `reconstruction`  created: 2017-10-10T12:39:02Z merged: 2017-10-11T07:37:59Z

1. [20874](http://github.com/cms-sw/cmssw/pull/20874){:target="_blank"}  from **@mrodozov**: Fix Fireworks/* pkgs comp warnings after clang-tidy `visualization`  created: 2017-10-10T12:30:29Z merged: 2017-10-11T07:38:12Z

1. [20872](http://github.com/cms-sw/cmssw/pull/20872){:target="_blank"}  from **@cms-tsg-storm**: HLT V4.0 Mercury (94X) `core`  `hlt`  created: 2017-10-10T09:21:54Z merged: 2017-10-20T07:55:40Z

1. [20871](http://github.com/cms-sw/cmssw/pull/20871){:target="_blank"}  from **@rekovic**: [94X] L1 no hack conditions - cleaned `core`  `dqm`  `l1`  `operations`  created: 2017-10-10T07:55:18Z merged: 2017-10-11T07:50:18Z

1. [20870](http://github.com/cms-sw/cmssw/pull/20870){:target="_blank"}  from **@DryRun**: HCALDQM: fix castorDigis.InputLabel for heavy ion run type `dqm`  created: 2017-10-10T04:02:44Z merged: 2017-10-11T07:51:01Z

1. [20869](http://github.com/cms-sw/cmssw/pull/20869){:target="_blank"}  from **@bcmcms**: Hcal rel val update9 xy v2 `dqm`  created: 2017-10-09T22:32:24Z merged: 2017-10-19T10:02:19Z

1. [20868](http://github.com/cms-sw/cmssw/pull/20868){:target="_blank"}  from **@bsunanda**: Run2-hcx157 Update getGeometry method for HcalGeometry to enable standard access `geometry`  created: 2017-10-09T20:32:36Z merged: 2017-10-16T11:19:16Z

1. [20865](http://github.com/cms-sw/cmssw/pull/20865){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for EgammaAnalysis `analysis`  created: 2017-10-09T16:27:52Z merged: 2017-10-10T06:22:52Z

1. [20864](http://github.com/cms-sw/cmssw/pull/20864){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for ElectroWeakAnalysis `analysis`  created: 2017-10-09T16:27:51Z merged: 2017-10-10T06:23:04Z

1. [20861](http://github.com/cms-sw/cmssw/pull/20861){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for Fireworks `visualization`  created: 2017-10-09T16:26:29Z merged: 2017-10-09T18:35:56Z

1. [20860](http://github.com/cms-sw/cmssw/pull/20860){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for HLTrigger `hlt`  created: 2017-10-09T16:26:28Z merged: 2017-10-10T06:23:23Z

1. [20859](http://github.com/cms-sw/cmssw/pull/20859){:target="_blank"}  from **@rekovic**: [94x] L1T OMTF introduce packer, unpacker, config DQM `dqm`  `l1`  created: 2017-10-09T15:38:09Z merged: 2017-10-21T17:09:00Z

1. [20858](http://github.com/cms-sw/cmssw/pull/20858){:target="_blank"}  from **@perrotta**: Get rid of unused variables in reco particle flow pf tracking `reconstruction`  created: 2017-10-09T15:02:55Z merged: 2017-10-12T15:17:36Z

1. [20857](http://github.com/cms-sw/cmssw/pull/20857){:target="_blank"}  from **@mrodozov**: Fix build errors and comp warnings in L1Trigger/L1TMuonEndCap `l1`  created: 2017-10-09T14:42:34Z merged: 2017-10-10T06:26:17Z

1. [20854](http://github.com/cms-sw/cmssw/pull/20854){:target="_blank"}  from **@mrodozov**: Fix comp warngns in Alignment/CocoaDaq-CocoaFit `alca`  created: 2017-10-09T12:41:03Z merged: 2017-10-10T09:08:11Z

1. [20853](http://github.com/cms-sw/cmssw/pull/20853){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for FastSimulation `fastsim`  created: 2017-10-09T12:28:48Z merged: 2017-10-09T19:07:02Z

1. [20852](http://github.com/cms-sw/cmssw/pull/20852){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for FastSimDataFormats `fastsim`  created: 2017-10-09T12:28:47Z merged: 2017-10-09T19:59:32Z

1. [20851](http://github.com/cms-sw/cmssw/pull/20851){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for EventFilter `daq`  `l1`  `reconstruction`  created: 2017-10-09T12:28:45Z merged: 2017-10-10T06:26:31Z

1. [20850](http://github.com/cms-sw/cmssw/pull/20850){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoPixelVertexing `reconstruction`  created: 2017-10-09T12:28:44Z merged: 2017-10-10T06:26:43Z

1. [20849](http://github.com/cms-sw/cmssw/pull/20849){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoParticleFlow `reconstruction`  created: 2017-10-09T12:28:43Z merged: 2017-10-09T19:59:07Z

1. [20848](http://github.com/cms-sw/cmssw/pull/20848){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoMuon `hlt`  `reconstruction`  created: 2017-10-09T12:28:43Z merged: 2017-10-10T06:27:03Z

1. [20847](http://github.com/cms-sw/cmssw/pull/20847){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoMET `analysis`  `reconstruction`  created: 2017-10-09T12:28:42Z merged: 2017-10-09T18:36:13Z

1. [20846](http://github.com/cms-sw/cmssw/pull/20846){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoLuminosity `reconstruction`  created: 2017-10-09T12:28:41Z merged: 2017-10-09T19:05:40Z

1. [20845](http://github.com/cms-sw/cmssw/pull/20845){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoLocalTracker `reconstruction`  `upgrade`  created: 2017-10-09T12:28:40Z merged: 2017-10-09T20:28:10Z

1. [20844](http://github.com/cms-sw/cmssw/pull/20844){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoLocalMuon `reconstruction`  `upgrade`  created: 2017-10-09T12:28:39Z merged: 2017-10-10T06:27:17Z

1. [20843](http://github.com/cms-sw/cmssw/pull/20843){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoLocalFastTime `reconstruction`  `upgrade`  created: 2017-10-09T12:28:38Z merged: 2017-10-09T19:59:19Z

1. [20842](http://github.com/cms-sw/cmssw/pull/20842){:target="_blank"}  from **@mrodozov**: Fix compilation warnings (ClassDef macro) `alca`  `core`  created: 2017-10-09T10:15:35Z merged: 2017-10-09T18:34:24Z

1. [20841](http://github.com/cms-sw/cmssw/pull/20841){:target="_blank"}  from **@mrodozov**: Fix multiple comp warnings for unused variables `alca`  `db`  `dqm`  `pdmv`  `reconstruction`  created: 2017-10-09T10:01:24Z merged: 2017-10-09T19:06:09Z

1. [20840](http://github.com/cms-sw/cmssw/pull/20840){:target="_blank"}  from **@arizzi**: MiniAOD: use all genParticles for patJets partonFlavour `analysis`  `reconstruction`  created: 2017-10-09T09:07:36Z merged: 2017-10-11T11:26:46Z

1. [20836](http://github.com/cms-sw/cmssw/pull/20836){:target="_blank"}  from **@davidlange6**: fix compilation error in IB ( l1 muon) `l1`  created: 2017-10-09T07:36:59Z merged: 2017-10-09T08:48:03Z

1. [20835](http://github.com/cms-sw/cmssw/pull/20835){:target="_blank"}  from **@wmtford**: Remove unnecessary find()s, commented couts; tidy `dqm`  created: 2017-10-09T02:35:20Z merged: 2017-10-11T07:37:47Z

1. [20834](http://github.com/cms-sw/cmssw/pull/20834){:target="_blank"}  from **@rekovic**: [94x] L1T BMTF introduce packer and small emulator fix `l1`  created: 2017-10-09T01:24:36Z merged: 2017-10-23T17:07:59Z

1. [20832](http://github.com/cms-sw/cmssw/pull/20832){:target="_blank"}  from **@rekovic**: [94x] L1T TwinMux `alca`  `db`  `l1`  `operations`  created: 2017-10-08T23:56:41Z merged: 2017-10-20T08:59:15Z

1. [20831](http://github.com/cms-sw/cmssw/pull/20831){:target="_blank"}  from **@stahlleiton**: OnlineDQM : Tune L1T Muon QTs v3 `dqm`  created: 2017-10-08T23:52:34Z merged: 2017-10-11T07:36:41Z

1. [20830](http://github.com/cms-sw/cmssw/pull/20830){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoLocalCalo `reconstruction`  `upgrade`  created: 2017-10-08T17:25:08Z merged: 2017-10-09T07:21:36Z

1. [20829](http://github.com/cms-sw/cmssw/pull/20829){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoJets `reconstruction`  created: 2017-10-08T17:25:07Z merged: 2017-10-09T07:21:18Z

1. [20828](http://github.com/cms-sw/cmssw/pull/20828){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoHI `reconstruction`  created: 2017-10-08T17:25:06Z merged: 2017-10-09T07:21:01Z

1. [20827](http://github.com/cms-sw/cmssw/pull/20827){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoEgamma `hlt`  `reconstruction`  created: 2017-10-08T17:25:05Z merged: 2017-10-09T07:20:46Z

1. [20826](http://github.com/cms-sw/cmssw/pull/20826){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoEcal `reconstruction`  created: 2017-10-08T17:25:04Z merged: 2017-10-09T07:20:23Z

1. [20825](http://github.com/cms-sw/cmssw/pull/20825){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoCTPPS `reconstruction`  created: 2017-10-08T17:25:03Z merged: 2017-10-09T07:20:09Z

1. [20824](http://github.com/cms-sw/cmssw/pull/20824){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoBTau `reconstruction`  created: 2017-10-08T17:25:02Z merged: 2017-10-09T07:19:55Z

1. [20822](http://github.com/cms-sw/cmssw/pull/20822){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for QCDAnalysis `analysis`  created: 2017-10-08T17:25:00Z merged: 2017-10-09T07:19:40Z

1. [20821](http://github.com/cms-sw/cmssw/pull/20821){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for MuonAnalysis `analysis`  created: 2017-10-08T11:33:15Z merged: 2017-10-09T07:19:26Z

1. [20820](http://github.com/cms-sw/cmssw/pull/20820){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for Mixing `simulation`  created: 2017-10-08T11:33:14Z merged: 2017-10-09T07:19:11Z

1. [20819](http://github.com/cms-sw/cmssw/pull/20819){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for MagneticField `reconstruction`  created: 2017-10-08T11:33:13Z merged: 2017-10-09T07:18:57Z

1. [20818](http://github.com/cms-sw/cmssw/pull/20818){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for L1TriggerOffline `l1`  created: 2017-10-08T11:33:13Z merged: 2017-10-09T07:18:43Z

1. [20814](http://github.com/cms-sw/cmssw/pull/20814){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for IgTools `analysis`  `core`  created: 2017-10-07T18:48:23Z merged: 2017-10-08T07:31:14Z

1. [20813](http://github.com/cms-sw/cmssw/pull/20813){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for IORawData `alca`  `analysis`  created: 2017-10-07T18:48:22Z merged: 2017-10-08T07:30:56Z

1. [20812](http://github.com/cms-sw/cmssw/pull/20812){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for IOPool `analysis`  `core`  created: 2017-10-07T18:48:21Z merged: 2017-10-08T07:30:36Z

1. [20811](http://github.com/cms-sw/cmssw/pull/20811){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for IOMC `analysis`  `core`  `generators`  `simulation`  created: 2017-10-07T18:48:20Z merged: 2017-10-08T07:30:15Z

1. [20810](http://github.com/cms-sw/cmssw/pull/20810){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for HiggsAnalysis `analysis`  created: 2017-10-07T18:48:19Z merged: 2017-10-08T07:29:54Z

1. [20808](http://github.com/cms-sw/cmssw/pull/20808){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for HLTriggerOffline `analysis`  `dqm`  created: 2017-10-07T18:48:17Z merged: 2017-10-08T07:29:34Z

1. [20807](http://github.com/cms-sw/cmssw/pull/20807){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoVertex `alca`  `reconstruction`  created: 2017-10-07T17:23:50Z merged: 2017-10-08T07:29:07Z

1. [20806](http://github.com/cms-sw/cmssw/pull/20806){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoVZero `reconstruction`  created: 2017-10-07T17:23:49Z merged: 2017-10-08T07:28:44Z

1. [20805](http://github.com/cms-sw/cmssw/pull/20805){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoTracker `reconstruction`  created: 2017-10-07T17:23:48Z merged: 2017-10-08T07:28:30Z

1. [20804](http://github.com/cms-sw/cmssw/pull/20804){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoTauTag `hlt`  `reconstruction`  created: 2017-10-07T17:23:47Z merged: 2017-10-08T07:27:49Z

1. [20803](http://github.com/cms-sw/cmssw/pull/20803){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoTBCalo `reconstruction`  created: 2017-10-07T17:23:46Z merged: 2017-10-08T07:27:04Z

1. [20802](http://github.com/cms-sw/cmssw/pull/20802){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for RecoRomanPot `reconstruction`  created: 2017-10-07T17:23:45Z merged: 2017-10-08T07:26:49Z

1. [20800](http://github.com/cms-sw/cmssw/pull/20800){:target="_blank"}  from **@davidlange6**: fix directory comparison in relmon tool `reconstruction`  created: 2017-10-07T15:29:23Z merged: 2017-10-07T18:42:51Z

1. [20799](http://github.com/cms-sw/cmssw/pull/20799){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for SUSYBSMAnalysis `analysis`  created: 2017-10-07T14:50:07Z merged: 2017-10-08T07:26:35Z

1. [20798](http://github.com/cms-sw/cmssw/pull/20798){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for TBDataFormats `analysis`  created: 2017-10-07T14:50:06Z merged: 2017-10-08T18:30:56Z

1. [20797](http://github.com/cms-sw/cmssw/pull/20797){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for SimTransport `simulation`  created: 2017-10-07T14:50:05Z merged: 2017-10-07T20:33:09Z

1. [20795](http://github.com/cms-sw/cmssw/pull/20795){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for Utilities `core`  created: 2017-10-07T12:12:24Z merged: 2017-10-07T17:17:38Z

1. [20793](http://github.com/cms-sw/cmssw/pull/20793){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for TrackingTools `reconstruction`  created: 2017-10-07T12:12:22Z merged: 2017-10-08T18:31:53Z

1. [20792](http://github.com/cms-sw/cmssw/pull/20792){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for TrackPropagation `reconstruction`  `simulation`  created: 2017-10-07T12:12:21Z merged: 2017-10-07T17:18:09Z

1. [20791](http://github.com/cms-sw/cmssw/pull/20791){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for TopQuarkAnalysis `analysis`  created: 2017-10-07T12:12:20Z merged: 2017-10-07T17:18:53Z

1. [20790](http://github.com/cms-sw/cmssw/pull/20790){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for TauAnalysis `analysis`  `simulation`  created: 2017-10-07T12:12:19Z merged: 2017-10-07T17:18:29Z

1. [20789](http://github.com/cms-sw/cmssw/pull/20789){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for DataFormats `alca`  `analysis`  `core`  `daq`  `generators`  `hlt`  `l1`  `reconstruction`  `simulation`  `upgrade`  created: 2017-10-07T08:01:35Z merged: 2017-10-09T12:41:02Z

1. [20788](http://github.com/cms-sw/cmssw/pull/20788){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for DQMServices `dqm`  created: 2017-10-07T08:01:34Z merged: 2017-10-07T13:03:11Z

1. [20787](http://github.com/cms-sw/cmssw/pull/20787){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for DQMOffline `dqm`  `l1`  created: 2017-10-07T08:01:33Z merged: 2017-10-07T16:02:09Z

1. [20786](http://github.com/cms-sw/cmssw/pull/20786){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for DQM `dqm`  `hlt`  created: 2017-10-07T08:01:32Z merged: 2017-10-07T13:35:45Z

1. [20785](http://github.com/cms-sw/cmssw/pull/20785){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for DPGAnalysis `analysis`  `pdmv`  created: 2017-10-07T08:01:31Z merged: 2017-10-07T13:35:07Z

1. [20784](http://github.com/cms-sw/cmssw/pull/20784){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for Configuration `pdmv`  created: 2017-10-07T08:01:30Z merged: 2017-10-07T13:02:29Z

1. [20783](http://github.com/cms-sw/cmssw/pull/20783){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for CondTools `alca`  `db`  `dqm`  `hlt`  `l1`  created: 2017-10-07T08:01:29Z merged: 2017-10-07T13:30:39Z

1. [20782](http://github.com/cms-sw/cmssw/pull/20782){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for CondFormats `alca`  `analysis`  `db`  `l1`  created: 2017-10-07T08:01:28Z merged: 2017-10-07T16:01:48Z

1. [20781](http://github.com/cms-sw/cmssw/pull/20781){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for CondCore `alca`  `db`  created: 2017-10-07T08:01:27Z merged: 2017-10-07T13:02:03Z

1. [20780](http://github.com/cms-sw/cmssw/pull/20780){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for CommonTools `analysis`  `reconstruction`  created: 2017-10-07T08:01:27Z merged: 2017-10-07T16:01:29Z

1. [20779](http://github.com/cms-sw/cmssw/pull/20779){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for CaloOnlineTools `alca`  `db`  created: 2017-10-07T08:01:26Z merged: 2017-10-07T13:01:50Z

1. [20778](http://github.com/cms-sw/cmssw/pull/20778){:target="_blank"}  from **@davidlange6**: Clang-tidy checks for Calibration `alca`  created: 2017-10-07T08:01:25Z merged: 2017-10-07T13:00:51Z

1. [20777](http://github.com/cms-sw/cmssw/pull/20777){:target="_blank"}  from **@heller3**: Adjust jet eta threshold for offline HT calculation in SUSY Lep+HT trigger DQM module `dqm`  created: 2017-10-06T23:40:21Z merged: 2017-10-10T14:32:33Z

1. [20776](http://github.com/cms-sw/cmssw/pull/20776){:target="_blank"}  from **@bsunanda**: Run2-alca100 Update IsoTrack calibration system to deal with only L1 trigger (no HLT) `alca`  created: 2017-10-06T21:09:50Z merged: 2017-10-16T10:59:27Z

1. [20775](http://github.com/cms-sw/cmssw/pull/20775){:target="_blank"}  from **@jkarancs**: 94X Update phase1 pixel thresholds `simulation`  created: 2017-10-06T16:18:01Z merged: 2017-10-09T18:34:09Z

1. [20774](http://github.com/cms-sw/cmssw/pull/20774){:target="_blank"}  from **@gartung**: FWCore/ParameterSet: Replace Exception in MassSearchReplaceAnyInputTagVisitor.enter() `core`  created: 2017-10-06T15:52:01Z merged: 2017-10-07T13:04:58Z

1. [20773](http://github.com/cms-sw/cmssw/pull/20773){:target="_blank"}  from **@drkovalskyi**: Muon simhit matching `analysis`  `operations`  `pdmv`  `reconstruction`  `simulation`  `upgrade`  created: 2017-10-06T13:55:29Z merged: 2017-10-24T06:29:01Z

1. [20771](http://github.com/cms-sw/cmssw/pull/20771){:target="_blank"}  from **@Sam-Harper**: Disabling high pt trained regression except for saturated E/gammas `reconstruction`  created: 2017-10-06T13:11:45Z merged: 2017-10-13T16:16:31Z

1. [20769](http://github.com/cms-sw/cmssw/pull/20769){:target="_blank"}  from **@mrodozov**: Fix compilation warnings in CalibCalorimetry pkg `alca`  created: 2017-10-06T12:30:36Z merged: 2017-10-07T08:05:59Z

1. [20767](http://github.com/cms-sw/cmssw/pull/20767){:target="_blank"}  from @mtosi: fix TRKDQM **@HLT** `dqm`  `hlt`  created: 2017-10-06T12:00:49Z merged: 2017-10-12T13:54:39Z

1. [20764](http://github.com/cms-sw/cmssw/pull/20764){:target="_blank"}  from **@davidlange6**: remove some divide by 0s and extend blacklist of histograms `dqm`  `reconstruction`  created: 2017-10-06T09:00:12Z merged: 2017-10-06T13:58:33Z

1. [20763](http://github.com/cms-sw/cmssw/pull/20763){:target="_blank"}  from **@smuzaffar**: use ClassDefOverride instead of ClassDef to avoid inconsistent-missing-override warning `core`  created: 2017-10-06T05:14:57Z merged: 2017-10-08T18:34:16Z

1. [20762](http://github.com/cms-sw/cmssw/pull/20762){:target="_blank"}  from **@cms-sw**: Alignment/CocoaFit: use ClassDefOverride to avoid inconsistent-missing-override warning `alca`  created: 2017-10-06T05:05:17Z merged: 2017-10-06T10:46:24Z

1. [20761](http://github.com/cms-sw/cmssw/pull/20761){:target="_blank"}  from **@cms-sw**: Alignment: use ClassDefOverride instead of ClassDef to avoid inconsistent-missing-override warning `alca`  created: 2017-10-06T05:01:47Z merged: 2017-10-06T12:45:44Z

1. [20759](http://github.com/cms-sw/cmssw/pull/20759){:target="_blank"}  from **@bsunanda**: Run2-hcx156 Fix bugs for first layer; active length computation `geometry`  created: 2017-10-05T20:43:52Z merged: 2017-10-11T07:31:07Z

1. [20758](http://github.com/cms-sw/cmssw/pull/20758){:target="_blank"}  from **@arunhep**: GT Updates with inclusion of RPCLink Maps for L1T, HCAL Pedestals and widths, StripBadChannel for MCV2 `alca`  created: 2017-10-05T20:25:20Z merged: 2017-10-11T07:53:35Z

1. [20757](http://github.com/cms-sw/cmssw/pull/20757){:target="_blank"}  from **@davidlange6**: clang-tidy checks for CalibTracker subsystem `alca`  created: 2017-10-05T15:42:20Z merged: 2017-10-06T07:28:22Z

1. [20756](http://github.com/cms-sw/cmssw/pull/20756){:target="_blank"}  from **@davidlange6**: clang checks for CalibMuon subsystem `alca`  created: 2017-10-05T15:42:08Z merged: 2017-10-06T07:38:48Z

1. [20755](http://github.com/cms-sw/cmssw/pull/20755){:target="_blank"}  from **@davidlange6**: clang-tidy checks for CalibCalorimetry subsystem `alca`  `l1`  created: 2017-10-05T14:32:33Z merged: 2017-10-06T07:38:34Z

1. [20754](http://github.com/cms-sw/cmssw/pull/20754){:target="_blank"}  from **@davidlange6**: clang check CalibFormats `alca`  created: 2017-10-05T14:31:59Z merged: 2017-10-06T07:29:13Z

1. [20753](http://github.com/cms-sw/cmssw/pull/20753){:target="_blank"}  from **@davidlange6**: clang-tidy checks for Alignment subsystem `alca`  created: 2017-10-05T13:54:13Z merged: 2017-10-05T20:23:16Z

1. [20752](http://github.com/cms-sw/cmssw/pull/20752){:target="_blank"}  from **@davidlange6**: clang-tidy checks for AnalysisDataFormats subsystem `analysis`  created: 2017-10-05T13:54:04Z merged: 2017-10-05T19:42:52Z

1. [20751](http://github.com/cms-sw/cmssw/pull/20751){:target="_blank"}  from **@davidlange6**: clang-tidy checks for AnalysisAlgos subsystem `analysis`  created: 2017-10-05T13:53:20Z merged: 2017-10-05T19:42:32Z

1. [20750](http://github.com/cms-sw/cmssw/pull/20750){:target="_blank"}  from **@davidlange6**: clang-tidy check for FWCore `core`  created: 2017-10-05T12:51:16Z merged: 2017-10-05T19:42:20Z

1. [20749](http://github.com/cms-sw/cmssw/pull/20749){:target="_blank"}  from **@mandrenguyen**: XeXe collision era and relval workflow `alca`  `analysis`  `dqm`  `generators`  `operations`  `pdmv`  `reconstruction`  `simulation`  `upgrade`  created: 2017-10-05T12:20:28Z merged: 2017-10-09T07:42:00Z

1. [20748](http://github.com/cms-sw/cmssw/pull/20748){:target="_blank"}  from **@mrodozov**: Fix comp warnings from DataFormats HcalDigi `simulation`  created: 2017-10-05T09:11:58Z merged: 2017-10-05T19:43:49Z

1. [20747](http://github.com/cms-sw/cmssw/pull/20747){:target="_blank"}  from **@alberto-sanchez**: updating relval which uses evtgen `generators`  created: 2017-10-04T17:30:38Z merged: 2017-10-10T09:48:26Z

1. [20743](http://github.com/cms-sw/cmssw/pull/20743){:target="_blank"}  from **@ashtipliyski**: Fix typo in handling exclusion of CALOL2 in online DQM `dqm`  created: 2017-10-04T15:31:32Z merged: 2017-10-07T13:38:14Z

1. [20742](http://github.com/cms-sw/cmssw/pull/20742){:target="_blank"}  from **@mrodozov**: Fix xerces xmlparser issue in aarch64 unique_ptr related sigsegv `geometry`  created: 2017-10-04T14:43:30Z merged: 2017-10-05T10:35:11Z

1. [20741](http://github.com/cms-sw/cmssw/pull/20741){:target="_blank"}  from **@ahinzmann**: Protect against missing track info in MiniAOD `reconstruction`  created: 2017-10-04T13:51:21Z merged: 2017-10-12T15:18:42Z

1. [20739](http://github.com/cms-sw/cmssw/pull/20739){:target="_blank"}  from **@cms-tsg-storm**: add HLTScouting event content `hlt`  created: 2017-10-04T13:10:54Z merged: 2017-10-23T15:42:58Z

1. [20736](http://github.com/cms-sw/cmssw/pull/20736){:target="_blank"}  from **@arunhep**: Update of wf1010.0 and run2_data_relval key `alca`  `pdmv`  `upgrade`  created: 2017-10-04T06:31:56Z merged: 2017-10-05T07:45:23Z

1. [20734](http://github.com/cms-sw/cmssw/pull/20734){:target="_blank"}  from **@alberto-sanchez**: fixing typo in tmp filename `generators`  created: 2017-10-03T23:20:50Z merged: 2017-10-05T07:45:58Z

1. [20733](http://github.com/cms-sw/cmssw/pull/20733){:target="_blank"}  from **@mkirsano**: Code to turn on VINCIA plugin version 2 `generators`  created: 2017-10-03T18:16:27Z merged: 2017-10-16T11:13:52Z

1. [20732](http://github.com/cms-sw/cmssw/pull/20732){:target="_blank"}  from **@jfernan2**: DTDQM change to monitor ZS data `dqm`  created: 2017-10-03T17:51:53Z merged: 2017-10-05T07:46:57Z

1. [20731](http://github.com/cms-sw/cmssw/pull/20731){:target="_blank"}  from **@lfinco**: New Hgg low-mass HLT path added to DQM  `dqm`  created: 2017-10-03T16:01:02Z merged: 2017-10-11T11:25:36Z

1. [20730](http://github.com/cms-sw/cmssw/pull/20730){:target="_blank"}  from **@Dr15Jones**: Work around inconsistency in ExternalLHEProducer `core`  `generators`  created: 2017-10-03T14:59:16Z merged: 2017-10-04T07:11:39Z

1. [20729](http://github.com/cms-sw/cmssw/pull/20729){:target="_blank"}  from **@lunik1**: Update quality test limits `dqm`  created: 2017-10-03T13:02:24Z merged: 2017-10-05T07:47:33Z

1. [20727](http://github.com/cms-sw/cmssw/pull/20727){:target="_blank"}  from **@cms-sw**: Fix compiler warning: Removed unused variable `reconstruction`  created: 2017-10-03T10:06:03Z merged: 2017-10-03T18:09:06Z

1. [20726](http://github.com/cms-sw/cmssw/pull/20726){:target="_blank"}  from **@mtosi**: FastTimerServiceClient bug fix `hlt`  created: 2017-10-03T08:58:55Z merged: 2017-10-05T08:10:58Z

1. [20723](http://github.com/cms-sw/cmssw/pull/20723){:target="_blank"}  from **@battibass**: [94X] Make muon HLT (L3/TkMu) work in phaseII scenarios `reconstruction`  `upgrade`  created: 2017-10-02T21:38:15Z merged: 2017-10-09T19:07:46Z

1. [20717](http://github.com/cms-sw/cmssw/pull/20717){:target="_blank"}  from **@fioriNTU**: tuning of Strip QTest for higher PU/track-density `dqm`  created: 2017-10-02T15:45:47Z merged: 2017-10-03T18:09:38Z

1. [20711](http://github.com/cms-sw/cmssw/pull/20711){:target="_blank"}  from **@ggovi**: Fixes for Conddb copy command `db`  created: 2017-10-02T08:12:14Z merged: 2017-10-06T07:06:38Z

1. [20710](http://github.com/cms-sw/cmssw/pull/20710){:target="_blank"}  from **@wmtford**: Trk hit assoc log debug `simulation`  created: 2017-10-02T04:27:27Z merged: 2017-10-04T07:15:44Z

1. [20705](http://github.com/cms-sw/cmssw/pull/20705){:target="_blank"}  from **@drkovalskyi**: Extract timing for tracker-only muons `reconstruction`  created: 2017-10-01T09:11:57Z merged: 2017-10-06T08:51:12Z

1. [20702](http://github.com/cms-sw/cmssw/pull/20702){:target="_blank"}  from **@osschar**: Enable usage of TTreeCache in Fireworks `core`  `visualization`  created: 2017-09-29T22:40:14Z merged: 2017-10-05T07:50:43Z

1. [20699](http://github.com/cms-sw/cmssw/pull/20699){:target="_blank"}  from **@fabozzi**: Update to 2017 data relvals `pdmv`  `upgrade`  created: 2017-09-29T15:01:10Z merged: 2017-10-03T14:16:30Z

1. [20693](http://github.com/cms-sw/cmssw/pull/20693){:target="_blank"}  from **@rvenditti**: Update to the ZMuSkim `pdmv`  created: 2017-09-28T16:07:30Z merged: 2017-10-10T11:09:57Z

1. [20691](http://github.com/cms-sw/cmssw/pull/20691){:target="_blank"}  from **@fabozzi**: Update of data re-miniAOD workflows `pdmv`  `upgrade`  created: 2017-09-28T15:40:46Z merged: 2017-10-03T18:15:02Z

1. [20685](http://github.com/cms-sw/cmssw/pull/20685){:target="_blank"}  from **@antoniovagnerini**: updating trigger names in MssmHbbMonitoring and MssmHbbBtagTriggerMon `dqm`  created: 2017-09-28T09:31:20Z merged: 2017-10-03T18:15:42Z

1. [20680](http://github.com/cms-sw/cmssw/pull/20680){:target="_blank"}  from **@davidcarbonis**: Phase1 pixel validation cluster loop fix `dqm`  created: 2017-09-27T19:52:42Z merged: 2017-10-03T18:17:11Z

1. [20672](http://github.com/cms-sw/cmssw/pull/20672){:target="_blank"}  from **@tstreble**: New Candidate+Point seeded tracking region producer for Tau HLT tracking `hlt`  `reconstruction`  created: 2017-09-27T16:10:22Z merged: 2017-10-06T12:47:27Z

1. [20668](http://github.com/cms-sw/cmssw/pull/20668){:target="_blank"}  from **@mrodozov**: Fix un-init member warnings in DataFormats/SiStripCluster `reconstruction`  created: 2017-09-27T14:07:38Z merged: 2017-10-06T07:07:08Z

1. [20655](http://github.com/cms-sw/cmssw/pull/20655){:target="_blank"}  from **@cms-met**: Adding chsMET and trackMET to miniAOD `analysis`  `reconstruction`  created: 2017-09-26T14:17:15Z merged: 2017-10-17T07:08:44Z

1. [20651](http://github.com/cms-sw/cmssw/pull/20651){:target="_blank"}  from **@capalmer85**: add LumiCorrections records and definitions; adding LumiInfo.h members/methods `alca`  `db`  `reconstruction`  created: 2017-09-25T18:46:01Z merged: 2017-10-17T15:49:55Z

1. [20649](http://github.com/cms-sw/cmssw/pull/20649){:target="_blank"}  from **@astakia**: L1T Muon Offline DQM - Resolution plots & bug fixes `dqm`  `l1`  created: 2017-09-25T16:22:42Z merged: 2017-10-20T07:55:21Z

1. [20643](http://github.com/cms-sw/cmssw/pull/20643){:target="_blank"}  from **@mmusich**: [94X] more Strip conditions supported by Payload Inspector `db`  created: 2017-09-25T09:20:38Z merged: 2017-10-16T10:45:30Z

1. [20642](http://github.com/cms-sw/cmssw/pull/20642){:target="_blank"}  from **@CTPPS**: CTPPS pixel clusterizer: patch in gain calibration call `reconstruction`  created: 2017-09-24T17:21:10Z merged: 2017-10-06T08:51:51Z

1. [20638](http://github.com/cms-sw/cmssw/pull/20638){:target="_blank"}  from **@rappoccio**: Updates to MiniAOD to satisfy JME/SMP/B2G requests for NanoAOD `analysis`  `dqm`  `generators`  `reconstruction`  created: 2017-09-23T21:06:32Z merged: 2017-10-05T19:48:57Z

1. [20635](http://github.com/cms-sw/cmssw/pull/20635){:target="_blank"}  from **@gkaratha**: dqm for triplemuon_5_3_3_dz in master br. `dqm`  created: 2017-09-23T10:46:18Z merged: 2017-10-10T06:27:30Z

1. [20626](http://github.com/cms-sw/cmssw/pull/20626){:target="_blank"}  from **@cms-nanoAOD**: NanoAOD prototype [RFC] `analysis`  `operations`  `reconstruction`  created: 2017-09-22T11:53:03Z merged: 2017-10-11T19:37:41Z

1. [20612](http://github.com/cms-sw/cmssw/pull/20612){:target="_blank"}  from **@drkovalskyi**: Standard muon selectors `analysis`  `reconstruction`  created: 2017-09-21T11:19:39Z merged: 2017-10-08T07:53:08Z

1. [20608](http://github.com/cms-sw/cmssw/pull/20608){:target="_blank"}  from **@bsunanda**: Run2-alca99 Modify all macros used to calibrate Hcal using IsoTracks `alca`  created: 2017-09-20T14:46:09Z merged: 2017-10-04T08:26:10Z

1. [20599](http://github.com/cms-sw/cmssw/pull/20599){:target="_blank"}  from **@depasse**: Upgrade of Ecal and Creation of Preshower Payload Inspector with Plot `db`  created: 2017-09-20T07:15:37Z merged: 2017-10-16T10:45:15Z

1. [20584](http://github.com/cms-sw/cmssw/pull/20584){:target="_blank"}  from **@gkaratha**: dqm for DoubleMu3_DCA_PFMET50_PFMHT60 `dqm`  created: 2017-09-19T14:46:31Z merged: 2017-10-10T06:27:42Z

1. [20567](http://github.com/cms-sw/cmssw/pull/20567){:target="_blank"}  from **@akhatiwa**: Added single module occupancy plots for on track digis and charge Vs  `dqm`  created: 2017-09-18T18:02:40Z merged: 2017-10-04T13:37:45Z

1. [20552](http://github.com/cms-sw/cmssw/pull/20552){:target="_blank"}  from **@bsunanda**: Run2-alca96 Add propagation tool from Hcal to Ecal `alca`  created: 2017-09-17T22:49:37Z merged: 2017-10-11T07:37:08Z

1. [20550](http://github.com/cms-sw/cmssw/pull/20550){:target="_blank"}  from **@Sam-Harper**: electron track isolation producer improvements + reading saturation info from the electron in HEEP V7.0 `reconstruction`  created: 2017-09-17T15:58:00Z merged: 2017-10-05T07:58:15Z

1. [20523](http://github.com/cms-sw/cmssw/pull/20523){:target="_blank"}  from **@bsunanda**: Run2-hcx155 Correct access to HcalGeometry from TauDiscriminationAgainstCaloMuon `reconstruction`  created: 2017-09-14T21:07:45Z merged: 2017-10-13T16:18:08Z

1. [20413](http://github.com/cms-sw/cmssw/pull/20413){:target="_blank"}  from **@popovvp**: CTPPS Pixel DQM add clusters `dqm`  created: 2017-09-07T11:17:50Z merged: 2017-10-13T09:32:16Z

1. [20410](http://github.com/cms-sw/cmssw/pull/20410){:target="_blank"}  from **@bsunanda**: Run2-hcx149 Bug fix for HcalNoiseAlgo and update for HcalHaloAlgo to make C11 compliant `reconstruction`  created: 2017-09-06T22:09:55Z merged: 2017-10-10T07:50:12Z

1. [20286](http://github.com/cms-sw/cmssw/pull/20286){:target="_blank"}  from **@abrinke1**: EMTF 2017 PR #6 - Emulator `alca`  `db`  `dqm`  `l1`  created: 2017-08-28T16:14:08Z merged: 2017-10-08T18:42:13Z

1. [20189](http://github.com/cms-sw/cmssw/pull/20189){:target="_blank"}  from **@Dr15Jones**: LogErrorHarvester depends on  EDProducers `core`  `operations`  `reconstruction`  created: 2017-08-16T17:56:40Z merged: 2017-10-14T13:05:20Z

1. [20000](http://github.com/cms-sw/cmssw/pull/20000){:target="_blank"}  from **@nsmith-**: Modify CaloLayer1 emulator to properly handle saturation in all cases `l1`  created: 2017-08-01T15:30:06Z merged: 2017-10-05T08:23:11Z

1. [19699](http://github.com/cms-sw/cmssw/pull/19699){:target="_blank"}  from **@sushilchauhan**: added hep17 folder, 2d eff plots for egammaHLT DQM and Validation `dqm`  created: 2017-07-12T08:27:54Z merged: 2017-10-17T07:19:58Z

1. [19253](http://github.com/cms-sw/cmssw/pull/19253){:target="_blank"}  from **@chenxvan**: Added scripts to produce Pixel Maps and the Cluster Noise and Size for Strip Maps `dqm`  `reconstruction`  created: 2017-06-15T16:41:29Z merged: 2017-10-07T13:32:43Z

#### CMSDIST Changes between Tags REL/CMSSW_9_4_0_pre2/slc6_amd64_gcc630 and REL/CMSSW_9_4_0_pre3/slc6_amd64_gcc630:
[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_9_4_0_pre2/slc6_amd64_gcc630...REL/CMSSW_9_4_0_pre3/slc6_amd64_gcc630)



1. [3507](http://github.com/cms-sw/cmssw/pull/3507){:target="_blank"}  from **@cms-sw**: Update tensorflow-sources.spec created: 2014-04-25T16:02:48Z merged: 2014-04-25T22:12:42Z

1. [3502](http://github.com/cms-sw/cmssw/pull/3502){:target="_blank"}  from **@cms-sw**: Update root to latest commits from v6-10 patches created: 2014-04-25T12:06:07Z merged: 2014-04-25T13:18:31Z

1. [3501](http://github.com/cms-sw/cmssw/pull/3501){:target="_blank"}  from **@civanch**: Fixed decay channels or K0 and antiK0 created: 2014-04-25T11:25:41Z merged: 2014-04-28T11:19:32Z

1. [3492](http://github.com/cms-sw/cmssw/pull/3492){:target="_blank"}  from **@mrodozov**: Update Theano version to 0.9.0 created: 2014-04-25T05:26:39Z merged: None

1. [3489](http://github.com/cms-sw/cmssw/pull/3489){:target="_blank"}  from **@cms-sw**: Updating RecoBTag-Combined to tag V01-00-07 created: 2014-04-24T21:31:53Z merged: 2014-04-25T18:48:53Z

1. [3485](http://github.com/cms-sw/cmssw/pull/3485){:target="_blank"}  from **@cms-sw**: Update root to latest commits from v6-10 patches created: 2014-04-24T19:15:11Z merged: 2014-04-24T21:22:15Z

1. [3484](http://github.com/cms-sw/cmssw/pull/3484){:target="_blank"}  from **@fwyzard**: do not include CUDA drivers in the external created: 2014-04-24T15:25:21Z merged: None

1. [3480](http://github.com/cms-sw/cmssw/pull/3480){:target="_blank"}  from **@mkirsano**: upgrade vincia to 2.2.00 created: 2014-04-24T13:04:08Z merged: 2014-04-25T17:30:58Z

1. [3475](http://github.com/cms-sw/cmssw/pull/3475){:target="_blank"}  from **@fwyzard**: update Intel VTune to version 2017.3.0.510739 created: 2014-04-24T11:00:57Z merged: 2014-04-30T05:24:25Z

1. [3474](http://github.com/cms-sw/cmssw/pull/3474){:target="_blank"}  from **@fwyzard**: include libcudart_static.a in the distribution created: 2014-04-24T09:39:07Z merged: 2014-04-24T20:36:32Z

1. [3434](http://github.com/cms-sw/cmssw/pull/3434){:target="_blank"}  from **@gudrutis**: updating vdt to v0.3.9 created: 2014-04-22T17:48:21Z merged: 2014-04-23T12:10:41Z

1. [3407](http://github.com/cms-sw/cmssw/pull/3407){:target="_blank"}  from **@cms-sw**: Update data-L1Trigger-L1TMuon.spec created: 2014-04-20T11:31:59Z merged: 2014-04-22T12:51:08Z
