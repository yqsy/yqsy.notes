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

