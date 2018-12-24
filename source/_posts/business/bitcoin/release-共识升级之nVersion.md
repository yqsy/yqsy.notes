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
- [3. 参考资料](#3-参考资料)

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
version: 2 num: 140752 firstHeight:  189565 lastHeight:  363689
version: 3 num:  29304 firstHeight:  341942 lastHeight:  388319
version: 4 num:  27212 firstHeight:  381993 lastHeight:  471390
```

根据代码得知不同的版本对应着不同的BIP协议:

```bash
UniValue SoftForkMajorityDesc
```

* version 1: 原始的区块版本
* version 2: BIP34
* version 3: BIP66
* version 4: BIP65


<a id="markdown-21-bip34" name="21-bip34"></a>
## 2.1. BIP34


`升级的目的,关键代码:`

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

`升级的目的,关键代码:`

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

分析以上代码得知,在达到BIP66的版本的高度的时候,会检查签名是否符合DER编码的规则.


<a id="markdown-23-bip65" name="23-bip65"></a>
## 2.3. BIP65

`升级的目的,关键代码:`

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

分析以上代码得知,在达到BIP65版本的高度的时候,使得`SCRIPT_VERIFY_CHECKLOCKTIMEVERIFY`生效.



<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

* https://github.com/bitcoin/bips/blob/master/bip-0034.mediawiki (BIP34)
* https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki (BIP66)
* https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki (BIP65)
