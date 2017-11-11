---
title: Windows开发Linux程序积累
date: 2017-11-06 15:20:00
categories: [coding]
---

<!-- TOC -->

- [1. 基础要点](#1-基础要点)
- [2. Windows类Linux操作环境](#2-windows类linux操作环境)
    - [2.1. Cygwin](#21-cygwin)
    - [2.2. MinGW](#22-mingw)
    - [2.3. MSYS](#23-msys)
    - [2.4. MinGW-w64](#24-mingw-w64)
    - [2.5. MYSYS2](#25-mysys2)
- [3. 代码同步](#3-代码同步)
    - [3.1. beyond compare](#31-beyond-compare)
    - [3.2. rsync](#32-rsync)

<!-- /TOC -->


<a id="markdown-1-基础要点" name="1-基础要点"></a>
# 1. 基础要点

平常开发的主要是Linux后台程序,开发平台为windows

因为有些语言或库对对于跨平台不理想,所以还是需要`windows编辑`+`Linux运行/调试`那么有几个问题需要注意,整理一下:

* Windows类Linux操作环境
* 如何将代码从Windows sync 到Linux之上
* 源代码文件从`CRLF`转换成`LF`
* 某些语言,tab转换成空格(在这里不重要)
* 某些语言,注意编码(在这里不重要)

<a id="markdown-2-windows类linux操作环境" name="2-windows类linux操作环境"></a>
# 2. Windows类Linux操作环境

* https://www.zhihu.com/question/22137175

<a id="markdown-21-cygwin" name="21-cygwin"></a>
## 2.1. Cygwin
提供了运行于Windows平台的类Unix环境,提供了一套抽象层dll,用于将部分Posix调用转换成Windows的调用API (基本就是传说中的GNU/NT系统 对照GNU/Linux,GNU/BSD,GNU/HURD)

<a id="markdown-22-mingw" name="22-mingw"></a>
## 2.2. MinGW
Minimalist GNU for Windows,用于进行Windows应用开发的GNU工具链(开发环境)

<a id="markdown-23-msys" name="23-msys"></a>
## 2.3. MSYS
辅助Windows版MinGW进行命令行开发的配套软件包,提供了部分Unix工具以使得MinGW的工具使用起来更方便一些.如果不喜欢庞大的Cygwin,而且使用不多,可以试试.不过喜欢完整体验,不在乎磁盘占用等等,还是推荐Cygwin而不是MSYS

<a id="markdown-24-mingw-w64" name="24-mingw-w64"></a>
## 2.4. MinGW-w64

新一代的MinGW,支持更多的API,支持64位应用开发

<a id="markdown-25-mysys2" name="25-mysys2"></a>
## 2.5. MYSYS2

fork了Cygwin,对于不喜欢庞大的Cygwin的用户而言,推荐试试mysys2

<a id="markdown-3-代码同步" name="3-代码同步"></a>
# 3. 代码同步

<a id="markdown-31-beyond-compare" name="31-beyond-compare"></a>
## 3.1. beyond compare
文件夹同步-镜像功能,使用sftp协议,缺点是需要手动点击同步,比较繁琐

<a id="markdown-32-rsync" name="32-rsync"></a>
## 3.2. rsync

* https://blog.tiger-workshop.com/add-rsync-to-git-bash-for-windows/
