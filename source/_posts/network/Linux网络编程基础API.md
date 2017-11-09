---
title: Linux网络编程基础API
date: 2017-11-09 20:15:44
categories: [网络相关]
---

<!-- TOC -->

- [1. 主机字节序和网络字节序](#1-主机字节序和网络字节序)
- [2. 常用socket函数](#2-常用socket函数)
- [3. 高级I/O函数](#3-高级io函数)
- [4. I/O复用](#4-io复用)
    - [4.1. select](#41-select)
    - [4.2. poll](#42-poll)
    - [4.3. epoll](#43-epoll)
        - [4.3.1. LT(Level Trigger)电平触发和ET(Edge Trigger)边沿触发](#431-ltlevel-trigger电平触发和etedge-trigger边沿触发)
    - [4.4. 三者区别](#44-三者区别)

<!-- /TOC -->

<a id="markdown-1-主机字节序和网络字节序" name="1-主机字节序和网络字节序"></a>
# 1. 主机字节序和网络字节序

字节序分为大端字节序(big endian)和小端字节序(little endian),`现代PC大多采用小端字节序`,因此小端字节序又被称为主机字节序.大端字节序也称为网络字节序,它给所有接收数据的主机提供了一个正确m解释收到的格式化数据的保证

https://github.com/yqsy/linux_socket_test/blob/master/check_byte_order.cpp


<a id="markdown-2-常用socket函数" name="2-常用socket函数"></a>
# 2. 常用socket函数

使用`man 2 fun`查看说明

* socket https://linux.die.net/man/2/socket
* bind https://linux.die.net/man/2/bind
* listen https://linux.die.net/man/2/listen
* accept https://linux.die.net/man/2/accept
* connect https://linux.die.net/man/2/connect
* close https://linux.die.net/man/2/close
* send https://linux.die.net/man/2/send
* recv https://linux.die.net/man/2/recv
* sendto https://linux.die.net/man/2/sendto
* recvfrom https://linux.die.net/man/2/recvfrom
* sendmsg https://linux.die.net/man/2/sendmsg
* recvmsg https://linux.die.net/man/2/recvmsg

地址信息
* getsockname 获取对应的本端socket地址 https://linux.die.net/man/2/getsockname
* getpeername 获取多赢的远端socket地址 https://linux.die.net/man/2/getpeername

socket选项
* getsockopt https://linux.die.net/man/2/getsockopt 
* setsockopt https://linux.die.net/man/2/setsockopt
* man 7 socket 获得选项说明 https://linux.die.net/man/7/socket

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171109_151310.png)

使用`man 3 fun`查看说明

* gethostbyaddr 根据IP地址获取主机的完整信息 https://linux.die.net/man/3/gethostbyaddr
* gethostbyname 根据主机名获取ip地址 https://linux.die.net/man/3/gethostbyname
* getservbyname 根据名称获取服务的完整信息 https://linux.die.net/man/3/getservbyname
* getservbyport 根据端口号获取某个服务的完整信息 https://linux.die.net/man/3/getservbyport
* getaddrinfo 既能通过主机名获得IP地址,也能通过服务名获得端口号 https://linux.die.net/man/3/getaddrinfo
* getnameinfo 通过socket地址同事获得以字符串表示的主机名和服务名 https://linux.die.net/man/3/getnameinfo

<a id="markdown-3-高级io函数" name="3-高级io函数"></a>
# 3. 高级I/O函数

* pipe 函数可以创建一个管道,以实现进程间通信
* dup/dup2 创建新的文件描述符,和原有文件描述符指向相同文件,管道或者网络连接https://github.com/yqsy/linux_socket_test/blob/master/dup_cgi.cpp
* readv和writev 从文件描述符读到分散的内存块中/将多块分散的内存数据一并写入文件描述符中
* sendfile 在两个文件描述符之间直接传递数据,从而避免了内核缓冲区和用户缓冲区之间的数据拷贝,效率很高,这被称为零拷贝
* mmap和munmap 共享内存
* splice 在两个文件描述符之间移动数据
* tee 在两个管道文件描述符之间复制数据
* fcntl 对文件描述符的各种控制操作


<a id="markdown-4-io复用" name="4-io复用"></a>
# 4. I/O复用

<a id="markdown-41-select" name="41-select"></a>
## 4.1. select
* https://linux.die.net/man/2/select

```c++
int select(int nfds, fd_set *readfds, fd_set *writefds,
           fd_set *exceptfds, struct timeval *timeout);
```

<a id="markdown-42-poll" name="42-poll"></a>
## 4.2. poll

* https://linux.die.net/man/2/poll
```c++
int poll(struct pollfd *fds, nfds_t nfds, int timeout);
```
和select 类似

<a id="markdown-43-epoll" name="43-epoll"></a>
## 4.3. epoll
* https://linux.die.net/man/4/epoll
* epoll_create https://linux.die.net/man/2/epoll_create
* epoll_ctl https://linux.die.net/man/2/epoll_ctl
* epoll_wait https://linux.die.net/man/2/epoll_wait

<a id="markdown-431-ltlevel-trigger电平触发和etedge-trigger边沿触发" name="431-ltlevel-trigger电平触发和etedge-trigger边沿触发"></a>
### 4.3.1. LT(Level Trigger)电平触发和ET(Edge Trigger)边沿触发

对于采用LT工作模式的文件描述符`(默认)`,当epoll_wait检测到其上有事件发生并将此事件通知应用程序后,应用程序可以不立即处理该事件,当应用程序下一次调用epoll_wait时,epoll_wait还会再次向应用程序通告此事件,直到该事件被处理.

对于采用ET工作模式的文件描述符,当epoll_wait检测到其上有事件发生并将此事件通知应用程序后,应用程序必须立即处理该事件,因为后续的epoll_wait调用将不再向应用程序通知这一事件.

ET模式在很大程度上降低了同一个epoll事件被重复触发的次数,因此效率要比LT模式高.

<a id="markdown-44-三者区别" name="44-三者区别"></a>
## 4.4. 三者区别

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171109_204839.png)
