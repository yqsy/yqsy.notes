---
title: tcp
date: 2017-11-07 20:15:44
categories: [网络相关]
---

<!-- TOC -->

- [1. TCP和UDP在内核缓冲区上的区别](#1-tcp和udp在内核缓冲区上的区别)
- [2. TCP头部](#2-tcp头部)
- [3. 链接建立与终止](#3-链接建立与终止)
- [4. 半关闭状态](#4-半关闭状态)
- [5. 连接超时](#5-连接超时)

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


![](http://ouxarji35.bkt.clouddn.com/snipaste_20171107_215803.png)

* kind2: 通信时,双方用该选项来协商最大报文段长度(Max Segment Size, MSS),TCP模块通常将MSS设置为(MTU-40)字节,避免本机发生IP分片,对以太网而言,MSS值是1460(1500-40)字节
* kind3: tcp头部,接收通告窗口大小时用16位表示,最大为65535字节,但实际上TCP模块允许的接收通告窗口远远不止这个数(为了提高吞吐量)`RFC 1323`
* kind4: 选择性确认(Selective Acknowledgement,SACK)选项,TCP模块会重传被确认的TCP报文段后续的所有报文段,这样原先已经正确传输的TCP报文段也可能重复发送,从而降低了TCP的性能.SACK技术使TCP模块只重新发送丢失的TCP报文段,`cat /proc/sys/net/ipv4/tcp_sack`查看是否开启
* kind5: SACK实际工作的选项
* kind8: 事件戳选项,该选项提供了较为准确的计算通信双方之间的回路事件(Round Trip Time,RTT)的方法`cat /proc/sys/net/ipv4/tcp_timestamps`

<a id="markdown-3-链接建立与终止" name="3-链接建立与终止"></a>
# 3. 链接建立与终止

* https://www.zhihu.com/question/24853633 (为什么需要3次握手)

> 为了防止已失效的连接请求报文段突然又传送到了服务端,因而产生错误client发出的第一个连接请求报文段并没有丢失，而是在某个网络结点长时间的滞留了，以致延误到连接释放以后的某个时间才到达server。本来这是一个早已失效的报文段。但server收到此失效的连接请求报文段后，就误认为是client再次发出的一个新的连接请求。于是就向client发出确认报文段，同意建立连接。假设不采用“三次握手”，那么只要server发出确认，新的连接就建立了。由于现在client并没有发出建立连接的请求，因此不会理睬server的确认，也不会向server发送数据。但server却以为新的运输连接已经建立，并一直等待client发来数据。这样，server的很多资源就白白浪费掉了。采用“三次握手”的办法可以防止上述现象发生。

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171107_222407.png)

<a id="markdown-4-半关闭状态" name="4-半关闭状态"></a>
# 4. 半关闭状态

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171108_123459.png)

TCP连接是全双工的,所以它允许两个方向的数据传输被独立关闭,换言之,通信的一端可以发送结束报文段给对方,告诉它本端已经完成了数据的发送,但允许继续接收来自对方的数据,直到对方也发送结束报文段以关闭连接

<a id="markdown-5-连接超时" name="5-连接超时"></a>
# 5. 连接超时

`cat /proc/sys/net/ipv4/tcp_syn_retries`,重连次数,windows是21秒,因为重连3次,3+6+12为21

* https://serverfault.com/questions/193160/which-is-the-default-tcp-connect-timeout-in-windows

```bash
# 测试脚本
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 t1 = datetime.now()
 try:
     sock.connect(('202.5.19.13', 443))
 except TimeoutError:
       pass
 except ConnectionRefusedError:
     pass
 t2 = datetime.now()
 print(t2 - t1)
```
