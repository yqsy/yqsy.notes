---
title: Libevent
date: 2017-11-12 22:58:21
categories: [网络相关]
---
<!-- TOC -->

- [1. 文档](#1-文档)
- [2. I/O框架库的作用](#2-io框架库的作用)
- [3. 安装](#3-安装)
- [4. 应用层面分析](#4-应用层面分析)
    - [4.1. 主体对象event_base](#41-主体对象event_base)
    - [4.2. 信号event](#42-信号event)
    - [4.3. 定时器event](#43-定时器event)

<!-- /TOC -->

<a id="markdown-1-文档" name="1-文档"></a>
# 1. 文档
* http://www.wangafu.net/~nickm/libevent-2.0/doxygen/html/event_8h.html#func-members
* http://www.wangafu.net/~nickm/libevent-book/


<a id="markdown-2-io框架库的作用" name="2-io框架库的作用"></a>
# 2. I/O框架库的作用

* 统一事件源,`I/O事件`,`信号`,`定时事件`,使代码简单易懂,又能避免一些潜在的逻辑错误
* 可移植性,不同的操作系统有不同的I/O复用方式,比如Solaris的dev/poll文件,FreeBSD的kqueue,Linux的epoll
* 对并发编程的支持.在多进程和多线程环境下,我们需要考虑各执行实体如何协同处理客户连接,信号和定时器,以避免竞态条件

>Unfortunately, none of the efficient interfaces is a ubiquitous standard. `Linux has epoll(), the BSDs (including Darwin) have kqueue(), Solaris has evports and /dev/poll…` and none of these operating systems has any of the others. So if you want to write a portable high-performance asynchronous application, you’ll need an abstraction that wraps all of these interfaces, and provides whichever one of them is the most efficient.

>And that’s what the lowest level of the Libevent API does for you. `It provides a consistent interface to various select() replacements`, using the most efficient version available on the computer where it’s running.

<a id="markdown-3-安装" name="3-安装"></a>
# 3. 安装
```bash
yum install libevent-devel -y
```

<a id="markdown-4-应用层面分析" name="4-应用层面分析"></a>
# 4. 应用层面分析


<a id="markdown-41-主体对象event_base" name="41-主体对象event_base"></a>
## 4.1. 主体对象event_base

* 申请 `event_init`
* 释放 `event_base_free`
* 执行event loop `event_base_dispatch`
* 退出event loop `event_base_loopexit`

<a id="markdown-42-信号event" name="42-信号event"></a>
## 4.2. 信号event

* 申请 `evsignal_new`
* 释放 `event_free`
* 添加 `event_add(signal_event, NULL);`

<a id="markdown-43-定时器event" name="43-定时器event"></a>
## 4.3. 定时器event

* 申请 `evtimer_new`
* 释放 `event_free`
* 添加 `event_add(timeout_event, &tv);`
