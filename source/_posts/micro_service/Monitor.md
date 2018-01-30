---
title: Monitor
date: 2018-01-02 14:08:11
categories: [微服务]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [核心问题](#核心问题)

<!-- /TOC -->


<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://blog.serverdensity.com/80-linux-monitoring-tools-know/ (80个监控工具)
* http://www.linuxscrew.com/2012/03/22/linux-monitoring-tools/ (排名前5监控系统)
* http://my-netdata.io/ (my-netdata.io)
* https://www.zabbix.com/
* https://www.nagios.org/
* https://github.com/nicolargo/glances (知乎上看到的工具,目测超好用)
* http://glances.readthedocs.io/en/stable/aoa/cpu.html (glance说明文档)
* http://zhuanlan.zhihu.com/p/20385707 (手写 监控,赞)
* https://github.com/nkrode/RedisLive (redis的监控赞,学习一下)
* https://github.com/XiaoMi/open-falcon (小米开源的监控)


<a id="markdown-核心问题" name="核心问题"></a>
# 核心问题

* 数据如何采集?应用程序提供查询接口?写入文件?还是直接提供web接口?
* 采集多台机器是否需要agent?
