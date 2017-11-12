---
title: Windows开发Linux程序积累
date: 2017-11-12 15:20:00
categories: [coding]
---

<!-- TOC -->

- [1. 基础要点](#1-基础要点)
- [2. Windows写LinuxC /C++代码](#2-windows写linuxc-c代码)
- [3. Windows类Linux操作环境](#3-windows类linux操作环境)
    - [3.1. Cygwin](#31-cygwin)
    - [3.2. MinGW](#32-mingw)
    - [3.3. MSYS](#33-msys)
    - [3.4. MinGW-w64](#34-mingw-w64)
    - [3.5. MYSYS2](#35-mysys2)
- [4. 代码同步](#4-代码同步)
    - [4.1. beyond compare](#41-beyond-compare)
    - [4.2. rsync+inotifywait](#42-rsyncinotifywait)

<!-- /TOC -->


<a id="markdown-1-基础要点" name="1-基础要点"></a>
# 1. 基础要点

平常开发的主要是Linux后台程序,开发平台为windows

因为有些语言或库对对于跨平台不理想,所以还是需要`windows编辑`+`Linux运行/调试`那么有几个问题需要注意,整理一下:

* Windows如何写Linux C/C++代码 (code complete/头文件)
* Windows类Linux操作环境
* 如何将代码从Windows sync 到Linux之上
* 源代码文件从`CRLF`转换成`LF`(git + ide搭配控制好)
* 某些语言,tab转换成空格(ide自动做到)
* 某些语言,注意编码(只有`c/c++`需要注意,不要写中文把)

<a id="markdown-2-windows写linuxc-c代码" name="2-windows写linuxc-c代码"></a>
# 2. Windows写LinuxC /C++代码

使用工具
* https://www.jetbrains.com/clion/ (太重量级了)
* https://code.visualstudio.com/insiders/ (轻巧些)
* understand (看代码用)

参考
* https://code.visualstudio.com/docs/languages/cpp

`Ctrl+Shift+P`将头文件目录设置成linux的头文件

* D:/reference/refer/usr/include
* D:/reference/refer/usr/include/c++/4.8.2

```bash
# linux
# 拷贝头文件
tar -cvzf /tmp/include.tgz /usr/include

# windows
scp root@192.168.198.130:/tmp/include.tgz /d/reference/refer/
tar -xvzf include.tgz
```

<a id="markdown-3-windows类linux操作环境" name="3-windows类linux操作环境"></a>
# 3. Windows类Linux操作环境

* https://www.zhihu.com/question/22137175

<a id="markdown-31-cygwin" name="31-cygwin"></a>
## 3.1. Cygwin
提供了运行于Windows平台的类Unix环境,提供了一套抽象层dll,用于将部分Posix调用转换成Windows的调用API (基本就是传说中的GNU/NT系统 对照GNU/Linux,GNU/BSD,GNU/HURD)

<a id="markdown-32-mingw" name="32-mingw"></a>
## 3.2. MinGW
Minimalist GNU for Windows,用于进行Windows应用开发的GNU工具链(开发环境)

<a id="markdown-33-msys" name="33-msys"></a>
## 3.3. MSYS
辅助Windows版MinGW进行命令行开发的配套软件包,提供了部分Unix工具以使得MinGW的工具使用起来更方便一些.如果不喜欢庞大的Cygwin,而且使用不多,可以试试.不过喜欢完整体验,不在乎磁盘占用等等,还是推荐Cygwin而不是MSYS

<a id="markdown-34-mingw-w64" name="34-mingw-w64"></a>
## 3.4. MinGW-w64

新一代的MinGW,支持更多的API,支持64位应用开发

<a id="markdown-35-mysys2" name="35-mysys2"></a>
## 3.5. MYSYS2

fork了Cygwin,对于不喜欢庞大的Cygwin的用户而言,推荐试试mysys2

<a id="markdown-4-代码同步" name="4-代码同步"></a>
# 4. 代码同步

<a id="markdown-41-beyond-compare" name="41-beyond-compare"></a>
## 4.1. beyond compare
文件夹同步-镜像功能,使用sftp协议,缺点是需要手动点击同步,比较繁琐

<a id="markdown-42-rsyncinotifywait" name="42-rsyncinotifywait"></a>
## 4.2. rsync+inotifywait

* https://blog.tiger-workshop.com/add-rsync-to-git-bash-for-windows/
* https://github.com/thekid/inotify-win

可以`排除.gitignore`中的文件以及`.git`文件夹,还有`删除多余的文件`
```bash
rsync -av ./ --filter=':- .gitignore' --cvs-exclude --delete root@192.168.198.130:/root/reference/linux_socket_test
```

inotifywait
```bash

inotifywait -mrq . | while read file ; do
    echo '111';
done

inotifywait -mrq . | while read file ; do
    rsync -av . --filter=':- .gitignore' --cvs-exclude --delete root@192.168.198.130:/root/reference/linux_socket_test;
done
```