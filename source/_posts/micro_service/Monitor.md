---
title: Monitor
date: 2018-01-02 14:08:11
categories: [微服务]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 核心问题](#2-核心问题)
- [3. 时序数据库实践](#3-时序数据库实践)
- [4. 分析小计](#4-分析小计)

<!-- /TOC -->


<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://www.zhihu.com/question/19636141/answer/13154248 (常用的运维,管理工具)
* https://blog.serverdensity.com/80-linux-monitoring-tools-know/ (80个监控工具)
* http://www.linuxscrew.com/2012/03/22/linux-monitoring-tools/ (排名前5监控系统)
* http://my-netdata.io/ (my-netdata.io 太复杂啦)
* https://hub.docker.com/r/titpetric/netdata/  (这也能在docker里面部署吗)
* https://www.zabbix.com/
* https://www.nagios.org/
* https://github.com/nicolargo/glances (知乎上看到的工具,目测超好用)
* http://glances.readthedocs.io/en/stable/aoa/cpu.html (glance说明文档)
* http://zhuanlan.zhihu.com/p/20385707 (手写 监控,赞)
* https://github.com/nkrode/RedisLive (redis的监控赞,学习一下)
* https://github.com/XiaoMi/open-falcon (小米开源的监控)
* https://zhuanlan.zhihu.com/p/32764309 (17个开源的运维监控系统)
* http://blog.csdn.net/yuzhihui_no1/article/details/65435471 (rdd数据库 时序图环形 复写)
* http://liubin.org/blog/2016/02/25/tsdb-list-part-1/ (时序数据库)
* https://oss.oetiker.ch/rrdtool/ (rrdtool)


<a id="markdown-2-核心问题" name="2-核心问题"></a>
# 2. 核心问题

* 数据如何采集?应用程序提供查询接口?写入文件?还是直接提供web接口?
* 采集多台机器是否需要agent?

<a id="markdown-3-时序数据库实践" name="3-时序数据库实践"></a>
# 3. 时序数据库实践

* https://github.com/pldimitrov/Rrd/issues/1  (安装)

```bash
yum install rrdtool-devel rrdtool -y
yum install python34-devel -y
pip3 install rrdtool
```

<a id="markdown-4-分析小计" name="4-分析小计"></a>
# 4. 分析小计

```
strace netstat -g &> 1.txt && grep 'open' ./1.txt  > 2.txt

https://www.centos.org/docs/5/html/5.1/Deployment_Guide/s2-proc-meminfo.html
vmstat 内存
open("/proc/meminfo", O_RDONLY)         = 3
open("/proc/stat", O_RDONLY)            = 4
open("/proc/vmstat", O_RDONLY)          = 5

iostat  cpu  / 磁盘I/O
open("/proc/diskstats", O_RDONLY)       = 3
open("/proc/uptime", O_RDONLY)          = 3
open("/proc/stat", O_RDONLY)            = 3

mpstat
open("/proc/interrupts", O_RDONLY)      = 3
open("/proc/softirqs", O_RDONLY)        = 3
open("/proc/uptime", O_RDONLY)          = 3
open("/proc/stat", O_RDONLY)            = 3


tcp 连接数
netstat -ant

open("/proc/net/tcp", O_RDONLY)         = 3
open("/proc/net/tcp6", O_RDONLY)        = 3

udp
netstat -anu

open("/proc/net/udp", O_RDONLY)         = 3
open("/proc/net/udp6", O_RDONLY)        = 3


所有监听
netstat -tuln

如果设置了-p则会读取每一个文件
open("/proc/net/tcp", O_RDONLY)         = 3
open("/proc/net/tcp6", O_RDONLY)        = 3
open("/proc/net/udp", O_RDONLY)         = 3
open("/proc/net/udp6", O_RDONLY)        = 3


静态分析
netstat -s
open("/proc/meminfo", O_RDONLY|O_CLOEXEC) = 3
open("/proc/net/snmp", O_RDONLY)        = 3
open("/proc/net/netstat", O_RDONLY)     = 3
open("/proc/net/sctp/snmp", O_RDONLY)   = -1 ENOENT (No such file or directory)


路由表
netstat -r

open("/etc/nsswitch.conf", O_RDONLY|O_CLOEXEC) = 4
open("/etc/resolv.conf", O_RDONLY|O_CLOEXEC) = 4
open("/etc/host.conf", O_RDONLY|O_CLOEXEC) = 4
open("/etc/hosts", O_RDONLY|O_CLOEXEC)  = 4
open("/etc/networks", O_RDONLY|O_CLOEXEC) = 4



网卡
netstat -i

open("/proc/net/dev", O_RDONLY)         = 6


网卡 similar to ifconfig
netstat -ie

open("/proc/net/dev", O_RDONLY)         = 6
open("/proc/net/if_inet6", O_RDONLY)    = 6


磁盘I/O
网络I/O
CPU
内存
中断
磁盘容量

业务信息
接口?


时间维度:
24小时
一周
一个月

86400 / 3 = 28800 (每天生成)
28800 * 30 = 201600

```
