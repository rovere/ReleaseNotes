---
layout: post
title:  "8_0_9"
date:   2017-10-07 22:04:13 +0200
categories: cmssw
relmajor: 8
relminor: 0
relsubminor: 9
---

# CMSSW_8_0_9
#### Changes since CMSSW_8_0_8_patch2:

[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_8_0_8_patch2...CMSSW_8_0_9)



1. [14677](http://github.com/cms-sw/cmssw/pull/14677){:target="_blank"}  from **@slava77**: cleanup RawToDigi redefinition of already loaded from RawToDigi_cff (bp of #14675) `operations`  created: 2016-05-28T01:21:14Z merged: 2016-05-29T20:01:57Z

1. [14662](http://github.com/cms-sw/cmssw/pull/14662){:target="_blank"}  from **@VinInn**: fix crash in case Limit on the number of clusters is really exceeded. `reconstruction`  created: 2016-05-27T14:10:11Z merged: 2016-05-27T18:22:02Z

1. [14658](http://github.com/cms-sw/cmssw/pull/14658){:target="_blank"}  from **@ggovi**: Fix for handling copy of offline synchronized tags `db`  created: 2016-05-27T12:32:55Z merged: 2016-05-29T19:58:41Z

1. [14650](http://github.com/cms-sw/cmssw/pull/14650){:target="_blank"}  from **@cms-l1t-offline**: Restore overflow check for et and ht sums `l1`  created: 2016-05-26T22:54:34Z merged: 2016-05-27T08:39:07Z

1. [14647](http://github.com/cms-sw/cmssw/pull/14647){:target="_blank"}  from **@cms-l1t-offline**: Adding L1REPACK:FullMC workflow to run on RAW of MC (80x) `operations`  created: 2016-05-26T16:26:25Z merged: 2016-05-27T07:46:17Z

1. [14646](http://github.com/cms-sw/cmssw/pull/14646){:target="_blank"}  from **@cms-l1t-offline**: MCprod l1t Tau Iso Option-21 80x `l1`  created: 2016-05-26T16:22:17Z merged: 2016-05-27T08:41:16Z

1. [14617](http://github.com/cms-sw/cmssw/pull/14617){:target="_blank"}  from **@cms-l1t-offline**: Clean-up L1T unpacker warnings `l1`  created: 2016-05-24T10:38:32Z merged: 2016-05-24T15:10:43Z

1. [14613](http://github.com/cms-sw/cmssw/pull/14613){:target="_blank"}  from **@cms-l1t-offline**: Update OMTF treatment of Muons at edge of OMTF acceptance `l1`  created: 2016-05-24T09:55:18Z merged: 2016-05-24T15:10:53Z

1. [14602](http://github.com/cms-sw/cmssw/pull/14602){:target="_blank"}  from **@ndaci**:  Add a cut in the HLTPFJetIDProducer module. `hlt`  created: 2016-05-23T08:34:01Z merged: 2016-05-24T15:11:16Z

1. [14600](http://github.com/cms-sw/cmssw/pull/14600){:target="_blank"}  from **@CTPPS**: CTPPS: new CondFormats related to TOTEM RP raw data and digi - backport of #13838 `alca`  `db`  created: 2016-05-23T08:02:55Z merged: 2016-05-27T16:36:28Z

1. [14596](http://github.com/cms-sw/cmssw/pull/14596){:target="_blank"}  from **@smuzaffar**: Fix for runtestTqafTopEventSelection unit test: use againstElectronVLooseMVA6 instead of againstElectronVLooseMVA5 `analysis`  `reconstruction`  created: 2016-05-21T16:19:30Z merged: 2016-05-24T18:53:09Z

1. [14588](http://github.com/cms-sw/cmssw/pull/14588){:target="_blank"}  from **@duanders**: Use PFMETCollection in scouting PF producer `hlt`  created: 2016-05-20T12:26:11Z merged: 2016-05-23T12:12:16Z

1. [14587](http://github.com/cms-sw/cmssw/pull/14587){:target="_blank"}  from **@duanders**: Fix deltaR calculation in HLT widejet module `hlt`  created: 2016-05-20T11:49:24Z merged: 2016-05-22T07:12:34Z

1. [14583](http://github.com/cms-sw/cmssw/pull/14583){:target="_blank"}  from **@ggovi**: Fix for GTEntry_t hash function `db`  created: 2016-05-20T08:41:20Z merged: 2016-05-25T16:26:24Z

1. [14580](http://github.com/cms-sw/cmssw/pull/14580){:target="_blank"}  from **@CTPPS**: CTPPS: new DataFormats for local TOTEM RP reconstruction, backport of #14134 `reconstruction`  created: 2016-05-19T22:25:50Z merged: 2016-05-24T08:14:47Z

1. [14579](http://github.com/cms-sw/cmssw/pull/14579){:target="_blank"}  from **@CTPPS**: CTPPS: new DataFormats related to TOTEM RP raw data and digi - backport of PR #13837 `reconstruction`  `simulation`  created: 2016-05-19T22:10:55Z merged: 2016-05-24T18:54:32Z

1. [14578](http://github.com/cms-sw/cmssw/pull/14578){:target="_blank"}  from **@CTPPS**: Adding new detectors - integration of RomanPot detectors for CTPPS project - backport of PR #13766 `simulation`  created: 2016-05-19T21:54:25Z merged: 2016-05-22T07:15:12Z

1. [14570](http://github.com/cms-sw/cmssw/pull/14570){:target="_blank"}  from **@cms-l1t-offline**: Update L1T to l1t-tsg-v7-cand performance (80x) `dqm`  `l1`  created: 2016-05-19T10:00:36Z merged: 2016-05-23T13:07:07Z

1. [14568](http://github.com/cms-sw/cmssw/pull/14568){:target="_blank"}  from **@idebruyn**: TH1ClusterCharge and TH1ClusterStoNCorr plots per ring `dqm`  created: 2016-05-19T09:53:38Z merged: 2016-05-29T19:58:28Z

1. [14567](http://github.com/cms-sw/cmssw/pull/14567){:target="_blank"}  from **@dmitrijus**: Disable broken Ewk*DQM modules `dqm`  created: 2016-05-19T09:08:21Z merged: 2016-05-22T07:11:59Z

1. [14566](http://github.com/cms-sw/cmssw/pull/14566){:target="_blank"}  from **@OlivierBondu**: Update ResonanceDecayFilterHook.cc `generators`  created: 2016-05-19T08:07:11Z merged: 2016-05-22T07:14:43Z

1. [14551](http://github.com/cms-sw/cmssw/pull/14551){:target="_blank"}  from **@cms-l1t-offline**: L1 repack 2016 2015 (Full, uGT, Full2015Data) cmssw808 `l1`  `operations`  created: 2016-05-18T12:30:44Z merged: 2016-05-23T13:08:37Z

1. [14531](http://github.com/cms-sw/cmssw/pull/14531){:target="_blank"}  from **@fioriNTU**: retune max value for Chi2 `dqm`  created: 2016-05-17T14:08:24Z merged: 2016-05-22T07:13:23Z

1. [14530](http://github.com/cms-sw/cmssw/pull/14530){:target="_blank"}  from **@rmanzoni**: [RecoTauTag] allow complete relax of tau isolation at high pt `reconstruction`  created: 2016-05-17T13:11:42Z merged: 2016-05-22T07:13:02Z

1. [14528](http://github.com/cms-sw/cmssw/pull/14528){:target="_blank"}  from **@smorovic**: Adding merging type (DAQ) and changing defaults `daq`  `dqm`  `hlt`  `reconstruction`  created: 2016-05-17T09:53:57Z merged: 2016-05-22T07:14:19Z

1. [14512](http://github.com/cms-sw/cmssw/pull/14512){:target="_blank"}  from **@usarica**: Muon analysis updates 8.0.x `alca`  `analysis`  created: 2016-05-16T13:36:35Z merged: 2016-05-24T08:41:20Z

1. [14501](http://github.com/cms-sw/cmssw/pull/14501){:target="_blank"}  from **@bartosik-hep**: 80X: HLT path/module-name updates in the HLTObjectMonitor `dqm`  created: 2016-05-13T21:48:13Z merged: 2016-05-23T12:14:04Z

1. [14477](http://github.com/cms-sw/cmssw/pull/14477){:target="_blank"}  from **@fwyzard**: L1TGlobalProducer: migrate to stream module (80x) `l1`  created: 2016-05-12T14:01:18Z merged: 2016-05-23T13:09:20Z

1. [14467](http://github.com/cms-sw/cmssw/pull/14467){:target="_blank"}  from **@VinInn**: fix det search tollerances for Cosmics `reconstruction`  created: 2016-05-12T05:14:06Z merged: 2016-05-24T08:16:32Z

1. [14462](http://github.com/cms-sw/cmssw/pull/14462){:target="_blank"}  from **@kpedro88**: Monitor CASTOR table data (80X) `alca`  `reconstruction`  `simulation`  created: 2016-05-11T19:55:18Z merged: 2016-05-27T08:29:49Z

1. [14445](http://github.com/cms-sw/cmssw/pull/14445){:target="_blank"}  from **@cms-tsg-storm**: HLT development in May (80X) `alca`  `dqm`  `hlt`  created: 2016-05-11T08:02:14Z merged: 2016-05-27T16:38:33Z

1. [14437](http://github.com/cms-sw/cmssw/pull/14437){:target="_blank"}  from **@ggovi**: Changes for O2O deployment and monitoring `db`  created: 2016-05-10T15:45:03Z merged: 2016-05-27T07:41:47Z

1. [14421](http://github.com/cms-sw/cmssw/pull/14421){:target="_blank"}  from **@diguida**: Fixes for RunInfo O2O and cleanup of PopCon interface (80X) `alca`  `db`  created: 2016-05-09T16:51:24Z merged: 2016-05-25T15:52:17Z

1. [14336](http://github.com/cms-sw/cmssw/pull/14336){:target="_blank"}  from **@Martin-Grunewald**: Prescale access for stage-2 environment (80X) `analysis`  `dqm`  `hlt`  `l1`  `reconstruction`  created: 2016-05-03T07:34:46Z merged: 2016-05-29T19:59:22Z

1. [14265](http://github.com/cms-sw/cmssw/pull/14265){:target="_blank"}  from **@mmusich**: DropBox metadata - 2016 (80X) `alca`  `db`  created: 2016-04-27T07:53:31Z merged: 2016-05-23T12:18:29Z

1. [13972](http://github.com/cms-sw/cmssw/pull/13972){:target="_blank"}  from **@fioriNTU**: improve TkMaps `dqm`  created: 2016-04-07T12:13:48Z merged: 2016-05-27T07:42:24Z

1. [13813](http://github.com/cms-sw/cmssw/pull/13813){:target="_blank"}  from **@vkhristenko**: Online HCAL DQM adding a 3rd application `dqm`  created: 2016-03-23T10:56:21Z merged: 2016-05-24T08:20:20Z

#### CMSDIST Changes between Tags REL/CMSSW_8_0_8_patch2/slc6_amd64_gcc530 and REL/CMSSW_8_0_9/slc6_amd64_gcc530:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_8_0_8_patch2/slc6_amd64_gcc530...REL/CMSSW_8_0_9/slc6_amd64_gcc530)



1. [2304](http://github.com/cms-sw/cmssw/pull/2304){:target="_blank"}  from **@cms-sw**: Update data-L1Trigger-L1TMuon.spec created: 2014-02-05T09:24:58Z merged: 2014-02-18T14:52:15Z

1. [2300](http://github.com/cms-sw/cmssw/pull/2300){:target="_blank"}  from **@degano**: Update CUDA to version 7.5.18 created: 2014-02-05T02:27:06Z merged: 2014-02-07T21:24:12Z
