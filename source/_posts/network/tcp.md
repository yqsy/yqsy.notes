---
title: tcp
date: 2017-11-07 20:15:44
categories: [网络相关]
---

<!-- TOC -->

- [1. TCP和UDP在内核缓冲区上的区别](#1-tcp和udp在内核缓冲区上的区别)
- [2. TCP头部](#2-tcp头部)

<!-- /TOC -->


<a id="markdown-1-tcp和udp在内核缓冲区上的区别" name="1-tcp和udp在内核缓冲区上的区别"></a>
# 1. TCP和UDP在内核缓冲区上的区别

?recvfrom底层没有缓冲区吗?

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171107_205238.png)


<a id="markdown-2-tcp头部" name="2-tcp头部"></a>
# 2. TCP头部

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171107_205720.png)

* 16位端口号(port number):告知主机该报文段是来自哪里,`/etc/services`
* 32位序号(sequence number):一次TCP通信过程中某一个方向上的字节流的每个字节的编号
* 32位确认号(acknowledgement number):用作对另一放发送来的TCP报文段的响应.其值是TCP报文段的序号值加1
* 4位头部长度(header length):标识该TCP头部有多少个字节,4位最大能表示15,所以TCP头部最长是60字节
* 6位包含:
  * URG标志: 表示紧急指针(urgent pointer)是否有效
  * ACK标志: 表示确认号是否有效
  * PSH标志: 提示接收端应用程序应该立即从TCP接收缓冲区中读走数据,为接收后续数据腾出控件
  * RST标志: 表示要求对方重新建立连接,常常称为复位报文段
  * SYN标志: 表示请求建立一个连接,常常称为同步报文段
  * FIN标志: 表示通知对方本端要关闭了,常常成为结束报文段
* 16位窗口大小(window size): 是TCP`流量控制`的一个手段,指的是接收通告窗口(Receiver Window,RWND).它告诉对方本端的TCP接收缓冲区还能容纳多少字节的数据,这样对方就可以控制发送数据的速度
* 16位校验和(TCP checksum): 由发送端填充,接收端对TCP报文段执行CRC算法以校验TCP报文段在整个传输过程中是否损坏
* 16位紧急指针(urgent pointer): 是一个正的偏移量,它和序号字段的值相加表示最后一个紧急数据的下一字节的序号
