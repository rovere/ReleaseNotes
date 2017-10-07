---
layout: post
title:  "7_6_0"
date:   2017-10-07 19:52:18 +0200
categories: cmssw
relmajor: 7
relminor: 6
relsubminor: 0
---

# CMSSW_7_6_0
#### Changes since CMSSW_7_6_0_pre7:

:arrow_right: Merge due to automatic forward port
[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_7_6_0_pre7...CMSSW_7_6_0)



1. [12198](http://github.com/cms-sw/cmssw/pull/12198){:target="_blank"}  from **@davidlange6**: update to gensim recycling that matches beamspot in GT `comparison`  `pdmv`  created: 2015-10-30T08:09:20Z merged: 2015-10-30T10:23:36Z

1. [12178](http://github.com/cms-sw/cmssw/pull/12178){:target="_blank"}  from **@muell149**: minor updates to path names and axis ranges `comparison`  `dqm`  created: 2015-10-29T17:32:42Z merged: 2015-10-30T13:06:43Z

1. [12168](http://github.com/cms-sw/cmssw/pull/12168){:target="_blank"}  from **@diguida**: Revision of snapshotTime handling in HLT and new Run2 MC GT with ES fixes `alca`  `comparison`  `hlt`  created: 2015-10-29T13:58:22Z merged: 2015-10-30T13:06:29Z

1. [12159](http://github.com/cms-sw/cmssw/pull/12159){:target="_blank"}  from **@pohsun**: ADC region reduced to 100 for strip ClusterStoNCorr summaries. `dqm`  created: 2015-10-29T00:25:18Z merged: 2015-10-30T10:46:47Z

1. [12145](http://github.com/cms-sw/cmssw/pull/12145){:target="_blank"}  from **@fwyzard**: Revert the HCAL method 3 response correction `comparison`  `hlt`  created: 2015-10-28T15:59:44Z merged: 2015-10-28T20:27:09Z

1. [12142](http://github.com/cms-sw/cmssw/pull/12142){:target="_blank"}  from **@fojensen**: add vertex covariance for V0Producer 76x `reconstruction`  created: 2015-10-28T15:00:35Z merged: 2015-10-29T11:01:22Z

1. [12137](http://github.com/cms-sw/cmssw/pull/12137){:target="_blank"}  from **@smorovic**: Monitoring JSON changes in DAQ (76X) `daq`  `dqm`  `hlt`  `reconstruction`  created: 2015-10-28T11:45:13Z merged: 2015-10-30T10:46:58Z

1. [12132](http://github.com/cms-sw/cmssw/pull/12132){:target="_blank"}  from **@gpetruc**: Add hcal fraction to packed candidates (76X) `analysis`  `comparison`  created: 2015-10-27T22:06:48Z merged: 2015-10-30T10:26:17Z

1. [12122](http://github.com/cms-sw/cmssw/pull/12122){:target="_blank"}  from **@gpetruc**: MiniAOD event content updates for 76X `analysis`  created: 2015-10-27T13:51:04Z merged: 2015-10-28T08:14:18Z

1. [12121](http://github.com/cms-sw/cmssw/pull/12121){:target="_blank"}  from **@davidlt**: CalibCalorimetry/EcalLaserAnalyzer: disable object I/O (ClassDef) `alca`  `comparison`  created: 2015-10-27T13:48:59Z merged: 2015-10-28T14:46:27Z

1. [12118](http://github.com/cms-sw/cmssw/pull/12118){:target="_blank"}  from **@mark-grimes**: Take out the era customisations now that L1 comes from GT (76X) `l1`  created: 2015-10-27T12:28:44Z merged: 2015-10-27T17:36:17Z

1. [12117](http://github.com/cms-sw/cmssw/pull/12117){:target="_blank"}  from **@mark-grimes**: Add eras for 2016 and Run 1 (76X) `operations`  created: 2015-10-27T12:20:26Z merged: 2015-10-28T08:16:28Z

1. [12111](http://github.com/cms-sw/cmssw/pull/12111){:target="_blank"}  from **@lgray**: Fix VID python behavior and ignored cuts (76X) `analysis`  created: 2015-10-27T09:56:52Z merged: 2015-10-28T13:16:12Z

1. [12106](http://github.com/cms-sw/cmssw/pull/12106){:target="_blank"}  from **@vkhristenko**: Fixing Offline DQM Bug `dqm`  created: 2015-10-26T20:29:46Z merged: 2015-10-29T12:21:45Z

1. [12100](http://github.com/cms-sw/cmssw/pull/12100){:target="_blank"}  from **@fwyzard**: use dedicated calibrations at HLT `alca`  `hlt`  `reconstruction`  created: 2015-10-26T16:02:41Z merged: 2015-10-28T20:26:08Z

1. [12096](http://github.com/cms-sw/cmssw/pull/12096){:target="_blank"}  from **@cms-l1t-offline**: deprecate caloparams by local config for all but HI work flows `dqm`  `l1`  created: 2015-10-26T13:45:31Z merged: 2015-10-27T17:41:30Z

1. [12080](http://github.com/cms-sw/cmssw/pull/12080){:target="_blank"}  from **@ferencek**: Reverting the src parameter value for PAT jet partons `analysis`  created: 2015-10-23T20:32:56Z merged: 2015-10-28T14:45:06Z

1. [12079](http://github.com/cms-sw/cmssw/pull/12079){:target="_blank"}  from **@mmusich**: New GTs for 76X: Updates for MC DR Production and other fixes `alca`  `hlt`  `operations`  `pdmv`  created: 2015-10-23T19:37:48Z merged: 2015-10-25T21:14:29Z

1. [12078](http://github.com/cms-sw/cmssw/pull/12078){:target="_blank"}  from **@hengne**: relval scripts update after 760pre7 validation `pdmv`  created: 2015-10-23T18:18:55Z merged: 2015-10-26T10:26:24Z

1. [12076](http://github.com/cms-sw/cmssw/pull/12076){:target="_blank"}  from **@slava77**: raise exception if MINIAOD is requested in HeavyIonsRun2 (same as #12075) `operations`  created: 2015-10-23T13:22:31Z merged: 2015-10-24T07:35:06Z

1. [12074](http://github.com/cms-sw/cmssw/pull/12074){:target="_blank"}  from **@gennai**: Alca beam spot harvester fix v2 cmssw 7 6 x `alca`  created: 2015-10-23T11:43:20Z merged: 2015-10-25T14:31:14Z

1. [12072](http://github.com/cms-sw/cmssw/pull/12072){:target="_blank"}  from **@vdutta**: Updates for tracker DQM plots, 76X `dqm`  created: 2015-10-23T10:31:57Z merged: 2015-10-29T12:22:00Z

1. [12068](http://github.com/cms-sw/cmssw/pull/12068){:target="_blank"}  from **@davidlange6**: 76x version of removing invalid detids fix for fastsim pileup `simulation`  created: 2015-10-23T09:11:19Z merged: 2015-10-27T17:41:39Z

1. [12064](http://github.com/cms-sw/cmssw/pull/12064){:target="_blank"}  from **@hengne**: fix era typo `pdmv`  created: 2015-10-23T08:36:48Z merged: 2015-10-24T07:24:40Z

1. [12061](http://github.com/cms-sw/cmssw/pull/12061){:target="_blank"}  from **@ferencek**: Update RelVal input to CMSSW_7_6_0_pre7 `analysis`  `comparison`  created: 2015-10-23T02:05:31Z merged: 2015-10-28T14:44:47Z

1. [12057](http://github.com/cms-sw/cmssw/pull/12057){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-hcx44 Add protection to HcalTopology `geometry`  created: 2015-10-22T20:18:56Z merged: 2015-10-27T06:55:46Z

1. [12053](http://github.com/cms-sw/cmssw/pull/12053){:target="_blank"}  from **@jbrands**: fixing bug for cut-based jet pu ID `reconstruction`  created: 2015-10-22T15:27:21Z merged: 2015-10-28T08:21:25Z

1. [12044](http://github.com/cms-sw/cmssw/pull/12044){:target="_blank"}  from **@fwyzard**: add a label to indentify the PFProducer calibrations `hlt`  `reconstruction`  created: 2015-10-22T09:30:44Z merged: 2015-10-23T08:21:13Z

1. [12041](http://github.com/cms-sw/cmssw/pull/12041){:target="_blank"}  from **@hardenbr**: EcalRechitsDigis fix save behavior to check for end of list 76X `hlt`  created: 2015-10-22T09:16:34Z merged: 2015-10-23T08:26:13Z

1. [12040](http://github.com/cms-sw/cmssw/pull/12040){:target="_blank"}  from **@mandrenguyen**: Adding a vertex smearing configution for pp at 5 TeV, based on latest info from the LHC `comparison`  `operations`  `simulation`  created: 2015-10-22T08:29:55Z merged: 2015-10-28T14:44:30Z

1. [12034](http://github.com/cms-sw/cmssw/pull/12034){:target="_blank"}  from **@mariadalfonso**: METfilters: fix forth bad EE supercluster `analysis`  created: 2015-10-21T21:11:12Z merged: 2015-10-27T14:17:33Z

1. [12031](http://github.com/cms-sw/cmssw/pull/12031){:target="_blank"}  from **@Dr15Jones**: Set ROOT histogram fitting to be thread-safe `reconstruction`  created: 2015-10-21T19:43:07Z merged: 2015-10-24T08:24:36Z

1. [12028](http://github.com/cms-sw/cmssw/pull/12028){:target="_blank"}  from **@lgray**: Fix failing relval missing new ECAL digi params (76X) `simulation`  created: 2015-10-21T17:32:07Z merged: 2015-10-22T12:49:36Z

1. [12024](http://github.com/cms-sw/cmssw/pull/12024){:target="_blank"}  from **@nickmccoll**: Make ClusterMultiplicityFilter multithread safe `reconstruction`  created: 2015-10-21T12:00:28Z merged: 2015-10-22T07:26:16Z

1. [12021](http://github.com/cms-sw/cmssw/pull/12021){:target="_blank"}  from **@threus**: fixed avgfedDigiOccvsLumi ME `dqm`  created: 2015-10-21T11:20:29Z merged: 2015-10-29T12:22:11Z

1. [12020](http://github.com/cms-sw/cmssw/pull/12020){:target="_blank"}  from **@dmitrijus**: Remove unused package DQM/PhysicsHWW `dqm`  created: 2015-10-21T10:56:18Z merged: 2015-10-24T07:33:18Z

1. [12002](http://github.com/cms-sw/cmssw/pull/12002){:target="_blank"}  from **@smdogra**: Reco changes for centralityBin in DQM `dqm`  `reconstruction`  created: 2015-10-20T20:19:54Z merged: 2015-10-29T12:31:28Z

1. [12000](http://github.com/cms-sw/cmssw/pull/12000){:target="_blank"}  from **@wmtan**: Fix packed gen particle copy and move ctors `analysis`  created: 2015-10-20T19:10:40Z merged: 2015-10-21T13:43:57Z

1. [11995](http://github.com/cms-sw/cmssw/pull/11995){:target="_blank"}  from **@fioriNTU**: ready to use cfg for shifters `analysis`  `comparison`  created: 2015-10-20T15:48:06Z merged: 2015-10-27T14:17:55Z

1. [11991](http://github.com/cms-sw/cmssw/pull/11991){:target="_blank"}  from **@nickmccoll**: Removed static analyzer errors from RecoLocalTracker `reconstruction`  created: 2015-10-20T15:22:46Z merged: 2015-10-22T07:26:41Z

1. [11987](http://github.com/cms-sw/cmssw/pull/11987){:target="_blank"}  from **@davidlt**: Double buffer size for 'name1' and 'name2' `dqm`  created: 2015-10-20T13:43:19Z merged: 2015-10-28T10:22:07Z

1. [11981](http://github.com/cms-sw/cmssw/pull/11981){:target="_blank"}  from **@Martin-Grunewald**: Eras for TSG tests `hlt`  created: 2015-10-20T11:37:14Z merged: 2015-10-20T17:21:22Z

1. [11980](http://github.com/cms-sw/cmssw/pull/11980){:target="_blank"}  from **@ggovi**: Introduced new synchronization types in conddb tools `db`  created: 2015-10-20T10:48:51Z merged: 2015-10-26T10:26:38Z

1. [11976](http://github.com/cms-sw/cmssw/pull/11976){:target="_blank"}  from **@smuzaffar**: drop Alignment/CocoaAnalysis package which is sub-set of Alignment/CocoaFit `alca`  created: 2015-10-20T07:46:26Z merged: 2015-10-20T17:24:23Z

1. [11973](http://github.com/cms-sw/cmssw/pull/11973){:target="_blank"}  from **@smuzaffar**: fix duplicateReflexLibrarySearch: look for function name too in classes_def.xml files `core`  created: 2015-10-19T22:32:59Z merged: 2015-10-20T07:08:33Z

1. [11972](http://github.com/cms-sw/cmssw/pull/11972){:target="_blank"}  from **@rovere**: Prevent V0 sim2reco candidate to share the same TrackRef `dqm`  created: 2015-10-19T22:28:13Z merged: 2015-10-20T11:56:26Z

1. [11969](http://github.com/cms-sw/cmssw/pull/11969){:target="_blank"}  from **@pablodecm**: Change cMVAv2 range in DQM to [-1,1] `dqm`  created: 2015-10-19T17:52:51Z merged: 2015-10-22T07:26:52Z

1. [11967](http://github.com/cms-sw/cmssw/pull/11967){:target="_blank"}  from **@lathomas**: Typo in CSCTightHalo2015Filter `analysis`  `reconstruction`  created: 2015-10-19T17:30:06Z merged: 2015-10-30T10:25:52Z

1. [11965](http://github.com/cms-sw/cmssw/pull/11965){:target="_blank"}  from **@Dr15Jones**: Remove last usage of edm::LazyGetter and edm::RefGetter `alca`  `core`  created: 2015-10-19T15:17:54Z merged: 2015-10-21T12:58:04Z

1. [11963](http://github.com/cms-sw/cmssw/pull/11963){:target="_blank"}  from **@davidlange6**: Quieting 76x step2 and step3 `analysis`  `core`  `dqm`  `l1`  `pdmv`  `reconstruction`  `simulation`  created: 2015-10-19T15:17:09Z merged: 2015-10-25T21:16:07Z

1. [11959](http://github.com/cms-sw/cmssw/pull/11959){:target="_blank"}  from **@ggovi**: Replaced synchronization types according to the new policy.  `alca`  `db`  created: 2015-10-19T13:48:45Z merged: 2015-10-26T10:26:43Z

1. [11957](http://github.com/cms-sw/cmssw/pull/11957){:target="_blank"}  from **@davidlt**: Fireworks/Core: remove intrusive macros breaking libstdc++ `comparison`  `visualization`  created: 2015-10-19T12:51:02Z merged: 2015-10-24T08:33:17Z

1. [11956](http://github.com/cms-sw/cmssw/pull/11956){:target="_blank"}  from **@davidlt**: MuonAnalysis/MomentumScaleCalibration: remove intrusive macros breaking libstdc++ `analysis`  created: 2015-10-19T12:28:18Z merged: 2015-10-23T09:28:55Z

1. [11955](http://github.com/cms-sw/cmssw/pull/11955){:target="_blank"}  from **@davidlt**: PerfTools/Callgrind: remove intrusive macros breaking libstdc++ `comparison`  `core`  created: 2015-10-19T12:14:08Z merged: 2015-10-19T15:37:04Z

1. [11954](http://github.com/cms-sw/cmssw/pull/11954){:target="_blank"}  from **@davidlt**: Remove intrusive macros breaking libstdc++ `reconstruction`  created: 2015-10-19T11:54:11Z merged: 2015-10-21T10:01:55Z

1. [11953](http://github.com/cms-sw/cmssw/pull/11953){:target="_blank"}  from **@davidlt**: Remove intrusive macros breaking libstdc++ `reconstruction`  created: 2015-10-19T11:33:14Z merged: 2015-10-21T10:02:01Z

1. [11951](http://github.com/cms-sw/cmssw/pull/11951){:target="_blank"}  from **@davidlt**: DataFormats/EcalDigi: remove intrusive macros breaking libstdc++ `comparison`  `core`  `simulation`  created: 2015-10-19T09:34:20Z merged: 2015-10-19T15:37:22Z

1. [11863](http://github.com/cms-sw/cmssw/pull/11863){:target="_blank"}  from **@davidlange6**: revert back the 75x automerge for HLT config v4 `comparison`  `hlt`  created: 2015-10-18T07:59:41Z merged: 2015-10-18T08:37:17Z

1. [11862](http://github.com/cms-sw/cmssw/pull/11862){:target="_blank"}  from **@davidlange6**: guard against era being none `comparison`  `operations`  created: 2015-10-17T10:30:16Z merged: 2015-10-17T10:42:53Z

1. [11860](http://github.com/cms-sw/cmssw/pull/11860){:target="_blank"}  from **@davidlange6**: fix up recently introduced problems  in IB tests `comparison`  `pdmv`  `reconstruction`  created: 2015-10-17T08:13:53Z merged: 2015-10-17T18:40:49Z

1. [11855](http://github.com/cms-sw/cmssw/pull/11855){:target="_blank"}  from **@rappoccio**: Adding no-HF grid-based rho (76x forward-port #11773), and fixing existing bugged central rho values `reconstruction`  created: 2015-10-16T17:16:01Z merged: 2015-10-23T08:21:46Z

1. [11854](http://github.com/cms-sw/cmssw/pull/11854){:target="_blank"}  from **@makortel**: Fix TrackingVertex->TrackingParticle links in premixing `simulation`  created: 2015-10-16T14:32:03Z merged: 2015-10-21T09:57:14Z

1. [11848](http://github.com/cms-sw/cmssw/pull/11848){:target="_blank"}  from **@davidlt**: Remove constexpr from ringOrder `reconstruction`  created: 2015-10-16T10:04:38Z merged: 2015-10-19T09:56:43Z

1. [11847](http://github.com/cms-sw/cmssw/pull/11847){:target="_blank"}  from **@Dr15Jones**: Removed unnecessary include and forward declaration of RefGetter `hlt`  `reconstruction`  created: 2015-10-16T10:00:50Z merged: 2015-10-17T18:41:19Z

1. [11846](http://github.com/cms-sw/cmssw/pull/11846){:target="_blank"}  from **@Dr15Jones**: Removed edm::LazyGetter<> related dictionaries `reconstruction`  created: 2015-10-16T10:00:00Z merged: 2015-10-19T10:01:42Z

1. [11843](http://github.com/cms-sw/cmssw/pull/11843){:target="_blank"}  from **@davidlt**: DataFormats/Common: change from std::swap to edm::swap `core`  created: 2015-10-16T08:40:00Z merged: 2015-10-16T19:56:15Z

1. [11838](http://github.com/cms-sw/cmssw/pull/11838){:target="_blank"}  from **@jhgoh**: bugfix: assign muon PDG id using PFMuon charge `reconstruction`  created: 2015-10-15T23:33:07Z merged: 2015-10-19T10:01:47Z

1. [11835](http://github.com/cms-sw/cmssw/pull/11835){:target="_blank"}  from **@BetterWang**: EP code bug fix `reconstruction`  created: 2015-10-15T20:22:15Z merged: 2015-10-19T09:57:00Z

1. [11833](http://github.com/cms-sw/cmssw/pull/11833){:target="_blank"}  from @bendavid: add additional shower setting (formally) needed for consistent aMC**@NL** `comparison`  `generators`  created: 2015-10-15T18:05:36Z merged: 2015-10-16T05:23:21Z

1. [11832](http://github.com/cms-sw/cmssw/pull/11832){:target="_blank"}  from **@capalmer85**: PCC ntupler 76x - October2015 `reconstruction`  created: 2015-10-15T17:26:59Z merged: 2015-10-23T08:21:52Z

1. [11831](http://github.com/cms-sw/cmssw/pull/11831){:target="_blank"}  from **@rovere**: Flag the globalEfficiencies plot in the DQMGenericClient `dqm`  created: 2015-10-15T16:42:05Z merged: 2015-10-19T10:06:35Z

1. [11828](http://github.com/cms-sw/cmssw/pull/11828){:target="_blank"}  from **@hroskes**: No more cmsStage etc. scripts `alca`  `analysis`  created: 2015-10-15T16:39:32Z merged: 2015-10-20T11:51:40Z

1. [11827](http://github.com/cms-sw/cmssw/pull/11827){:target="_blank"}  from **@Dr15Jones**: Made RefCore and RefCoreWithIndex icc compatible `core`  created: 2015-10-15T15:37:00Z merged: 2015-10-16T19:56:37Z

1. [11825](http://github.com/cms-sw/cmssw/pull/11825){:target="_blank"}  from **@barvic**: 76X - Fix for handling of rare case of CFEB data corruption `reconstruction`  created: 2015-10-15T15:32:37Z merged: 2015-10-16T13:06:36Z

1. [11823](http://github.com/cms-sw/cmssw/pull/11823){:target="_blank"}  from **@mark-grimes**: Fix --dump_python option in cmsDriver `comparison`  `operations`  created: 2015-10-15T15:18:10Z merged: 2015-10-16T20:05:15Z

1. [11820](http://github.com/cms-sw/cmssw/pull/11820){:target="_blank"}  from **@sethzenz**: Prevent VirtualJetProducer from wasting time on setup if input empty `reconstruction`  created: 2015-10-15T14:48:14Z merged: 2015-10-19T10:02:03Z

1. [11819](http://github.com/cms-sw/cmssw/pull/11819){:target="_blank"}  from **@govoni**: Update TTbar_13TeV_TuneCUETP8M1_cfi.py `comparison`  `generators`  created: 2015-10-15T14:00:59Z merged: 2015-10-16T05:50:26Z

1. [11817](http://github.com/cms-sw/cmssw/pull/11817){:target="_blank"}  from **@mark-grimes**: Make the L1REPACK step work with the Run 2 eras `fastsim`  `l1`  `operations`  created: 2015-10-15T13:14:45Z merged: 2015-10-16T06:00:29Z

1. [11814](http://github.com/cms-sw/cmssw/pull/11814){:target="_blank"}  from **@Dr15Jones**: removed unused SiStripMonitorMuonHLT `dqm`  created: 2015-10-15T12:52:33Z merged: 2015-10-16T05:23:42Z

1. [11813](http://github.com/cms-sw/cmssw/pull/11813){:target="_blank"}  from **@dmitrijus**: Fix statics in CastorDigiMonitor. `dqm`  created: 2015-10-15T12:09:54Z merged: 2015-10-24T07:32:05Z

1. [11812](http://github.com/cms-sw/cmssw/pull/11812){:target="_blank"}  from **@Dr15Jones**: Removed unused HITSiStripRawToClustersRoI `alca`  created: 2015-10-15T09:30:21Z merged: 2015-10-15T12:41:15Z

1. [11811](http://github.com/cms-sw/cmssw/pull/11811){:target="_blank"}  from **@fabozzi**: added FEVTDEBUGHLT as output of step2 data relvals `pdmv`  created: 2015-10-15T09:20:45Z merged: 2015-10-21T10:02:16Z

1. [11810](http://github.com/cms-sw/cmssw/pull/11810){:target="_blank"}  from **@Dr15Jones**: Removed old LazyGetter calls from HLTDummyCollections `hlt`  created: 2015-10-15T08:44:10Z merged: 2015-10-15T12:51:15Z

1. [11807](http://github.com/cms-sw/cmssw/pull/11807){:target="_blank"}  from **@alja**: 75x Fireworks: fix MuonDigi accessor type `comparison`  `visualization`  created: 2015-10-14T22:46:54Z merged: 2015-10-15T07:36:12Z

1. [11804](http://github.com/cms-sw/cmssw/pull/11804){:target="_blank"}  from **@mbandrews**: Fix TestPulse RMS binning and output `dqm`  created: 2015-10-14T22:25:36Z merged: 2015-10-16T05:24:51Z

1. [11801](http://github.com/cms-sw/cmssw/pull/11801){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-hcx42 Bug fix for HcalTopology `geometry`  created: 2015-10-14T20:03:15Z merged: 2015-10-15T08:00:49Z

1. [11800](http://github.com/cms-sw/cmssw/pull/11800){:target="_blank"}  from **@diguida**: New Global Tags with cleanup and fixes for all scenarios. `alca`  created: 2015-10-14T19:30:23Z merged: 2015-10-15T12:41:30Z

1. [11798](http://github.com/cms-sw/cmssw/pull/11798){:target="_blank"}  from **@vandreev11**: Fix a typo in MaterialNames, new material in HGCEE `geometry`  created: 2015-10-14T17:19:14Z merged: 2015-10-19T10:02:08Z

1. [11790](http://github.com/cms-sw/cmssw/pull/11790){:target="_blank"}  from **@lveldere**: FastSim : muon validation : use fastsim era to define fastsim customs `dqm`  `fastsim`  `simulation`  created: 2015-10-14T14:11:33Z merged: 2015-10-29T07:21:01Z

1. [11789](http://github.com/cms-sw/cmssw/pull/11789){:target="_blank"}  from **@dertexaner**: Switch default HBHENoiseFilter settings to Run2-25ns configuration V2 - 76X `reconstruction`  `simulation`  created: 2015-10-14T14:10:52Z merged: 2015-10-23T08:21:58Z

1. [11788](http://github.com/cms-sw/cmssw/pull/11788){:target="_blank"}  from **@Dr15Jones**: Removed API for RefGetter and LazyGetter from EcalRegionCabling `reconstruction`  created: 2015-10-14T13:26:42Z merged: 2015-10-19T10:02:14Z

1. [11785](http://github.com/cms-sw/cmssw/pull/11785){:target="_blank"}  from **@smuzaffar**: remove duplicate run2 2015C workflows which were auto-forward ported from 75X `comparison`  `pdmv`  created: 2015-10-14T11:25:11Z merged: 2015-10-14T13:41:50Z

1. [11784](http://github.com/cms-sw/cmssw/pull/11784){:target="_blank"}  from **@lgray**: Add possibility for partial ECAL digitization (towards working HGCAL) `simulation`  created: 2015-10-14T10:29:42Z merged: 2015-10-19T10:06:46Z

1. [11783](http://github.com/cms-sw/cmssw/pull/11783){:target="_blank"}  from **@lveldere**: Fastsim: HF: use shower library also for run1 `fastsim`  `simulation`  created: 2015-10-14T08:06:38Z merged: 2015-10-22T13:01:54Z

1. [11779](http://github.com/cms-sw/cmssw/pull/11779){:target="_blank"}  from **@fwyzard**: make the behaviour of cmsRun and edmConfigDump more consistent `core`  created: 2015-10-13T23:50:04Z merged: 2015-10-16T13:06:57Z

1. [11772](http://github.com/cms-sw/cmssw/pull/11772){:target="_blank"}  from **@wmtan**: get rid of const_cast `core`  created: 2015-10-13T17:15:12Z merged: 2015-10-14T08:51:26Z

1. [11769](http://github.com/cms-sw/cmssw/pull/11769){:target="_blank"}  from **@igv4321**: Hcal simple reconstructor with method3 `reconstruction`  created: 2015-10-13T16:44:55Z merged: 2015-10-23T08:26:49Z

1. [11768](http://github.com/cms-sw/cmssw/pull/11768){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-gem10 Changes due to absent short chambers in GE21 `geometry`  created: 2015-10-13T16:36:11Z merged: 2015-10-19T10:02:20Z

1. [11766](http://github.com/cms-sw/cmssw/pull/11766){:target="_blank"}  from **@cms-tau-pog**: 3prong1pi0 new dms `reconstruction`  created: 2015-10-13T16:08:46Z merged: 2015-10-23T08:27:00Z

1. [11761](http://github.com/cms-sw/cmssw/pull/11761){:target="_blank"}  from **@slava77**: pick ecal fraction of 0 for a candidate with trackMomentum 0 (same as #11302 and  #11760) `comparison`  `reconstruction`  created: 2015-10-13T14:20:24Z merged: 2015-10-14T08:47:35Z

1. [11760](http://github.com/cms-sw/cmssw/pull/11760){:target="_blank"}  from **@slava77**: pick ecal fraction of 0 for a candidate with trackMomentum 0 (same as #11302) `reconstruction`  created: 2015-10-13T14:12:59Z merged: 2015-10-15T07:36:30Z

1. [11759](http://github.com/cms-sw/cmssw/pull/11759){:target="_blank"}  from **@Dr15Jones**: Remove use of non-const static in pat::UserData<> `analysis`  created: 2015-10-13T13:27:47Z merged: 2015-10-15T12:48:59Z

1. [11758](http://github.com/cms-sw/cmssw/pull/11758){:target="_blank"}  from **@Dr15Jones**: Made static const in LimiDetails `reconstruction`  created: 2015-10-13T12:53:05Z merged: 2015-10-16T05:26:20Z

1. [11757](http://github.com/cms-sw/cmssw/pull/11757){:target="_blank"}  from **@Dr15Jones**: Changed static to const in ClusterFP420 `reconstruction`  created: 2015-10-13T12:24:07Z merged: 2015-10-15T05:17:39Z

1. [11751](http://github.com/cms-sw/cmssw/pull/11751){:target="_blank"}  from **@dertexaner**: Adding HBHENegativeNoise bit to HcalRecHitFlagsToBeExcluded - 76X `reconstruction`  created: 2015-10-13T11:22:40Z merged: 2015-10-23T09:30:13Z

1. [11749](http://github.com/cms-sw/cmssw/pull/11749){:target="_blank"}  from **@Dr15Jones**: Made static const in MuonSelectors `reconstruction`  created: 2015-10-13T10:48:58Z merged: 2015-10-15T05:17:23Z

1. [11748](http://github.com/cms-sw/cmssw/pull/11748){:target="_blank"}  from **@Dr15Jones**: Fix thread safety problem in ParametrizationHelper::fromString `analysis`  created: 2015-10-13T10:36:49Z merged: 2015-10-15T05:17:07Z

1. [11746](http://github.com/cms-sw/cmssw/pull/11746){:target="_blank"}  from **@Dr15Jones**: Removed unnecessary const_cast in DataFormats/L1GlobalTrigger `l1`  created: 2015-10-13T09:52:06Z merged: 2015-10-15T05:16:51Z

1. [11745](http://github.com/cms-sw/cmssw/pull/11745){:target="_blank"}  from **@Dr15Jones**: Remove unnecessary const cast away in LTCDigi `l1`  created: 2015-10-13T09:21:53Z merged: 2015-10-15T05:16:36Z

1. [11744](http://github.com/cms-sw/cmssw/pull/11744){:target="_blank"}  from **@davidlt**: [UB] Initialize 'WasDecodingOk_' in 'EcalDCCHeaderRuntypeDecoder' `reconstruction`  created: 2015-10-13T09:13:40Z merged: 2015-10-15T05:16:22Z

1. [11743](http://github.com/cms-sw/cmssw/pull/11743){:target="_blank"}  from **@Dr15Jones**: Fix problems found by static analyzer in DataFormats/Scalers `daq`  `l1`  `reconstruction`  created: 2015-10-13T09:05:24Z merged: 2015-10-20T11:52:01Z

1. [11742](http://github.com/cms-sw/cmssw/pull/11742){:target="_blank"}  from **@slava77**: fix wrong auto-forward-port of RecoTLR of  #11741  `operations`  created: 2015-10-13T08:14:35Z merged: 2015-10-15T05:16:03Z

1. [11741](http://github.com/cms-sw/cmssw/pull/11741){:target="_blank"}  from **@slava77**: heavyIonsRun2 scenario for data processing `dqm`  `operations`  created: 2015-10-12T23:38:58Z merged: 2015-10-13T07:29:23Z

1. [11738](http://github.com/cms-sw/cmssw/pull/11738){:target="_blank"}  from **@lgray**: EGM ID Updates from recipes (76X) `analysis`  `reconstruction`  created: 2015-10-12T22:01:02Z merged: 2015-10-20T17:17:38Z

1. [11737](http://github.com/cms-sw/cmssw/pull/11737){:target="_blank"}  from **@lathomas**: Tuning the CSC Halo filter parameters `reconstruction`  created: 2015-10-12T21:22:52Z merged: 2015-10-15T12:42:19Z

1. [11734](http://github.com/cms-sw/cmssw/pull/11734){:target="_blank"}  from **@davidlt**: Fix UB by settting firstStep in AnnealingGhostTrackFitter `reconstruction`  created: 2015-10-12T15:20:03Z merged: 2015-10-15T05:22:56Z

1. [11728](http://github.com/cms-sw/cmssw/pull/11728){:target="_blank"}  from **@davidlt**: Add _UBSAN_ to CMSSW `comparison`  `core`  created: 2015-10-12T07:58:21Z merged: 2015-10-19T15:33:31Z

1. [11727](http://github.com/cms-sw/cmssw/pull/11727){:target="_blank"}  from **@serval2412**: cppcheck: Prefer prefix ++/-- operators for non-primitive types `alca`  created: 2015-10-11T21:12:41Z merged: 2015-10-15T12:46:26Z

1. [11726](http://github.com/cms-sw/cmssw/pull/11726){:target="_blank"}  from **@dertexaner**: HBHE isolated noise reflagger retuning for Run2 `reconstruction`  created: 2015-10-11T20:52:08Z merged: 2015-10-23T08:27:10Z

1. [11724](http://github.com/cms-sw/cmssw/pull/11724){:target="_blank"}  from **@Dr15Jones**: Fix python2.6 SyntaxError. `comparison`  `core`  created: 2015-10-11T13:10:14Z merged: 2015-10-11T14:27:48Z

1. [11721](http://github.com/cms-sw/cmssw/pull/11721){:target="_blank"}  from **@davidlt**: DQM/PixelLumi: definite static const int members `dqm`  created: 2015-10-10T13:09:05Z merged: 2015-10-15T05:21:02Z

1. [11720](http://github.com/cms-sw/cmssw/pull/11720){:target="_blank"}  from **@fwyzard**: cmsCheckMultithreading replaced by edmCheckmultithreading `hlt`  created: 2015-10-10T11:37:22Z merged: 2015-10-11T14:31:10Z

1. [11719](http://github.com/cms-sw/cmssw/pull/11719){:target="_blank"}  from **@fwyzard**: cmsCheckMultithreading replaced by edmCheckmultithreading `hlt`  created: 2015-10-10T11:37:16Z merged: 2015-10-12T12:36:19Z

1. [11716](http://github.com/cms-sw/cmssw/pull/11716){:target="_blank"}  from **@vandreev11**: Hgcal v7geometry xml files `geometry`  created: 2015-10-09T18:01:39Z merged: 2015-10-12T20:26:12Z

1. [11715](http://github.com/cms-sw/cmssw/pull/11715){:target="_blank"}  from **@silviodonato**: HLT BTV DQM offline - safe for missing collections `dqm`  created: 2015-10-09T15:37:52Z merged: 2015-10-15T05:20:45Z

1. [11714](http://github.com/cms-sw/cmssw/pull/11714){:target="_blank"}  from **@Dr15Jones**: Removed unused typedef from HLTTrackHaloFilter `hlt`  created: 2015-10-09T15:20:11Z merged: 2015-10-11T14:36:24Z

1. [11713](http://github.com/cms-sw/cmssw/pull/11713){:target="_blank"}  from **@Dr15Jones**: Removed unused DetSetLazyVector class `core`  created: 2015-10-09T14:50:02Z merged: 2015-10-11T14:36:29Z

1. [11711](http://github.com/cms-sw/cmssw/pull/11711){:target="_blank"}  from **@bsunanda**: bsunanda: Run2-hcx40 Update the hit validation package to match Phase2 simulation  `dqm`  created: 2015-10-09T07:10:34Z merged: 2015-10-16T13:12:09Z

1. [11710](http://github.com/cms-sw/cmssw/pull/11710){:target="_blank"}  from **@slehti**: HLTTauDQM: Bugfix `dqm`  created: 2015-10-09T06:13:08Z merged: 2015-10-15T05:19:52Z

1. [11708](http://github.com/cms-sw/cmssw/pull/11708){:target="_blank"}  from **@hengne**: Relval update after 7_6_0_pre6 `generators`  `pdmv`  created: 2015-10-09T06:07:35Z merged: 2015-10-13T07:26:44Z

1. [11706](http://github.com/cms-sw/cmssw/pull/11706){:target="_blank"}  from **@Dr15Jones**: const thread-safe packed classes `analysis`  created: 2015-10-09T03:49:01Z merged: 2015-10-15T05:19:19Z

1. [11705](http://github.com/cms-sw/cmssw/pull/11705){:target="_blank"}  from **@lihux25**: Fix the duplicated HF channels `reconstruction`  created: 2015-10-08T22:30:07Z merged: 2015-10-12T12:41:23Z

1. [11704](http://github.com/cms-sw/cmssw/pull/11704){:target="_blank"}  from **@lihux25**: Fix the duplicated HF channels `reconstruction`  created: 2015-10-08T22:17:40Z merged: 2015-10-11T14:31:26Z

1. [11694](http://github.com/cms-sw/cmssw/pull/11694){:target="_blank"}  from **@ndaci**: Added new categories (DSTJets,DSTMuons) for scouting triggers. `dqm`  created: 2015-10-08T15:39:04Z merged: 2015-10-15T12:51:25Z

1. [11690](http://github.com/cms-sw/cmssw/pull/11690){:target="_blank"}  from **@mark-grimes**: Switch AddOn tests to use Run 2 eras `comparison`  `core`  created: 2015-10-08T13:30:33Z merged: 2015-10-26T13:36:54Z

1. [11688](http://github.com/cms-sw/cmssw/pull/11688){:target="_blank"}  from **@cms-btv-pog**: Switch on hadronFlavourHasPriority for b-tag Validation module. `dqm`  created: 2015-10-08T09:53:10Z merged: 2015-10-15T07:36:50Z

1. [11685](http://github.com/cms-sw/cmssw/pull/11685){:target="_blank"}  from **@cms-btv-pog**: b-tag GBRForest payloads from GT `analysis`  `reconstruction`  created: 2015-10-08T05:53:08Z merged: 2015-10-16T06:03:04Z

1. [11683](http://github.com/cms-sw/cmssw/pull/11683){:target="_blank"}  from **@mrcarver**: Removed JetIdCleaning from SUSY path names (CMSHLT-601 for 76X) `dqm`  created: 2015-10-07T20:33:24Z merged: 2015-10-15T12:51:31Z

1. [11680](http://github.com/cms-sw/cmssw/pull/11680){:target="_blank"}  from **@wmtan**: Replace LinkDef file witl XML selection file in PhysicsTools/TagAndProbe `analysis`  created: 2015-10-07T20:15:05Z merged: 2015-10-26T14:56:30Z

1. [11676](http://github.com/cms-sw/cmssw/pull/11676){:target="_blank"}  from **@richard-cms**: L1 MHT and forward Jet fixes `l1`  created: 2015-10-07T18:57:24Z merged: 2015-10-11T14:31:31Z

1. [11673](http://github.com/cms-sw/cmssw/pull/11673){:target="_blank"}  from **@wmtan**: Replace LinkDef files with XML selextion files.in CalibCalorimetry/EcalLaserAnalyzer `alca`  created: 2015-10-07T18:40:06Z merged: 2015-10-12T12:31:15Z

1. [11671](http://github.com/cms-sw/cmssw/pull/11671){:target="_blank"}  from **@nhanvtran**: update to PUPPI;speedup, low PU corr `analysis`  `reconstruction`  created: 2015-10-07T16:12:03Z merged: 2015-10-23T08:23:21Z

1. [11670](http://github.com/cms-sw/cmssw/pull/11670){:target="_blank"}  from **@ianna**: Thread-safe DB Geometry Builders `db`  created: 2015-10-07T15:54:12Z merged: 2015-10-27T06:56:32Z

1. [11666](http://github.com/cms-sw/cmssw/pull/11666){:target="_blank"}  from **@makortel**: Fix the definition of pileup tracks in MultiTrackValidator `dqm`  created: 2015-10-07T09:38:31Z merged: 2015-10-15T06:01:15Z

1. [11661](http://github.com/cms-sw/cmssw/pull/11661){:target="_blank"}  from **@wmtan**: replace most LinkDef.h files with XML selection files `alca`  `analysis`  `db`  `dqm`  `reconstruction`  `simulation`  created: 2015-10-06T20:12:39Z merged: 2015-10-17T09:10:13Z

1. [11657](http://github.com/cms-sw/cmssw/pull/11657){:target="_blank"}  from **@gsafronov**: 75X: fix pT selection in HLTrigger/special/src/HLTPixlMBFilt.cc `comparison`  `hlt`  created: 2015-10-06T16:07:37Z merged: 2015-10-15T07:35:18Z

1. [11653](http://github.com/cms-sw/cmssw/pull/11653){:target="_blank"}  from **@rovere**: Restore v0 validation   `dqm`  `reconstruction`  `simulation`  created: 2015-10-06T14:38:42Z merged: 2015-10-15T05:22:06Z

1. [11652](http://github.com/cms-sw/cmssw/pull/11652){:target="_blank"}  from **@ianna**: Extended 2019 Scenario Scripts `db`  created: 2015-10-06T13:12:00Z merged: 2015-10-12T12:31:46Z

1. [11651](http://github.com/cms-sw/cmssw/pull/11651){:target="_blank"}  from **@lgray**: Forward port HGCalRecAlgos/Producers from CMSSW_6_2_0_SLHC26_patch3 (76X) `reconstruction`  created: 2015-10-06T13:04:14Z merged: 2015-10-11T14:36:37Z

1. [11644](http://github.com/cms-sw/cmssw/pull/11644){:target="_blank"}  from **@jmduarte**: RazorHbb HLT DQM for 76X `dqm`  created: 2015-10-06T05:48:59Z merged: 2015-10-15T06:06:19Z

1. [11638](http://github.com/cms-sw/cmssw/pull/11638){:target="_blank"}  from **@alja**: 75x Fireworks: fix problem with muon global track propagation `comparison`  `visualization`  created: 2015-10-05T16:30:42Z merged: 2015-10-12T12:36:37Z

1. [11636](http://github.com/cms-sw/cmssw/pull/11636){:target="_blank"}  from **@jasperlauwers**: Adding VBF H to Invisible paths + associated code fix `dqm`  created: 2015-10-05T14:09:05Z merged: 2015-10-15T06:01:26Z

1. [11624](http://github.com/cms-sw/cmssw/pull/11624){:target="_blank"}  from **@makortel**: Migrate away from explicit comparisons of GeomDetEnumerators::PixelBarrel/PixelEndcap `alca`  `fastsim`  `geometry`  `reconstruction`  created: 2015-10-02T15:02:58Z merged: 2015-10-16T13:12:43Z

1. [11615](http://github.com/cms-sw/cmssw/pull/11615){:target="_blank"}  from **@cmkuo**: fix ES unpacker when the 2nd OptoRX is diabled, but the 1t and 3rd Op `reconstruction`  created: 2015-10-02T03:33:05Z merged: 2015-10-12T12:41:39Z

1. [11604](http://github.com/cms-sw/cmssw/pull/11604){:target="_blank"}  from **@kkrajczar**: For HI HLT: migration of 5 HI tracking modules to stream modules (75X backport) `reconstruction`  created: 2015-10-01T16:06:26Z merged: 2015-10-12T12:41:45Z

1. [11594](http://github.com/cms-sw/cmssw/pull/11594){:target="_blank"}  from **@ggovi**: Back-port of several fixes and improvements for the conddb tools `db`  created: 2015-10-01T13:12:15Z merged: 2015-10-12T12:36:43Z

1. [11586](http://github.com/cms-sw/cmssw/pull/11586){:target="_blank"}  from **@Martin-Grunewald**: Addition of PFMET to Trigger Data Formats (75X) `hlt`  created: 2015-10-01T07:25:12Z merged: 2015-10-13T07:31:56Z

1. [11551](http://github.com/cms-sw/cmssw/pull/11551){:target="_blank"}  from **@dmitrijus**: A fix for the DQMStreamerReader (75x) `dqm`  created: 2015-09-29T14:27:12Z merged: 2015-10-12T12:36:50Z

1. [11548](http://github.com/cms-sw/cmssw/pull/11548){:target="_blank"}  from **@cms-tsg-storm**: 76X hlt25ns round six `fastsim`  `hlt`  created: 2015-09-29T12:22:41Z merged: 2015-10-16T13:12:51Z

1. [11545](http://github.com/cms-sw/cmssw/pull/11545){:target="_blank"}  from **@sushilchauhan**: fix for LS range of fit if there are no event processed in a LS `dqm`  created: 2015-09-29T12:11:46Z merged: 2015-10-12T12:36:57Z

1. [11541](http://github.com/cms-sw/cmssw/pull/11541){:target="_blank"}  from **@hengne**: relval scripts update, 2015c data workflows, a couple of fixes. `alca`  `hlt`  `pdmv`  `simulation`  created: 2015-09-29T10:27:35Z merged: 2015-10-13T07:32:08Z

1. [11536](http://github.com/cms-sw/cmssw/pull/11536){:target="_blank"}  from **@smorovic**: Checksum parameter cfi export (75X) `daq`  `reconstruction`  created: 2015-09-28T16:53:47Z merged: 2015-10-12T12:37:03Z

1. [11531](http://github.com/cms-sw/cmssw/pull/11531){:target="_blank"}  from **@taroni**: fixing emulator fenix bug `l1`  created: 2015-09-28T14:18:10Z merged: 2015-10-12T12:51:19Z

1. [11523](http://github.com/cms-sw/cmssw/pull/11523){:target="_blank"}  from **@arcidiac**: Fix for the Streams' names to be monitored `dqm`  created: 2015-09-28T11:04:20Z merged: 2015-10-15T09:27:08Z

1. [11521](http://github.com/cms-sw/cmssw/pull/11521){:target="_blank"}  from **@slehti**: Bugfix in HLTTauDQMPath affecting L2 plots `dqm`  created: 2015-09-28T10:18:05Z merged: 2015-10-12T12:41:51Z

1. [11509](http://github.com/cms-sw/cmssw/pull/11509){:target="_blank"}  from **@fwyzard**: hltDiff: compare TriggerResults event by event (75x) `comparison`  `hlt`  created: 2015-09-26T10:38:39Z merged: 2015-10-12T15:16:43Z

1. [11497](http://github.com/cms-sw/cmssw/pull/11497){:target="_blank"}  from **@kpedro88**: merge SLHC updates for CaloTowers `alca`  `db`  `geometry`  `hlt`  `reconstruction`  `simulation`  created: 2015-09-25T18:33:14Z merged: 2015-10-20T11:52:31Z

1. [11484](http://github.com/cms-sw/cmssw/pull/11484){:target="_blank"}  from **@cms-tsg-storm**: 75X hlt25ns round5 plus updated frozenv4 `hlt`  created: 2015-09-25T08:15:21Z merged: 2015-10-15T07:51:39Z

1. [11474](http://github.com/cms-sw/cmssw/pull/11474){:target="_blank"}  from **@davidlange6**: Fix mistakes in hcal customise function created: 2015-09-24T20:02:55Z merged: 2015-09-24T20:03:31Z

1. [11464](http://github.com/cms-sw/cmssw/pull/11464){:target="_blank"}  from **@threus**: updated x-axes for several SiStripDQM MEs (75x) `dqm`  created: 2015-09-24T16:04:58Z merged: 2015-10-12T12:37:22Z

1. [11457](http://github.com/cms-sw/cmssw/pull/11457){:target="_blank"}  from **@smorovic**: Freeing INI file buffer after writing the file is finished (75X) `core`  created: 2015-09-24T13:45:05Z merged: 2015-10-12T12:42:14Z

1. [11444](http://github.com/cms-sw/cmssw/pull/11444){:target="_blank"}  from **@dinardo**: Now the code is able to handle non consecutive LS `dqm`  created: 2015-09-23T22:43:36Z merged: 2015-10-15T07:56:40Z

1. [11417](http://github.com/cms-sw/cmssw/pull/11417){:target="_blank"}  from **@argiro**: PositionCalc Fix `reconstruction`  created: 2015-09-22T09:55:43Z merged: 2015-10-12T12:46:26Z

1. [11406](http://github.com/cms-sw/cmssw/pull/11406){:target="_blank"}  from **@lgray**: Fix sigmaIetaIphi for photon regression (75X) `reconstruction`  created: 2015-09-21T22:21:53Z merged: 2015-10-12T12:51:31Z

1. [11400](http://github.com/cms-sw/cmssw/pull/11400){:target="_blank"}  from **@Dr15Jones**: Change mayConsume to conditional consumes in PATJetProducer `analysis`  created: 2015-09-21T15:57:24Z merged: 2015-09-28T13:32:30Z

1. [11391](http://github.com/cms-sw/cmssw/pull/11391){:target="_blank"}  from **@Martin-Grunewald**: 75X: New GT with L1T v5 and thus new HLT selection `alca`  `hlt`  created: 2015-09-21T10:44:06Z merged: 2015-10-15T09:27:14Z

1. [11362](http://github.com/cms-sw/cmssw/pull/11362){:target="_blank"}  from **@cms-met**: Change the type1 jet pt threshold from 10 to 15 GeV `analysis`  created: 2015-09-18T15:59:36Z merged: 2015-10-12T12:51:36Z

1. [11251](http://github.com/cms-sw/cmssw/pull/11251){:target="_blank"}  from **@dmitrijus**:   Replace mark-and-delete at next merge algorithm in DQMStore (76x) `dqm`  created: 2015-09-15T11:07:21Z merged: 2015-10-27T17:39:14Z

1. [11131](http://github.com/cms-sw/cmssw/pull/11131){:target="_blank"}  from **@wouf**: Update Hydjet2 and Hydjet1 `generators`  created: 2015-09-04T14:37:46Z merged: 2015-10-29T16:32:10Z

1. [11096](http://github.com/cms-sw/cmssw/pull/11096){:target="_blank"}  from **@VinInn**: fix inner outer for OutIn in 75X `reconstruction`  created: 2015-09-03T08:49:50Z merged: 2015-10-12T12:42:21Z

1. [11060](http://github.com/cms-sw/cmssw/pull/11060){:target="_blank"}  from **@duanders**: Use new primary vertex filter in hotline and high MET skim `alca`  `pdmv`  created: 2015-09-01T09:48:37Z merged: 2015-10-29T12:26:43Z

1. [10839](http://github.com/cms-sw/cmssw/pull/10839){:target="_blank"}  from **@yetkinyilmaz**: Option for DAS query in ConfigBuilder 75X `comparison`  `operations`  created: 2015-08-18T11:57:25Z merged: 2015-10-13T07:37:30Z

1. [10517](http://github.com/cms-sw/cmssw/pull/10517){:target="_blank"}  from **@alberto-sanchez**: Adding Onia states to pruned gen particles `analysis`  created: 2015-08-02T14:00:18Z merged: 2015-10-16T06:01:52Z

1. [10494](http://github.com/cms-sw/cmssw/pull/10494){:target="_blank"}  from **@ianna**: Use Hcal Trigger Tower Geometry from Event Setup `alca`  `db`  `l1`  created: 2015-07-31T08:54:51Z merged: 2015-10-27T06:56:39Z

1. [10320](http://github.com/cms-sw/cmssw/pull/10320){:target="_blank"}  from **@jhgoh**: RivetAnalyzer consumes migration 76X `generators`  created: 2015-07-23T13:38:38Z merged: 2015-10-19T11:28:28Z

1. [10176](http://github.com/cms-sw/cmssw/pull/10176){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-alca18 Restore Olgas code and modify the others to do both NZS and iterative analysis `alca`  created: 2015-07-13T17:57:58Z merged: 2015-10-23T09:32:24Z

#### CMSDIST Changes between Tags REL/CMSSW_7_6_0_pre7/slc6_amd64_gcc493 and REL/CMSSW_7_6_0/slc6_amd64_gcc493:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_7_6_0_pre7/slc6_amd64_gcc493...REL/CMSSW_7_6_0/slc6_amd64_gcc493)



1. [1925](http://github.com/cms-sw/cmssw/pull/1925){:target="_blank"}  from **@degano**: Update data for RecoJets/JetProducers. created: 2013-12-27T23:15:31Z merged: 2013-12-28T09:43:30Z

1. [1915](http://github.com/cms-sw/cmssw/pull/1915){:target="_blank"}  from **@smuzaffar**: update root to use cms/c1ca998 i.e current tip of root 6-02 branches created: 2013-12-20T20:01:12Z merged: None

1. [1908](http://github.com/cms-sw/cmssw/pull/1908){:target="_blank"}  from **@davidlt**: gmp-static: set --host and --build to for a generic build created: 2013-12-20T09:41:20Z merged: 2013-12-20T11:17:47Z

1. [1905](http://github.com/cms-sw/cmssw/pull/1905){:target="_blank"}  from **@davidlt**: Remmove unsupported command by icpc and ifort created: 2013-12-19T21:25:19Z merged: 2013-12-19T21:26:46Z

1. [1904](http://github.com/cms-sw/cmssw/pull/1904){:target="_blank"}  from **@degano**: Update root to the tip of the branch. created: 2013-12-19T21:16:15Z merged: 2013-12-31T07:40:45Z

1. [1902](http://github.com/cms-sw/cmssw/pull/1902){:target="_blank"}  from **@degano**: Advance RecoJets/JetProducers data to latest update. created: 2013-12-19T19:38:38Z merged: 2013-12-20T12:53:16Z

1. [1900](http://github.com/cms-sw/cmssw/pull/1900){:target="_blank"}  from **@degano**: Upgrade Frontier client to version 2.8.14 and pacparser to 1.3.5. created: 2013-12-19T19:11:50Z merged: 2013-12-19T22:02:53Z

1. [1897](http://github.com/cms-sw/cmssw/pull/1897){:target="_blank"}  from **@cms-sw**: Revert "Update frontier client to 2.8.13 and pacparser to 1.3.5." created: 2013-12-19T16:33:12Z merged: None

1. [1895](http://github.com/cms-sw/cmssw/pull/1895){:target="_blank"}  from **@cms-sw**: Revert "Advance fastjet-contrib to version cms/v1.020." created: 2013-12-19T15:25:02Z merged: None

1. [1891](http://github.com/cms-sw/cmssw/pull/1891){:target="_blank"}  from **@degano**: Advance fastjet-contrib to version cms/v1.020. created: 2013-12-19T13:29:20Z merged: 2013-12-19T21:59:15Z

1. [1888](http://github.com/cms-sw/cmssw/pull/1888){:target="_blank"}  from **@degano**: Advance release for RecoEgamma/ElectronIdentification data. created: 2013-12-19T09:25:46Z merged: None

1. [1882](http://github.com/cms-sw/cmssw/pull/1882){:target="_blank"}  from **@degano**: Update frontier client to 2.8.13 and pacparser to 1.3.5. created: 2013-12-18T20:54:02Z merged: 2013-12-19T10:19:20Z

1. [1881](http://github.com/cms-sw/cmssw/pull/1881){:target="_blank"}  from **@degano**: Update py2-dxr to use pysqlite 2.8 to load extension in sqlite 3.8. created: 2013-12-18T20:33:49Z merged: 2013-12-18T20:52:24Z
