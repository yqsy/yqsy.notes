---
title: 交易费用
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. pay to public key (P2PK)](#2-pay-to-public-key-p2pk)
- [3. pay to public key hash(P2PKH)](#3-pay-to-public-key-hashp2pkh)
- [4. pay to script hash (P2SH)](#4-pay-to-script-hash-p2sh)
- [5. 参考资料](#5-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

上一文<密钥和地址>我们讲到比特币的转账借助了`unspent transaction output (UTXO)`(未花费输出),`Secp256k1 with ECDSA`(椭圆曲线数字签名)等技术,完成了货币的支付职能.这一文我们了解其具体实现的方式-脚本语言.

比特币的脚本语言使用了基于堆栈的执行方式,也即是计算机最底层的汇编语言的执行方式.而比特币的交易验证引擎依赖于两类脚本来验证比特币的交易:

* `锁定交易` - 表示所属权身份(公钥/公钥hash),只有使用私钥进行签名才可以解锁
* `解锁交易` - 使用私钥进行签名解锁,随即可以生成新的锁定交易,将货币的所属权交给新的身份(公钥/公钥hash)



<a id="markdown-2-pay-to-public-key-p2pk" name="2-pay-to-public-key-p2pk"></a>
# 2. pay to public key (P2PK)

参考中本聪在2009年所创造的创世区块时的`锁定交易`
```bash
CreateGenesisBlock

CScript() << ParseHex("04678afdb0fe5548271967f1a67130b7105cd6a828e03909a67962e0ea1f61deb649f6bc3f4cef38c4f35504e51ec112de5c384df7ba0b8d578a4c702b6bf11d5f") << OP_CHECKSIG;
```

rpc指令generate出块奖励的`锁定脚本`:
```bash
generate -> CWallet::GetScriptForMining

script->reserveScript = CScript() << ToByteVector(pubkey) << OP_CHECKSIG;
```

解锁交易时的`签名`:
```bash
signrawtransactionwithkey -> SignTransaction -> ProduceSignature -> SignStep -> CreateSig -> MutableTransactionSignatureCreator::CreateSig -> CKey::Sign
```

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
OP_CHECKSIG
<pubKey>

# scriptSig (in)
<sig>
```

通过挖矿奖励获得P2PK的`锁定交易`:

注意:

挖矿产生的奖励只在100个区块后才可以被使用
```c++
/** Coinbase transaction outputs can only be spent after this number of new blocks (network rule) */
static const int COINBASE_MATURITY = 100;
```

```bash
bg 101
bbasetx 1



```

<a id="markdown-3-pay-to-public-key-hashp2pkh" name="3-pay-to-public-key-hashp2pkh"></a>
# 3. pay to public key hash(P2PKH)


<a id="markdown-4-pay-to-script-hash-p2sh" name="4-pay-to-script-hash-p2sh"></a>
# 4. pay to script hash (P2SH)



<a id="markdown-5-参考资料" name="5-参考资料"></a>
# 5. 参考资料

* https://en.bitcoin.it/wiki/Transaction (常见交易为P2PKH,P2SH)
* https://bitcoin.org/en/developer-examples (examples)
* https://en.bitcoin.it/wiki/Script (opcode)
* https://siminchen.github.io/bitcoinIDE/build/editor.html (堆栈脚本可视化)
* https://bitcoin-script-debugger.visvirial.com (常见交易种类的调试)
* https://github.com/bitcoin/bitcoin/blob/v0.17.0/doc/descriptors.md (源代码中的交易种类)
* https://bitcoincore.org/en/doc/0.17.0/ (rpc接口说明)