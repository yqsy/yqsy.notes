---
title: 区块的存储
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 区块的存储](#2-区块的存储)
- [3. 参考资料](#3-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

比特币的特点:所有信息公开透明.通过写代码来浏览比特币的存储数据得知所有的区块信息,交易信息.可以做一些非常有趣的事情. 例如: 账本内有多少垃圾数据?哪位用户的钱包地址币最多?共识版本号经过了怎么样的迁移?


<a id="markdown-2-区块的存储" name="2-区块的存储"></a>
# 2. 区块的存储

重要的几个数据存储文件如下`(下文着重讲述高亮的2处文件)`:

* `blocks/blkxxxxx.dat (block data)`
* blocks/revxxxxx.dat (block undo data)
* `blocks/index/* block index (leveldb) `
* chainstate/* block chain state database (leveldb)


`打开文件处代码,可以通过这个回溯到相关读写处:`
```c++
// blocks/blkxxxxx.dat 
FILE* OpenBlockFile(const CDiskBlockPos &pos, bool fReadOnly) {
    return OpenDiskFile(pos, "blk", fReadOnly);
}

// blocks/index/*
CBlockTreeDB::CBlockTreeDB(size_t nCacheSize, bool fMemory, bool fWipe) : CDBWrapper(gArgs.IsArgSet("-blocksdir") ? GetDataDir() / "blocks" / "index" : GetBlocksDir() / "index", nCacheSize, fMemory, fWipe) {

leveldb::Status status = leveldb::DB::Open(options, path.string(), &pdb);
```

`核心存储区块的逻辑:`
```bash
SaveBlockToDisk

# 包括3步
# 1. GetSerializeSize 获取存储区块的大小
# 2. FindBlockPos 寻找到存储的位置
# 3. WriteBlockToDisk 写到磁盘上
```

`使用python代码做存储的演示:`




<a id="markdown-3-参考资料" name="3-参考资料"></a>
# 3. 参考资料

* https://en.bitcoin.it/wiki/Bitcoin_Core_0.11_(ch_2):_Data_Storage
* https://github.com/bitcoin/bitcoin/blob/0.17/doc/files.md

