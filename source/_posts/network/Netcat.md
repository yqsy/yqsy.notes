---
title: Netcat
date: 2017-12-16 13:10:18
categories: [网络相关]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 操作模式](#2-操作模式)
- [3. 所有版本](#3-所有版本)
- [4. 阻塞实现细节](#4-阻塞实现细节)
- [5. 非阻塞实现细节](#5-非阻塞实现细节)
    - [5.1. 阻塞I/O搭配 多路复用的问题](#51-阻塞io搭配-多路复用的问题)

<!-- /TOC -->


<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://en.wikipedia.org/wiki/Netcat


<a id="markdown-2-操作模式" name="2-操作模式"></a>
# 2. 操作模式

server:  
bind + listen + accept  


client:  
resolve adderss + connect  


<a id="markdown-3-所有版本" name="3-所有版本"></a>
# 3. 所有版本

* http://localhost:8080/source/xref/recipes/tpc/bin/netcat.cc  (thread-per-connection)
* http://localhost:8080/source/xref/recipes/python/netcat.py (IO-multiplexing)
* http://localhost:8080/source/xref/recipes/python/netcat-nonblock.py (IO-multiplexing)


Load generator: chargen
* http://localhost:8080/source/xref/recipes/tpc/bin/chargen.cc 
* http://localhost:8080/source/xref/recipes/python/chargen.py
* http://localhost:8080/source/xref/muduo/examples/simple/chargen/


<a id="markdown-4-阻塞实现细节" name="4-阻塞实现细节"></a>
# 4. 阻塞实现细节

阻塞I/O(thread per connection):  
每个连接对应两个线程,一个线程管一个方向(发,收),这种模型在go语言中用的很多,因为代价很低

读stdin->写socket ==== 读socket->写stdout

主线程负责读standin,写socket  
另外一根线程负责读socket,写standout  

难点是通知另外线程退出

* 读standin返回0 (好办)
* 读socket返回0  (主线程还堵塞在读standin,没好的办法唤醒)


特点
* 可以自动节流限速
* 适用连接数目不是很多
* 或者线程非常廉价 (c/c++/java不满足)

<a id="markdown-5-非阻塞实现细节" name="5-非阻塞实现细节"></a>
# 5. 非阻塞实现细节

io复用不是复用io,是复用执行线程的control.也被叫做event-driven,event-based,reactor

bsd->select  
atmt->poll  

其实io复用是在线程之前出现的,是因为单线程程序想处理多个描述符文件,只能使用io复用这样的方式,检查一遍哪个文件有事件,再去找到相应的文件去读写

<a id="markdown-51-阻塞io搭配-多路复用的问题" name="51-阻塞io搭配-多路复用的问题"></a>
## 5.1. 阻塞I/O搭配 多路复用的问题

* 比如客户连接进来了,多路复用得到信号,这时候连接断开了,调用阻塞accept函数,accept会永远阻塞下去.
* 比如write,可能对方的接收缓冲区已经满了,且不收,己方的发送缓冲区也已经满了,write会永远阻塞下去.
