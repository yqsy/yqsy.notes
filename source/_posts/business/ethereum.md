---
title: ethereum
date: 2018-07-12 14:29:58
categories: [business]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 缺陷](#2-缺陷)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* https://github.com/ZtesoftCS/go-ethereum-code-analysis (源码分析!!!)
* https://www.ethereum.org/greeter (开发入门)
* https://ethereum.org/cli (安装cli)
* http://ethdocs.org/en/latest/contracts-and-transactions/contracts.html (什么是合约)
* https://solidity.readthedocs.io/en/latest/ (所用语言,类似js)
* https://www.cnblogs.com/tinyxiong/p/7878468.html (什么是智能合约?)
* https://github.com/ethereum/wiki/wiki/White-Paper (以太坊白皮书)
* https://github.com/ethereum/dapp-bin (示例)
* https://blog.csdn.net/huangshulang1234/article/details/79374085 (讲的蛮清楚)
* https://ethfans.org/posts/a-gentle-introduction-to-ethereum (基础介绍)

```
# 拉代码
go get -u github.com/ethereum/go-ethereum

cloc ./ --exclude-dir=tests,vendor
```

<a id="markdown-2-缺陷" name="2-缺陷"></a>
# 2. 缺陷

* http://baijiahao.baidu.com/s?id=1596196077071413605&wfr=spider&for=pc


---

* 以太坊网络的效率低容易造成网络堵塞,容易受到DDOS的攻击致使主网瘫痪
* 暂时采用POW,造成了大量的网络资源浪费
* 真实世界的数据上链的难度较大,且数据上链的成本较高

以太坊创始人v神也意识到了这些问题,已经提出了使用
* 分片（Sharding)
* 侧链(Plasma)
* 雷电网络(Radien Network)

