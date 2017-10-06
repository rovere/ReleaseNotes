---
layout: post
title:  "7_0_0_pre12"
date:   2017-10-06 16:42:42 +0200
categories: cmssw
relmajor: 7
relminor: 0
relsubminor: 0
relpre: _pre12
---

# CMSSW_7_0_0_pre12
#### Changes since CMSSW_7_0_0_pre11:

1. [2055](http://github.com/cms-sw/cmssw/pull/2055){:target="_blank"}  from **@ggovi**: DB fixes -- CondDB KeyList adapted to avoid dependency on the target CondFormat. `db`  created: 2014-01-17T09:59:33Z merged: 2014-01-20T10:45:37Z

1. [2080](http://github.com/cms-sw/cmssw/pull/2080){:target="_blank"}  from **@davidlange6**: Misc fix -- reduce buffer size for FEVTHLTDEBUG output given the 2000++ branches tha... `operations`  created: 2014-01-20T10:39:02Z merged: 2014-01-20T10:41:06Z

1. [1910](http://github.com/cms-sw/cmssw/pull/1910){:target="_blank"}  from **@jpavel**: Reco fixes -- 70x tau id trigger default config `reconstruction`  created: 2013-12-20T12:52:57Z merged: 2014-01-20T10:37:44Z

1. [2044](http://github.com/cms-sw/cmssw/pull/2044){:target="_blank"}  from **@lgray**: Reco fixes -- Fixes to Cluster Shape Variables monitored in EXO DQM + #1986 Code Review  `reconstruction`  created: 2014-01-16T13:17:27Z merged: 2014-01-17T13:26:20Z

1. [2047](http://github.com/cms-sw/cmssw/pull/2047){:target="_blank"}  from **@wddgit**: Sim fixes -- Bug fix. This bug will break the DataMixingModule completely. `simulation`  created: 2014-01-16T16:31:19Z merged: 2014-01-17T11:22:39Z

1. [1935](http://github.com/cms-sw/cmssw/pull/1935){:target="_blank"}  from **@fwyzard**: Misc fixes -- FastTimerService, part 3 `hlt`  created: 2013-12-31T01:02:18Z merged: 2014-01-17T10:18:20Z

1. [2048](http://github.com/cms-sw/cmssw/pull/2048){:target="_blank"}  from **@gartung**: Multicore fixes -- Add [[cms::thread_safe]] to non-const function static var Registry::instance()::s_reg `core`  created: 2014-01-16T19:09:15Z merged: 2014-01-16T21:32:12Z

1. [2049](http://github.com/cms-sw/cmssw/pull/2049){:target="_blank"}  from **@Dr15Jones**: Framework fixes -- edm::refToPtr now handles null Refs `core`  created: 2014-01-16T20:09:31Z merged: 2014-01-16T21:30:24Z

1. [2002](http://github.com/cms-sw/cmssw/pull/2002){:target="_blank"}  from **@fwyzard**: Db fixes -- LumiCorrectionSource: workaround CORAL not handling Timestamps `reconstruction`  created: 2014-01-12T14:45:23Z merged: 2014-01-16T19:23:19Z

1. [1986](http://github.com/cms-sw/cmssw/pull/1986){:target="_blank"}  from **@bendavid**: Reco fix -- EGM GED bug fixes for pre12 (AOD size, cluster double counting, rechit fraction usage) `analysis`  `dqm`  `reconstruction`  `simulation`  created: 2014-01-10T16:41:51Z merged: 2014-01-16T12:47:38Z

1. [2043](http://github.com/cms-sw/cmssw/pull/2043){:target="_blank"}  from **@ggovi**: Fix for support of reconnect in new Condition Database - required by HLT `db`  created: 2014-01-16T11:27:43Z merged: 2014-01-16T11:33:02Z

1. [1864](http://github.com/cms-sw/cmssw/pull/1864){:target="_blank"}  from **@trocino**: HLT updates -- L2muon changes: L2MuonSeedGenerator, L2MuonProducer `reconstruction`  created: 2013-12-18T08:09:23Z merged: 2014-01-15T15:49:38Z

1. [1913](http://github.com/cms-sw/cmssw/pull/1913){:target="_blank"}  from **@diguida**: Consumes migration -- Validation/TrackerHits `dqm`  created: 2013-12-20T16:47:34Z merged: 2014-01-15T14:27:44Z

1. [1959](http://github.com/cms-sw/cmssw/pull/1959){:target="_blank"}  from **@lveldere**: Fastsim fixes -- New tuning of HF `fastsim`  created: 2014-01-07T18:48:17Z merged: 2014-01-15T14:24:35Z

1. [1708](http://github.com/cms-sw/cmssw/pull/1708){:target="_blank"}  from **@mkirsano**: Generators fixes -- Redesign jet matching mg fast jet `generators`  created: 2013-12-06T17:59:50Z merged: 2014-01-15T14:24:01Z

1. [2028](http://github.com/cms-sw/cmssw/pull/2028){:target="_blank"}  from **@inugent**: Validation updates -- Adding validation for Higgs->tautau CP and tau lifetime/decaylength in TauValidation `generators`  created: 2014-01-14T19:25:37Z merged: 2014-01-15T14:22:17Z

1. [2008](http://github.com/cms-sw/cmssw/pull/2008){:target="_blank"}  from **@mkirsano**: Generators updates -- Lheint clean1 `generators`  created: 2014-01-13T11:38:36Z merged: 2014-01-15T14:07:54Z

1. [2009](http://github.com/cms-sw/cmssw/pull/2009){:target="_blank"}  from **@mkirsano**: Generators fixes -- fix pydata loading problem, ported from 6_2_X `generators`  created: 2014-01-13T11:54:32Z merged: 2014-01-15T14:07:07Z

1. [2027](http://github.com/cms-sw/cmssw/pull/2027){:target="_blank"}  from **@HuguesBrun**: Generators updates -- Add a fragment for H125 in bb produced by VBF `generators`  created: 2014-01-14T16:54:37Z merged: 2014-01-15T14:06:03Z

1. [2023](http://github.com/cms-sw/cmssw/pull/2023){:target="_blank"}  from **@perrotta**: Consumes migration -- Fix a getByToken call in RecoTauTag/HLTProducers/src/CandidateSeededTrac... `hlt`  created: 2014-01-14T08:38:43Z merged: 2014-01-15T14:00:09Z

1. [2024](http://github.com/cms-sw/cmssw/pull/2024){:target="_blank"}  from **@mommsen**: DAQ fixes -- Fix corruption of dat files `daq`  created: 2014-01-14T13:26:08Z merged: 2014-01-15T09:33:12Z

1. [1970](http://github.com/cms-sw/cmssw/pull/1970){:target="_blank"}  from **@abdoulline**: ROOT6 fix -- fix of issues https://hypernews.cern.ch/HyperNews/CMS/get/swReleases/3982.html `alca`  created: 2014-01-09T08:17:12Z merged: 2014-01-14T21:34:35Z

1. [1831](http://github.com/cms-sw/cmssw/pull/1831){:target="_blank"}  from **@ggovi**: DB improvements -- Fixes to allow the parallel use of ORA db and new CondDB `alca`  `db`  `dqm`  `l1`  created: 2013-12-16T15:27:00Z merged: 2014-01-14T20:30:47Z

1. [1991](http://github.com/cms-sw/cmssw/pull/1991){:target="_blank"}  from **@Dr15Jones**: Reco fixes -- Declare several classes as non-storable `reconstruction`  created: 2014-01-10T21:21:31Z merged: 2014-01-14T13:29:15Z

1. [1980](http://github.com/cms-sw/cmssw/pull/1980){:target="_blank"}  from **@gartung**: Multithreading fixes -- make static bool static std::atomic<bool> `db`  created: 2014-01-09T19:04:30Z merged: 2014-01-14T13:05:29Z

1. [1914](http://github.com/cms-sw/cmssw/pull/1914){:target="_blank"}  from **@alja**: Fireworks fixes -- Fireworks table entries and tooltips for CSCDetId  `analysis`  `reconstruction`  `visualization`  created: 2013-12-20T17:25:50Z merged: 2014-01-14T13:02:54Z

1. [1989](http://github.com/cms-sw/cmssw/pull/1989){:target="_blank"}  from **@Dr15Jones**: AT fixes -- Need to declare a member variable transient for AssociationMaps `analysis`  created: 2014-01-10T20:56:42Z merged: 2014-01-14T13:02:26Z

1. [1976](http://github.com/cms-sw/cmssw/pull/1976){:target="_blank"}  from **@gartung**: Multithreading fixes -- Make file static variable const `alca`  `db`  created: 2014-01-09T17:12:53Z merged: 2014-01-14T09:29:25Z

1. [2013](http://github.com/cms-sw/cmssw/pull/2013){:target="_blank"}  from **@fwyzard**: DQM fixes -- automatically support all DQMStore book\* calls in the IBooker (v2) `dqm`  created: 2014-01-13T15:03:20Z merged: 2014-01-14T06:34:01Z

1. [1996](http://github.com/cms-sw/cmssw/pull/1996){:target="_blank"}  from **@Dr15Jones**: Multithreading fixes -- Add stack size control `core`  created: 2014-01-11T20:43:33Z merged: 2014-01-13T14:05:54Z

1. [1936](http://github.com/cms-sw/cmssw/pull/1936){:target="_blank"}  from **@Martin-Grunewald**: Reco update -- Use new but equivalent CaloMETProducer instead of deprecated generic MET... `hlt`  `reconstruction`  created: 2013-12-31T09:26:04Z merged: 2014-01-13T13:01:38Z

1. [1940](http://github.com/cms-sw/cmssw/pull/1940){:target="_blank"}  from **@TaiSakuma**: Reco cleanups -- Prepare to delete METProducer `analysis`  `dqm`  `hlt`  `reconstruction`  created: 2014-01-03T01:58:28Z merged: 2014-01-13T13:00:37Z

1. [1974](http://github.com/cms-sw/cmssw/pull/1974){:target="_blank"}  from **@venturia**: Misc cleanups -- Removed dependencies which were not needed `dqm`  `reconstruction`  created: 2014-01-09T13:00:10Z merged: 2014-01-13T12:36:40Z

1. [1973](http://github.com/cms-sw/cmssw/pull/1973){:target="_blank"}  from **@borrello**: DQM fixes -- Updated file for testing to include MET plot `dqm`  created: 2014-01-09T12:38:43Z merged: 2014-01-13T11:25:15Z

1. [1938](http://github.com/cms-sw/cmssw/pull/1938){:target="_blank"}  from **@fwyzard**: DQM fixes -- DQMStore: avoid cloning MonitorElements that are not going to be merged `dqm`  created: 2014-01-01T13:57:20Z merged: 2014-01-13T11:24:55Z

1. [1934](http://github.com/cms-sw/cmssw/pull/1934){:target="_blank"}  from **@fwyzard**: DQM cleanup -- Automatically support all DQMStore book\* calls in the IBooker `dqm`  created: 2013-12-31T00:43:19Z merged: 2014-01-13T11:24:00Z

1. [1998](http://github.com/cms-sw/cmssw/pull/1998){:target="_blank"}  from **@davidlt**: DataFormats/Histograms: rename `debug' macro to`METOEDMFORMAT_DEBUG' `core`  `dqm`  created: 2014-01-12T07:48:37Z merged: 2014-01-12T07:49:19Z

1. [1990](http://github.com/cms-sw/cmssw/pull/1990){:target="_blank"}  from **@Dr15Jones**: AT fix -- Fixed transient/persistent argument mixup `analysis`  created: 2014-01-10T21:17:43Z merged: 2014-01-11T13:51:03Z

1. [1958](http://github.com/cms-sw/cmssw/pull/1958){:target="_blank"}  from **@rappoccio**: Bug fix : adding JEC producers for AK5CHS and AK7CHS `analysis`  created: 2014-01-07T18:26:54Z merged: 2014-01-10T15:37:37Z

1. [1985](http://github.com/cms-sw/cmssw/pull/1985){:target="_blank"}  from **@mommsen**: DAQ updates -- Close file after writing the init message. `daq`  created: 2014-01-10T11:44:04Z merged: 2014-01-10T12:55:04Z

1. [1952](http://github.com/cms-sw/cmssw/pull/1952){:target="_blank"}  from **@vkuznet**: Fix naming collision between locally defined function and variable phi. `reconstruction`  created: 2014-01-06T15:19:58Z merged: 2014-01-09T15:09:13Z

1. [1966](http://github.com/cms-sw/cmssw/pull/1966){:target="_blank"}  from **@Dr15Jones**: Framework fixes -- Added option to set gDebug from InitRootHandler's parameters `core`  created: 2014-01-08T20:13:14Z merged: 2014-01-09T10:32:03Z

1. [1962](http://github.com/cms-sw/cmssw/pull/1962){:target="_blank"}  from **@deguio**: DQM fixes -- Updating the memory references for whiteRabbit tests `dqm`  created: 2014-01-08T15:40:12Z merged: 2014-01-09T09:49:11Z

1. [1963](http://github.com/cms-sw/cmssw/pull/1963){:target="_blank"}  from **@inugent**: Generator fix -- Patch for undertemined decay modes and adding Z+gamma mode in Generator Higgs Validation. `generators`  created: 2014-01-08T16:51:25Z merged: 2014-01-09T09:48:23Z

1. [1961](http://github.com/cms-sw/cmssw/pull/1961){:target="_blank"}  from **@davidlt**: Misc fixes -- CommonTools/TrackerMap: add missing std:: in print_TrackerMap.cc `dqm`  `reconstruction`  created: 2014-01-08T11:53:18Z merged: 2014-01-08T13:25:37Z

1. [1960](http://github.com/cms-sw/cmssw/pull/1960){:target="_blank"}  from **@davidlt**: Misc fixes -- DQM/TrackingMonitorClient: add missing std:: `dqm`  created: 2014-01-08T11:52:54Z merged: 2014-01-08T12:55:35Z

1. [1957](http://github.com/cms-sw/cmssw/pull/1957){:target="_blank"}  from **@slava77**: Reco fix -- Moved dict for ValueMap of vector of PFCandidateRef from EgammaCandidate... `reconstruction`  created: 2014-01-07T16:00:43Z merged: 2014-01-07T21:42:03Z

1. [1956](http://github.com/cms-sw/cmssw/pull/1956){:target="_blank"}  from **@slava77**: Reco fix -- rename typedef to avoid duplicate def with ElectronSeedRefVector::iterator `reconstruction`  created: 2014-01-07T14:42:42Z merged: 2014-01-07T16:49:05Z

1. [1955](http://github.com/cms-sw/cmssw/pull/1955){:target="_blank"}  from **@thomreis**: DQM fixes -- Fix for manual offline egamma HLT validation script `dqm`  created: 2014-01-07T13:46:52Z merged: 2014-01-07T16:29:27Z

1. [1944](http://github.com/cms-sw/cmssw/pull/1944){:target="_blank"}  from **@alja**: Fireworks fixes -- 70x improve unittest for fireworks configuration. `visualization`  created: 2014-01-03T18:58:24Z merged: 2014-01-07T14:07:10Z

1. [1948](http://github.com/cms-sw/cmssw/pull/1948){:target="_blank"}  from **@Dr15Jones**: Multithreading fixes -- Removed DQM and PoolDBOutputServices from threaded jobs `core`  created: 2014-01-05T19:28:16Z merged: 2014-01-05T19:33:29Z

1. [1943](http://github.com/cms-sw/cmssw/pull/1943){:target="_blank"}  from **@Dr15Jones**: Multithreading fixes -- Remove the HeavyIon module that depends on TkDetMap `core`  created: 2014-01-03T17:27:28Z merged: 2014-01-05T16:16:11Z

1. [1945](http://github.com/cms-sw/cmssw/pull/1945){:target="_blank"}  from **@Dr15Jones**: Tools fixes -- Extended Helgrind Suppressions to more TBB and Framework internals `core`  created: 2014-01-04T02:14:45Z merged: 2014-01-04T19:10:28Z

1. [1946](http://github.com/cms-sw/cmssw/pull/1946){:target="_blank"}  from **@Dr15Jones**: Misc fixes -- Properly handle built in customise additions `operations`  created: 2014-01-04T16:20:03Z merged: 2014-01-04T19:06:30Z

1. [1942](http://github.com/cms-sw/cmssw/pull/1942){:target="_blank"}  from **@Dr15Jones**: Misc cleanup -- Allow cmsDriver.py to accept multiple --customise options `operations`  created: 2014-01-03T16:37:44Z merged: 2014-01-03T22:51:46Z

1. [1931](http://github.com/cms-sw/cmssw/pull/1931){:target="_blank"}  from **@alja**: Fireworks fixes -- Fix crash in Fireworks DetailView, import missing changes from CVS head for scaling of RecHits `visualization`  created: 2013-12-30T18:10:45Z merged: 2014-01-01T12:12:39Z

1. [1916](http://github.com/cms-sw/cmssw/pull/1916){:target="_blank"}  from **@demattia**: AlCa fixes -- Added MVAs to the prompt GT `alca`  created: 2013-12-20T20:35:39Z merged: 2013-12-20T20:50:13Z
