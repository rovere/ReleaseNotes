---
layout: post
title:  "8_1_0_pre6"
date:   2017-10-05 18:46:15 +0200
categories: cmssw
relmajor: 8
relminor: 1
relsubminor: 0

relpre: _pre6
---

# CMSSW_8_1_0_pre6
#### Changes since CMSSW_8_1_0_pre5:

[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_8_1_0_pre5...CMSSW_8_1_0_pre6)



1. [14677](http://github.com/cms-sw/cmssw/pull/14677)  from @slava77: cleanup RawToDigi redefinition of already loaded from RawToDigi_cff (bp of #14675) `operations`  created: 2016-05-28T01:21:14Z merged: 2016-05-29T20:01:57Z

1. [14667](http://github.com/cms-sw/cmssw/pull/14667)  from @kpedro88: remove unneeded hgchebackDigitizer `simulation`  created: 2016-05-27T15:36:39Z merged: 2016-05-28T18:59:37Z

1. [14662](http://github.com/cms-sw/cmssw/pull/14662)  from @VinInn: fix crash in case Limit on the number of clusters is really exceeded. `reconstruction`  created: 2016-05-27T14:10:11Z merged: 2016-05-27T18:22:02Z

1. [14661](http://github.com/cms-sw/cmssw/pull/14661)  from @VinInn: fix crash in case Limit on the number of clusters is really exceeded. `reconstruction`  created: 2016-05-27T14:02:01Z merged: 2016-05-28T18:59:51Z

1. [14658](http://github.com/cms-sw/cmssw/pull/14658)  from @ggovi: Fix for handling copy of offline synchronized tags `db`  created: 2016-05-27T12:32:55Z merged: 2016-05-29T19:58:41Z

1. [14657](http://github.com/cms-sw/cmssw/pull/14657)  from @ggovi: Fix for handling copy of offline synchronized tags `db`  created: 2016-05-27T12:32:17Z merged: 2016-05-27T16:52:14Z

1. [14656](http://github.com/cms-sw/cmssw/pull/14656)  from @jshlee: fireworks Gem and me0 segments 81x `visualization`  created: 2016-05-27T11:38:54Z merged: 2016-05-28T19:00:03Z

1. [14654](http://github.com/cms-sw/cmssw/pull/14654)  from @cms-l1t-offline: Change default caloParams to use Tau Iso Option 21 `comparison`  `l1`  created: 2016-05-27T08:45:59Z merged: 2016-05-27T08:47:24Z

1. [14653](http://github.com/cms-sw/cmssw/pull/14653)  from @davidlt: Blacklist -xSSE3 (ICC) in condformats_serialization_generate.py `comparison`  `db`  created: 2016-05-27T08:29:30Z merged: 2016-05-27T08:29:44Z

1. [14651](http://github.com/cms-sw/cmssw/pull/14651)  from @cms-l1t-offline: Restore overflow check for et and ht sums (81x) `l1`  created: 2016-05-27T01:26:48Z merged: 2016-05-27T08:38:57Z

1. [14650](http://github.com/cms-sw/cmssw/pull/14650)  from @cms-l1t-offline: Restore overflow check for et and ht sums `l1`  created: 2016-05-26T22:54:34Z merged: 2016-05-27T08:39:07Z

1. [14648](http://github.com/cms-sw/cmssw/pull/14648)  from @kpedro88: remove redundant HGCal unit test `simulation`  created: 2016-05-26T18:54:25Z merged: 2016-05-27T08:22:27Z

1. [14647](http://github.com/cms-sw/cmssw/pull/14647)  from @cms-l1t-offline: Adding L1REPACK:FullMC workflow to run on RAW of MC (80x) `operations`  created: 2016-05-26T16:26:25Z merged: 2016-05-27T07:46:17Z

1. [14646](http://github.com/cms-sw/cmssw/pull/14646)  from @cms-l1t-offline: MCprod l1t Tau Iso Option-21 80x `l1`  created: 2016-05-26T16:22:17Z merged: 2016-05-27T08:41:16Z

1. [14640](http://github.com/cms-sw/cmssw/pull/14640)  from @wmtan: Use unique_ptr, not auto_ptr, in Full Simulation `l1`  `simulation`  created: 2016-05-26T05:17:32Z merged: 2016-05-27T08:25:02Z

1. [14639](http://github.com/cms-sw/cmssw/pull/14639)  from @cms-tau-pog: restore functionality of removeMCMatching in PAT coreTools.py `analysis`  `reconstruction`  created: 2016-05-25T21:17:49Z merged: 2016-05-28T19:00:08Z

1. [14635](http://github.com/cms-sw/cmssw/pull/14635)  from @cms-l1t-offline: Adding L1REPACK:FullMC workflow to run on RAW of MC. `operations`  created: 2016-05-25T14:40:35Z merged: 2016-05-27T07:38:17Z

1. [14633](http://github.com/cms-sw/cmssw/pull/14633)  from @ggovi: Several improvements for the conddb tools `db`  created: 2016-05-25T13:04:34Z merged: 2016-05-26T13:25:52Z

1. [14629](http://github.com/cms-sw/cmssw/pull/14629)  from @gartung: don't disable any default checkers as this causes the CMS one to not run `comparison`  `core`  created: 2016-05-24T20:39:09Z merged: 2016-05-25T05:42:55Z

1. [14628](http://github.com/cms-sw/cmssw/pull/14628)  from @boudoul: cleaning obsolete names of phase2 geometry in tracker packages `analysis`  `simulation`  created: 2016-05-24T18:47:58Z merged: 2016-05-25T16:15:53Z

1. [14621](http://github.com/cms-sw/cmssw/pull/14621)  from @makortel: Use pixel seed extension for phase1 in initialStep `reconstruction`  created: 2016-05-24T15:38:08Z merged: 2016-05-26T17:35:28Z

1. [14618](http://github.com/cms-sw/cmssw/pull/14618)  from @safarzad: adding HLTPFMET170_BeamHaloCleaned to SUSY DQM `dqm`  created: 2016-05-24T10:52:44Z merged: 2016-05-25T15:43:47Z

1. [14617](http://github.com/cms-sw/cmssw/pull/14617)  from @cms-l1t-offline: Clean-up L1T unpacker warnings `l1`  created: 2016-05-24T10:38:32Z merged: 2016-05-24T15:10:43Z

1. [14614](http://github.com/cms-sw/cmssw/pull/14614)  from @mtosi: fix tracking DQM client config `dqm`  created: 2016-05-24T10:21:08Z merged: 2016-05-24T15:11:05Z

1. [14613](http://github.com/cms-sw/cmssw/pull/14613)  from @cms-l1t-offline: Update OMTF treatment of Muons at edge of OMTF acceptance `l1`  created: 2016-05-24T09:55:18Z merged: 2016-05-24T15:10:53Z

1. [14610](http://github.com/cms-sw/cmssw/pull/14610)  from @boudoul: Introducing PU WFs for phase2 `pdmv`  created: 2016-05-23T20:14:38Z merged: 2016-05-25T15:51:57Z

1. [14608](http://github.com/cms-sw/cmssw/pull/14608)  from @mmarionncern: Fix posftix and scheduled mode issue in the runMETUncertainty tool `analysis`  `reconstruction`  created: 2016-05-23T17:52:20Z merged: 2016-05-27T07:36:30Z

1. [14604](http://github.com/cms-sw/cmssw/pull/14604)  from @cms-l1t-offline: Update OMTF treatment of Muon at edge of OMTF acceptance `l1`  created: 2016-05-23T10:09:42Z merged: 2016-05-23T12:35:32Z

1. [14602](http://github.com/cms-sw/cmssw/pull/14602)  from @ndaci:  Add a cut in the HLTPFJetIDProducer module. `hlt`  created: 2016-05-23T08:34:01Z merged: 2016-05-24T15:11:16Z

1. [14601](http://github.com/cms-sw/cmssw/pull/14601)  from @ndaci: Add a cut in the HLTPFJetIDProducer module. `hlt`  created: 2016-05-23T08:32:19Z merged: 2016-05-24T08:14:02Z

1. [14600](http://github.com/cms-sw/cmssw/pull/14600)  from @CTPPS: CTPPS: new CondFormats related to TOTEM RP raw data and digi - backport of #13838 `alca`  `db`  created: 2016-05-23T08:02:55Z merged: 2016-05-27T16:36:28Z

1. [14599](http://github.com/cms-sw/cmssw/pull/14599)  from @kpedro88: Fix QIE11 unpacking bug `reconstruction`  created: 2016-05-22T21:44:29Z merged: 2016-05-25T06:10:52Z

1. [14598](http://github.com/cms-sw/cmssw/pull/14598)  from @ebrondol: Phase2 tracking reconstruction in 81X `reconstruction`  `simulation`  created: 2016-05-22T15:15:13Z merged: 2016-05-25T15:52:06Z

1. [14596](http://github.com/cms-sw/cmssw/pull/14596)  from @smuzaffar: Fix for runtestTqafTopEventSelection unit test: use againstElectronVLooseMVA6 instead of againstElectronVLooseMVA5 `analysis`  `reconstruction`  created: 2016-05-21T16:19:30Z merged: 2016-05-24T18:53:09Z

1. [14594](http://github.com/cms-sw/cmssw/pull/14594)  from @bsunanda: bsunanda:Run2-hcx83 Update Geometry to handle minimum depth > 1 and max phi > 72 `geometry`  `reconstruction`  created: 2016-05-20T18:01:57Z merged: 2016-05-25T06:10:30Z

1. [14592](http://github.com/cms-sw/cmssw/pull/14592)  from @ghellwig: Latest MillePede fixes 81X `alca`  created: 2016-05-20T16:24:56Z merged: 2016-05-24T09:37:28Z

1. [14591](http://github.com/cms-sw/cmssw/pull/14591)  from @cms-l1t-offline: Clean-up L1T unpacker warnings `l1`  created: 2016-05-20T14:18:31Z merged: 2016-05-22T07:10:06Z

1. [14590](http://github.com/cms-sw/cmssw/pull/14590)  from @duanders: Fix deltaR calculation in widejet module (81X) `comparison`  `hlt`  created: 2016-05-20T13:36:00Z merged: 2016-05-22T07:12:21Z

1. [14589](http://github.com/cms-sw/cmssw/pull/14589)  from @duanders: Use PFMETCollection in scouting PF producer (81X) `comparison`  `hlt`  created: 2016-05-20T12:54:05Z merged: 2016-05-22T07:11:49Z

1. [14588](http://github.com/cms-sw/cmssw/pull/14588)  from @duanders: Use PFMETCollection in scouting PF producer `hlt`  created: 2016-05-20T12:26:11Z merged: 2016-05-23T12:12:16Z

1. [14587](http://github.com/cms-sw/cmssw/pull/14587)  from @duanders: Fix deltaR calculation in HLT widejet module `hlt`  created: 2016-05-20T11:49:24Z merged: 2016-05-22T07:12:34Z

1. [14586](http://github.com/cms-sw/cmssw/pull/14586)  from @schneiml: Phase 1 Pixel DQM (number 4, the story continues) `dqm`  `reconstruction`  created: 2016-05-20T11:27:41Z merged: 2016-05-24T08:40:47Z

1. [14584](http://github.com/cms-sw/cmssw/pull/14584)  from @friccita: use full geometry cffs for MB plotting scripts `comparison`  `dqm`  `geometry`  created: 2016-05-20T09:25:49Z merged: 2016-05-25T06:11:30Z

1. [14583](http://github.com/cms-sw/cmssw/pull/14583)  from @ggovi: Fix for GTEntry_t hash function `db`  created: 2016-05-20T08:41:20Z merged: 2016-05-25T16:26:24Z

1. [14582](http://github.com/cms-sw/cmssw/pull/14582)  from @olivito: SUSY HLT DQM updates for trimuon and dimu+MET paths, 81X `dqm`  created: 2016-05-19T23:10:06Z merged: 2016-05-25T15:53:58Z

1. [14580](http://github.com/cms-sw/cmssw/pull/14580)  from @CTPPS: CTPPS: new DataFormats for local TOTEM RP reconstruction, backport of #14134 `reconstruction`  created: 2016-05-19T22:25:50Z merged: 2016-05-24T08:14:47Z

1. [14579](http://github.com/cms-sw/cmssw/pull/14579)  from @CTPPS: CTPPS: new DataFormats related to TOTEM RP raw data and digi - backport of PR #13837 `reconstruction`  `simulation`  created: 2016-05-19T22:10:55Z merged: 2016-05-24T18:54:32Z

1. [14578](http://github.com/cms-sw/cmssw/pull/14578)  from @CTPPS: Adding new detectors - integration of RomanPot detectors for CTPPS project - backport of PR #13766 `simulation`  created: 2016-05-19T21:54:25Z merged: 2016-05-22T07:15:12Z

1. [14574](http://github.com/cms-sw/cmssw/pull/14574)  from @smuzaffar: use era Run2_2016 for testRecoMETMETProducers unit test `reconstruction`  created: 2016-05-19T18:13:40Z merged: 2016-05-19T20:27:15Z

1. [14572](http://github.com/cms-sw/cmssw/pull/14572)  from @kpedro88: fix scope of hbheCells `simulation`  created: 2016-05-19T17:29:36Z merged: 2016-05-20T07:17:21Z

1. [14571](http://github.com/cms-sw/cmssw/pull/14571)  from @mmusich: 81X  SiStrip Gains PCL cleanup `alca`  `db`  `operations`  `pdmv`  created: 2016-05-19T13:21:42Z merged: 2016-05-25T15:45:15Z

1. [14570](http://github.com/cms-sw/cmssw/pull/14570)  from @cms-l1t-offline: Update L1T to l1t-tsg-v7-cand performance (80x) `dqm`  `l1`  created: 2016-05-19T10:00:36Z merged: 2016-05-23T13:07:07Z

1. [14569](http://github.com/cms-sw/cmssw/pull/14569)  from @idebruyn: TH1ClusterCharge and TH1ClusterStoNCorr plots per ring `dqm`  created: 2016-05-19T09:53:43Z merged: 2016-05-19T18:46:09Z

1. [14568](http://github.com/cms-sw/cmssw/pull/14568)  from @idebruyn: TH1ClusterCharge and TH1ClusterStoNCorr plots per ring `dqm`  created: 2016-05-19T09:53:38Z merged: 2016-05-29T19:58:28Z

1. [14567](http://github.com/cms-sw/cmssw/pull/14567)  from @dmitrijus: Disable broken Ewk*DQM modules `dqm`  created: 2016-05-19T09:08:21Z merged: 2016-05-22T07:11:59Z

1. [14566](http://github.com/cms-sw/cmssw/pull/14566)  from @OlivierBondu: Update ResonanceDecayFilterHook.cc `generators`  created: 2016-05-19T08:07:11Z merged: 2016-05-22T07:14:43Z

1. [14563](http://github.com/cms-sw/cmssw/pull/14563)  from @davidlt: CondCore/PopCon: define static constexpr member `alca`  `db`  created: 2016-05-19T07:01:52Z merged: 2016-05-19T10:18:25Z

1. [14561](http://github.com/cms-sw/cmssw/pull/14561)  from @bsunanda: bsunanda:Phase2-hgx53 Add 4 module setup of TB `geometry`  `simulation`  created: 2016-05-18T22:13:10Z merged: 2016-05-19T18:45:29Z

1. [14560](http://github.com/cms-sw/cmssw/pull/14560)  from @Dr15Jones: RootDelayedReader now uses std::exception_ptr `core`  created: 2016-05-18T21:32:03Z merged: 2016-05-19T07:02:12Z

1. [14558](http://github.com/cms-sw/cmssw/pull/14558)  from @alja: 80x Fireworks: Make shortcut to palette interface  `comparison`  `visualization`  created: 2016-05-18T18:24:09Z merged: 2016-05-18T19:35:29Z

1. [14557](http://github.com/cms-sw/cmssw/pull/14557)  from @davidlange6: change das_client.py to das_client in cmsDriver `comparison`  `operations`  `pdmv`  created: 2016-05-18T15:37:54Z merged: 2016-05-18T18:55:00Z

1. [14556](http://github.com/cms-sw/cmssw/pull/14556)  from @OlivierBondu: Update ResonanceDecayFilterHook.cc `comparison`  `generators`  created: 2016-05-18T14:42:16Z merged: 2016-05-19T08:31:19Z

1. [14554](http://github.com/cms-sw/cmssw/pull/14554)  from @ANSH0712: Fastsim triplet seed selection branch `fastsim`  `reconstruction`  created: 2016-05-18T13:22:16Z merged: 2016-05-22T17:08:24Z

1. [14553](http://github.com/cms-sw/cmssw/pull/14553)  from @cms-l1t-offline: Rekovic l1 repack 2016 2015 cmssw81x `l1`  `operations`  created: 2016-05-18T13:12:18Z merged: 2016-05-19T08:33:48Z

1. [14551](http://github.com/cms-sw/cmssw/pull/14551)  from @cms-l1t-offline: L1 repack 2016 2015 (Full, uGT, Full2015Data) cmssw808 `l1`  `operations`  created: 2016-05-18T12:30:44Z merged: 2016-05-23T13:08:37Z

1. [14550](http://github.com/cms-sw/cmssw/pull/14550)  from @civanch: Fixed Sim exceptions and printouts `simulation`  created: 2016-05-18T12:21:20Z merged: 2016-05-23T07:10:34Z

1. [14548](http://github.com/cms-sw/cmssw/pull/14548)  from @dmitrijus: Disable broken Ewk*DQM modules `dqm`  created: 2016-05-18T11:56:07Z merged: 2016-05-18T16:07:15Z

1. [14545](http://github.com/cms-sw/cmssw/pull/14545)  from @mmusich: Include full alignment and APE for Pixel Phase-I detector `alca`  `geometry`  created: 2016-05-18T08:52:35Z merged: 2016-05-19T14:44:34Z

1. [14544](http://github.com/cms-sw/cmssw/pull/14544)  from @makortel: Unify tracking iteration configurations in RECO, DQM, and VALIDATION, and automatize cluster removal `dqm`  `reconstruction`  `simulation`  created: 2016-05-18T07:58:08Z merged: 2016-05-25T15:53:27Z

1. [14543](http://github.com/cms-sw/cmssw/pull/14543)  from @smorovic: Adding merging type (DAQ) and changing defaults (81X) `daq`  `dqm`  `hlt`  `reconstruction`  created: 2016-05-18T07:46:14Z merged: 2016-05-18T15:49:29Z

1. [14542](http://github.com/cms-sw/cmssw/pull/14542)  from @Dr15Jones: Made static TiXmlBase::entity const `comparison`  `core`  created: 2016-05-17T21:44:49Z merged: 2016-05-19T07:03:46Z

1. [14541](http://github.com/cms-sw/cmssw/pull/14541)  from @bsunanda: bsunanda:Run2-alca45 Add a filter which filters out isolated bunch with Jet triggers `alca`  `operations`  created: 2016-05-17T21:32:22Z merged: 2016-05-28T19:01:05Z

1. [14538](http://github.com/cms-sw/cmssw/pull/14538)  from @lathomas: Typo correction in config file `reconstruction`  created: 2016-05-17T17:22:18Z merged: 2016-05-20T07:17:50Z

1. [14537](http://github.com/cms-sw/cmssw/pull/14537)  from @bsunanda: bsunanda:Phase2-gem15 ME0 with eta partitions `geometry`  created: 2016-05-17T16:35:48Z merged: 2016-05-19T10:21:04Z

1. [14536](http://github.com/cms-sw/cmssw/pull/14536)  from @davidlt: Utilities/StaticAnalyzers: adjust to LLVM/Clang 3.8.0 `comparison`  `core`  created: 2016-05-17T16:20:15Z merged: 2016-05-17T16:20:24Z

1. [14535](http://github.com/cms-sw/cmssw/pull/14535)  from @cms-l1t-offline: Update L1T to l1t-tsg-v7-cand performance (81x) `comparison`  `dqm`  `l1`  created: 2016-05-17T14:39:36Z merged: 2016-05-19T08:32:47Z

1. [14533](http://github.com/cms-sw/cmssw/pull/14533)  from @fioriNTU: retune max value for Chi2 `dqm`  created: 2016-05-17T14:19:28Z merged: 2016-05-18T15:49:50Z

1. [14531](http://github.com/cms-sw/cmssw/pull/14531)  from @fioriNTU: retune max value for Chi2 `dqm`  created: 2016-05-17T14:08:24Z merged: 2016-05-22T07:13:23Z

1. [14530](http://github.com/cms-sw/cmssw/pull/14530)  from @rmanzoni: [RecoTauTag] allow complete relax of tau isolation at high pt `reconstruction`  created: 2016-05-17T13:11:42Z merged: 2016-05-22T07:13:02Z

1. [14529](http://github.com/cms-sw/cmssw/pull/14529)  from @rmanzoni: [RecoTauTag] allow complete relax of tau isolation at high pt `reconstruction`  created: 2016-05-17T12:24:20Z merged: 2016-05-18T07:20:53Z

1. [14528](http://github.com/cms-sw/cmssw/pull/14528)  from @smorovic: Adding merging type (DAQ) and changing defaults `daq`  `dqm`  `hlt`  `reconstruction`  created: 2016-05-17T09:53:57Z merged: 2016-05-22T07:14:19Z

1. [14524](http://github.com/cms-sw/cmssw/pull/14524)  from @jruizvar: Updates Calo Scouting triggers in EXO DQM  (81X) `dqm`  created: 2016-05-16T21:59:00Z merged: 2016-05-18T07:28:03Z

1. [14523](http://github.com/cms-sw/cmssw/pull/14523)  from @ebrondol: 2023 workflows up to tracking reco `geometry`  `operations`  `pdmv`  `reconstruction`  `simulation`  created: 2016-05-16T19:42:10Z merged: 2016-05-20T07:29:26Z

1. [14522](http://github.com/cms-sw/cmssw/pull/14522)  from @Dr15Jones: Added Erf and Landau functions to FormulaEvaluator `analysis`  `reconstruction`  created: 2016-05-16T18:46:14Z merged: 2016-05-18T19:34:31Z

1. [14521](http://github.com/cms-sw/cmssw/pull/14521)  from @alja: 80x Fireworks: Implement palettes `comparison`  `visualization`  created: 2016-05-16T18:18:16Z merged: 2016-05-17T12:39:02Z

1. [14520](http://github.com/cms-sw/cmssw/pull/14520)  from @aspiezia: Adding the cosmic during collision reconstruction in CMSSW81X `fastsim`  `operations`  `reconstruction`  created: 2016-05-16T17:54:49Z merged: 2016-05-25T16:08:58Z

1. [14518](http://github.com/cms-sw/cmssw/pull/14518)  from @mbandrews: Fix statistics of Trend plots `dqm`  created: 2016-05-16T16:02:57Z merged: 2016-05-25T06:12:30Z

1. [14513](http://github.com/cms-sw/cmssw/pull/14513)  from @fioriNTU: Ready to use cfg for shifters `analysis`  created: 2016-05-16T14:51:12Z merged: 2016-05-18T08:22:35Z

1. [14512](http://github.com/cms-sw/cmssw/pull/14512)  from @usarica: Muon analysis updates 8.0.x `alca`  `analysis`  created: 2016-05-16T13:36:35Z merged: 2016-05-24T08:41:20Z

1. [14511](http://github.com/cms-sw/cmssw/pull/14511)  from @usarica: Muon analysis updates 8.1.x `alca`  `analysis`  created: 2016-05-16T13:35:09Z merged: 2016-05-18T08:26:52Z

1. [14507](http://github.com/cms-sw/cmssw/pull/14507)  from @ggovi: Fix for GTEntry_t hash function `db`  created: 2016-05-15T16:12:24Z merged: 2016-05-18T08:09:29Z

1. [14506](http://github.com/cms-sw/cmssw/pull/14506)  from @sarafiorendi: add tentative propagation to ME2 if MB2 fails (backport of #14505) `reconstruction`  created: 2016-05-14T17:45:18Z merged: 2016-05-18T19:35:41Z

1. [14505](http://github.com/cms-sw/cmssw/pull/14505)  from @sarafiorendi: Seeding of L2 muons: propagate L1 cands to ME2 if propagation to MB2 fails  `reconstruction`  created: 2016-05-14T17:38:34Z merged: 2016-05-18T07:26:33Z

1. [14502](http://github.com/cms-sw/cmssw/pull/14502)  from @fwyzard: L1TGlobalPrescaler: implement arbitrary prescales on top of the existing L1 uGT results `core`  `l1`  created: 2016-05-13T23:24:33Z merged: 2016-05-17T15:47:31Z

1. [14501](http://github.com/cms-sw/cmssw/pull/14501)  from @bartosik-hep: 80X: HLT path/module-name updates in the HLTObjectMonitor `dqm`  created: 2016-05-13T21:48:13Z merged: 2016-05-23T12:14:04Z

1. [14500](http://github.com/cms-sw/cmssw/pull/14500)  from @bartosik-hep: HLT path/module-name updates in the HLTObjectMonitor `dqm`  created: 2016-05-13T21:30:45Z merged: 2016-05-19T18:46:50Z

1. [14499](http://github.com/cms-sw/cmssw/pull/14499)  from @alja: 80x Fireworks:Fix problem in finding detail view for given class type `comparison`  `visualization`  created: 2016-05-13T20:31:09Z merged: 2016-05-17T12:39:14Z

1. [14496](http://github.com/cms-sw/cmssw/pull/14496)  from @mkirsano: Prepare Pythia8Interface to pythia8 219 `comparison`  `generators`  created: 2016-05-13T16:45:08Z merged: 2016-05-18T08:07:48Z

1. [14494](http://github.com/cms-sw/cmssw/pull/14494)  from @Dr15Jones: Added Erf and Landau functions to FormulaEvaluator `analysis`  `reconstruction`  created: 2016-05-13T14:34:26Z merged: 2016-05-18T07:24:11Z

1. [14489](http://github.com/cms-sw/cmssw/pull/14489)  from @cecchcms: some APV plots removed `dqm`  created: 2016-05-13T07:27:01Z merged: 2016-05-18T07:24:22Z

1. [14486](http://github.com/cms-sw/cmssw/pull/14486)  from @alja:  80x Fireworks:Update table view content (attempt No2) `comparison`  `visualization`  created: 2016-05-12T20:00:18Z merged: 2016-05-17T12:39:25Z

1. [14483](http://github.com/cms-sw/cmssw/pull/14483)  from @andresib: Update SUSYBSM_HLT_VBF_Mu_cff.py `dqm`  created: 2016-05-12T18:40:32Z merged: 2016-05-25T15:49:14Z

1. [14482](http://github.com/cms-sw/cmssw/pull/14482)  from @kpedro88: add QIE11 support in hcal digitization `alca`  `geometry`  `operations`  `simulation`  created: 2016-05-12T18:38:50Z merged: 2016-05-17T15:50:50Z

1. [14478](http://github.com/cms-sw/cmssw/pull/14478)  from @davidlange6: remove some printout in every event `comparison`  `l1`  created: 2016-05-12T14:41:38Z merged: 2016-05-12T14:41:46Z

1. [14477](http://github.com/cms-sw/cmssw/pull/14477)  from @fwyzard: L1TGlobalProducer: migrate to stream module (80x) `l1`  created: 2016-05-12T14:01:18Z merged: 2016-05-23T13:09:20Z

1. [14474](http://github.com/cms-sw/cmssw/pull/14474)  from @fwyzard: HLT DQM: add protection for empty L1 uGT collection `dqm`  created: 2016-05-12T12:43:38Z merged: 2016-05-12T14:37:37Z

1. [14469](http://github.com/cms-sw/cmssw/pull/14469)  from @hengne: relval matrix update `pdmv`  created: 2016-05-12T07:52:28Z merged: 2016-05-18T09:44:49Z

1. [14467](http://github.com/cms-sw/cmssw/pull/14467)  from @VinInn: fix det search tollerances for Cosmics `reconstruction`  created: 2016-05-12T05:14:06Z merged: 2016-05-24T08:16:32Z

1. [14465](http://github.com/cms-sw/cmssw/pull/14465)  from @cms-l1t-offline: L1T Minimum Bias Trigger (80x) `l1`  created: 2016-05-11T21:12:49Z merged: 2016-05-12T14:38:32Z

1. [14462](http://github.com/cms-sw/cmssw/pull/14462)  from @kpedro88: Monitor CASTOR table data (80X) `alca`  `reconstruction`  `simulation`  created: 2016-05-11T19:55:18Z merged: 2016-05-27T08:29:49Z

1. [14461](http://github.com/cms-sw/cmssw/pull/14461)  from @kpedro88: Monitor CASTOR table data (81X) `alca`  `reconstruction`  `simulation`  created: 2016-05-11T19:55:14Z merged: 2016-05-20T10:41:27Z

1. [14456](http://github.com/cms-sw/cmssw/pull/14456)  from @bsunanda: bsunanda:Run2-hcx82 Add the possibility of a FrontEnd map for HCAL `alca`  `db`  created: 2016-05-11T15:35:18Z merged: 2016-05-22T07:08:22Z

1. [14451](http://github.com/cms-sw/cmssw/pull/14451)  from @lowette: Geometric CPE and persistent rechits for Phase 2 tracker local reco `reconstruction`  created: 2016-05-11T12:01:07Z merged: 2016-05-19T09:24:34Z

1. [14449](http://github.com/cms-sw/cmssw/pull/14449)  from @kovitang: Negative and positive  C-tagger in 81X `analysis`  `reconstruction`  created: 2016-05-11T10:14:29Z merged: 2016-05-18T07:18:24Z

1. [14446](http://github.com/cms-sw/cmssw/pull/14446)  from @cms-tsg-storm: HLT development in May (81X) `alca`  `dqm`  `hlt`  created: 2016-05-11T08:02:55Z merged: 2016-05-27T08:26:18Z

1. [14445](http://github.com/cms-sw/cmssw/pull/14445)  from @cms-tsg-storm: HLT development in May (80X) `alca`  `dqm`  `hlt`  created: 2016-05-11T08:02:14Z merged: 2016-05-27T16:38:33Z

1. [14437](http://github.com/cms-sw/cmssw/pull/14437)  from @ggovi: Changes for O2O deployment and monitoring `db`  created: 2016-05-10T15:45:03Z merged: 2016-05-27T07:41:47Z

1. [14421](http://github.com/cms-sw/cmssw/pull/14421)  from @diguida: Fixes for RunInfo O2O and cleanup of PopCon interface (80X) `alca`  `db`  created: 2016-05-09T16:51:24Z merged: 2016-05-25T15:52:17Z

1. [14420](http://github.com/cms-sw/cmssw/pull/14420)  from @diguida: Fixes for RunInfo O2O and cleanup of PopCon interface `alca`  `db`  created: 2016-05-09T16:51:13Z merged: 2016-05-18T07:28:16Z

1. [14403](http://github.com/cms-sw/cmssw/pull/14403)  from @wmtan: Use unique_ptr, not auto_ptr, in L1 `l1`  created: 2016-05-07T03:38:49Z merged: 2016-05-24T08:07:30Z

1. [14400](http://github.com/cms-sw/cmssw/pull/14400)  from @jshlee: GEM and ME0 segments 81 x `reconstruction`  created: 2016-05-06T16:08:23Z merged: 2016-05-26T23:48:34Z

1. [14395](http://github.com/cms-sw/cmssw/pull/14395)  from @slehti: HLT Tau DQM updated to stage2 L1 `dqm`  created: 2016-05-06T13:15:58Z merged: 2016-05-25T15:55:04Z

1. [14393](http://github.com/cms-sw/cmssw/pull/14393)  from @olivito: updating SUSY HLT DQM config for lep+HT triggers `dqm`  created: 2016-05-06T11:13:02Z merged: 2016-05-25T16:21:40Z

1. [14390](http://github.com/cms-sw/cmssw/pull/14390)  from @pvmulder: First version of the candidatebased GhostTrack tagger `analysis`  `dqm`  `reconstruction`  created: 2016-05-05T21:16:40Z merged: 2016-05-22T17:08:44Z

1. [14382](http://github.com/cms-sw/cmssw/pull/14382)  from @dildick: L1CSC Trigger Primitive conditions DB vs Python config comparator `l1`  created: 2016-05-05T00:04:13Z merged: 2016-05-26T06:31:22Z

1. [14368](http://github.com/cms-sw/cmssw/pull/14368)  from @tanmaymudholkar: Added names for hardcoded constants and added one TP plot `dqm`  created: 2016-05-04T09:37:46Z merged: 2016-05-18T07:34:22Z

1. [14361](http://github.com/cms-sw/cmssw/pull/14361)  from @wmtan: Use unique_ptr, not auto_ptr, in Alignment/Calibration `alca`  created: 2016-05-03T22:34:11Z merged: 2016-05-18T07:33:29Z

1. [14356](http://github.com/cms-sw/cmssw/pull/14356)  from @makortel: Add pixel-only seed extension `dqm`  `hlt`  `reconstruction`  created: 2016-05-03T14:21:24Z merged: 2016-05-24T08:14:35Z

1. [14342](http://github.com/cms-sw/cmssw/pull/14342)  from @hengne: relval update data workflow reco step, and re-work the LHE-based fullSim workflows for HLT validation `generators`  `pdmv`  created: 2016-05-03T09:39:04Z merged: 2016-05-17T15:50:34Z

1. [14336](http://github.com/cms-sw/cmssw/pull/14336)  from @Martin-Grunewald: Prescale access for stage-2 environment (80X) `analysis`  `dqm`  `hlt`  `l1`  `reconstruction`  created: 2016-05-03T07:34:46Z merged: 2016-05-29T19:59:22Z

1. [14328](http://github.com/cms-sw/cmssw/pull/14328)  from @minano: Adding getBlade/getLadder functions `dqm`  created: 2016-05-02T15:17:22Z merged: 2016-05-18T07:33:04Z

1. [14325](http://github.com/cms-sw/cmssw/pull/14325)  from @cms-tsg-storm: Towards the first hlt menu for 2016 - 80X `hlt`  created: 2016-05-02T14:51:13Z merged: 2016-05-12T14:40:48Z

1. [14312](http://github.com/cms-sw/cmssw/pull/14312)  from @Martin-Grunewald: Prescale access for stage-2 environment (81X) `analysis`  `dqm`  `hlt`  `l1`  `reconstruction`  created: 2016-04-29T22:15:06Z merged: 2016-05-20T07:58:34Z

1. [14265](http://github.com/cms-sw/cmssw/pull/14265)  from @mmusich: DropBox metadata - 2016 (80X) `alca`  `db`  created: 2016-04-27T07:53:31Z merged: 2016-05-23T12:18:29Z

1. [14233](http://github.com/cms-sw/cmssw/pull/14233)  from @vdutta: Input files for offline TkCommissioner tool, 81X `comparison`  `dqm`  created: 2016-04-25T12:20:37Z merged: 2016-05-19T10:40:16Z

1. [14029](http://github.com/cms-sw/cmssw/pull/14029)  from @CTPPS: CTPPS new reconstruction geometry related to TOTEM RP detectors `alca`  `db`  `geometry`  created: 2016-04-12T07:02:06Z merged: 2016-05-22T17:09:29Z

1. [14010](http://github.com/cms-sw/cmssw/pull/14010)  from @ianna: 2015 Extended Scenario with Tracker Material Variations `db`  `geometry`  created: 2016-04-11T06:21:43Z merged: 2016-05-18T10:09:36Z

1. [13972](http://github.com/cms-sw/cmssw/pull/13972)  from @fioriNTU: improve TkMaps `dqm`  created: 2016-04-07T12:13:48Z merged: 2016-05-27T07:42:24Z

1. [13930](http://github.com/cms-sw/cmssw/pull/13930)  from @clint-richardson: added double lepton DQM `dqm`  created: 2016-04-05T12:52:50Z merged: 2016-05-25T15:52:35Z

1. [13877](http://github.com/cms-sw/cmssw/pull/13877)  from @mileva: Adding new class GEMDigiSimLink in 81X `simulation`  created: 2016-03-31T14:16:35Z merged: 2016-05-25T16:12:21Z

1. [13813](http://github.com/cms-sw/cmssw/pull/13813)  from @vkhristenko: Online HCAL DQM adding a 3rd application `dqm`  created: 2016-03-23T10:56:21Z merged: 2016-05-24T08:20:20Z

#### CMSDIST Changes between Tags REL/CMSSW_8_1_0_pre5/slc6_amd64_gcc530 and REL/CMSSW_8_1_0_pre6/slc6_amd64_gcc530:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_8_1_0_pre5/slc6_amd64_gcc530...REL/CMSSW_8_1_0_pre6/slc6_amd64_gcc530)



1. [2302](http://github.com/cms-sw/cmssw/pull/2302)  from @degano: Update data files for L1Trigger/L1TMuon. created: 2014-02-05T08:54:13Z merged: 2014-02-06T08:16:51Z

1. [2298](http://github.com/cms-sw/cmssw/pull/2298)  from @degano: Update GeneratorInterface/EvtGenInterface data. created: 2014-02-04T21:52:05Z merged: 2014-02-04T22:06:11Z

1. [2294](http://github.com/cms-sw/cmssw/pull/2294)  from @mkirsano: move to pythia8 219 from tarball created: 2014-02-04T16:53:01Z merged: None

1. [2293](http://github.com/cms-sw/cmssw/pull/2293)  from @degano: Update CUDA to version 7.5. created: 2014-02-04T16:47:37Z merged: 2014-02-05T11:33:14Z
