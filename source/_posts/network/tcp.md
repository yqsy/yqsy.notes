---
title: tcp
date: 2017-11-07 20:15:44
categories: [网络相关]
---

<!-- TOC -->

- [1. TCP和UDP在内核缓冲区上的区别](#1-tcp和udp在内核缓冲区上的区别)
- [2. TCP头部](#2-tcp头部)
- [3. 链接建立与终止](#3-链接建立与终止)
    - [3.1. TIME_WAIT状态](#31-time_wait状态)
    - [3.2. 半关闭状态](#32-半关闭状态)
    - [3.3. 半打开连接](#33-半打开连接)
    - [3.4. 连接超时](#34-连接超时)
- [4. TCP状态转移](#4-tcp状态转移)
- [5. 数据流](#5-数据流)
    - [5.1. 交互数据流](#51-交互数据流)
        - [5.1.1. Nagle算法](#511-nagle算法)
        - [5.1.2. 延迟ack](#512-延迟ack)
    - [5.2. 成块数据流](#52-成块数据流)
    - [5.3. 带外数据](#53-带外数据)
- [6. 超时重传](#6-超时重传)
- [7. 拥塞控制](#7-拥塞控制)
    - [7.1. 慢启动和拥塞避免](#71-慢启动和拥塞避免)
    - [7.2. 快速重传和快速恢复](#72-快速重传和快速恢复)

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

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171108_134734.png)


<a id="markdown-31-time_wait状态" name="31-time_wait状态"></a>
## 3.1. TIME_WAIT状态

`RFC 1122`的建议值是2min

* 可靠地终止TCP连接
* 保证让迟来的TCP报文段有足够的时间被识别并丢弃

客户端程序不用担心TIME_WAIT的问题,因为客户端一般使用系统自动分配的临时端口号来建立连接,如果是服务器主动关闭连接后异常终止,我们可以使用`SO_REUSEADDR`来强制进程立即使用TIME_WAIT状态的连接占用的端口

<a id="markdown-32-半关闭状态" name="32-半关闭状态"></a>
## 3.2. 半关闭状态

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171108_123459.png)

TCP连接是全双工的,所以它允许两个方向的数据传输被独立关闭,换言之,通信的一端可以发送结束报文段给对方,告诉它本端已经完成了数据的发送,但允许继续接收来自对方的数据,直到对方也发送结束报文段以关闭连接

<a id="markdown-33-半打开连接" name="33-半打开连接"></a>
## 3.3. 半打开连接

服务器(或客户端)关闭或者异常终止了连接,而对方没有接收到结束报文段(比如发生了网络故障),此时,客户端(或服务器)还维持着原来的连接,而服务器(或客户端)即使重启,也已经没有该连接的任何信息了.我们称这种状态为`半打开连接`

服务器会对客户端半打开连接状态时发送的报文回应复位报文段

<a id="markdown-34-连接超时" name="34-连接超时"></a>
## 3.4. 连接超时

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

<a id="markdown-4-tcp状态转移" name="4-tcp状态转移"></a>
# 4. TCP状态转移

`粗虚线`表示典型的`服务器`端连接的状态转移.`粗实线`表示典型的`客户端`连接的状态转移

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171108_134609.png)

<a id="markdown-5-数据流" name="5-数据流"></a>
# 5. 数据流


<a id="markdown-51-交互数据流" name="51-交互数据流"></a>
## 5.1. 交互数据流
交互数据流仅包含很少的字节,例如`telnet`,`ssh`


<a id="markdown-511-nagle算法" name="511-nagle算法"></a>
### 5.1.1. Nagle算法
一个TCP连接通信双方在任意时刻都最多只能发送一个未被确认的TCP报文段,在该TCP报文段的确认到达之前不能发送其他TCP报文段.`确认数据到达的越快,数据发送的越快`,`避免大量的小数据`

<a id="markdown-512-延迟ack" name="512-延迟ack"></a>
### 5.1.2. 延迟ack
接收到数据时不是立即发送ACK,相反,它推迟发送.以便ACK与需要沿该方向发送的数据一起发送,绝大多数采用时延为200ms

<a id="markdown-52-成块数据流" name="52-成块数据流"></a>
## 5.2. 成块数据流
成块数据流对传输效率要求高.比如`ftp`

当传输大量大块数据的时候,发送方辉连续发送多个TCP报文段,接收方可以一次确认所有这些报文段.`接收通告窗口大小决定发送方能连续发送多少个TCP报文段`

`PSH`标志通知接收方尽快读取数据

<a id="markdown-53-带外数据" name="53-带外数据"></a>
## 5.3. 带外数据

>现在考虑TCP接收带外数据的过程。TCP接收端只有在接收到紧急指针标志时才检查紧急指针，然后根据紧急指针所指的位置确定带外数据的位置，并将它读入一个特殊的缓存中。这个缓存只有1字节，称为带外缓存。如果上层应用程序没有及时将带外数据从带外缓存中读出，则后续的带外数据（如果有的话）将覆盖它


<a id="markdown-6-超时重传" name="6-超时重传"></a>
# 6. 超时重传

Linux有两个重要的内核参数与TCP超时重传有关: `/proc/sys/net/ipv4/tcp_retries1` 和 `/proc/sys/net/ipv4/tcp_retries2`,前者指定在底层IP接管之前TCP最少执行的重传次数,默认值是3.后者指定连接放弃之前TCP最多可以执行的重传次数,默认值是15.

<a id="markdown-7-拥塞控制" name="7-拥塞控制"></a>
# 7. 拥塞控制

`提高网络利用率`,`降低丢包率`,并`保证网络资源对每条数据流的公平性`

`RFC 5681`详细介绍了拥塞控制的四个部分:慢启动(slow start), 拥塞避免(congestion avoidance), 快速重传(fast retransmit)和快速恢复(fast recovery)

拥塞控制算法在Linux下有多种实现,比如reno算法,vegas算法,cubic算法,`/proc/sys/net/ipv4/tcp_congestion_control`文件指示机器当前所使用的拥塞控制算法

拥塞控制的最终受控变量是发送端向网络一次连续写入的数据量,我们成为`SWND(Send Window,发送窗口)`,不过发送端最终以TCP报文段来发送数据,所以SWND限定了发送端能连续发送的TCP报文段数量,这`些TCP报文段的最大长度成为SMSS(Sender Maximum Segment Size,发送者最大端大小)`,其值一般等于MSS以太网1460?

![](http://ouxarji35.bkt.clouddn.com/snipaste_20171108_215332.png)

<a id="markdown-71-慢启动和拥塞避免" name="71-慢启动和拥塞避免"></a>
## 7.1. 慢启动和拥塞避免

TCP连接建立好以后,被设置成初始值`IW(Initial Window)`,大小为2~4个SMSS,此后发送端每收到接收端一个确认,其CWND就按照以下公式增加:
```
CWND += min(N, SMSS)
```
这样一来CWND将按照指数形式扩大(可见慢启动不慢),并最终导致网络拥塞,因此TCP拥塞控制中定义了另一个重要的状态变量:`慢启动门限(slow start threshold size,ssthresg)`,TCP拥塞控制将进入拥塞避免阶段

`RFC 5681`中提到了如下两种实现方式:

* 每个RTT事件内按照公式计算新的CWND,而不论该RTT时间内发送端接收到多少个确认
```
CWND += min(N, SMSS)
```
* 每收到一个对新数据的确认报文段,就按照公式来更新CWND
```
CWND+=SMSS*SMSS/CWND
```

如果拥塞已经发生,发送端判断拥塞发生的依据有如下两个
* 传输超时,或者说TCP重传定时器溢出,做如下调整
```
ssthresh=max(FlightSize/2, 2*SMSS)
```
* 接收到重复的确认报文段(快速重传和快速恢复)

<a id="markdown-72-快速重传和快速恢复" name="72-快速重传和快速恢复"></a>
## 7.2. 快速重传和快速恢复

发送端可能接收到重复的确认报文段,比如TCP报文段丢失,或者接收端收到乱序的TCP报文段并重排之等.拥塞控制算法需要判断当收到重复的确认报文段时,网络是否真的发生了拥塞.具体做法是:`发送端如果连续收到3个重复的确认报文段,就认为时拥塞发生了`,然后它启用快速重传和快速恢复算法来处理拥塞,过程如下:

* 1) 当收到第3个重复的确认报文段,计算ssthresh,然后立即重传丢失的报文段,并设置`CWND=ssthresh+3*SMSS`
* 2) 每次收到1个重复的确认时,设置CWND=CWND+SMSS,此时发送端可以发送新的TCP报文段
* 3) 当收到新数据的确认时,设置CWND=ssthresh

快速重传和快速恢复完成之后,拥塞控制将恢复到拥塞避免的阶段.
