---
title: 隔离见证交易
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. P2WPKH](#2-p2wpkh)
- [3. P2WSH](#3-p2wsh)
- [4. P2SH-P2WPKH](#4-p2sh-p2wpkh)
- [5. P2SH-P2WSH](#5-p2sh-p2wsh)
- [6. 参考资料](#6-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明


<a id="markdown-2-p2wpkh" name="2-p2wpkh"></a>
# 2. P2WPKH

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
scriptPubKey: 0 <20-byte-key-hash>

# scriptSig (in)
witness:      <signature> <pubkey>
scriptSig:    (empty)
```

<a id="markdown-3-p2wsh" name="3-p2wsh"></a>
# 3. P2WSH

加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
scriptPubKey: 0 <32-byte-hash>

# scriptSig (in)
witness:      0 <signature1> <1 <pubkey1> <pubkey2> 2 CHECKMULTISIG>
scriptSig:    (empty)
```

<a id="markdown-4-p2sh-p2wpkh" name="4-p2sh-p2wpkh"></a>
# 4. P2SH-P2WPKH


加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
scriptPubKey: HASH160 <20-byte-script-hash> EQUAL

# scriptSig (in)
witness:      <signature> <pubkey>
scriptSig:    <0 <20-byte-key-hash>>
```


<a id="markdown-5-p2sh-p2wsh" name="5-p2sh-p2wsh"></a>
# 5. P2SH-P2WSH


加锁与解锁的堆栈:

```bash
# scriptPubKey (prev out)
scriptPubKey: HASH160 <20-byte-hash> EQUAL

# scriptSig (in)
witness:      0 <signature1> <1 <pubkey1> <pubkey2> 2 CHECKMULTISIG>
scriptSig:    <0 <32-byte-hash>>
```

<a id="markdown-6-参考资料" name="6-参考资料"></a>
# 6. 参考资料

* https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki (BIP141)
