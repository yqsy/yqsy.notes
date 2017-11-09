---
title: Linux服务器程序规范
date: 2017-11-07 20:15:44
categories: [网络相关]
---

<!-- TOC -->

- [1. 规范](#1-规范)
- [2. 日志](#2-日志)
- [3. 系统资源限制](#3-系统资源限制)
- [4. 改变进程的根目录](#4-改变进程的根目录)
- [5. 服务器程序后台化](#5-服务器程序后台化)

<!-- /TOC -->

<a id="markdown-1-规范" name="1-规范"></a>
# 1. 规范

* Linux服务器程序一般以后台进程形式运行,后台进程又称守护进程(daemon),它没有控制终端,因而也不会意外接收到用户的输入,守护进程的父进程通常是init进程(PID为1的进程)
* Linux服务器程序通常有一套日志系统,它至少能输出日志到文件,大部分后台进程都在`/var/log`目录下拥有自己的日志目录
* Linux服务器程序一般以某个专门的非root身份运行,比如mysqld,httpd,syslogd等后台进程,分别拥有自己的运行账户mysql,apache和syslog
* Linux服务器程序通常是可配置的,服务器程序通常能处理很多命令行选项,如果一次运行的选项太多,则可以用配置文件来管理,绝大多数服务器程序都有配置问啊进,并存放在/etc目录下
* Linux服务器进程通常会在启动的时候生成一个PID文件并存入/var/run目录中,以记录后台进程的PID
* Linux服务器程序通常需要考虑系统资源和限制,以预测自身能承受多大负荷,比如进程可用文件描述符总数和内存总量等


<a id="markdown-2-日志" name="2-日志"></a>
# 2. 日志

rsyslogd守护进程在接收到用户进程或内核输入的日志后,会把它们输出至某些特定的日志文件,默认情况下,调试信息会保存至`/var/log/debug`,普通信息保存至`/var/log/messages`,内核信息则保存至`/var/log/kern.log`

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171109_162755.png)

<a id="markdown-3-系统资源限制" name="3-系统资源限制"></a>
# 3. 系统资源限制

* getrlimit
* setrlimit

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171109_163251.png)

<a id="markdown-4-改变进程的根目录" name="4-改变进程的根目录"></a>
# 4. 改变进程的根目录

* getcwd
* chdir

<a id="markdown-5-服务器程序后台化" name="5-服务器程序后台化"></a>
# 5. 服务器程序后台化

```c++

bool daemonize()
{
    /*创建子进程，关闭父进程，这样可以使程序在后台运行*/
    pid_t pid = fork();
    if (pid < 0)
    {
        return false;
    }
    else if (pid > 0)
    {
        exit(0);
    }
    /*设置文件权限掩码。当进程创建新文件（使用open(const char*pathname,int flags,mode_t mode)系统调用）时，文件的权限将是mode＆0777*/
    umask(0);
    /*创建新的会话，设置本进程为进程组的首领*/
    pid_t sid = setsid();
    if (sid < 0)
    {
        return false;
    }
    /*切换工作目录*/
    if ((chdir("/")) < 0)
    {
        return false;
    }
    /*关闭标准输入设备、标准输出设备和标准错误输出设备*/
    close(STDIN_FILENO);
    close(STDOUT_FILENO);
    close(STDERR_FILENO);
    /*关闭其他已经打开的文件描述符，代码省略*/
    /*将标准输入、标准输出和标准错误输出都定向到/dev/null文件*/
    open("/dev/null", O_RDONLY);
    open("/dev/null", O_RDWR);
    open("/dev/null", O_RDWR);
    return true;
}
```

Linux提供了完成同样功能的库函数:
```c++
#include <unistd.h>
int daemon(int nochdir, int noclose);
```
