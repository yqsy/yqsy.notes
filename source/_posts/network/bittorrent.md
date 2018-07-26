---
title: bittorrent
date: 2018-06-07 18:54:33
categories: [网络相关]
---


<!-- TOC -->


<!-- /TOC -->


* https://zh.wikipedia.org/wiki/BitTorrent_(%E5%8D%8F%E8%AE%AE) (wiki)
* https://www.bittorrent.com/ (官网)
* https://github.com/ipfs/go-ipfs/tree/master/exchange/bitswap

2001年4余额时发布,在2001年7月2日首次正式应用


根据BitTorrent协议,文件发布者会根据要发布的文件生成通过一个.torrent文件,包含
* Tracker信息,Tracker服务器的地址和针对Tracker服务器的设置
* 文件信息,根据对目标文件的计算生成的,结果根据`Bencode`规则进行编码,把提供下载的文件虚拟分成`大小相等的块`,块大小必须为`2k的整数次方`,并把每个块的`索引信息`和`Hash`验证码写入种子文件中.种子文件就是被下载文件的索引

下载流程:
BT客户端首先解析种子文件得到`Tracker地址`,然后连接Tracker服务器.`Tracker服务器`回应下载者的请求,提供下载者`其他下载者的IP`.

下载者再连接其他下载者,根据种子文件,两者分别`告知`对方自己`已经有的块`,然后`交换`对方所`没有的数据`.

