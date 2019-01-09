---
title: 源码编译与调试
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明


```bash
# 获取v0.17.0源码 创建阅读分支
cd /mnt/disk1/linux/reference/refer
git clone https://github.com/bitcoin/bitcoin
cd bitcoin
git checkout tags/v0.17.0 -b readerbranch

# 修改configure.ac 关闭优化,改成-O0
252:    [-Og],
253:    [[DEBUG_CXXFLAGS="$DEBUG_CXXFLAGS -Og"]],
611:  CXXFLAGS="$CXXFLAGS -Og"

# 开启附加调试
echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope

# 编译调试版本
./autogen.sh && ./configure --enable-debug
make -j 8 && sudo make install
```

添加阅读源码的CMakeFile.txt

```bash
cmake_minimum_required(VERSION 3.12)
project(src)

set(CMAKE_CXX_STANDARD 11)

include_directories(${PROJECT_SOURCE_DIR}/secp256k1/include
        ${PROJECT_SOURCE_DIR}/leveldb/include
        ${PROJECT_SOURCE_DIR}/univalue/include
        ${PROJECT_SOURCE_DIR}
        )


file(GLOB_RECURSE SRCS *.cpp *,h)

add_executable(src ${SRCS})
```



<a id="markdown-2-参考资料" name="2-参考资料"></a>
# 2. 参考资料

* https://github.com/bitcoin/bitcoin/blob/v0.17.0/doc/build-unix.md
