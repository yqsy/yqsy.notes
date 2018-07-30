---
title: bittorrent
date: 2018-06-07 18:54:33
categories: [网络相关]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. torrent实践](#2-torrent实践)
- [3. DHT(Kademlia)](#3-dhtkademlia)
    - [3.1. 路由表(节点)](#31-路由表节点)
    - [3.2. DHT表(文件信息)](#32-dht表文件信息)

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

<a id="markdown-3-dhtkademlia" name="3-dhtkademlia"></a>
# 3. DHT(Kademlia)

* https://segmentfault.com/a/1190000006254137 (路由表)
* http://www.ic.unicamp.br/~bit/ensino/mo809_1s13/papers/P2P/Kademlia-%20A%20Peer-to-Peer%20Information%20System%20Based%20on%20the%20XOR%20Metric%20.pdf (论文)
* https://blog.csdn.net/hoping/article/details/5307320 (翻译)


主要思想: 全网维护一个巨大的文件索引哈希表.

仅需要提供key,那么就能从表中查询到存储的`节点地址`返回给查询点

这个哈希表会被分割成小块,按照一定的算法和规则分布到全网各个节点上.`每个节点仅需要维护一小块哈希表`.这样节点查询文件时,只要将查询报文路由到`相应的节点即可`. ipfs使用:
* Kademlia DHT
* CoralDHT
* S/Kademlia


Kademlia DHT:

* 节点ID与`关键字`是同样的值域,都是SHA-1算法生成的`160位熵值`
* 使用`XOR异或运算`,`计算`任意两个节点的`距离`或是`节点和关键字`的`距离`
* 查询一条请求路径的时候,每个节点的信息都是完备的,只需要`log(n)量级跳转`
* 可根据`查询速度`和`存储量`的需求,调整每个节点需要维护的DHT的大小

每个节点自身维护一个路由表和一个DHT

* 路由表: 保存网络中一部分`节点`的`连接信息`
* `DHT`: 用于存放`文件信息`

<a id="markdown-31-路由表节点" name="31-路由表节点"></a>
## 3.1. 路由表(节点)

节点路由表 `K-Buket`:


最终生成的二叉树需要如下需求:
* 每个网络节点可以从根节点出发,`沿着它的最短唯一前缀到达`
* 每个网络节点都应该是`叶子节点`

节点路由表用于保存每个节点`与自己一定距离范围`内`其他节点的连接信息`,每一条路由信息由如下三部分组成
* IP Address
* UDP Port
* Node ID


KAD路由表将距离分成`160个K桶`(存放K个数据的桶),编号为i的路由表,存放着距离为`[2^i,2^(i+1)]`的k条路由信息,每个K桶内部信息存放位置是根据`上次看到的时间顺序排列`.最早的`(least-recently)`看到的放在头部,最后`(most-recently)`看到的放在尾部.因为网络中节点可能处于`在线或者离线状态`,而在之前经常在线的节点,我们需要`访问的时候也大概率在线`,那我们会优先访问它.

在bittorrent的实现中,取值为k=8,每个K-Bucket覆盖距离范围呈指数增长,那么只需要保存至多160K个路由信息就足以覆盖全部的节点范围了.对于一个有N节点的Kad网络,做多只需要经过logN步查询,就可以准确定位到目标节点.


更新:  

收到消息时,发送者y的IP地址就是被用来更新对应的k桶,具体步骤如下:
* 计算自己和发送者的ID距离: d(x,y) = x ⊕ y
* 通过距离d选择对应的k桶进行更新操作
* 如果y的IP地址已经存在于这个k桶中,则把对应项移到该k桶的尾部(Most-Recently)
* 如果y的IP地址没有记录在该k桶中
  * 如果k桶的记录项小于k个,则直接把y的(IP address,UDP port,Node ID) 信息插入队列尾部
  * 如果k桶的记录项大于k个,则选择头部的记录项z进行RPC_PING
    * 如果z没有响应,则从k桶中移除z的信息,并把y的消息插入队列尾部
    * 如果z有响应,则把z的信息移到队列尾部,同时忽略y的消息


得到最近的节点(加入查找ID值为t的节点):  
* 计算到t的距离:d(x,y) = x ⊕ y
* ...

节点加入和离开:

* 对自己的节点ID执行一次FIND_NODE操作,然后根据收到的信息更新自己的k桶内容
* ...

<a id="markdown-32-dht表文件信息" name="32-dht表文件信息"></a>
## 3.2. DHT表(文件信息)

在Kademlia每个`DHT`条目包含 `<key,value> `   ??????? 这个在源码哪里???
* key: 文件的hash值
* value: 节点ID


异或:  
如果给定了x,任意一个a(a>=0)都会唯一确定另一个节点y,满足:  
`d(x,y) = a` ,假设这里的`x是我们需要查询的文件key`,我们主需要`不断更新y`,使得y沿着d(x,y)下降的方向找下去,那么一定能收敛到`距离x最近的点`,`文件?????`总是存放在`网络编号与文件哈希`的XOR最近的几个节点上.换句话说只要`沿着XOR距离降低`的方向查找,从任意一个网络节点开始查询,我们总能找到这个存放文件的地址.而且每次更新总能筛选掉一半的节点,那么最多只需Log(n)步即可到达


