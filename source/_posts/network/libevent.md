---
title: libevent
date: 2017-11-12 22:58:21
categories: [网络相关]
---
<!-- TOC -->

- [1. 文档](#1-文档)
- [2. I/O框架库的作用](#2-io框架库的作用)
- [3. 特点](#3-特点)
- [4. 安装](#4-安装)
- [5. 应用层面分析](#5-应用层面分析)
    - [5.1. 主体对象event_base](#51-主体对象event_base)
    - [5.2. 信号event](#52-信号event)
    - [5.3. 定时器event](#53-定时器event)

<!-- /TOC -->

<a id="markdown-1-文档" name="1-文档"></a>
# 1. 文档
* http://www.wangafu.net/~nickm/libevent-2.0/doxygen/html/event_8h.html#func-members
* http://www.wangafu.net/~nickm/libevent-book/
* http://www.wangafu.net/~nickm/libevent-book/Ref4_event.html (常量看这个)
* http://www.wangafu.net/~nickm/libevent-book/Ref6_bufferevent.html (buffer event)
* http://www.wangafu.net/~nickm/libevent-2.0/doxygen/html/buffer_8h.html (bufferevent 声明查看这个)
* site:http://www.wangafu.net/~nickm/libevent-2.0/doxygen (这样搜索函数)

<a id="markdown-2-io框架库的作用" name="2-io框架库的作用"></a>
# 2. I/O框架库的作用

* 统一事件源,`I/O事件`,`信号`,`定时事件`,使代码简单易懂,又能避免一些潜在的逻辑错误
* 可移植性,不同的操作系统有不同的I/O复用方式,比如Solaris的dev/poll文件,FreeBSD的kqueue,Linux的epoll
* 对并发编程的支持.在多进程和多线程环境下,我们需要考虑各执行实体如何协同处理客户连接,信号和定时器,以避免竞态条件

>Unfortunately, none of the efficient interfaces is a ubiquitous standard. `Linux has epoll(), the BSDs (including Darwin) have kqueue(), Solaris has evports and /dev/poll…` and none of these operating systems has any of the others. So if you want to write a portable high-performance asynchronous application, you’ll need an abstraction that wraps all of these interfaces, and provides whichever one of them is the most efficient.

>And that’s what the lowest level of the Libevent API does for you. `It provides a consistent interface to various select() replacements`, using the most efficient version available on the computer where it’s running.


<a id="markdown-3-特点" name="3-特点"></a>
# 3. 特点

Libevent is a library for writing `fast portable nonblocking IO`. Its design goals are:

* Portability  
A program written using Libevent should work across all the platforms Libevent supports. Even when there is no really good way to do nonblocking IO, Libevent should support the so-so ways, so that your program can run in restricted environments.

* Speed  
Libevent tries to use the fastest available nonblocking IO implementations on each platform, and not to introduce much overhead as it does so.

* Scalability  
Libevent is designed to `work well` even with programs that need to have `tens of thousands of active sockets.`

* Convenience  
Whenever possible, the most natural way to write a program with Libevent should be the stable, portable way.

Libevent is divided into the following components:

* evutil  
Generic functionality to abstract out the differences between different platforms' networking implementations.

* event and event_base  
This is the heart of Libevent. It provides an abstract API to the various platform-specific, event-based nonblocking IO backends. It can let you know when sockets are ready to read or write, do basic timeout functionality, and detect OS signals.

* bufferevent  
These functions provide a more convenient wrapper around Libevent’s event-based core. They let your application request buffered reads and writes, and rather than informing you when sockets are ready to do, they let you know when IO has actually occurred.

The bufferevent interface also has multiple backends, so that
it can take advantage of systems that provide faster ways to do
nonblocking IO, such as the Windows IOCP API.
evbuffer
This module implements the buffers underlying bufferevents, and provides functions for efficient and/or convenient access.

* evhttp  
A simple HTTP client/server implementation.

* evdns  
A simple DNS client/server implementation.

* evrpc  
A simple RPC implementation.

<a id="markdown-4-安装" name="4-安装"></a>
# 4. 安装
```bash
yum install libevent-devel -y
```

<a id="markdown-5-应用层面分析" name="5-应用层面分析"></a>
# 5. 应用层面分析


<a id="markdown-51-主体对象event_base" name="51-主体对象event_base"></a>
## 5.1. 主体对象event_base

* 申请 `event_init`
* 释放 `event_base_free`
* 执行event loop `event_base_dispatch`
* 退出event loop `event_base_loopexit`

<a id="markdown-52-信号event" name="52-信号event"></a>
## 5.2. 信号event

* 申请 `evsignal_new`
* 释放 `event_free`
* 添加 `event_add(signal_event, NULL);`

<a id="markdown-53-定时器event" name="53-定时器event"></a>
## 5.3. 定时器event

* 申请 `evtimer_new`
* 释放 `event_free`
* 添加 `event_add(timeout_event, &tv);`
