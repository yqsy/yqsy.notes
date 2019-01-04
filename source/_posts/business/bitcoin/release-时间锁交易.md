---
title: 时间锁交易
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. nLockTime](#2-nlocktime)
- [3. CheckLockTimeVerify](#3-checklocktimeverify)
- [4. nSequence](#4-nsequence)
- [5. CheckSequenceVerify](#5-checksequenceverify)
- [6. 参考资料](#6-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

设想一种功能: 锁定某一笔钱直到若干年后才能被消费. 这样的功能在传统中心化软件中无法真正做到,因为中心化系统的规则并不是真正的规则.在区块链软件中,规则一旦制定,随着时间的推移其修改的成本会变的越来越高.这里做一下时间锁相关的交易,并跟踪到相关代码来分析.

<a id="markdown-2-nlocktime" name="2-nlocktime"></a>
# 2. nLockTime 

代码:
```bash
# nLockTime在500000000 以内表示高度. 相应nLockTime 高度 / 时间 已经过去时交易可被打包.
IsFinalTx <- ContextualCheckBlock
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

# 1) 创建交易 (到达2000高度后可被打包)
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
```

<a id="markdown-3-checklocktimeverify" name="3-checklocktimeverify"></a>
# 3. CheckLockTimeVerify

(BIP65)

代码:
```bash
EvalScript 

case OP_CHECKLOCKTIMEVERIFY:
# 省略
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

创建带有CheckLockTimeVerify的`锁定交易`:

```bash
PRE_TXID=`_bbasehash 1`
PRE_VOUT=0

# 获得新的地址
NEWEC=`bx seed | bx ec-new`
NEWADDRESS_INFO=`parse_privkey $NEWEC`

# 提取公钥
NEWPUBKEY=`echo $NEWADDRESS_INFO | sed -n 11p | awk '{print $2}'`

# 提取私钥做备用
NEWPRVKEY=`echo $NEWADDRESS_INFO | sed -n 10p | awk '{print $2}'`

# 30s后解锁
CURRENTTIME=`date +%s`
CURRENTTIME=`expr $CURRENTTIME + 10`
CURRENTTIME_HEX=`printf "%X" $CURRENTTIME`
CURRENTTIME_HEX=`echo ${CURRENTTIME_HEX:6:2}${CURRENTTIME_HEX:4:2}${CURRENTTIME_HEX:2:2}${CURRENTTIME_HEX:0:2}`

SCRIPT=`bx script-encode "[$CURRENTTIME] checklocktimeverify drop [$NEWPUBKEY] checksig"`

SCRIPT_ADDR=`echo $SCRIPT | bx sha256 | bx ripemd160 | bx base58check-encode --version 5`

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
    "'$SCRIPT_ADDR'": 49.9999
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

# 4) 打包
bg 1
```

对该比脚本输出进行`解锁交易`,引用到该笔交易的地址,并使用私钥进行签名

```bash
PRE_TXID=`_bhtxhash 102 1`
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
    "'$NEWPRVKEY'"
]
''' '''
[
    {
        "txid": "'$UTXOID'",
        "vout": '$UTXO_VOUT',
        
    }
]
'''`

SIGNED_RAWTX=`echo $SIGNED_RAWTX_JSON | python -c 'import json,sys;obj=json.load(sys.stdin);print(obj["hex"])'`

# 3)发送交易
bitcoin-cli sendrawtransaction $SIGNED_RAWTX

```


<a id="markdown-4-nsequence" name="4-nsequence"></a>
# 4. nSequence

(BIP68 / 112/113)
 
<a id="markdown-5-checksequenceverify" name="5-checksequenceverify"></a>
# 5. CheckSequenceVerify

(BIP68 / 112/113)


<a id="markdown-6-参考资料" name="6-参考资料"></a>
# 6. 参考资料

* https://en.bitcoin.it/wiki/Timelock (维基百科)
* https://coinb.in/#newTimeLocked (在线生成锁定脚本)
