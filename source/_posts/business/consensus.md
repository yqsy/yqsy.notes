---
title: 共识算法
date: 2018-07-09 17:57:25
categories: [business]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 继续总结](#2-继续总结)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
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


paxos:
* https://lamport.azurewebsites.net/pubs/lamport-paxos.pdf (论文)

raft:
* http://thesecretlivesofdata.com/raft/ (动画)
* https://en.wikipedia.org/wiki/Raft_(computer_science)
* https://github.com/coreos/etcd (在etcd中有实现) 
* https://zhuanlan.zhihu.com/p/26506491 (简易实现raft算法)
* https://raft.github.io/raft.pdf (论文)

允许正常节点(N为总数): n >= (N/2) + 1

* 5台机器,必须3台正常. 
* 100台机器,必须51台正常

pbft:  
* https://en.wikipedia.org/wiki/Byzantine_fault_tolerance
* http://pmg.csail.mit.edu/papers/osdi99.pdf (论文)

有t个错误节点时,正常节点n必须满足: n >= 3t + 1   ==> 设 t=N-n, 得 n >= (3N+1)/4

* 5台机器,必须4台正常
* 100台机器,必须75台正常

<a id="markdown-2-继续总结" name="2-继续总结"></a>
# 2. 继续总结

![](http://on-img.com/chart_image/5b66f7c3e4b025cf4936d7e2.png)


* 私有链: 共识算法为传统`分布式系统强一致性算法`,适用环境是`不考虑`集群中存在`作恶`节点,只考虑`系统/网络故障节点`
* 联盟链: 既考虑`作恶`节点,又要考虑`故障`节点.每个`新`加入的`节点`都是需要`严格验证`和`审核`
* 公有链: 既考虑`作恶`节点,又要考虑`故障`节点.每个`新`加入的`节点`不需要严格验证和审核

