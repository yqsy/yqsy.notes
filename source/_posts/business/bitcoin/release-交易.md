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
- [5. 交易数据](#5-交易数据)
- [6. 参考资料](#6-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

上一文<密钥和地址>我们讲到比特币的转账借助了`unspent transaction output (UTXO)`(未花费输出),`Secp256k1 with ECDSA`(椭圆曲线数字签名)等技术,完成了货币的支付职能.这一文我们了解其具体实现的方式-脚本语言.

比特币的脚本语言使用了基于堆栈的执行方式,也即是计算机最底层的汇编语言的执行方式.而比特币的交易验证引擎依赖于两类脚本来验证比特币的交易:

* `锁定交易` - 表示所属权身份(公钥/公钥hash),只有使用私钥进行签名才可以解锁
* `解锁交易` - 使用私钥进行签名解锁,随即可以生成新的锁定交易,将货币的所属权交给新的身份(公钥/公钥hash)


**请注意,以下示例每一次启动前都会删除所有的历史数据!**

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

script->reserveScr
ipt = CScript() << ToByteVector(pubkey) << OP_CHECKSIG;
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

注意:  

挖矿产生的奖励只在100个区块后才可以被使用
```c++
/** Coinbase transaction outputs can only be spent after this number of new blocks (network rule) */
static const int COINBASE_MATURITY = 100;
```

通过挖矿奖励获得P2PK的`锁定交易`:

```bash
bg 101

# 查锁定交易
bbasetx 1

# 查询余额
bitcoin-cli getbalance

```

对该比挖矿奖励进行`解锁交易`,引用到该笔交易的地址,并使用私钥进行签名:

```bash
PRE_TXID=`_bbasehash 1`
PRE_VOUT=0

# 获得新的地址
NEWEC=`bx seed | bx ec-new`
NEWADDRESS_INFO=`parse_privkey $NEWEC`

# 提取P2PKH地址
NEWP2PkHADDR=`echo $NEWADDRESS_INFO | sed -n 13p | awk '{print $2}'`

# 1) 创建交易
RAWTX=`bitcoin-cli createrawtransaction '''
[
    {
        "txid": "'$PRE_TXID'",
        "vout": '$PRE_VOUT'
    }
]
''' '''
{
    "'$NEWP2PkHADDR'": 49.9999
}
'''
`

# 从钱包中获得第一个区块奖励的私钥
PRE_ADDRESS=`bbasetx 1 | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["vout"][0]["scriptPubKey"]["addresses"][0])' `
PRE_PRIKEYWIF=`bitcoin-cli dumpprivkey $PRE_ADDRESS`

# 2) 签名交易
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$PRE_PRIKEYWIF'"
]
'''`

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3) 发送交易
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 4) 生成区块打包区块
bg 1

# 查询新地址信息
echo $NEWADDRESS_INFO

# 导入新地址到钱包
bitcoin-cli importaddress $NEWP2PkHADDR

# 查询新地址接受到的金额# pay to wit
bitcoin-cli getreceivedbyaddress $NEWP2PkHADDR 0

# 查询这一笔交易
bhtx 102 1
```

<a id="markdown-3-pay-to-public-key-hashp2pkh" name="3-pay-to-public-key-hashp2pkh"></a>
# 3. pay to public key hash(P2PKH)

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
OP_CHECKSIG
OP_EQUALVERIFY
<pubkeyHash>
OP_HASH160
OP_DUP

# scriptSig (in)
<pubKey>
<sig>
```

通过挖矿奖励获得P2PKH的`锁定交易`:

```bash
# 获得coinbase的地址
COINBASEEC=`bx seed | bx ec-new`
COINBASEECADDRESS_INFO=`parse_privkey $COINBASEEC`

# 提取P2PKH地址
COINBASECP2PKHADDR=`echo $COINBASEECADDRESS_INFO | sed -n 13p | awk '{print $2}'`

bitcoin-cli generatetoaddress 101 $COINBASECP2PKHADDR

# 查询锁定脚本
bbasetx 1

# 提取私钥并导入到钱包
COINBASEPRIKEYWIF=`echo $COINBASEECADDRESS_INFO | sed -n 10p | awk '{print $2}'`
bitcoin-cli importprivkey $COINBASEPRIKEYWIF

# 查询余额
bitcoin-cli getbalance
```

对该比挖矿奖励进行`解锁交易`,引用到该笔交易的地址,并使用私钥进行签名:

```bash
PRE_TXID=`_bbasehash 1`
PRE_VOUT=0

# 获得新的地址
NEWEC=`bx seed | bx ec-new`
NEWADDRESS_INFO=`parse_privkey $NEWEC`

# 提取P2PKH地址
NEWP2PkHADDR=`echo $NEWADDRESS_INFO | sed -n 13p | awk '{print $2}'`

# 1) 创建交易
RAWTX=`bitcoin-cli createrawtransaction '''
[
    {
        "txid": "'$PRE_TXID'",
        "vout": '$PRE_VOUT'
    }
]
''' '''
{
    "'$NEWP2PkHADDR'": 49.9999
}
'''`

# 2) 签名交易
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$COINBASEPRIKEYWIF'"
]
'''`

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3)发送交易
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 4) 生成打包区块
bg 1

# 查询新地址信息
echo $NEWADDRESS_INFO

# 导入新地址到钱包
bitcoin-cli importaddress $NEWP2PkHADDR

# 查询新地址接受到的金额
bitcoin-cli getreceivedbyaddress $NEWP2PkHADDR 0

# 查询这一笔交易
bhtx 102 1
```


<a id="markdown-4-pay-to-script-hash-p2sh" name="4-pay-to-script-hash-p2sh"></a>
# 4. pay to script hash (P2SH)

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev COINBASEP2SHADDRut)
OP_EQUAL
[20-byte-hash of {[pubkey] OP_CHECKSIG} ]
OP_HASH160

# scriptSig (in)
{[pubkey] OP_CHECKSIG}
[signature]
```

通过挖矿奖励获得P2SH的`锁定交易`:


```bash
# 获得coinbase的地址
COINBASEEC=`bx seed | bx ec-new`
COINBASEECADDRESS_INFO=`parse_privkey $COINBASEEC`

# 提取P2SH地址
COINBASECP2SHADDR=`echo $COINBASEECADDRESS_INFO | sed -n 15p | awk '{print $2}'`

bitcoin-cli generatetoaddress 101 $COINBASECP2SHADDR

# 查询锁定脚本
bbasetx 1

# 导入私钥到钱包
COINBASEPRIKEYWIF=`echo $COINBASEECADDRESS_INFO | sed -n 10p | awk '{print $2}'`
bitcoin-cli importprivkey $COINBASEPRIKEYWIF

# 查询余额
bitcoin-cli getbalance
```

对该比挖矿奖励进行`解锁交易`,引用到该笔交易的地址,并使用私钥进行签名:

```bash
PRE_TXID=`_bbasehash 1`
PRE_VOUT=0

# 获得新的地址
NEWEC=`bx seed | bx ec-new`
NEWADDRESS_INFO=`parse_privkey $NEWEC`

# 提取P2PKH地址
NEWP2PkHADDR=`echo $NEWADDRESS_INFO | sed -n 13p | awk '{print $2}'`

# 1) 创建交易
RAWTX=`bitcoin-cli createrawtransaction '''
[
    {
        "txid": "'$PRE_TXID'",
        "vout": '$PRE_VOUT'
    }
]
''' '''
{
    "'$NEWP2PkHADDR'": 49.9999
}
'''`

# 2) 签名交易
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$COINBASEPRIKEYWIF'"
]
'''`

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3)发送交易
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 4) 生成打包区块
bg 1

# 查询新地址信息
echo $NEWADDRESS_INFO

# 导入新地址到钱包
bitcoin-cli importaddress $NEWP2PkHADDR

# 查询新地址接受到的金额
bitcoin-cli getreceivedbyaddress $NEWP2PkHADDR 0

# 查询这一笔交易
bhtx 102 1
```

<a id="markdown-5-交易数据" name="5-交易数据"></a>
# 5. 交易数据

* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/P2PK  (P2Pk)
* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/P2PKH (P2PKH)
* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/P2SH (P2SH)

<a id="markdown-6-参考资料" name="6-参考资料"></a>
# 6. 参考资料

* https://en.bitcoin.it/wiki/Transaction (常见交易为P2PKH,P2SH)
* https://bitcoin.org/en/developer-examples (examples)
* https://en.bitcoin.it/wiki/Script (opcode)
* https://siminchen.github.io/bitcoinIDE/build/editor.html (堆栈脚本可视化)
* https://bitcoin-script-debugger.visvirial.com (常见交易种类的调试)
* https://github.com/bitcoin/bitcoin/blob/v0.17.0/doc/descriptors.md (源代码中的交易种类)
* https://bitcoincore.org/en/doc/0.17.0/ (rpc接口说明)
