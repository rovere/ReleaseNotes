---
layout: post
title:  "8_0_0_pre2"
date:   2017-10-07 22:04:13 +0200
categories: cmssw
relmajor: 8
relminor: 0
relsubminor: 0
relpre: _pre2
---

# CMSSW_8_0_0_pre2
#### Changes since CMSSW_8_0_0_pre1:

:arrow_right: Merge due to automatic forward port
[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_8_0_0_pre1...CMSSW_8_0_0_pre2)



1. [12430](http://github.com/cms-sw/cmssw/pull/12430){:target="_blank"}  from **@davidlange6**: PackedCandidates.. comment out parts of unit test that are not expected to work given that data are packed upon creation with precision loss `analysis`  `comparison`  `reconstruction`  created: 2015-11-16T11:18:08Z merged: 2015-11-16T12:25:44Z

1. [12429](http://github.com/cms-sw/cmssw/pull/12429){:target="_blank"}  from **@hdelanno**: Fix the way the folder is handled in SiPixelHLT in 8_0_X `dqm`  created: 2015-11-16T11:12:57Z merged: 2015-11-16T17:11:25Z

1. [12420](http://github.com/cms-sw/cmssw/pull/12420){:target="_blank"}  from **@wmtan**: Remove obsolete conditional compilations in Framework only `comparison`  `core`  created: 2015-11-14T00:01:29Z merged: 2015-11-16T17:08:07Z

1. [12418](http://github.com/cms-sw/cmssw/pull/12418){:target="_blank"}  from **@wmtan**: Make dependency messages consistent with other reports `core`  created: 2015-11-13T19:59:41Z merged: 2015-11-14T06:23:06Z

1. [12416](http://github.com/cms-sw/cmssw/pull/12416){:target="_blank"}  from **@rrabadan**: missing-, inactive-, valid-hits and clusterChargePerCm trackerMaps `dqm`  created: 2015-11-13T17:56:16Z merged: 2015-11-16T17:11:38Z

1. [12407](http://github.com/cms-sw/cmssw/pull/12407){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-hcx49 First attempt of hexagonal geometry for HGCal `geometry`  created: 2015-11-12T21:34:51Z merged: 2015-11-16T13:11:56Z

1. [12403](http://github.com/cms-sw/cmssw/pull/12403){:target="_blank"}  from **@lveldere**: fastsim: use fastsim era to define fastsim customs to mixing `fastsim`  `operations`  `simulation`  created: 2015-11-12T15:02:58Z merged: 2015-11-15T10:09:23Z

1. [12402](http://github.com/cms-sw/cmssw/pull/12402){:target="_blank"}  from **@deguio**: fix harvesting T0 `operations`  created: 2015-11-12T13:27:26Z merged: 2015-11-13T06:59:57Z

1. [12396](http://github.com/cms-sw/cmssw/pull/12396){:target="_blank"}  from **@lveldere**: FastSim/Configuration: remove outdated documentation and tests `fastsim`  created: 2015-11-12T10:37:56Z merged: 2015-11-12T19:56:15Z

1. [12394](http://github.com/cms-sw/cmssw/pull/12394){:target="_blank"}  from **@diguida**: Fix for the reconnect-each-run policy in CondDBESSource 80X `db`  created: 2015-11-12T09:29:00Z merged: 2015-11-16T17:11:49Z

1. [12391](http://github.com/cms-sw/cmssw/pull/12391){:target="_blank"}  from **@makortel**: Another fix to TrackingVertex->TrackingParticle links in premixing `simulation`  created: 2015-11-12T08:57:30Z merged: 2015-11-14T06:24:21Z

1. [12390](http://github.com/cms-sw/cmssw/pull/12390){:target="_blank"}  from **@davidlt**: Use ExtVec on PPC64LE `reconstruction`  created: 2015-11-12T08:24:53Z merged: 2015-11-12T21:25:23Z

1. [12389](http://github.com/cms-sw/cmssw/pull/12389){:target="_blank"}  from **@Dr15Jones**: Consolidated framework thread_local into one package `core`  created: 2015-11-11T22:50:22Z merged: 2015-11-13T07:00:17Z

1. [12387](http://github.com/cms-sw/cmssw/pull/12387){:target="_blank"}  from **@forthommel**: Updated SiStrip unpacker (new FED readout modes) `reconstruction`  created: 2015-11-11T21:47:12Z merged: 2015-11-16T07:46:16Z

1. [12380](http://github.com/cms-sw/cmssw/pull/12380){:target="_blank"}  from **@gouskos**: additional dqm plot for the pixel barrel occupancy vs module and ladd `dqm`  created: 2015-11-11T15:43:23Z merged: 2015-11-16T17:11:58Z

1. [12376](http://github.com/cms-sw/cmssw/pull/12376){:target="_blank"}  from **@wmtan**: Fix FileInPath test in FWCore/PythonParameterSet `core`  created: 2015-11-11T15:08:02Z merged: 2015-11-12T06:46:11Z

1. [12367](http://github.com/cms-sw/cmssw/pull/12367){:target="_blank"}  from **@davidlange6**: PackedCandidate restore old behavior `analysis`  `comparison`  created: 2015-11-10T20:55:28Z merged: 2015-11-11T09:48:12Z

1. [12365](http://github.com/cms-sw/cmssw/pull/12365){:target="_blank"}  from **@gartung**: update symbols.py to produce reasonable dot graphs `core`  created: 2015-11-10T19:55:34Z merged: 2015-11-12T06:51:10Z

1. [12362](http://github.com/cms-sw/cmssw/pull/12362){:target="_blank"}  from **@davidlt**: Remove -1 from ClassVersionID field in selection rules `reconstruction`  `simulation`  created: 2015-11-10T18:04:36Z merged: 2015-11-12T06:56:10Z

1. [12361](http://github.com/cms-sw/cmssw/pull/12361){:target="_blank"}  from **@mark-grimes**: phase1Pixel era digi to/from raw additions `comparison`  `operations`  created: 2015-11-10T17:50:52Z merged: 2015-11-12T06:53:04Z

1. [12360](http://github.com/cms-sw/cmssw/pull/12360){:target="_blank"}  from **@wmtan**: Fix hi relvals `analysis`  `comparison`  `generators`  `simulation`  created: 2015-11-10T17:38:04Z merged: 2015-11-11T08:29:23Z

1. [12359](http://github.com/cms-sw/cmssw/pull/12359){:target="_blank"}  from **@mark-grimes**: phase1Pixel era validation additions `comparison`  `dqm`  created: 2015-11-10T17:03:09Z merged: 2015-11-12T07:31:48Z

1. [12358](http://github.com/cms-sw/cmssw/pull/12358){:target="_blank"}  from **@mbandrews**: Fix Pedestal EB RMS threshold. Add chi2 cut on DQM timing. `comparison`  `dqm`  created: 2015-11-10T16:54:00Z merged: 2015-11-16T17:10:13Z

1. [12353](http://github.com/cms-sw/cmssw/pull/12353){:target="_blank"}  from **@rkunnawa**: HIN Jet DQM/Validation in 80X, with removing commented out code `dqm`  created: 2015-11-10T16:10:30Z merged: 2015-11-11T14:21:35Z

1. [12352](http://github.com/cms-sw/cmssw/pull/12352){:target="_blank"}  from **@mmusich**: Updating JEC in data/mc and fixes for HI `alca`  created: 2015-11-10T15:28:32Z merged: 2015-11-11T08:31:14Z

1. [12350](http://github.com/cms-sw/cmssw/pull/12350){:target="_blank"}  from **@ianna**: Castor 2015 Scenarios `db`  `geometry`  created: 2015-11-10T14:46:53Z merged: 2015-11-16T17:12:09Z

1. [12347](http://github.com/cms-sw/cmssw/pull/12347){:target="_blank"}  from **@vandreev11**: fix for testHGCalLocalReco script `reconstruction`  created: 2015-11-10T14:14:09Z merged: 2015-11-11T08:31:24Z

1. [12342](http://github.com/cms-sw/cmssw/pull/12342){:target="_blank"}  from **@vanbesien**: Replaced the contents of the fed config by fedtest `dqm`  created: 2015-11-10T11:10:29Z merged: 2015-11-10T19:41:34Z

1. [12337](http://github.com/cms-sw/cmssw/pull/12337){:target="_blank"}  from **@goni**: Cmssw 80x dqm histo range fix for HI `dqm`  created: 2015-11-10T10:54:21Z merged: 2015-11-11T08:31:30Z

1. [12332](http://github.com/cms-sw/cmssw/pull/12332){:target="_blank"}  from **@gartung**: clangSA update symbols.py script and fix potential bug in fixAnonNS(). `core`  created: 2015-11-10T03:18:50Z merged: 2015-11-10T08:56:15Z

1. [12331](http://github.com/cms-sw/cmssw/pull/12331){:target="_blank"}  from **@mdhildreth**: Add 25ns scenario for Fall 2015 MC to match data `operations`  `simulation`  created: 2015-11-10T02:55:28Z merged: 2015-11-10T06:36:44Z

1. [12330](http://github.com/cms-sw/cmssw/pull/12330){:target="_blank"}  from **@Dr15Jones**: Fix problem in edmStreamStallGrapher `core`  created: 2015-11-10T00:54:46Z merged: 2015-11-10T09:01:14Z

1. [12329](http://github.com/cms-sw/cmssw/pull/12329){:target="_blank"}  from **@fwyzard**: ignore empty paths when determining the first and last [End]Path `hlt`  created: 2015-11-10T00:05:38Z merged: 2015-11-10T06:41:17Z

1. [12324](http://github.com/cms-sw/cmssw/pull/12324){:target="_blank"}  from **@kpedro88**: save particleFlowRecHitHBHE and particleFlowRecHitHF collections `reconstruction`  created: 2015-11-09T17:20:16Z merged: 2015-11-11T09:51:13Z

1. [12322](http://github.com/cms-sw/cmssw/pull/12322){:target="_blank"}  from **@davidlt**: Fix temporaries in the header `dqm`  created: 2015-11-09T16:09:18Z merged: 2015-11-10T17:02:31Z

1. [12319](http://github.com/cms-sw/cmssw/pull/12319){:target="_blank"}  from **@ianna**: HGCal DB Geometry Reader `db`  `geometry`  created: 2015-11-09T15:20:28Z merged: 2015-11-12T07:31:11Z

1. [12313](http://github.com/cms-sw/cmssw/pull/12313){:target="_blank"}  from **@hroskes**: Fix systematic misalignment tool `alca`  created: 2015-11-08T18:42:05Z merged: 2015-11-10T09:01:24Z

1. [12311](http://github.com/cms-sw/cmssw/pull/12311){:target="_blank"}  from **@srimanob**: fix FlatPU prob. `simulation`  created: 2015-11-08T17:39:28Z merged: 2015-11-09T08:34:32Z

1. [12309](http://github.com/cms-sw/cmssw/pull/12309){:target="_blank"}  from **@mkirsano**: clean LHEInterface: remove files that are not compiled `generators`  created: 2015-11-07T17:09:31Z merged: 2015-11-08T12:56:11Z

1. [12307](http://github.com/cms-sw/cmssw/pull/12307){:target="_blank"}  from **@VinInn**: Stateless clusterizer for SiStrip `reconstruction`  created: 2015-11-07T15:19:42Z merged: 2015-11-12T06:51:24Z

1. [12305](http://github.com/cms-sw/cmssw/pull/12305){:target="_blank"}  from **@lathomas**: Reload calogeometry for every event:  `reconstruction`  created: 2015-11-07T01:32:28Z merged: 2015-11-10T06:41:23Z

1. [12303](http://github.com/cms-sw/cmssw/pull/12303){:target="_blank"}  from **@wmtan**: Fix heavy ion relval tests `analysis`  `generators`  `simulation`  created: 2015-11-06T23:49:17Z merged: 2015-11-11T09:46:21Z

1. [12301](http://github.com/cms-sw/cmssw/pull/12301){:target="_blank"}  from **@bsunanda**: bsunanda:Run2-hcx47 Add trigger primitive version in geometry `geometry`  created: 2015-11-06T22:32:50Z merged: 2015-11-11T08:36:24Z

1. [12300](http://github.com/cms-sw/cmssw/pull/12300){:target="_blank"}  from **@kpedro88**: save particleFlowRecHitHBHE and particleFlowRecHitHF collections `reconstruction`  created: 2015-11-06T20:42:53Z merged: 2015-11-10T09:01:34Z

1. [12299](http://github.com/cms-sw/cmssw/pull/12299){:target="_blank"}  from **@gpetruc**: MuonAnalysis/MuonAssociators: getByToken in TriggerObjectFilterByCollection `analysis`  `comparison`  created: 2015-11-06T20:40:53Z merged: 2015-11-09T08:35:31Z

1. [12297](http://github.com/cms-sw/cmssw/pull/12297){:target="_blank"}  from **@fratnikov**: data mixer tuning for HCAL and ECAL `operations`  `simulation`  created: 2015-11-06T19:20:18Z merged: 2015-11-10T08:57:48Z

1. [12296](http://github.com/cms-sw/cmssw/pull/12296){:target="_blank"}  from **@mariadalfonso**: Met uncertainties from GT: remove txt file dependency `analysis`  created: 2015-11-06T19:01:09Z merged: 2015-11-10T06:39:55Z

1. [12294](http://github.com/cms-sw/cmssw/pull/12294){:target="_blank"}  from **@fabozzi**: replacing 2012 relval with 2015 relval for reduced matrix tests `pdmv`  created: 2015-11-06T17:48:10Z merged: 2015-11-08T13:01:09Z

1. [12293](http://github.com/cms-sw/cmssw/pull/12293){:target="_blank"}  from **@fabozzi**: replacing 2012 relval with 2015 relval for reduced matrix tests `pdmv`  created: 2015-11-06T17:21:54Z merged: 2015-11-10T08:56:29Z

1. [12281](http://github.com/cms-sw/cmssw/pull/12281){:target="_blank"}  from **@ghellwig**: Fix bug in caching of surface deformations. `alca`  created: 2015-11-06T10:37:30Z merged: 2015-11-10T06:41:28Z

1. [12277](http://github.com/cms-sw/cmssw/pull/12277){:target="_blank"}  from **@smorovic**: Fix race condition in DAQ modules for 80X (make new PR) `daq`  `reconstruction`  created: 2015-11-05T17:59:54Z merged: 2015-11-12T06:51:29Z

1. [12275](http://github.com/cms-sw/cmssw/pull/12275){:target="_blank"}  from **@mark-grimes**: phase1Pixel era digitisation additions `comparison`  `simulation`  created: 2015-11-05T16:44:57Z merged: 2015-11-12T07:31:27Z

1. [12269](http://github.com/cms-sw/cmssw/pull/12269){:target="_blank"}  from **@ggovi**: Clean up from conddb V1 code `alca`  `db`  `dqm`  created: 2015-11-05T14:12:07Z merged: 2015-11-12T06:51:36Z

1. [12266](http://github.com/cms-sw/cmssw/pull/12266){:target="_blank"}  from **@ggovi**: Fix for conddb python tools `db`  created: 2015-11-05T10:49:00Z merged: 2015-11-12T06:51:41Z

1. [12257](http://github.com/cms-sw/cmssw/pull/12257){:target="_blank"}  from **@bbockelm**: Provide a utility for efficiently copying multiple files to the local `core`  created: 2015-11-04T15:42:55Z merged: 2015-11-11T09:51:24Z

1. [12236](http://github.com/cms-sw/cmssw/pull/12236){:target="_blank"}  from **@friccita**: corrected wrong cfi file called for PhaseIPixel tag in dumpSimGeometry_cfg.py `comparison`  `visualization`  created: 2015-11-03T00:10:47Z merged: 2015-11-08T16:41:27Z

1. [12230](http://github.com/cms-sw/cmssw/pull/12230){:target="_blank"}  from **@istaslis**: Set mva tight value of initial step to be equal to highPurity mva (76X version of #12223) `reconstruction`  created: 2015-11-02T15:51:47Z merged: 2015-11-10T08:56:40Z

1. [12060](http://github.com/cms-sw/cmssw/pull/12060){:target="_blank"}  from **@ferencek**: Updated logic in HadronAndPartonSelector `analysis`  created: 2015-10-23T01:27:49Z merged: 2015-11-10T06:37:49Z

1. [11910](http://github.com/cms-sw/cmssw/pull/11910){:target="_blank"}  from **@sachikot**: SCAL online DQM monitoring `dqm`  created: 2015-10-19T08:09:54Z merged: 2015-11-10T19:45:44Z

1. [11909](http://github.com/cms-sw/cmssw/pull/11909){:target="_blank"}  from **@fioriNTU**: Fix TrackSplit module `comparison`  `dqm`  created: 2015-10-19T08:09:37Z merged: 2015-11-10T19:46:10Z

1. [11892](http://github.com/cms-sw/cmssw/pull/11892){:target="_blank"}  from **@JetMETdqmval**: update PFJetID for RunII, add ak8 MiniAOD monitoring, adopt ak4CHS JEC for type1 MET `analysis`  `dqm`  created: 2015-10-19T07:24:37Z merged: 2015-11-16T07:49:10Z

1. [11879](http://github.com/cms-sw/cmssw/pull/11879){:target="_blank"}  from **@bsunanda**: bsunanda:Run2 hcx43 Modify the scripts (Salavat) for pion scans `comparison`  `dqm`  created: 2015-10-19T07:23:16Z merged: 2015-11-10T19:48:15Z

1. [11612](http://github.com/cms-sw/cmssw/pull/11612){:target="_blank"}  from **@cms-btv-pog**: Updated flavor parton selection for Pythia8 `analysis`  `comparison`  created: 2015-10-01T20:30:37Z merged: 2015-11-10T08:50:28Z

#### CMSDIST Changes between Tags REL/CMSSW_8_0_0_pre1/slc6_amd64_gcc493 and REL/CMSSW_8_0_0_pre2/slc6_amd64_gcc493:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_8_0_0_pre1/slc6_amd64_gcc493...REL/CMSSW_8_0_0_pre2/slc6_amd64_gcc493)



1. [1963](http://github.com/cms-sw/cmssw/pull/1963){:target="_blank"}  from **@smuzaffar**: update branch and tag in  root.spec created: 2014-01-08T16:51:25Z merged: 2014-01-09T09:48:23Z

1. [1962](http://github.com/cms-sw/cmssw/pull/1962){:target="_blank"}  from **@degano**: Update sherpa to version 2.2.0 with CMS patches. created: 2014-01-08T15:40:12Z merged: 2014-01-09T09:49:11Z

1. [1960](http://github.com/cms-sw/cmssw/pull/1960){:target="_blank"}  from **@iahmad-khan**: added new davix tool created: 2014-01-08T11:52:54Z merged: 2014-01-08T12:55:35Z

1. [1955](http://github.com/cms-sw/cmssw/pull/1955){:target="_blank"}  from **@degano**: Update pythia8 to include Heavy other matching patch. created: 2014-01-07T13:46:52Z merged: 2014-01-07T16:29:27Z

1. [1954](http://github.com/cms-sw/cmssw/pull/1954){:target="_blank"}  from **@degano**: Update Openloops to CMS version 1.2.3. created: 2014-01-07T12:47:23Z merged: None
