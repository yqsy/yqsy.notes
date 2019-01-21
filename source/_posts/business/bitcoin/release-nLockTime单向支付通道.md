---
title: nLockTime单向支付通道
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 实践](#2-实践)
    - [2.1. 场景一: 用户在时间到后花费](#21-场景一-用户在时间到后花费)
- [3. 缺陷](#3-缺陷)
- [4. 参考资料](#4-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

设想一种支付方式: 用户把钱抵押给商家时,1. 商家可以看到钱但是不可以私自挪动钱,商家想要花费任意一点钱都需要征得用户的同意.  2. 用户在指定时间后可以退款.  

让我们来思考一下使用比特币的脚本如何实现这个逻辑(可以参考`<nLockTime时间锁交易>`的场景二双因素钱包 (GreenAddress)):

```bash
IF
    <service pubkey> CHECKSIGVERIFY
ELSE
    <expiry time> CHECKLOCKTIMEVERIFY DROP
ENDIF
<user pubkey> CHECKSIG
```

<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践

得到一笔资金:

```bash
# [压缩]
# 私钥: f1a80f81857decd896b1c51ede9460e445013ec8386bf8d778c523b60802b12e
# 私钥WIF: L5KTc49MiBTpueR8Ed5etFXRE9ZiZhqrYxudYWru6KetGkVAgzZW
# 公钥: 023908ead084840b8a67307025837548d44e65a59fb528263c263d1fa5e1782a4d
# 公钥hash: fa4d6873e5203075dcf32f8594f67125bf57e9b6
# P2PKH地址: 1PpUfMwTE4sSEsCWko3eUDPjHb98htX9HK
# URI: bitcoin:1PpUfMwTE4sSEsCWko3eUDPjHb98htX9HK
# P2SH-P2WPKH: 32TuMaeEVhdwPhohBrZRcDzmrRmYEs4Px9
# P2WPKH: bc1qlfxksul9yqc8th8n97zefan3ykl406dk52fw62

COINBASECP2PKHADDR=1PpUfMwTE4sSEsCWko3eUDPjHb98htX9HK

bitcoin-cli generatetoaddress 101 $COINBASECP2PKHADDR

# 查询锁定脚本
bbasetx 1

# 提取私钥并导入到钱包
COINBASEPRIKEYWIF=L5KTc49MiBTpueR8Ed5etFXRE9ZiZhqrYxudYWru6KetGkVAgzZW
bitcoin-cli importprivkey $COINBASEPRIKEYWIF

# 查询余额
bitcoin-cli getbalance
```

使用python脚本(可以直接使用命令行)，生成新的锁定交易，到新的地址：
```bash

# 用户的私钥信息:
# [压缩]
# 私钥: 9e93d1702f131626916f693592fd1cfddfe15b1e88c363c756dfceedecd850c3
# 私钥WIF: L2XxuM4B7GiVFwWhtriLugfWxMAB8AAn63dpygovyczESzBK6p4o
# 公钥: 030c080a2e82c342172d5e8845877e8a576cfd5ce2117e78bb15574a39dd00e58e
# 公钥hash: 600682ebd83c160b24d908752dbe52d1b2413b5c
# P2PKH地址: 19kjfqWzcujpK4SgyuSv6Lk9SfVwrV4hDt
# URI: bitcoin:19kjfqWzcujpK4SgyuSv6Lk9SfVwrV4hDt
# P2SH-P2WPKH: 3Km2LMyYzekRzH9DFComM7M8bqyfwg2bzh
# P2WPKH: bc1qvqrg967c8stqkfxepp6jm0jj6xeyzw6u7kkxc3

# 商家的私钥信息:
# [压缩]
# 私钥: 28f97e1aabce0cd8c7d166f25c18fa522dfa758ace160592bd93ef9dd38b90b7
# 私钥WIF: KxbMqfhaN8NFXPCmHE4ZupJfBYRDj46iT1YxNqHrJcrpmaKMiL6C
# 公钥: 03aa9f9253b5e8ce3f23bef805e035c9268a1157ba3d52ca0468ca3ebae3a5aea3
# 公钥hash: 4b482b072b3937ae2e987b9ad2194f22d6d9fcdb
# P2PKH地址: 17s48iNQ6ys4CWRvFn6wYT6rExfoJXyxzA
# URI: bitcoin:17s48iNQ6ys4CWRvFn6wYT6rExfoJXyxzA
# P2SH-P2WPKH: 3K9GUYjRznoXBugGj6DxaFcGPdUek1nNMP
# P2WPKH: bc1qfdyzkpet8ym6ut5c0wddyx20yttdnlxmf7sj2w

# 脚本:


# 地址
SCRIPT_ADDR=39QGYRrmYXM3pLD6xAEoQiyiA1Gd4uZ2j1

UTXOID=`bitcoin-cli sendtoaddress $SCRIPT_ADDR 50.0 "" "" true`

# 打包交易至区块
bg 1

# 打印交易哈希 (动态会变)
echo $UTXOID
```

<a id="markdown-21-场景一-用户在时间到后花费" name="21-场景一-用户在时间到后花费"></a>
## 2.1. 场景一: 用户在时间到后花费

请注意,这是其中一个场景,执行完后删除数据,再去执行其他场景
```bash
# scriptPubKey (prev out)
OP_EQUAL
<20-byte-hash of script>
OP_HASH160

# redeemScript

OP_CHECKSIG
<userPubkey>           <- 
OP_ENDIF
OP_DROP
OP_CHECKLOCKTIMEVERIFY <- 
<expiry time>
OP_ELSE
OP_CHECKSIGVERIFY
<servicePubkey>
OP_IF

# scriptSig (in)
<sig>
```

使用python脚本，把P2SH的币转到其他的地址. (把上面的UTXOID粘贴到,python脚本中(因为会动态变化),来生成新的交易)
```bash

bg 198

# 用户成功在时间到之后将P2SH的资金退款到自己的账户
bitcoin-cli sendrawtransaction $python脚本打印的交易数据

bg 1

bhtx 301 1

```


<a id="markdown-3-缺陷" name="3-缺陷"></a>
# 3. 缺陷



<a id="markdown-4-参考资料" name="4-参考资料"></a>
# 4. 参考资料

* https://github.com/petertodd/checklocktimeverify-demos (BIP65 demo - python 单向支付通道)
* https://github.com/mruddy/bip65-demos (BIP65 demo - nodejs)
* https://github.com/tianmingyun/MasterBitcoin2CN/blob/master/ch12.md (精通比特币,应用章节-简单支付通道示例)
