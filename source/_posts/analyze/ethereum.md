---
title: ethereum
date: 2018-08-12 09:09:01
categories: [项目分析]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. block/transaction](#2-blocktransaction)
- [3. merkle patricia trie](#3-merkle-patricia-trie)
- [4. pow](#4-pow)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* http://blog.51cto.com/11821908/2059711 (pow角度解析)
* https://github.com/ZtesoftCS/go-ethereum-code-analysis (源码分析!!!)
* https://github.com/ethereum/go-ethereum

```bash
go get github.com/ethereum/go-ethereum
cd /home/yq/go/src/github.com/ethereum/go-ethereum
cloc ./ --exclude-dir=tests,vendor
```


```bash
./accounts     # 以太坊账户管理
./build        # 编译脚本
./cmd         et
    ./abigen  et-> go接口
    ./bootnodeet点
    ./clef    et
    ./ethkey  et
    ./evm     et
    ./faucet  et
    ./geth    et
    ./internalet
    ./p2psim   # 模拟http api
    ./puppeth  # 新的以太坊网络的向导
    ./rlpdump  # rlp数据的格式化输出
    ./swarm    # swarm网络的接入点
    ./utils    # 公共工具
    ./wnode    # 简单的whisper节点
./common       
./consensus    # 共识算法
./console
./containers   # 各种docker filet
./contracts    # 合约 ???
./core         # 核心
./crypto       # 加密算法
./dashboard    # 看板
./eth          # 以太坊协议
./ethclient    # RPC客户端
./ethdb        # 数据库,包括levet
./ethstats     # 网络状态的报告et
./event        # 处理实时的事件
./internal
./les          # 轻量级协议子集
./light        # 提供给以太坊轻量级客户端按需检索的功能
./log
./metrics      # 磁盘计数器
./miner        # 区块创建和挖矿
./mobile       # 移动端使用的wrapper
./node         # 多种类型节点
./p2p          # p2p协议
./params
./rlp          # 序列化处理器
./rpc          # 远程方法调用
./signer
./swarm
./tests
./trie         # Merkle Patricia Tries
./vendor      
./whisper      # whisper节点的协议


```

<a id="markdown-2-blocktransaction" name="2-blocktransaction"></a>
# 2. block/transaction

* https://ethereum.stackexchange.com/questions/268/ethereum-block-architecture (框架图)


```go

// Header represents a block header in the Ethereum blockchain.
type Header struct {
    // 父区块哈希
    ParentHash  common.Hash    
    
    // 叔区块哈希
    UncleHash   common.Hash    
    
    // 矿工地址
    Coinbase    common.Address et
    
    // StateDB中state Trie根节et希值
    Root        common.Hash    et
    
    // Block中tx Trie根节点RLPet
    TxHash      common.Hash    et
    
    // Block中Receipt Trie根节点RLP哈希值
    ReceiptHash common.Hash    
    
    Bloom       Bloom  
    
    // 区块难度
    Difficulty  *big.Int       
    
    // 区块序号
    Number      *big.Int       
    
    // 区块内搜索Gas消耗的理论上限
    GasLimit    uint64
    
    // 区块内搜索Transaction执行时消耗的Gas总和
    GasUsed     uint64   
    
    // 当时时间戳
	Time        *big.Int       
	Extra       []byte         
    MixDigest   common.Hash    
    
    // 随机数num值
	Nonce       BlockNonce     
}

```

![](http://ouxarji35.bkt.clouddn.com/eOwjD.png)

<a id="markdown-3-merkle-patricia-trie" name="3-merkle-patricia-trie"></a>
# 3. merkle patricia trie


<a id="markdown-4-pow" name="4-pow"></a>
# 4. pow


> RAND(h, n) <= M / d
* RAND: 概念函数,代表一系列复杂运算
* h: 区块Header的Hash
* n: Header中的Nonce
* M: 一个极大的数 2^256-1
* d: 区块难度

`mine 函数` 挖矿


```go
// We don't have to update hash rate on every nonce, so update after after 2^X nonces
attempts++
if (attempts % (1 << 15)) == 0 {
	ethash.hashrate.Mark(attempts)
	attempts = 0
}
// Compute the PoW value of this nonce

// hashimotoFull 就是 RAND(h, n)
digest, result := hashimotoFull(dataset.dataset, hash, nonce)

// 如果结果满足RAND(h, n) <= M / d
if new(big.Int).SetBytes(result).Cmp(target) <= 0 {
	// Correct nonce found, create a new header with it
	header = types.CopyHeader(header)
	header.Nonce = types.EncodeNonce(nonce)
	header.MixDigest = common.BytesToHash(digest)
	// Seal and return a block (if still needed)
	select {
	case found <- block.WithSeal(header):
		logger.Trace("Ethash nonce found and reported", "attempts", nonce-seed, "nonce", nonce)
	case <-abort:
		logger.Trace("Ethash nonce found but discarded", "attempts", nonce-seed, "nonce", nonce)
	}
	break search
}
```

重新计算难度:
* calcDifficultyByzantium
* `calcDifficultyHomestead`
* calcDifficultyFrontier

