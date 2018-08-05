---
title: 共识算法
date: 2018-07-09 17:57:25
categories: [business]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 继续总结](#2-继续总结)

<!-- /TOC -->


# 1. 说明

* POW(Proof-of-Work) (比特币,莱特币,以太坊)
* POS(Proof of Stake) 权益证明机制 
* DPOS(Delegated Proof of Stake) 委托权益证明(股份授权证明机制)    EOS  (还是中心化咯?) 
* PBFT(Practical Byzantine Fault Tolerance)  拜占庭容错算法 1999
* DBFT (delegated BFT) 授权拜占庭容错 (小蚁区块链)
* Paxos  希腊议会1990
* Raft, 比paxos 更容易理解

---
* https://blog.csdn.net/lsttoy/article/details/61624287 (csdn的资料)
* https://en.wikipedia.org/wiki/Cryptocurrency (所有机制)
* https://zhuanlan.zhihu.com/p/35847127 (美图的共识算法维度整理)
* https://zhuanlan.zhihu.com/p/38627527 (美图dpos实现)

raft:
* http://thesecretlivesofdata.com/raft/

# 2. 继续总结

![](http://on-img.com/chart_image/5b66f7c3e4b025cf4936d7e2.png)


* 私有链: 共识算法为传统`分布式系统强一致性算法`,适用环境是`不考虑`集群中存在`作恶`节点,只考虑`系统/网络故障节点`
* 联盟链: 既考虑`作恶`节点,又要考虑`故障`节点.每个`新`加入的`节点`都是需要`严格验证`和`审核`
* 公有链: 既考虑`作恶`节点,又要考虑`故障`节点.每个`新`加入的`节点`不需要严格验证和审核


