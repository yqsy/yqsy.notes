---
title: blockchain
date: 2018-07-09 15:45:03
categories: [business]
---


<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 比特币私钥,公钥,钱包维度梳理](#2-比特币私钥公钥钱包维度梳理)
- [3. 交易速度的限制主要是什么?每秒7笔怎么算的](#3-交易速度的限制主要是什么每秒7笔怎么算的)
- [4. 比特币的根本技术](#4-比特币的根本技术)
- [5. 为什么比特币地址要用公钥哈希而不直接使用公钥?](#5-为什么比特币地址要用公钥哈希而不直接使用公钥)

<!-- /TOC -->

<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源
* https://www.blockchain.com/zh-cn/explorer (比特币区块链浏览器)

---

* https://github.com/liuchengxu/blockchain-tutorial/blob/master/content/SUMMARY.md (很好的中文资料)
* https://www.zhihu.com/question/27687960/answer/148814714 (知乎资料索引)
* https://github.com/chaozh/awesome-blockchain-cn (所有资料)
* https://bbs.huaweicloud.com/community/usersnew/id_1518334573351109 (讲比特币的专栏)
* http://book.8btc.com/books/6/masterbitcoin2cn/_book/ (精通比特币书)

<a id="markdown-2-比特币私钥公钥钱包维度梳理" name="2-比特币私钥公钥钱包维度梳理"></a>
# 2. 比特币私钥,公钥,钱包维度梳理

* https://blog.csdn.net/jeason29/article/details/51576659 

![](http://ouxarji35.bkt.clouddn.com/1-14112FU345.png)


1. 生成256bits的随机数作为`私钥`
2. 经过SECP256K1椭圆曲线算法生成`公钥`
3. 通过RIPEMD160 HASHj计算得到`公钥hash`
4. 版本号放到`公钥hash`头部,对其进行`两次SHA256`运算将结果的前4字节作为校验值连接在尾部
5. 将上一步结果使用BASE58进行编码,就得到了`钱包地址`


公钥 私钥 钱包地址相互的关系?

![](http://ouxarji35.bkt.clouddn.com/1-14112FU348.png)


交易过程?

使用 `私钥` 对交易进行签名

![](http://ouxarji35.bkt.clouddn.com/1-14112FU350.png)

1. 交易原始数据包括`转账数额`和`转入钱包地址`,用私钥对原始数据进行签名
2. 生成转出钱包`公钥`?不是本来就有公钥了吗?
3. 将`公钥`和`签名`添加到原始交易数据中,生成了正式的交易数据,这样就可以广播到比特币网络进行转账了


使用 `公钥`  对签名进行认证

![](http://ouxarji35.bkt.clouddn.com/1-14112FU342.png)



<a id="markdown-3-交易速度的限制主要是什么每秒7笔怎么算的" name="3-交易速度的限制主要是什么每秒7笔怎么算的"></a>
# 3. 交易速度的限制主要是什么?每秒7笔怎么算的

* https://www.zhihu.com/question/41004649
* https://www.zhihu.com/question/41004649/answer/145731141

---
* 定义每一个区块的一个账册的大小是1MiB
* 每10分钟产生一个这样的区块
* 每个最基本的比特交易的大小是250B

```
1MiB = 1024 * 1024 B = 1048576 B

1048576 / 250 = 4194 (个)  -- 一个区块可有4194个比特币的转账记录

4194 / 600 ≈ 7 (个/s) -- 大约7秒钟能交易一个比特币
```

<a id="markdown-4-比特币的根本技术" name="4-比特币的根本技术"></a>
# 4. 比特币的根本技术


* `POW` 工作量证明的共识达成机制是Adma在Hashcash里提出来的
* 将`全部交易计入一本总账`,并给交易打时间戳来`防范双花攻击`(double-spend attack)的思想是的 b-money 和 Nick Szabo 的 Bitgold 提出来的
* P2P技术比不上2001年出现的BitTorrent

中本聪自创的
* 区块链的设计 + UTXO `Unspent Transaction Output`


<a id="markdown-5-为什么比特币地址要用公钥哈希而不直接使用公钥" name="5-为什么比特币地址要用公钥哈希而不直接使用公钥"></a>
# 5. 为什么比特币地址要用公钥哈希而不直接使用公钥?

* https://zhuanlan.zhihu.com/p/28196364
