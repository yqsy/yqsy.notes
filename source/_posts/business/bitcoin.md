---
title: bitcoin
date: 2018-07-09 15:45:03
categories: [business]
---


<!-- TOC -->

- [1. 问题积累](#1-问题积累)
- [2. 比特币交易速度每秒7笔怎么算出来的?](#2-比特币交易速度每秒7笔怎么算出来的)
- [3. 比特币一笔交易的占用大小是多少?](#3-比特币一笔交易的占用大小是多少)
- [4. 比特币当前的区块容量是多少?](#4-比特币当前的区块容量是多少)
- [5. 比特币当前的区块头占用空间是多少?](#5-比特币当前的区块头占用空间是多少)
- [6. 比特币当前的全量区块占用空间是多少?](#6-比特币当前的全量区块占用空间是多少)
- [7. timestamp为uint32_t 未来有什么危机?](#7-timestamp为uint32_t-未来有什么危机)
- [8. 比特币分为哪几种节点?](#8-比特币分为哪几种节点)
- [9. 比特币的问题](#9-比特币的问题)

<!-- /TOC -->


<a id="markdown-1-问题积累" name="1-问题积累"></a>
# 1. 问题积累


<a id="markdown-2-比特币交易速度每秒7笔怎么算出来的" name="2-比特币交易速度每秒7笔怎么算出来的"></a>
# 2. 比特币交易速度每秒7笔怎么算出来的?

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

<a id="markdown-3-比特币一笔交易的占用大小是多少" name="3-比特币一笔交易的占用大小是多少"></a>
# 3. 比特币一笔交易的占用大小是多少?

<a id="markdown-4-比特币当前的区块容量是多少" name="4-比特币当前的区块容量是多少"></a>
# 4. 比特币当前的区块容量是多少? 

<a id="markdown-5-比特币当前的区块头占用空间是多少" name="5-比特币当前的区块头占用空间是多少"></a>
# 5. 比特币当前的区块头占用空间是多少?

```c++
class CBlockHeader
{
    int32_t nVersion;
    uint256 hashPrevBlock;
    uint256 hashMerkleRoot;
    uint32_t  nTime;
    uint32_t nBits;
    uint32_t nNonce;
}

80字节

自从2009-01-03产生区块开始,截止2018年-05-29日 产生525000个区块.累计区块头占用空间:
525000 * 80 = 40MB

平均一年区块头占用空间:
52500 * 80 = 4MB
```

<a id="markdown-6-比特币当前的全量区块占用空间是多少" name="6-比特币当前的全量区块占用空间是多少"></a>
# 6. 比特币当前的全量区块占用空间是多少?

<a id="markdown-7-timestamp为uint32_t-未来有什么危机" name="7-timestamp为uint32_t-未来有什么危机"></a>
# 7. timestamp为uint32_t 未来有什么危机?

<a id="markdown-8-比特币分为哪几种节点" name="8-比特币分为哪几种节点"></a>
# 8. 比特币分为哪几种节点?


Reference Client (Bitcoin Core) (比特币核心客户端)
* Wallet (钱包)
* Miner (矿工)
* Full Blockchain (全量数据)
* Network Routing Node (路由网络)

---

* Full Block Chain Node (全量节点) --- 全量数据 +  路由网络
* Solo Miner (单独矿工) --- 矿工 + 全量数据 + 路由网络
* Lightweight (SPV) Wallet (轻量级钱包) --- 钱包 + 路由网络

---

* Pool Protocol Servers (协议服务器)--- 1. pool mining nodes 2. Stratum nodes
* Mining Nodes (矿池) --- 矿工 + pool mining nodes 或 矿工 + Stratum nodes
* Lightweight (SPV) Stratum wallet --- 钱包+Stratum nodes

<a id="markdown-9-比特币的问题" name="9-比特币的问题"></a>
# 9. 比特币的问题

* 算力集中化
* 私钥丢失/盗窃
* 隐私
* public key 量子攻击
* 粉尘攻击
