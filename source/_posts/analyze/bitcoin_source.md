---
title: bitcoin_source
date: 2018-08-09 11:51:23
categories: [项目分析]
---

<!-- TOC -->

- [1. 源码拉取](#1-源码拉取)
- [2. 代码组织](#2-代码组织)
- [3. 有用的文档](#3-有用的文档)
- [4. 源码详细](#4-源码详细)

<!-- /TOC -->

<a id="markdown-1-源码拉取" name="1-源码拉取"></a>
# 1. 源码拉取


v0.17.0


```bash
cd /mnt/disk1/linux/reference/refer
git clone https://github.com/bitcoin/bitcoin
cd bitcoin
git checkout tags/v0.17.0 -b pkc
```

<a id="markdown-2-代码组织" name="2-代码组织"></a>
# 2. 代码组织
```bash

# 代码文件组织 .cpp .c .h
./qt                 280723     # qt *
./bench              126491     # bench mark
./test               92572      # test
./secp256k1          18712      # 椭圆曲线加密算法 * 
./wallet             17493      # 钱包
./rpc                7734       # rpc
./leveldb            6200       # 引用的leveldb库 *
./script             6031       # 脚本实现
./crypto             5712       # 对称/非堆成 加密算法
./univalue           2401       # json *
./policy             1860       # 策略,费用计算
./interfaces         1438       # node接口,钱包接口  
./support            864        # 内存池
./index              716        # blockchain的存储层
./primitives         708        # 区块/交易
./consensus          669        # 共识, markle tree
./zmq                652        # zeromq 接口
./compat             539        # 压缩　　
./config             434        # 配置

```

<a id="markdown-3-有用的文档" name="3-有用的文档"></a>
# 3. 有用的文档

```bash
.
├── assets-attribution.md     # 开源库的使用
├── benchmarking.md           # 密码相关函数的评测
├── bips.md                   # 实现的? BIPS协议规范
├── bitcoin_logo_doxygen.png 
├── build-freebsd.md          # freebsd的编译方法
├── build-netbsd.md           # netbsd的编译方法
├── build-openbsd.md          # openbsd的编译方法
├── build-osx.md              # osx的编译方法
├── build-unix.md             # unix的编译方法
├── build-windows.md          # windows的编译方法
├── dependencies.md           # 依赖库的清单
├── descriptors.md            # rpc scantxoutset 检索说明
├── developer-notes.md        # 编程规范
├── dnsseed-policy.md         # dns seed 规则 
├── Doxyfile.in          
├── files.md                  # 在~./bitcoin/中的各个配置文件作用的说明
├── fuzzing.md                # 模糊测试?
├── gitian-building.md        # 交叉编译?
├── init.md                   # 初始化脚本的配置和说明
├── man                       #
├── README.md                 # 索引
├── README_osx.md
├── README_windows.txt
├── reduce-traffic.md      # 减少带宽
├── release-notes          # 版本更新说明
├── release-notes.md       # 发布升级说明
├── release-process.md     # 升级过程?
├── REST-interface.md      # rest接口
├── shared-libraries.md    # 提供验证的借口
├── tor.md                 # 对接洋葱头
├── translation_process.md # 国际化
├── translation_strings_policy.md # 国际化
├── travis-ci.md           # 持续集成
└── zmq.md                 # 通过zeromq广播?

```

<a id="markdown-4-源码详细" name="4-源码详细"></a>
# 4. 源码详细


