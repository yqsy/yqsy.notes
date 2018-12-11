---
title: 交易费用
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 简单花费](#2-简单花费)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

比特币的交易采用的是UTXO(Unspent Transaction Output)技术.中文名称为未花费输出.本文做了一些交易的示范来帮助理解.

<a id="markdown-2-简单花费" name="2-简单花费"></a>
# 2. 简单花费

输出1区块的coinbase奖励(101区块生效),输出10,找零40 (102区块交易)

```bash
bg 101
bbalance
NEWADDR=`bnewaddr` && bsendaddress $NEWADDR 10.00
blistunspent 0
bg 1
blistunspent

# 查看该比交易
bhtx 102 1
```


<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

* https://bitcoin.org/en/developer-examples

