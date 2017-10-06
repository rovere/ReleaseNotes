---
layout: post
title:  "7_2_2"
date:   2017-10-06 17:36:55 +0200
categories: cmssw
relmajor: 7
relminor: 2
relsubminor: 2
---

# CMSSW_7_2_2
#### Changes since CMSSW_7_2_1_patch4:

[compare to previous](https://github.com/cms-sw/cmssw/compare/CMSSW_7_2_1_patch4...CMSSW_7_2_2)



1. [6480](http://github.com/cms-sw/cmssw/pull/6480){:target="_blank"}  from **@Sam-Harper**: removing spurious error message from GsfElectron::ecalDriven()  72X `reconstruction`  created: 2014-11-18T16:44:59Z merged: 2014-11-19T08:51:27Z

1. [6485](http://github.com/cms-sw/cmssw/pull/6485){:target="_blank"}  from **@vadler**: 72X - fix `HadronAndPartonSelector` for unknown generators `analysis`  created: 2014-11-18T22:04:10Z merged: 2014-11-19T08:46:20Z

1. [6465](http://github.com/cms-sw/cmssw/pull/6465){:target="_blank"}  from **@apfeiffer1**: remove use of oracle for plugins, 72x version `db`  created: 2014-11-18T09:26:19Z merged: 2014-11-19T07:41:09Z

1. [6364](http://github.com/cms-sw/cmssw/pull/6364){:target="_blank"}  from **@wddgit**: Bug fix for NewEventStreamFileReader `core`  created: 2014-11-12T23:12:22Z merged: 2014-11-18T17:23:04Z

1. [6389](http://github.com/cms-sw/cmssw/pull/6389){:target="_blank"}  from **@ggovi**: Changed payload proxy cache as required from Framework - for 72X `alca`  `db`  created: 2014-11-13T21:33:26Z merged: 2014-11-18T17:22:53Z

1. [6418](http://github.com/cms-sw/cmssw/pull/6418){:target="_blank"}  from **@slava77**: fix crash in CtfSpecialSeedGenerator ocurring at run boundaries `reconstruction`  created: 2014-11-15T01:05:25Z merged: 2014-11-18T17:22:34Z

1. [5949](http://github.com/cms-sw/cmssw/pull/5949){:target="_blank"}  from **@ggovi**: PopCon packages updated with new functionalities for executing the uploa... `alca`  `db`  created: 2014-10-22T19:27:49Z merged: 2014-11-18T17:20:08Z

1. [6073](http://github.com/cms-sw/cmssw/pull/6073){:target="_blank"}  from **@tlampen**: Backport of #6030. Add features offline validation for72 x `alca`  created: 2014-10-29T10:33:36Z merged: 2014-11-18T17:19:47Z

1. [6194](http://github.com/cms-sw/cmssw/pull/6194){:target="_blank"}  from **@mbluj**: Tau DQM fix: HLTEgammaGeneric and HLT2PhotonTau filters for (72X) `dqm`  created: 2014-11-04T12:09:25Z merged: 2014-11-18T17:19:06Z

1. [6012](http://github.com/cms-sw/cmssw/pull/6012){:target="_blank"}  from cms-analysis-tools/CMSSW_7_3_X_AT_genHFHad... `analysis`  created: 2014-10-27T09:50:06Z merged: 2014-10-30T22:33:06Z

1. [6320](http://github.com/cms-sw/cmssw/pull/6320){:target="_blank"}  from **@yiiyama**: Fix filter for ecal_ and collection names for ecal_, ecalcalib_ `dqm`  created: 2014-11-11T02:09:22Z merged: 2014-11-18T17:18:18Z

1. [6391](http://github.com/cms-sw/cmssw/pull/6391){:target="_blank"}  from **@ggovi**: fix for IOVService test concurrency - 72X `alca`  `db`  created: 2014-11-13T21:37:18Z merged: 2014-11-18T17:18:06Z

1. [6477](http://github.com/cms-sw/cmssw/pull/6477){:target="_blank"}  from **@Dr15Jones**: Avoid an infinite loop in InitRootHandlers destructor `core`  created: 2014-11-18T14:44:24Z merged: 2014-11-18T17:16:43Z

1. [6478](http://github.com/cms-sw/cmssw/pull/6478){:target="_blank"}  from **@bbockelm**: Provide the ability to do a separate cache-hint for cloning. `core`  created: 2014-11-18T14:58:13Z merged: 2014-11-18T17:16:32Z

1. [6437](http://github.com/cms-sw/cmssw/pull/6437){:target="_blank"}  from **@smuzaffar**: Added the missing Done Checking dependency message needed by the IBs scripts created: 2014-11-17T11:25:37Z merged: 2014-11-17T11:25:56Z

1. [6339](http://github.com/cms-sw/cmssw/pull/6339){:target="_blank"}  from **@smorovic**: \* reading event type from FED header instead of L1 history `daq`  created: 2014-11-11T18:43:04Z merged: 2014-11-11T20:19:37Z

1. [6338](http://github.com/cms-sw/cmssw/pull/6338){:target="_blank"}  from **@smorovic**: Bugfix in TCDS data block reading `daq`  created: 2014-11-11T16:08:22Z merged: 2014-11-11T16:18:18Z

1. [6275](http://github.com/cms-sw/cmssw/pull/6275){:target="_blank"}  from **@dmitrijus**: Running an online DQM application will no longer require the monitoring ... `dqm`  created: 2014-11-07T16:59:56Z merged: 2014-11-11T15:52:55Z

1. [6287](http://github.com/cms-sw/cmssw/pull/6287){:target="_blank"}  from **@Martin-Grunewald**: Fix of HLTDeDxFilter for 72X `reconstruction`  created: 2014-11-08T05:23:16Z merged: 2014-11-11T15:52:44Z

1. [6309](http://github.com/cms-sw/cmssw/pull/6309){:target="_blank"}  from **@fwyzard**: TriggerRatesMonitor: fix booking of L1 Tech trigger rate plots `dqm`  created: 2014-11-10T14:26:40Z merged: 2014-11-11T15:52:32Z

#### CMSDIST Changes between Tags REL/CMSSW_7_2_1_patch4/slc6_amd64_gcc481 and REL/CMSSW_7_2_2/slc6_amd64_gcc481:

[compare to previous](https://github.com/cms-sw/cmsdist/compare/REL/CMSSW_7_2_1_patch4/slc6_amd64_gcc481...REL/CMSSW_7_2_2/slc6_amd64_gcc481)


