---
title: 共识软件升级之nVersion
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 早期版本升级](#2-早期版本升级)
    - [2.1. BIP34](#21-bip34)
    - [2.2. BIP66](#22-bip66)
    - [2.3. BIP65](#23-bip65)
    - [2.4. 总结](#24-总结)
- [3. 新升级方式BIP-9](#3-新升级方式bip-9)
    - [3.1. BIP68 112 113](#31-bip68-112-113)
    - [3.2. BIP141 143 147](#32-bip141-143-147)
- [4. 总结](#4-总结)
- [5. 参考资料](#5-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```c++
CBlockHeader

int32_t nVersion;
uint256 hashPrevBlock;
uint256 hashMerkleRoot;
uint32_t  nTime;
uint32_t nBits;
uint32_t nNonce;
```

<a id="markdown-2-早期版本升级" name="2-早期版本升级"></a>
# 2. 早期版本升级

通过之前的<区块的存储>文章介绍的知识,下载一份比特币的全量数据,编写脚本来得知区块版本的迁移,数据如下:

```bash
version: 1 num: 215047 firstHeight:       0 lastHeight:  227835 
version: 2 num: 140752 firstHeight:  189565 lastHeight:  363689 (BIP34) 生效高度: 227931
version: 3 num:  29304 firstHeight:  341942 lastHeight:  388319 (BIP66) 生效高度: 363725
version: 4 num:  27212 firstHeight:  381993 lastHeight:  471390 (BIP65) 生效高度: 388381
```

根据代码得知不同的版本对应着不同的BIP协议:

```bash
UniValue SoftForkMajorityDesc
```

* version 1: 原始的区块版本
* version 2: BIP34
* version 3: BIP66
* version 4: BIP65


![](./pic/bip34.png)



<a id="markdown-21-bip34" name="21-bip34"></a>
## 2.1. BIP34


升级的目的,关键代码:

```c++
// ContextualCheckBlock <- CChainState::AcceptBlock <- ProcessNewBlock <- ProcessMessage(3 usages)

if (nHeight >= consensusParams.BIP34Height)
{
    CScript expect = CScript() << nHeight;
    if (block.vtx[0]->vin[0].scriptSig.size() < expect.size() ||
        !std::equal(expect.begin(), expect.end(), block.vtx[0]->vin[0].scriptSig.begin())) {
        return state.DoS(100, false, REJECT_INVALID, "bad-cb-height", false, "block height mismatch in coinbase");
    }
}
```

分析以上代码得知,在当达到BIP34的版本的高度的时候,会强制检查区块的高度,`在coinbase的见证脚本中必须有高度的信息.`


`升级的过程,概述`:

* 75%规则: 如果最后1000个区块的750个是版本2或更高,则`A.版本2在coinbase中必须包含块高度`, `B.版本1仍被网络接受`. 此时新旧版本规则共存
* 95%规则: 如果最后1000个区块的950个是版本2或更高,则 `版本1不再视为有效`



<a id="markdown-22-bip66" name="22-bip66"></a>
## 2.2. BIP66

升级的目的,关键代码:

```bash
# GetBlockScriptFlags <- CChainState::ConnectBlock <- CChainState::ConnectTip <- CChainState::ActivateBestChainStep <- CChainState::ActivateBestChain <- ProcessNewBlock <- ProcessMessage(3 usages)

# 给区块的flag置上检查位
if (pindex->nHeight >= consensusparams.BIP66Height) {
    flags |= SCRIPT_VERIFY_DERSIG;
}

# CheckSignatureEncoding <- EvalScript(2 usages) <- VerifyScript(3 usages)
# 检查签名的格式,符合DER编码
if ((flags & (SCRIPT_VERIFY_DERSIG | SCRIPT_VERIFY_LOW_S | SCRIPT_VERIFY_STRICTENC)) != 0 && !IsValidSignatureEncoding(vchSig)) {
    return set_error(serror, SCRIPT_ERR_SIG_DER);
```

BIP66沿用BIP34的升级规则.

分析以上代码得知,在达到BIP66的版本的高度的时候,会检查签名是否符合DER编码的规则.


<a id="markdown-23-bip65" name="23-bip65"></a>
## 2.3. BIP65

升级的目的,关键代码:

```bash
# GetBlockScriptFlags <- CChainState::ConnectBlock <- CChainState::ConnectTip <- CChainState::ActivateBestChainStep <- CChainState::ActivateBestChain <- ProcessNewBlock <- ProcessMessage(3 usages)

# 给区块的flag置上检查位
if (pindex->nHeight >= consensusparams.BIP65Height) {
    flags |= SCRIPT_VERIFY_CHECKLOCKTIMEVERIFY;
}

# EvalScript <- VerifyScript(3 usages)
# 开启OP_CHECKLOCKTIMEVERIFY
case OP_CHECKLOCKTIMEVERIFY:
{
    if (!(flags & SCRIPT_VERIFY_CHECKLOCKTIMEVERIFY)) {
        // not enabled; treat as a NOP2
        break;
    }
```

BIP65沿用BIP34的升级规则.

分析以上代码得知,在达到BIP65版本的高度的时候,使得`SCRIPT_VERIFY_CHECKLOCKTIMEVERIFY`生效,支持`OP_CHECKLOCKTIMEVERIFY`指令. 简称`CLTV`.

<a id="markdown-24-总结" name="24-总结"></a>
## 2.4. 总结

区块链的本意是`尊重用户的利益`.因为共识软件的升级可能会损失部分用户的利益,所以当部分用户认为升级的利益的损失或升级带来的风险不能在接受范围之内时,用户可以选择不升级.

BIP34,66,65的升级方式可以概括为3个阶段:

* 阶段一: 同意比例达到[0,0.75)阶段. `"混乱"阶段"`,版本共存,并且新版本号码产生的区块可能不符合新版本的规则.
* 阶段二: 同意比例达到[0.75,0.95)阶段. `"共存阶段"`,版本共存,并且新版本号码产生的区块必须符合新版本的规则.
* 阶段三: 同意比例达到[0.95,1]阶段. `"升级完成阶段"`,必须是新版本,且符合新版本的规则.

`思考一个孤块的问题:`

![](./pic/bip34-2.png)

当处于阶段三时,部分矿工由于没有及时升级到新版本,或者不愿意升级到新版本(参考BIP65升级过程),此时会产生孤块的情况.

由于比特币网络的共识规则是"最长链优先",故孤块并不是什么问题: 因为产生孤块的矿工竞争不过最长链,所以会对已经产生的区块(为了得到奖励花费大量电力)视为沉默成本,并参与到最长链的挖掘中去.

`思考一个向前兼容 & 向后兼容的问题:`

向前兼容:  
* A. 增加限制 (coinbase见证放高度 / 签名符合DER编码) - 前面的版本可以兼容后面的版本产生的数据
* B. 拓展功能 (支持新的操作符) - 前面的版本可以兼容后面的版本产生的数据

如果在阶段一或二中,版本处于`混乱/共存阶段`,当发送一笔拥有新版本才支持的操作符的交易时,会产生混乱(发送给旧版本的节点交易 和 发送给新版本的节点交易时会发生不一致的情况).作为用户在这个过程中尽量不去使用新的扩展功能,毕竟没有像互联网中心化那样可以切换流量,隔离升级.以免造成功能时灵时不灵的问题.

---
向后兼容:  

新版本中做调整后可以是`向后兼容`的,在判断多少区块高度之前数据不支持某种功能(coinbase见证放高度 / 签名符合DER编码 / 支持新的操作符) 

`思考BIP34升级方式的问题:`

* 一次只能升级一个版本或者多个版本打包在一起升级(更高的版本号).
* 不能在时间的维度做升级的规划,不能永久的拒绝某个升级.
* nVersion为有符号数,负数不能被利用 (代码中以 >= 2来判断).


<a id="markdown-3-新升级方式bip-9" name="3-新升级方式bip-9"></a>
# 3. 新升级方式BIP-9

旧式升级方式在升级了3个版本(nVersion=2,3,4)之后就被BIP-9替换了. 传统的升级方式的特点是生成区块的区块头部的`nVersion`代表了该区块的所处版本.但是在BIP-9中,我们在区块链浏览器中观察最新出的区块很有可能是`0x20000000`,`0x20000000`的含义是BIP-9的初始值,不包含任何`已有`的版本的信息,这和以往的认知观念不同.BIP-9方式下的当前区块版本是由历史区块数据进行遍历决定的 --- 在某一个时间范围内,以2016区块(两周)作为跨度,并用状态机的方式遍历每一个区间来切换状态,当赞成比例到达95%时就视为升级成功.

如果没有发出软分叉时,矿工将版本字段设置为`0x20000000`,二进制如下:  
```bash
00100000000000000000000000000000
```

顶部的`001`表示支持两个不同机制的未来升级方式`(010,011)`. 最顶部的`0`表示符号位,因为nVersion被解释为有符号数.实际的版本升级字段一共有29bit,代表29个功能. 使用集合表示为 {0,...,28}.


`再次通过脚本来得知区块版本的迁移,数据如下:`

```bash
version:     20000000 num:   113998 firstHeight:   407021 lastHeight:   553026  (预设值)
version:     20000001 num:     4976 firstHeight:   411264 lastHeight:   455393  (CSV)
version:     20000002 num:    15833 firstHeight:   438914 lastHeight:   530699  (SEGWIT)
```

相关代码:

```c++
// BlockAssembler::CreateNewBlock <- generateBlocks <- generate

// 计算下一个区块的nVersion
pblock->nVersion = ComputeBlockVersion(pindexPrev, chainparams.GetConsensus());

// 判断CSV特性是否开启
VersionBitsState(pindex->pprev, chainparams.GetConsensus(), Consensus::DEPLOYMENT_CSV, versionbitscache) == ThresholdState::ACTIVE

// 判断隔离见证特性是否开启
VersionBitsState(pindexPrev, params, Consensus::DEPLOYMENT_SEGWIT, versionbitscache) == ThresholdState::ACTIVE

// CMainParams 初始化函数 (省略部分)
[Consensus::DEPLOYMENT_TESTDUMMY].bit = 28;
[Consensus::DEPLOYMENT_TESTDUMMY].nStartTime = 1199145601; // January 1, 2008
[Consensus::DEPLOYMENT_TESTDUMMY].nTimeout = 1230767999; // December 31, 2008

// Deployment of BIP68, BIP112, and BIP113.
[Consensus::DEPLOYMENT_CSV].bit = 0;
[Consensus::DEPLOYMENT_CSV].nStartTime = 1462060800; // May 1st, 2016
[Consensus::DEPLOYMENT_CSV].nTimeout = 1493596800; // May 1st, 2017

// Deployment of SegWit (BIP141, BIP143, and BIP147)
[Consensus::DEPLOYMENT_SEGWIT].bit = 1;
[Consensus::DEPLOYMENT_SEGWIT].nStartTime = 1479168000; // November 15th, 2016.
[Consensus::DEPLOYMENT_SEGWIT].nTimeout = 1510704000; // November 15th, 2017.
```

状态的变化方式:

* DEFINED -> STARTED (开始时间到) -> LOCKED_IN (同意超过1916块) -> ACTIVE (激活)
* DEFINED -> FAILED (失败,没有开始)
* DEFINED -> STARTED (开始时间到) -> FAILED (失败,有开始)

![](https://raw.githubusercontent.com/bitcoin/bips/master/bip-0009/states.png)

源码细节以图的方式展示:  

![](./pic/bip9_extra.png)


<a id="markdown-31-bip68-112-113" name="31-bip68-112-113"></a>
## 3.1. BIP68 112 113

升级的目的 & 关键代码:

* CTxIn 中nSequence的支持 (相对时间锁)
* CHECKSEQUENCEVERIFY 指令支持
* GetMedianTimePast 时间使用中位数

BIP68:  

```bash
# CChainState::ConnectBlock
if (VersionBitsState(pindex->pprev, chainparams.GetConsensus(), Consensus::DEPLOYMENT_CSV, versionbitscache) == ThresholdState::ACTIVE) {
    nLockTimeFlags |= LOCKTIME_VERIFY_SEQUENCE;
}

# CalculateSequenceLocks 
# 支持 CTxIn 中的 nSequence
```

BIP112:  

```bash
# ContextualCheckBlock
if (VersionBitsState(pindex->pprev, consensusparams, Consensus::DEPLOYMENT_CSV, versionbitscache) == ThresholdState::ACTIVE) {
    flags |= SCRIPT_VERIFY_CHECKSEQUENCEVERIFY;
}

# EvalScript <- VerifyScript(3 usages)
# 开启OP_CHECKSEQUENCEVERIFY
if (!(flags & SCRIPT_VERIFY_CHECKSEQUENCEVERIFY)) {
    // not enabled; treat as a NOP3
    break;
}
```

BIP113:  

```bash
# GetBlockScriptFlags
if (VersionBitsState(pindexPrev, consensusParams, Consensus::DEPLOYMENT_CSV, versionbitscache) == ThresholdState::ACTIVE) {
    nLockTimeFlags |= LOCKTIME_MEDIAN_TIME_PAST;
}

# CheckFinalTx / ContextualCheckBlock / CreateNewBlock
# 把原始取时间的方式换成区过去11个区块的中位数
```

<a id="markdown-32-bip141-143-147" name="32-bip141-143-147"></a>
## 3.2. BIP141 143 147


升级的目的 & 关键代码:

* 隔离见证的支持 
* 新事务摘要算法
* 修复OP_CHECKMULTISIG,OP_CHECKMULTISIGVERIFY


BIP141:

```bash

```

BIP143:

```bash

```

BIP147:

```bash

```


<a id="markdown-4-总结" name="4-总结"></a>
# 4. 总结



<a id="markdown-5-参考资料" name="5-参考资料"></a>
# 5. 参考资料

* https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki (BIP34)
* https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki (BIP66)
* https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki (BIP65)
* https://en.bitcoin.it/wiki/Softfork (软分叉 & BIP65升级过程中的问题)
* https://www.zhihu.com/question/47239021?sort=created (前向兼容 & 后向兼容)

---

* https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki (BIP9)
* https://bitcoincore.org/en/2016/06/08/version-bits-miners-faq/#when-should-miners-set-bits (BI9-官方文档)
* https://github.com/bitcoin/bips/blob/master/bip-0068.mediawiki (BIP68)
* https://github.com/bitcoin/bips/blob/master/bip-0112.mediawiki (BIP112)
* https://github.com/bitcoin/bips/blob/master/bip-0113.mediawiki (BIP113)
* https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki (BIP141)
* https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki (BIP143)
* https://github.com/bitcoin/bips/blob/master/bip-0147.mediawiki (BIP147)
