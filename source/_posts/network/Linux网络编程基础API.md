---
title: Linux网络编程基础API
date: 2017-11-07 20:15:44
categories: [网络相关]
---

<!-- TOC -->

- [1. 主机字节序和网络字节序](#1-主机字节序和网络字节序)
- [2. 常用socket函数](#2-常用socket函数)
- [3. 高级I/O函数](#3-高级io函数)

<!-- /TOC -->

<a id="markdown-1-主机字节序和网络字节序" name="1-主机字节序和网络字节序"></a>
# 1. 主机字节序和网络字节序

字节序分为大端字节序(big endian)和小端字节序(little endian),`现代PC大多采用小端字节序`,因此小端字节序又被称为主机字节序.大端字节序也称为网络字节序,它给所有接收数据的主机提供了一个正确解释收到的格式化数据的保证

https://github.com/yqsy/linux_socket_test/blob/master/check_byte_order.cpp


<a id="markdown-2-常用socket函数" name="2-常用socket函数"></a>
# 2. 常用socket函数

使用`man 2 fun`查看说明

* socket
* bind
* listen
* accept
* connect
* close
* send
* recv
* sendto
* recvfrom
* sendmsg
* recvmsg

地址信息
* getsockname 获取对应的本端socket地址
* getpeername 获取多赢的远端socket地址

socket选项
* getsockopt  
* setsockopt
* man 7 socket 获得选项说明

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171109_151310.png)

使用`man 3 fun`查看说明

* gethostbyaddr 根据IP地址获取主机的完整信息
* gethostbyname 根据主机名获取ip地址
* getservbyname 根据名称获取服务的完整信息
* getservbyport 根据端口号获取某个服务的完整信息
* getaddrinfo 既能通过主机名获得IP地址,也能通过服务名获得端口号
* getnameinfo 通过socket地址同事获得以字符串表示的主机名和服务名

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

