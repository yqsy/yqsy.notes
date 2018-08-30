---
title: bitcoin
date: 2018-08-09 11:51:23
categories: [项目分析]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. block/transaction](#2-blocktransaction)
- [3. merkle tree spv轻量钱包验证](#3-merkle-tree-spv轻量钱包验证)
- [4. pow](#4-pow)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* https://github.com/bitpay/copay (轻量实现)
* https://github.com/btcsuite/btcd (go实现)
* https://github.com/btcsuite/btcd/blob/master/docs/README.md (go实现文档)
* https://github.com/bitcoin/bitcoin (c++实现)

---
* https://bitcoin.org/bitcoin.pdf (比特币论文)
* https://wenku.baidu.com/view/c62c067cb307e87101f69642.html (翻译)



<a id="markdown-2-blocktransaction" name="2-blocktransaction"></a>
# 2. block/transaction

```c++
// 区块头,80字节
class CBlockHeader
{
    // 版本号
    int32_t nVersion;
    
    // 上一个区块的hash值
    uint256 hashPrevBlock;

    // merkle tree 的根值
    uint256 hashMerkleRoot;
    
    // 当前时间戳
    uint32_t nTime;

    // 当前挖矿的难度,越小,难度越大
    uint32_t nBits;

    // 随机数
    uint32_t nNonce;
}


class CBlock : public CBlockHeader
{
    // 交易列表
    std::vector<CTransactionRef> vtx;

    // 不知道
    mutable bool fChecked;
}

class CTransaction
{
    const std::vector<CTxIn> vin;
    
    const std::vector<CTxOut> vout;
}

class CTxIn
{
    COutPoint prevout; // 包含1.前一笔交易的哈希 2.下标
    CScript scriptSig;
    uint32_t nSequence; 
}

class CTxOut
{
    CAmount nValue;
    CScript scriptPubKey;
}

```

![](http://ouxarji35.bkt.clouddn.com/ukuq0.png)

![](http://ouxarji35.bkt.clouddn.com/transactions-diagram.png)

<a id="markdown-3-merkle-tree-spv轻量钱包验证" name="3-merkle-tree-spv轻量钱包验证"></a>
# 3. merkle tree spv轻量钱包验证

![](http://ouxarji35.bkt.clouddn.com/2Ep7y.png)

比特币验证分为:

* 支付验证: 非常复杂 1. 余额是否可供支出 2. 是否存在双花 3. 脚本是否能通过
* 交易验证: 只判断支付的交易是否已经被验证过

验证一笔交易时只需要验证:

* 交易hash
* 树根hash
* merkle path(我理解为关键branch的hash)


相关资料:

* https://en.wikipedia.org/wiki/Merkle_tree (wiki)
* https://media.consensys.net/ever-wonder-how-merkle-trees-work-c2f8b7100ed3 (香蕉演示)
* https://github.com/richpl/merkletree (java-验证特性呢?)
* https://github.com/c-geek/merkle (js-验证特性呢?)


问题, merkle path在验证时怎么得到?

* https://bitcoin.stackexchange.com/questions/50674/why-is-the-full-merkle-path-needed-to-verify-a-transaction/50680(提问)

>> In order to verify that a transaction is included in a block, without having to download all the transactions in the block, they use an authentication path, or a merkle path. 

参考
* https://bitcoin.org/en/developer-reference#merkleblock

>>搜索　MSG_MERKLEBLOCK　

<a id="markdown-4-pow" name="4-pow"></a>
# 4. pow

`generateBlocks 函数` 挖矿


```c++
// 不断变更nNonce来做hash
// 如果小于当前难度值,算完成
while (nMaxTries > 0 && pblock->nNonce < nInnerLoopCount && !CheckProofOfWork(pblock->GetHash(), pblock->nBits, Params().GetConsensus())) {
    ++pblock->nNonce;
    --nMaxTries;
}
        
```

`CalculateNextWorkRequired 函数` 重新计算难度

`CreateNewBlock 函数` 铸币,第一笔交易为奖励矿工获得奖励和手续费的特殊交易
