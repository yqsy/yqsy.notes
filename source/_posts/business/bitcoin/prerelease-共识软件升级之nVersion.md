---
title: 共识软件升级之nVersion
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---


<!-- TOC -->

- [1. 共识软件升级之nVersion](#1-共识软件升级之nversion)

<!-- /TOC -->


<a id="markdown-1-共识软件升级之nversion" name="1-共识软件升级之nversion"></a>
# 1. 共识软件升级之nVersion


```c++
CBlockHeader

int32_t nVersion;
uint256 hashPrevBlock;
uint256 hashMerkleRoot;
uint32_t  nTime;
uint32_t nBits;
uint32_t nNonce;
```
