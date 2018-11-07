---
title: ethereum
date: 2018-08-12 09:09:01
categories: [项目分析]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. block/transaction](#2-blocktransaction)

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
