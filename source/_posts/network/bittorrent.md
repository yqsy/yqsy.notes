---
title: bittorrent
date: 2018-06-07 18:54:33
categories: [网络相关]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. torrent实践](#2-torrent实践)
- [3. Kademlia](#3-kademlia)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* https://zh.wikipedia.org/wiki/BitTorrent_(%E5%8D%8F%E8%AE%AE) (wiki)
* https://www.bittorrent.com/ (官网)
* https://github.com/ipfs/go-ipfs/tree/master/exchange/bitswap (ipfs的改进)

---

* https://stackoverflow.com/questions/19749085/calculating-the-info-hash-of-a-torrent-file (如何解析infohash)
* https://github.com/transmission/transmission (命令行工具)
* https://github.com/webtorrent/parse-torrent (nodejs解析torrent文件)

---
源码:
* https://github.com/shiyanhui/dht (这个能跑,但我觉得写的很烂)
* https://github.com/fanpei91/p2pspider (也是嗅探)
* https://github.com/anacrolix/torrent (Full-featured )

2001年4余额时发布,在2001年7月2日首次正式应用


根据BitTorrent协议,文件发布者会根据要发布的文件生成通过一个.torrent文件,包含  
* Tracker信息,Tracker服务器的地址和针对Tracker服务器的设置
* 文件信息,根据对目标文件的计算生成的,结果根据`Bencode`规则进行编码,把提供下载的文件虚拟分成`大小相等的块`,块大小必须为`2k的整数次方`,并把每个块的`索引信息`和`Hash`验证码写入种子文件中.种子文件就是被下载文件的索引

下载流程:  
BT客户端首先解析种子文件得到`Tracker地址`,然后连接Tracker服务器.`Tracker服务器`回应下载者的请求,提供下载者`其他下载者的IP`.

下载者再连接其他下载者,根据种子文件,两者分别`告知`对方自己`已经有的块`,然后`交换`对方所`没有的数据`.此时不需要其他服务器参与,分散了单个线路上的数据流量,因此减少了服务器的负担

优点:  
* 一般的HTTP/FTP下载,发布文件仅在某个或某几个服务器,下载的人太多,服务器的带宽很容易不胜负荷,变得很慢.  
* 而BitTorrent协议下载的特点是，`下载的人越多`，`提供的宽带也越多`，`下载的速度就越快`．拥有完整的文件用户也越来越多，使文件的＂寿命＂不断延长．

DHT网络:  

可以在无Tracker的情况下下载

全称分布式哈希表(`Distributed Hash Table`),一种分布式存储方法.在不需要服务器的情况下,每个客户端都负责一个`小范围的路由`,并存储一小部分数据,从而实现整个DHT网络的寻址和存储.从而实现整个DHT网络的寻址和存储,使用支持该技术的BT下载软件,`用户无需连上Tracker就可以下载`,因为软件会在DHT网络中寻找下载同一个文件的其他用户并与之通讯,开始下载任务.

算法: https://zh.wikipedia.org/wiki/Kademlia 

<a id="markdown-2-torrent实践" name="2-torrent实践"></a>
# 2. torrent实践

```bash
# 安装
sudo npm install -g parse-torrent

# 查看种子文件
parse-torrent ./1.torrent

```

<a id="markdown-3-kademlia" name="3-kademlia"></a>
# 3. Kademlia

* https://segmentfault.com/a/1190000006254137 (路由表)
