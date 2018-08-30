---
title: bitcoin_source
date: 2018-08-09 11:51:23
categories: [项目分析]
---

<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

```bash
# 搜入口
src/univalue/gen/gen.cpp:78:int main (int argc, char *argv[])
src/qt/bitcoin.cpp:556:int main(int argc, char *argv[])
src/bench/bench_bitcoin.cpp:49:int main(int argc, char** argv)

src/bitcoin-tx.cpp:837:int main(int argc, char* argv[])
src/bitcoind.cpp:184:int main(int argc, char* argv[])
src/bitcoin-cli.cpp:514:int main(int argc, char* argv[])
```


```bash
# 代码文件组织
./bench           # benchmark
./compat          # 压缩　　
./consensus       # 共识, markle tree
./crypto          # 对称/非堆成 加密算法
./index           # blockchain的存储层
./interfaces      # node接口,钱包接口  
./leveldb         # 引用的leveldb库 *
./policy          # 策略,费用计算
./primitives      # 区块/交易
./qt              # 前台代码  *
./rpc             # json rpc 接口 
./script          # 脚本实现
./secp256k1       # 椭圆曲线加密算法 * 
./support         # 内存池
./test            # 测试用例
./univalue        # json *
./wallet          # 钱包
./zmq             # zeromq 接口


# 源码
.
├── addrdb.cpp
├── addrdb.h
├── addrman.cpp
├── addrman.h
├── amount.h
├── arith_uint256.cpp
├── arith_uint256.h
├── base58.cpp
├── base58.h
├── bech32.cpp
├── bech32.h
├── bench
│   ├── base58.cpp
│   ├── bech32.cpp
│   ├── bench_bitcoin.cpp
│   ├── bench.cpp
│   ├── bench.h
│   ├── block_assemble.cpp
│   ├── ccoins_caching.cpp
│   ├── checkblock.cpp
│   ├── checkqueue.cpp
│   ├── coin_selection.cpp
│   ├── crypto_hash.cpp
│   ├── data
│   ├── examples.cpp
│   ├── lockedpool.cpp
│   ├── mempool_eviction.cpp
│   ├── merkle_root.cpp
│   ├── prevector.cpp
│   ├── rollingbloom.cpp
│   └── verify_script.cpp
├── bitcoin-cli.cpp
├── bitcoind.cpp
├── bitcoin-tx.cpp
├── blockencodings.cpp
├── blockencodings.h
├── bloom.cpp
├── bloom.h
├── chain.cpp
├── chain.h
├── chainparamsbase.cpp
├── chainparamsbase.h
├── chainparams.cpp
├── chainparams.h
├── chainparamsseeds.h
├── checkpoints.cpp
├── checkpoints.h
├── checkqueue.h
├── clientversion.cpp
├── clientversion.h
├── coins.cpp
├── coins.h
├── compat
│   ├── byteswap.h
│   ├── endian.h
│   ├── glibc_compat.cpp
│   ├── glibc_sanity.cpp
│   ├── glibcxx_sanity.cpp
│   ├── sanity.h
│   └── strnlen.cpp
├── compat.h
├── compressor.cpp
├── compressor.h
├── config
├── consensus
│   ├── consensus.h
│   ├── merkle.cpp 
│   ├── merkle.h  # CBlock类vtx -> 交易hash vec-> 树根hash
│   ├── params.h
│   ├── tx_verify.cpp
│   ├── tx_verify.h
│   └── validation.h
├── core_io.h
├── core_memusage.h
├── core_read.cpp
├── core_write.cpp
├── crypto
│   ├── aes.cpp
│   ├── aes.h
│   ├── chacha20.cpp
│   ├── chacha20.h
│   ├── common.h
│   ├── ctaes
│   │   └── ctaes.h
│   ├── hmac_sha256.cpp
│   ├── hmac_sha256.h
│   ├── hmac_sha512.cpp
│   ├── hmac_sha512.h
│   ├── ripemd160.cpp
│   ├── ripemd160.h
│   ├── sha1.cpp
│   ├── sha1.h
│   ├── sha256_avx2.cpp
│   ├── sha256.cpp
│   ├── sha256.h
│   ├── sha256_shani.cpp
│   ├── sha256_sse41.cpp
│   ├── sha256_sse4.cpp
│   ├── sha512.cpp
│   └── sha512.h
├── cuckoocache.h
├── dbwrapper.cpp
├── dbwrapper.h
├── fs.cpp
├── fs.h
├── hash.cpp
├── hash.h         # 计算hash
├── httprpc.cpp
├── httprpc.h
├── httpserver.cpp
├── httpserver.h
├── index
│   ├── base.cpp
│   ├── base.h
│   ├── txindex.cpp
│   └── txindex.h
├── indirectmap.h
├── init.cpp
├── init.h
├── interfaces
│   ├── handler.cpp
│   ├── handler.h
│   ├── node.cpp
│   ├── node.h
│   ├── wallet.cpp
│   └── wallet.h
├── key.cpp
├── key.h
├── key_io.cpp
├── key_io.h
├── keystore.cpp
├── keystore.h
├── leveldb
├── limitedmap.h
├── logging.cpp
├── logging.h
├── memusage.h
├── merkleblock.cpp
├── merkleblock.h    #  验证某笔交易的合法性
├── miner.cpp        # 铸币
├── miner.h
├── netaddress.cpp
├── netaddress.h
├── netbase.cpp
├── netbase.h
├── net.cpp
├── net.h
├── netmessagemaker.h
├── net_processing.cpp
├── net_processing.h
├── noui.cpp
├── noui.h
├── obj
├── obj-test
├── outputtype.cpp
├── outputtype.h
├── policy
│   ├── feerate.cpp
│   ├── feerate.h
│   ├── fees.cpp
│   ├── fees.h
│   ├── policy.cpp
│   ├── policy.h
│   ├── rbf.cpp
│   └── rbf.h
├── pow.cpp
├── pow.h
├── prevector.h
├── primitives # 原始的?
│   ├── block.cpp
│   ├── block.h # CBlockHeader 和 CBlock, CTransactionRef
│   ├── transaction.cpp 
│   └── transaction.h # CTransaction CTxIn CTxOut
├── protocol.cpp
├── protocol.h
├── pubkey.cpp
├── pubkey.h
├── qt
├── random.cpp
├── random.h
├── rest.cpp
├── reverse_iterator.h
├── reverselock.h
├── rpc
│   ├── blockchain.cpp
│   ├── blockchain.h
│   ├── client.cpp
│   ├── client.h
│   ├── mining.cpp      # 挖矿,生成区块
│   ├── mining.h
│   ├── misc.cpp
│   ├── net.cpp
│   ├── protocol.cpp
│   ├── protocol.h
│   ├── rawtransaction.cpp
│   ├── rawtransaction.h
│   ├── register.h
│   ├── server.cpp
│   ├── server.h
│   ├── util.cpp
│   └── util.h
├── scheduler.cpp
├── scheduler.h
├── script  # 脚本
│   ├── bitcoinconsensus.cpp
│   ├── bitcoinconsensus.h
│   ├── descriptor.cpp
│   ├── descriptor.h
│   ├── interpreter.cpp
│   ├── interpreter.h
│   ├── ismine.cpp
│   ├── ismine.h
│   ├── script.cpp
│   ├── script_error.cpp
│   ├── script_error.h
│   ├── script.h         # CScript CScriptBase
│   ├── sigcache.cpp
│   ├── sigcache.h
│   ├── sign.cpp
│   ├── sign.h           # 签名
│   ├── standard.cpp
│   └── standard.h
├── secp256k1
├── serialize.h
├── shutdown.cpp
├── shutdown.h
├── span.h
├── streams.h
├── support
│   ├── allocators
│   │   ├── secure.h
│   │   └── zeroafterfree.h
│   ├── cleanse.cpp
│   ├── cleanse.h
│   ├── events.h
│   ├── lockedpool.cpp
│   └── lockedpool.h
├── sync.cpp
├── sync.h
├── test
├── threadinterrupt.cpp
├── threadinterrupt.h
├── threadsafety.h
├── timedata.cpp
├── timedata.h
├── tinyformat.h
├── torcontrol.cpp
├── torcontrol.h
├── txdb.cpp
├── txdb.h
├── txmempool.cpp   
├── txmempool.h      # CTxMemPoolEntry CTxMemPool 交易池
├── ui_interface.cpp
├── ui_interface.h
├── uint256.cpp
├── uint256.h
├── undo.h
├── univalue   # json
├── util.cpp
├── util.h
├── utilmemory.h
├── utilmoneystr.cpp
├── utilmoneystr.h
├── utilstrencodings.cpp
├── utilstrencodings.h
├── utiltime.cpp
├── utiltime.h
├── validation.cpp
├── validation.h
├── validationinterface.cpp
├── validationinterface.h
├── versionbits.cpp
├── versionbits.h
├── version.h
├── wallet
│   ├── coincontrol.cpp
│   ├── coincontrol.h
│   ├── coinselection.cpp
│   ├── coinselection.h
│   ├── crypter.cpp
│   ├── crypter.h
│   ├── db.cpp
│   ├── db.h
│   ├── feebumper.cpp
│   ├── feebumper.h
│   ├── fees.cpp
│   ├── fees.h
│   ├── init.cpp
│   ├── rpcdump.cpp
│   ├── rpcwallet.cpp
│   ├── rpcwallet.h
│   ├── test
│   ├── wallet.cpp
│   ├── walletdb.cpp
│   ├── walletdb.h
│   ├── wallet.h        # CMerkleTx <- CWalletTx  包装了交易
│   ├── walletutil.cpp
│   └── walletutil.h
├── walletinitinterface.h
├── warnings.cpp
├── warnings.h
└── zmq
    ├── zmqabstractnotifier.cpp
    ├── zmqabstractnotifier.h
    ├── zmqconfig.h
    ├── zmqnotificationinterface.cpp
    ├── zmqnotificationinterface.h
    ├── zmqpublishnotifier.cpp
    ├── zmqpublishnotifier.h
    ├── zmqrpc.cpp
    └── zmqrpc.h


```
