---
layout: post
title:  "7_4_1"
date:   2017-10-07 19:13:38 +0200
categories: cmssw
relmajor: 7
relminor: 4
relsubminor: 1
---

# CMSSW_7_4_1_ROOT5
cms-bot is going to build this release
# CMSSW_7_4_1
#### Changes since CMSSW_7_4_0:

[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_7_4_0...CMSSW_7_4_1)



1. [8872](http://github.com/cms-sw/cmssw/pull/8872){:target="_blank"}  from **@diguida**: Update to simplified ecal pfcluster corrections on top of new Global Tags for PF corrections plus fixes for Run2 MC production `alca`  `reconstruction`  created: 2015-04-24T09:35:51Z merged: 2015-04-25T08:16:49Z

1. [8862](http://github.com/cms-sw/cmssw/pull/8862){:target="_blank"}  from **@bbockelm**: Allow local file system detection to handle bind mounts. `core`  created: 2015-04-24T01:26:46Z merged: 2015-04-24T08:35:07Z

1. [8861](http://github.com/cms-sw/cmssw/pull/8861){:target="_blank"}  from **@Dr15Jones**: Fixed use of hash filename `simulation`  created: 2015-04-23T23:15:19Z merged: 2015-04-24T08:34:39Z

1. [8796](http://github.com/cms-sw/cmssw/pull/8796){:target="_blank"}  from **@ahinzmann**: Add CaloJet pT to MiniAOD `analysis`  created: 2015-04-20T15:28:10Z merged: 2015-04-24T08:19:24Z

1. [8419](http://github.com/cms-sw/cmssw/pull/8419){:target="_blank"}  from **@cwohrman**: add castor lowPTjet trigger and reweight threshold via gain v2 `simulation`  created: 2015-03-19T17:38:03Z merged: 2015-04-24T07:47:12Z

1. [8800](http://github.com/cms-sw/cmssw/pull/8800){:target="_blank"}  from **@lveldere**: FastSim: 74X: bug fix: use same tau DQM plot harvester as FullSim `dqm`  `reconstruction`  `simulation`  created: 2015-04-20T16:33:04Z merged: 2015-04-23T17:45:13Z

1. [8843](http://github.com/cms-sw/cmssw/pull/8843){:target="_blank"}  from **@arizzi**: MINIAOD BUGFIX: pvREF not set for some electrons `analysis`  `reconstruction`  created: 2015-04-23T07:35:05Z merged: 2015-04-23T17:25:04Z

1. [8840](http://github.com/cms-sw/cmssw/pull/8840){:target="_blank"}  from **@cms-l1t-offline**: update L1TRCTParameters for FGCut,HOECut, and EIC Isolation `l1`  created: 2015-04-22T23:49:49Z merged: 2015-04-23T16:59:30Z

1. [8838](http://github.com/cms-sw/cmssw/pull/8838){:target="_blank"}  from **@rappoccio**: Backport from #8837 : Index bug in miniAOD substructure jets `analysis`  created: 2015-04-22T21:12:37Z merged: 2015-04-23T16:21:38Z

1. [8805](http://github.com/cms-sw/cmssw/pull/8805){:target="_blank"}  from **@igv4321**: Hcal noise filters backport `reconstruction`  `simulation`  created: 2015-04-21T00:07:57Z merged: 2015-04-23T13:01:15Z

1. [8847](http://github.com/cms-sw/cmssw/pull/8847){:target="_blank"}  from **@batinkov**: The script dqmdata_cleaner.py is deleted. `dqm`  created: 2015-04-23T08:36:25Z merged: 2015-04-23T12:29:00Z

1. [8831](http://github.com/cms-sw/cmssw/pull/8831){:target="_blank"}  from **@deguio**: avoid having axis resized for LogMessageMonitor `dqm`  created: 2015-04-22T16:11:12Z merged: 2015-04-23T12:12:12Z

1. [8781](http://github.com/cms-sw/cmssw/pull/8781){:target="_blank"}  from **@cms-tsg-storm**: HLT: Fixes and rationalisation/reuse of cfg files for tests `core`  `fastsim`  `hlt`  created: 2015-04-19T19:25:24Z merged: 2015-04-22T14:44:19Z

1. [8820](http://github.com/cms-sw/cmssw/pull/8820){:target="_blank"}  from **@cms-l1t-offline**: update FW version to latest HW `l1`  created: 2015-04-22T05:03:34Z merged: 2015-04-22T14:11:38Z

1. [8779](http://github.com/cms-sw/cmssw/pull/8779){:target="_blank"}  from **@sushilchauhan**: firststep and pixel tracking for 74X and minor fixes as for 73X `dqm`  created: 2015-04-18T17:44:56Z merged: 2015-04-22T14:07:05Z

1. [8765](http://github.com/cms-sw/cmssw/pull/8765){:target="_blank"}  from **@fwyzard**: migrate more modules to be multi-thread safe `analysis`  `hlt`  `reconstruction`  created: 2015-04-17T03:15:08Z merged: 2015-04-21T18:51:23Z

1. [8768](http://github.com/cms-sw/cmssw/pull/8768){:target="_blank"}  from **@fwyzard**: edmPluginHelp: differentiate thread-safe from legacy output modules `core`  created: 2015-04-17T07:40:12Z merged: 2015-04-21T16:11:53Z

1. [8612](http://github.com/cms-sw/cmssw/pull/8612){:target="_blank"}  from **@abbiendi**: Backport to 74X of PR #8199 (cosmicMuonValidation) `dqm`  `reconstruction`  `simulation`  created: 2015-03-31T12:02:03Z merged: 2015-04-21T16:09:49Z

1. [8720](http://github.com/cms-sw/cmssw/pull/8720){:target="_blank"}  from **@emanueledimarco**: Disable Not Working leading edge recovery for saturated ECAL RecHits (7_4_X back-port) `reconstruction`  created: 2015-04-14T08:14:20Z merged: 2015-04-21T16:09:33Z

1. [8760](http://github.com/cms-sw/cmssw/pull/8760){:target="_blank"}  from **@emanueledimarco**: ECAL unpacker: consider the ADC hysteresis in the gain switches (back-port to 74X) `reconstruction`  created: 2015-04-16T10:48:30Z merged: 2015-04-21T16:09:23Z

1. [8773](http://github.com/cms-sw/cmssw/pull/8773){:target="_blank"}  from **@mmarionncern**: Update PF hadron calibration code `reconstruction`  created: 2015-04-17T14:23:48Z merged: 2015-04-21T16:09:03Z

1. [8776](http://github.com/cms-sw/cmssw/pull/8776){:target="_blank"}  from **@silviodonato**: Adding of HLT2PhotonMET `hlt`  created: 2015-04-17T15:32:34Z merged: 2015-04-21T16:08:54Z

1. [8806](http://github.com/cms-sw/cmssw/pull/8806){:target="_blank"}  from **@mdhildreth**: 74X: Set noise off in ES for PreMixing step `simulation`  created: 2015-04-21T00:16:09Z merged: 2015-04-21T16:08:21Z

1. [8755](http://github.com/cms-sw/cmssw/pull/8755){:target="_blank"}  from **@rappoccio**: Fixing reversed distance in accessing subjet collections `analysis`  created: 2015-04-15T19:18:31Z merged: 2015-04-21T16:06:15Z

1. [8757](http://github.com/cms-sw/cmssw/pull/8757){:target="_blank"}  from **@deguio**: fix typo in the definition of the T0 sequences for tracking `dqm`  created: 2015-04-16T10:18:42Z merged: 2015-04-21T16:06:06Z

1. [8750](http://github.com/cms-sw/cmssw/pull/8750){:target="_blank"}  from **@slava77**:  bug fixes in CSC (ME11) trigger primitives for re-emulation; fix ME11 selective readout (fw port of 73X #8664 ) `l1`  `reconstruction`  created: 2015-04-15T15:08:44Z merged: 2015-04-21T16:03:57Z

1. [8689](http://github.com/cms-sw/cmssw/pull/8689){:target="_blank"}  from **@elaird**: add feds `reconstruction`  created: 2015-04-09T11:41:47Z merged: 2015-04-16T00:16:51Z

1. [8722](http://github.com/cms-sw/cmssw/pull/8722){:target="_blank"}  from **@arizzi**: Fix bug in PVAssignment: missing abs for dxy `reconstruction`  created: 2015-04-14T09:10:42Z merged: 2015-04-16T00:04:47Z

1. [8746](http://github.com/cms-sw/cmssw/pull/8746){:target="_blank"}  from **@franzoni**: PU scenarios for TSG RunIISpring15DR74x `operations`  `simulation`  created: 2015-04-15T05:54:04Z merged: 2015-04-16T00:04:00Z

1. [8724](http://github.com/cms-sw/cmssw/pull/8724){:target="_blank"}  from **@bachtis**: Added protection for negative HCAL energy in presence of HO causing NAN in PF `reconstruction`  created: 2015-04-14T10:19:44Z merged: 2015-04-14T22:21:07Z

1. [8568](http://github.com/cms-sw/cmssw/pull/8568){:target="_blank"}  from **@gpetruc**:   Fix logic of tev muon track embedding code (74X version of #8568) `analysis`  created: 2015-03-27T15:11:37Z merged: 2015-04-14T06:34:52Z

1. [8697](http://github.com/cms-sw/cmssw/pull/8697){:target="_blank"}  from **@suchandradutta**: Bug fix in SiStripHotStripAlgorithmFromClusterOccupancy and update on README `alca`  created: 2015-04-10T14:14:07Z merged: 2015-04-14T06:34:37Z

1. [8693](http://github.com/cms-sw/cmssw/pull/8693){:target="_blank"}  from **@cms-tsg-storm**: A few HLT integrations and bug fixes on top of CMSSW_7_4_0 `hlt`  created: 2015-04-10T11:07:22Z merged: 2015-04-14T06:26:45Z

1. [8663](http://github.com/cms-sw/cmssw/pull/8663){:target="_blank"}  from **@wmtan**: fix memory leaks in FastTSGFromPropagation `fastsim`  created: 2015-04-03T22:03:19Z merged: 2015-04-07T08:35:22Z

1. [8585](http://github.com/cms-sw/cmssw/pull/8585){:target="_blank"}  from **@lveldere**: FastSim bugfix for gtDigis (7_4_X) `dqm`  `fastsim`  created: 2015-03-30T09:02:42Z merged: 2015-04-02T10:41:54Z

#### CMSDIST Changes between Tags REL/CMSSW_7_4_0/slc6_amd64_gcc491 and REL/CMSSW_7_4_1/slc6_amd64_gcc491:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_7_4_0/slc6_amd64_gcc491...REL/CMSSW_7_4_1/slc6_amd64_gcc491)



1. [1507](http://github.com/cms-sw/cmssw/pull/1507){:target="_blank"}  from **@davidlt**: Fix broken auto-forward port created: 2013-11-18T23:02:39Z merged: 2013-11-19T15:51:37Z

1. [1503](http://github.com/cms-sw/cmssw/pull/1503){:target="_blank"}  from **@davidlt**: root: incl. ROOT-7245 bugfix created: 2013-11-18T17:21:59Z merged: 2013-11-18T18:50:51Z
