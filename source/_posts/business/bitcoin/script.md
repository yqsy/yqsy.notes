---
title: script
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明


P2PKH

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

P2SH (BIP13 16)

```bash
# 单一签名
# scriptPubKey (prev out)
OP_EQUAL
[20-byte-hash of {[pubkey] OP_CHECKSIG} ]
OP_HASH160

# scriptSig (in)
{[pubkey] OP_CHECKSIG}
[signature]

# 3个签名
{2 [pubkey1] [pubkey2] [pubkey3] 3 OP_CHECKMULTISIG}
 
# 22个签名?
{OP_CHECKSIG OP_IF OP_CHECKSIGVERIFY OP_ELSE OP_CHECKMULTISIGVERIFY OP_ENDIF}
```

Multisig outputs (BIP 11)

```bash
# scriptPubKey (prev out)
OP_CHECKMULTISIG
n
{pubkey}...{pubkey}
m

# scriptSig (in)
...signatures...
OP_0
```

OP_RETURN (存数据)
```bash
# scriptPubKey (prev out)
<data2>
<data1>
OP_RETURN

# scriptSig (in)
# 空
```

Anyone-Can-Spend (不在p2p网络上传播)

```bash
OP_TRUE
```

Transaction Puzzle (猜谜吗)

```bash
# scriptPubKey (prev out)
OP_EQUAL
<given_hash>
OP_HASH256

# scriptSig (in)
<data> ?
```

Freezing funds until a time in the future (锁定一段时间)

```bash
# scriptPubKey (prev out)
OP_CHECKSIG
OP_EQUALVERIFY
<pubKeyHash>
OP_HASH160
OP_DUP
OP_DROP
OP_CHECKLOCKTIMEVERIFY
<expiry time>

# scriptSig (in)
<pubKey>
<sig>
```

Incentivized finding of hash collisions

```bash
# scriptPubKey (prev out)
OP_EQUAL
OP_SHA1
OP_SWAP
OP_SHA1
OP_VERIFY
OP_NOT
OP_EQUAL
OP_2DUP

# scriptSig (in)
<preimage2>
<preimage1>
```

