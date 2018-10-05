---
title: blockchain
date: 2018-07-09 15:45:03
categories: [business]
---


<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 问题积累](#2-问题积累)
- [3. 钱包提议](#3-钱包提议)

<!-- /TOC -->

<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源


* https://bitcoin.org/en/developer-documentation (教程列表)
* https://bitcoin.org/en/developer-guide
* https://bitcoin.org/en/developer-reference
* https://bitcoin.org/en/developer-examples
* https://bitcoincore.org/en/doc/0.16.3/ (rpc接口说明)
* http://chainquery.com/bitcoin-api/getblockchaininfo (rpc接口测试网页)
* https://live.blockcypher.com/btc-testnet/decodetx/ (decode transaction)

---

钱包:
* https://bitcoin.org/en/wallets/mobile/android/bitcoinwallet/

浏览器:
* https://www.blockchain.com/zh-cn/explorer

---

* https://github.com/liuchengxu/blockchain-tutorial/blob/master/content/SUMMARY.md (很好的中文资料)
* https://www.zhihu.com/question/27687960/answer/148814714 (知乎资料索引)
* https://github.com/chaozh/awesome-blockchain-cn (所有资料)
* https://bbs.huaweicloud.com/community/usersnew/id_1518334573351109 (讲比特币的专栏)
* http://book.8btc.com/books/6/masterbitcoin2cn/_book/ (精通比特币书)
* https://en.bitcoin.it/wiki/Category:BIP (bip)

<a id="markdown-2-问题积累" name="2-问题积累"></a>
# 2. 问题积累

> 比特币的根本技术是什么?


* `POW` 工作量证明的共识达成机制是Adma在Hashcash里提出来的
* 将`全部交易计入一本总账`,并给交易打时间戳来`防范双花攻击`(double-spend attack)的思想是的 b-money 和 Nick Szabo 的 Bitgold 提出来的
* P2P技术比不上2001年出现的BitTorrent

中本聪自创的
* 区块链的设计 + UTXO `Unspent Transaction Output`


> 比特币交易速度每秒7笔怎么算出来的?

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

> 比特币一笔交易的占用大小是多少?


> 比特币当前的区块容量是多少? 


> 比特币当前的区块头占用空间是多少?


> 比特币当前的全量区块占用空间是多少?



<a id="markdown-3-钱包提议" name="3-钱包提议"></a>
# 3. 钱包提议

* `BIP32 (HD钱包)` http://bip32.org/ (以特定规则生成私钥,只需要存储少量的种子,就能推算出无数个可用的私钥)
* BIP38 (纸钱包) https://bitcoinpaperwallet.com/bip38-password-encrypted-wallets/
* `BIP39 (助记码)` https://iancoleman.io/bip39/ (用有意义的助记词代替无意义的数字)
* `BIP43 (多用途HD钱包结构)` (提出了BIP32的规范)
* `BIP44` https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki (BIP43的特殊的应用)
* BIP49 (P2WPKH-nested-in-P2SH) https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki


BIP32  
![](https://www.puzzle.ch/wp-content/uploads/2018/03/bip32-489x480.png)


BIP39  
![](https://upload-images.jianshu.io/upload_images/4973506-de36ca63e801e4cb.png)
