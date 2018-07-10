---
title: 共识算法
date: 2018-07-09 17:57:25
categories: [business]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 解决什么问题](#2-解决什么问题)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* PoW(Proof-of-Work) 比特币 
* PoS(Proof of Stake) 以太坊,权益证明机制  
* DPoS(Delegated Proof of Stake) 委托权益证明机制  
* PBFT(Practical Byzantine Fault Tolerance)  拜占庭共识算法 1999
* Paxos  希腊议会1990
* Raft, 比paxos 更容易理解


<a id="markdown-2-解决什么问题" name="2-解决什么问题"></a>
# 2. 解决什么问题

![](http://ouxarji35.bkt.clouddn.com/%E6%B7%B1%E5%BA%A6%E6%88%AA%E5%9B%BE_%E9%80%89%E6%8B%A9%E5%8C%BA%E5%9F%9F_20180709175527.png)

分布式系统广播会产生共识问题,如果有一个破坏者发布恶意信息,那么就会破坏集体共识,出现坏账,错账!

