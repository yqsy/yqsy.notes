---
title: datastructure
date: 2018-08-01 11:24:52
categories: [business]
---

<!-- TOC -->

- [1. Merkle树](#1-merkle树)
- [2. Trie树](#2-trie树)
- [3. Merkle Patricia树](#3-merkle-patricia树)

<!-- /TOC -->

<a id="markdown-1-merkle树" name="1-merkle树"></a>
# 1. Merkle树


是二叉树,也可以是多叉树,
* 一组叶节点
* 一组中间节点
* 一个根节点

最下面的节点包含基础数据,每个中间节点是它的子节点的散列,根节点是它的子节点的散列

目的是: 允许区块的数据`可以零散地发送`,节点可以从一个节点下载区块头,从另外的源下载与其他相关的树的其他部分,`而依然能够确认所有的数据都是正确的`. 对交易记录进行篡改,对应的叶节点散列值也会改变,导致其Merkle树根值变化


<a id="markdown-2-trie树" name="2-trie树"></a>
# 2. Trie树

如果有两个value,它们有着基于相同前缀的key,它们的`相同前缀的长度占自身比例越大`,则代表着这两个value在树中的位置`越靠近`

<a id="markdown-3-merkle-patricia树" name="3-merkle-patricia树"></a>
# 3. Merkle Patricia树

在levelDB数据库中的表现形式为: key代表着节点的`RLP编码的SHA3散列值`,value是节点的`RLP编码`


