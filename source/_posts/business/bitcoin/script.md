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

