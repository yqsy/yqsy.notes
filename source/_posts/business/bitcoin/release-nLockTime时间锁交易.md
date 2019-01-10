---
title: nLockTime时间锁交易
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. nLockTime](#2-nlocktime)
- [3. CheckLockTimeVerify常用场景](#3-checklocktimeverify常用场景)
- [4. 场景四 冻结资金实践](#4-场景四-冻结资金实践)
- [5. 场景二 双因素钱包实践 (单向支付通道)](#5-场景二-双因素钱包实践-单向支付通道)
- [6. 交易数据](#6-交易数据)
- [7. 参考资料](#7-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```c++
class CTransaction    
int32_t nVersion;
std::vector<CTxIn> vin;
std::vector<CTxOut> vout;
uint32_t nLockTime;
```

设想一种功能: 锁定某一笔钱直到若干年后才能被消费. 这样的功能在传统中心化软件中无法真正做到,因为中心化系统的规则并不是真正的规则.在区块链软件中,规则一旦制定,随着时间的推移其修改的成本会变的越来越高.这里做一下时间锁相关的交易,并跟踪到相关代码来分析.

<a id="markdown-2-nlocktime" name="2-nlocktime"></a>
# 2. nLockTime 

代码:
```bash
# nLockTime在500000000 以内表示高度. 

# 1. nLockTime 为零时 可上链
# 2. nLockTime 已成为过去式 可上链
# 3. nLockTime 是未来式, 且所有的见证数据的nSequence 为0xffffffff  可上链 (所有的in的nSequence为0xffffffff(表示禁用nLockTime))

IsFinalTx <- ContextualCheckBlock

class CTransaction
const uint32_t nLockTime;
```

通过挖矿奖励得资金源:

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

创建带有nLockTime的`锁定交易`:

```bash
PRE_TXID=`_bbasehash 1`
PRE_VOUT=0

# 获得新的地址
NEWEC=`bx seed | bx ec-new`
NEWADDRESS_INFO=`parse_privkey $NEWEC`

# 提取P2PKH地址
NEWP2PkHADDR=`echo $NEWADDRESS_INFO | sed -n 13p | awk '{print $2}'`
send_payment
# 1) 创建交易 (到达2000高度send_payment后可被打包)
RAWTX=`bitcoin-cli createrasend_paymentwtransaction '''
[send_payment
    {send_payment
        "txid": "'$PRE_TXIDsend_payment'",
        "vout": '$PRE_VOUT'
    }
]
''' '''
{
    "'$NEWP2PkHADDR'": 49.9999
}
''' 2000`

# 2) 签名交易
SIGNED_RAWTX_JSON=`bitcoin-cli signrawtransactionwithkey $RAWTX '''
[
    "'$COINBASEPRIKEYWIF'"
]
'''`

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3)发送交易 (无法被打包, 无法被放入到交易池中)
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

bg 1899

# 2000个区块后可被打包
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

# 查询交易
bhtx 2001 1
```

<a id="markdown-3-checklocktimeverify常用场景" name="3-checklocktimeverify常用场景"></a>
# 3. CheckLockTimeVerify常用场景

(BIP65, CLTV)

场景一: 第三方托管(Escrow), Alice 和 Bob联合经营业务`(钱在两个人意见一致时才能使用)`,将所有资金锁定在2-of-2的多重交易输出中(必须得到2个人中的2个签名才可以解锁).为了避免其中一个人发生意外问题无法签名,所以任命Lenny作为第三方. Lenny 和任意Alice或Bob其中一人都可解锁交易,`为了避免Alice和Bob在经营业务时间中合谋,`所以用上了时间锁技术,在指定时间(3个月后)律师才可以和其中一人完成签名解锁交易.
```bash
IF
    <now + 3 months> CHECKLOCKTIMEVERIFY DROP
    <Lenny's pubkey> CHECKSIGVERIFY
    1
ELSE
    2
ENDIF
<Alice's pubkey> <Bob's pubkey> 2 CHECKMULTISIG
```

场景二: 双因素钱包 (GreenAddress). 一个密钥用户控制,一个密钥服务控制.在任何情况下,服务商和用户联合签名可以解密,用时间锁技术超过一定时间后用户可自行取钱.`(服务商使用钱必须征得用户的签名同意并且用户在指定时间后可退款)`

```bash
IF
    <service pubkey> CHECKSIGVERIFY
ELSE
    <expiry time> CHECKLOCKTIMEVERIFY DROP
ENDIF
<user pubkey> CHECKSIG
```

场景三: 数据的无信任付款(Trustless Payments for Publishing Data) 数据的买方购买数据`(比如一个珍贵的资料,买家只知道hash,不知道具体的数据)`,可以向指定脚本打币,当发布者出示了数据后可提走钱. 假设发布者迟迟不出示数据,使用时间锁技术使买方可以在指定时间后得到退款.

```bash
IF
    HASH160 <Hash160(encryption key)> EQUALVERIFY
    <publisher pubkey> CHECKSIG
ELSE
    <expiry time> CHECKLOCKTIMEVERIFY DROP
    <buyer pubkey> CHECKSIG
ENDIF
```

场景四: 冻结资金. `没有人能在提供的时间到来之前花费锁定的输出`

```bash
<expiry time> CHECKLOCKTIMEVERIFY DROP DUP HASH160 <pubKeyHash> EQUALVERIFY CHECKSIG
```


代码:
```bash
# EvalScript 

case OP_CHECKLOCKTIMEVERIFY:
# 省略

bool GenericTransactionSignatureChecker<T>::CheckLockTime

# 1. nLockTime 和 脚本锁定时间 必须符合范围规则
# 交易nLockTime < 50 亿 && 脚本锁定时间 < 50亿 (高度)
# 交易nLockTime >= 50亿 && 脚本锁定时间 > 50亿 (时间)

# 2. 脚本锁定时间 > 交易的nLockTime , 不可上链??? (脚本锁定时间必须在交易的nLockTime之内)

# 3. nSequence == 0xffffffff, 不可上链 (禁用nLockTime)
```

<a id="markdown-4-场景四-冻结资金实践" name="4-场景四-冻结资金实践"></a>
# 4. 场景四 冻结资金实践

通过挖矿奖励得资金源:

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

创建带有CheckLockTimeVerify的`锁定交易`:

```bash

```

对该比脚本输出进行`解锁交易`,引用到该笔交易的地址,并使用私钥进行签名

```bash

```

<a id="markdown-5-场景二-双因素钱包实践-单向支付通道" name="5-场景二-双因素钱包实践-单向支付通道"></a>
# 5. 场景二 双因素钱包实践 (单向支付通道) 




<a id="markdown-6-交易数据" name="6-交易数据"></a>
# 6. 交易数据

* https://raw.githubusercontent.com/yqsy/yqsy.notes/master/source/_posts/business/bitcoin/script/nLockTime (nLockTime)


<a id="markdown-7-参考资料" name="7-参考资料"></a>
# 7. 参考资料

* https://en.bitcoin.it/wiki/Timelock (百科)
* https://coinb.in/#newTimeLocked (在线生成锁定脚本)
* https://github.com/bitcoin/bips/blob/master/bip-0065.mediawiki (BIP65)
* https://github.com/petertodd/checklocktimeverify-demos (BIP65 demo - python 单向支付通道)
* https://github.com/mruddy/bip65-demos (BIP65 demo - nodejs)
