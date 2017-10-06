---
layout: post
title:  "9_3_0_pre1"
date:   2017-10-05 18:16:46 +0200
categories: cmssw
relmajor: 9
relminor: 3
relsubminor: 0

relpre: _pre1
---

# CMSSW_9_3_0_pre1
#### Changes since CMSSW_9_2_4:
[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_9_2_4...CMSSW_9_3_0_pre1)



1. [19525](http://github.com/cms-sw/cmssw/pull/19525)  from @arunhep: GT updates for V1MC production : contains SiPixelQuality, tracker reco material update, fix to CSC APEs `alca`  created: 2017-07-03T16:44:17Z merged: 2017-07-03T19:47:51Z

1. [19517](http://github.com/cms-sw/cmssw/pull/19517)  from @ggovi: IOV range returned ordered by since `db`  created: 2017-07-03T10:05:14Z merged: 2017-07-03T15:01:49Z

1. [19510](http://github.com/cms-sw/cmssw/pull/19510)  from @Martin-Grunewald: Do not throw on non-matching triggers in ecalTrgHLT (93X) `alca`  created: 2017-07-03T08:33:51Z merged: 2017-07-03T19:49:37Z

1. [19507](http://github.com/cms-sw/cmssw/pull/19507)  from @mmusich: update conditions for unit test `alca`  created: 2017-07-02T17:28:06Z merged: 2017-07-03T09:10:55Z

1. [19500](http://github.com/cms-sw/cmssw/pull/19500)  from @Dr15Jones: Provide default value for new parameter in Timing service. `core`  created: 2017-07-01T14:57:16Z merged: 2017-07-01T19:41:21Z

1. [19492](http://github.com/cms-sw/cmssw/pull/19492)  from @apana: pr93x L1T fix L1T_ZeroBias not firing in RelVal MC. `l1`  created: 2017-06-30T07:14:14Z merged: 2017-06-30T15:52:49Z

1. [19491](http://github.com/cms-sw/cmssw/pull/19491)  from @wddgit: New feature allowing special value @currentProcess for InputTag proce `core`  created: 2017-06-30T00:05:52Z merged: 2017-07-02T19:18:07Z

1. [19480](http://github.com/cms-sw/cmssw/pull/19480)  from @ianna: Add Detailed Cavern to 2019 Scenario `geometry`  `upgrade`  created: 2017-06-29T14:35:53Z merged: 2017-07-02T19:23:47Z

1. [19475](http://github.com/cms-sw/cmssw/pull/19475)  from @mandrenguyen: Swith to 2017 vtx smearing for HI wfs `pdmv`  `upgrade`  created: 2017-06-29T12:12:51Z merged: 2017-07-02T19:23:57Z

1. [19472](http://github.com/cms-sw/cmssw/pull/19472)  from @cmsbuild: make sure that workflow commands are written with all the quotes `pdmv`  `upgrade`  created: 2017-06-29T10:11:59Z merged: 2017-06-29T11:22:01Z

1. [19463](http://github.com/cms-sw/cmssw/pull/19463)  from @wddgit: Fix bug which affects SubProcesses using skipCurrentProcess `core`  created: 2017-06-28T16:30:18Z merged: 2017-06-29T07:13:34Z

1. [19455](http://github.com/cms-sw/cmssw/pull/19455)  from @dan131riley: add module label to module name printout in fatal signal handler `core`  created: 2017-06-27T19:02:22Z merged: 2017-06-28T07:13:05Z

1. [19453](http://github.com/cms-sw/cmssw/pull/19453)  from @apana: pr92/93x L1T allow correlations from other than bx=0 `l1`  created: 2017-06-27T16:48:38Z merged: 2017-06-28T07:14:00Z

1. [19452](http://github.com/cms-sw/cmssw/pull/19452)  from @kpedro88: Remove unneeded Phase2 geometries, workflows, Eras `db`  `geometry`  `operations`  `pdmv`  `upgrade`  `visualization`  created: 2017-06-27T16:45:07Z merged: 2017-06-28T16:35:48Z

1. [19442](http://github.com/cms-sw/cmssw/pull/19442)  from @ianna: Xerces Memory Leak Cleanup `alca`  `db`  `reconstruction`  created: 2017-06-27T10:17:01Z merged: 2017-06-30T12:12:22Z

1. [19440](http://github.com/cms-sw/cmssw/pull/19440)  from @ianna: Remove Obsolete Packages from BuildFiles `geometry`  created: 2017-06-27T09:43:21Z merged: 2017-06-27T14:24:20Z

1. [19437](http://github.com/cms-sw/cmssw/pull/19437)  from @fabozzi: reminiAOD workflows from 80X input (93X) `pdmv`  `upgrade`  created: 2017-06-27T07:29:02Z merged: 2017-06-28T07:44:02Z

1. [19430](http://github.com/cms-sw/cmssw/pull/19430)  from @mmusich: add SiStripCalMinBias to the upgrade phase-I samples `pdmv`  `upgrade`  created: 2017-06-26T15:28:48Z merged: 2017-06-28T07:14:54Z

1. [19429](http://github.com/cms-sw/cmssw/pull/19429)  from @gartung: FWCore/Services: Timing service updated to report modules that exceed a time threshold. `core`  created: 2017-06-26T15:27:18Z merged: 2017-06-29T07:14:39Z

1. [19426](http://github.com/cms-sw/cmssw/pull/19426)  from @slava77: cleanup uninitialized reads or conditions and leaks `analysis`  `dqm`  `reconstruction`  `simulation`  created: 2017-06-25T19:05:36Z merged: 2017-06-27T10:08:10Z

1. [19424](http://github.com/cms-sw/cmssw/pull/19424)  from @cms-sw: Revert "Revert "Update Phase 1 pixel gains in digitizer/clusterizer"" `comparison`  `hlt`  `reconstruction`  `simulation`  created: 2017-06-25T13:41:25Z merged: 2017-06-26T13:54:33Z

1. [19418](http://github.com/cms-sw/cmssw/pull/19418)  from @dildick: Fix for compiler warnings coming from getRPCfromCSC `l1`  created: 2017-06-23T16:01:56Z merged: 2017-06-28T08:08:36Z

1. [19417](http://github.com/cms-sw/cmssw/pull/19417)  from @Dr15Jones: Removing forking ability from cmsRun `core`  `daq`  `dqm`  `reconstruction`  created: 2017-06-23T15:27:07Z merged: 2017-06-28T16:34:36Z

1. [19416](http://github.com/cms-sw/cmssw/pull/19416)  from @ianna: Move Geometry Aligner Header `alca`  `geometry`  created: 2017-06-23T14:44:48Z merged: 2017-06-26T08:26:51Z

1. [19415](http://github.com/cms-sw/cmssw/pull/19415)  from @pieterdavid: Tracker sub-DetId deprecation for TrackFitters DebugHelpers.h `reconstruction`  created: 2017-06-23T14:12:13Z merged: 2017-06-27T09:17:17Z

1. [19414](http://github.com/cms-sw/cmssw/pull/19414)  from @leggat: ROC counting trend plots per layer/ring for phase 1 pixel DQM `dqm`  created: 2017-06-23T13:46:13Z merged: 2017-06-26T15:10:08Z

1. [19413](http://github.com/cms-sw/cmssw/pull/19413)  from @bsunanda: Run2-alca81 Modify and reallocate the scripts used for calibration `alca`  created: 2017-06-23T11:35:12Z merged: 2017-06-30T12:15:21Z

1. [19406](http://github.com/cms-sw/cmssw/pull/19406)  from @rappoccio: Rebase of #19222: JME python configuration cleanup for 92x `analysis`  `reconstruction`  created: 2017-06-22T15:21:48Z merged: 2017-06-30T07:28:15Z

1. [19404](http://github.com/cms-sw/cmssw/pull/19404)  from @kmcdermo: ootPhotons for 80X Legacy reprocessing `analysis`  `reconstruction`  created: 2017-06-22T12:57:29Z merged: 2017-07-03T19:57:04Z

1. [19401](http://github.com/cms-sw/cmssw/pull/19401)  from @alberto-sanchez: addressing issue 19340, adding checks to avoid possible acces violations `analysis`  created: 2017-06-21T19:49:13Z merged: 2017-06-27T09:16:20Z

1. [19399](http://github.com/cms-sw/cmssw/pull/19399)  from @dildick: Configuration to produce ME0 pseudo stubs for Phase-2 `core`  `l1`  `simulation`  `upgrade`  created: 2017-06-21T16:52:42Z merged: 2017-06-27T09:55:43Z

1. [19375](http://github.com/cms-sw/cmssw/pull/19375)  from @Sam-Harper: Adding Cross Trigger Support to E/gamma TnP DQM `dqm`  created: 2017-06-19T20:58:58Z merged: 2017-06-26T08:28:36Z

1. [19366](http://github.com/cms-sw/cmssw/pull/19366)  from @Dr15Jones: Implement async global end transitions `core`  created: 2017-06-19T14:37:41Z merged: 2017-06-26T13:49:26Z

1. [19353](http://github.com/cms-sw/cmssw/pull/19353)  from @Teemperor: Fix ODR problems and includes in Selections.h `analysis`  created: 2017-06-19T13:17:21Z merged: 2017-06-28T07:23:46Z

1. [19308](http://github.com/cms-sw/cmssw/pull/19308)  from @franzoni: Pf hadron calibration offline (reb) w/ AlCa updates `alca`  `db`  `reconstruction`  created: 2017-06-18T14:43:17Z merged: 2017-06-28T07:17:48Z

1. [19307](http://github.com/cms-sw/cmssw/pull/19307)  from @cms-egamma: ECAL PFCluster Correction 9X `alca`  `l1`  `reconstruction`  created: 2017-06-18T11:45:12Z merged: 2017-07-03T15:31:21Z

1. [19281](http://github.com/cms-sw/cmssw/pull/19281)  from @makortel: Add track selection MVA and all the input variables to TrackingNtuple `dqm`  created: 2017-06-16T13:19:10Z merged: 2017-07-02T19:25:20Z

1. [19267](http://github.com/cms-sw/cmssw/pull/19267)  from @makortel: Update online beamspot to quadruplet-only and rescale track uncertainties `dqm`  `reconstruction`  created: 2017-06-16T07:28:00Z merged: 2017-06-28T07:23:11Z

1. [19263](http://github.com/cms-sw/cmssw/pull/19263)  from @Sam-Harper: New Interface for E/gamma 2017 Pixel Matching `reconstruction`  created: 2017-06-15T21:44:33Z merged: 2017-06-30T07:24:28Z

1. [19235](http://github.com/cms-sw/cmssw/pull/19235)  from @cms-tsg-storm: HLT menu 2017 v1.1 `alca`  `hlt`  created: 2017-06-15T06:43:24Z merged: 2017-06-26T14:26:11Z

1. [19205](http://github.com/cms-sw/cmssw/pull/19205)  from @kmcdermo: Out-of-time photons for MiniAOD `analysis`  `reconstruction`  created: 2017-06-13T14:11:13Z merged: 2017-06-29T14:39:36Z

1. [19185](http://github.com/cms-sw/cmssw/pull/19185)  from @forthommel: CTPPS: fixes for 2017 diamond data taking operations `dqm`  `reconstruction`  created: 2017-06-09T21:17:39Z merged: 2017-06-27T07:13:13Z

1. [19164](http://github.com/cms-sw/cmssw/pull/19164)  from @kkotov: New CaloL{1,2} LUTs are taken care of by the L1T O2O `alca`  `db`  `l1`  created: 2017-06-09T10:45:10Z merged: 2017-07-02T19:28:44Z

1. [19149](http://github.com/cms-sw/cmssw/pull/19149)  from @clelange: HGCal clustering: label border hits with rho = rho_b as Halo instead of core `reconstruction`  `upgrade`  created: 2017-06-08T16:40:50Z merged: 2017-06-30T07:25:12Z

1. [19089](http://github.com/cms-sw/cmssw/pull/19089)  from @mandrenguyen: Add Phase I heavy-ion relval wf (take 2) `dqm`  `generators`  `operations`  `pdmv`  `reconstruction`  `upgrade`  created: 2017-06-04T16:03:42Z merged: 2017-06-28T07:18:41Z

1. [19052](http://github.com/cms-sw/cmssw/pull/19052)  from @wddgit: Initial implementation of PathStatus and EndPathStatus products `core`  created: 2017-05-31T21:24:31Z merged: 2017-06-27T07:21:14Z

1. [19029](http://github.com/cms-sw/cmssw/pull/19029)  from @makortel: Add minPhi+maxPhi to RecoTrackSelectorBase and TrackingParticleSelector `analysis`  `dqm`  `hlt`  `reconstruction`  `simulation`  created: 2017-05-31T09:19:25Z merged: 2017-06-28T07:26:18Z

1. [19014](http://github.com/cms-sw/cmssw/pull/19014)  from @sasharma6: DQM SMP PAG ISSUE `dqm`  created: 2017-05-30T13:48:38Z merged: 2017-06-26T14:15:45Z

1. [18971](http://github.com/cms-sw/cmssw/pull/18971)  from @gomber: Exo trigger prompt monitoring92 x `dqm`  created: 2017-05-26T18:27:57Z merged: 2017-07-03T14:59:46Z

1. [18875](http://github.com/cms-sw/cmssw/pull/18875)  from @dildick: Fit CSC comparator digis `l1`  `simulation`  created: 2017-05-22T07:38:01Z merged: 2017-06-26T14:17:13Z

1. [18841](http://github.com/cms-sw/cmssw/pull/18841)  from @DryRun: HCALDQM: fix RecHitTask crash, adc2fC from DB, fix TPTask, add plots  `dqm`  created: 2017-05-19T01:07:13Z merged: 2017-07-03T19:06:30Z

#### CMSDIST Changes between Tags REL/CMSSW_9_2_4/slc6_amd64_gcc530 and REL/CMSSW_9_3_0_pre1/slc6_amd64_gcc530:
[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_9_2_4/slc6_amd64_gcc530...REL/CMSSW_9_3_0_pre1/slc6_amd64_gcc530)



1. [3139](http://github.com/cms-sw/cmssw/pull/3139)  from @davidlange6: Tensorflow for slc6 created: 2014-04-01T14:27:37Z merged: None

1. [3136](http://github.com/cms-sw/cmssw/pull/3136)  from @davidlange6: refactor tensorflow to build from sources (and c interface) created: 2014-04-01T13:22:13Z merged: 2014-04-02T12:08:44Z

1. [3133](http://github.com/cms-sw/cmssw/pull/3133)  from @mrodozov: Update MagneticField-Interpolation tag to V01-00-02 created: 2014-04-01T10:41:38Z merged: 2014-04-02T12:03:47Z

1. [3130](http://github.com/cms-sw/cmssw/pull/3130)  from @cms-sw: added OpenMPI support for sherpa

1. [3128](http://github.com/cms-sw/cmssw/pull/3128)  from @cms-sw: update cmssw-config(build rules) tag to V05-05-25 created: 2014-04-01T08:14:32Z merged: None

1. [3125](http://github.com/cms-sw/cmssw/pull/3125)  from @davidlange6: adding hyperas and hyperopt created: 2014-03-31T20:43:37Z merged: 2014-03-31T20:45:16Z
