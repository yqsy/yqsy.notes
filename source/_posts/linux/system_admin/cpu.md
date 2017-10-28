---
title: cpu
date: 2017-10-23 14:26:38
categories: [linux, 系统管理]
---
<!-- TOC -->

- [1. 查看核心数量](#1-%E6%9F%A5%E7%9C%8B%E6%A0%B8%E5%BF%83%E6%95%B0%E9%87%8F)
- [2. 查看cpu信息](#2-%E6%9F%A5%E7%9C%8Bcpu%E4%BF%A1%E6%81%AF)

<!-- /TOC -->

# 1. 查看核心数量
```
grep 'processor' /proc/cpuinfo
```

# 2. 查看cpu信息
```
cat /proc/cpuinfo
lscpu
```