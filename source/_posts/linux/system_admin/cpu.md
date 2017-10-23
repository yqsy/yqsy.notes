---
title: cpu
date: 2017-10-23 14:26:38
categories: [linux, 系统管理]
---
<!-- TOC -->

- [1. 查看核心数量](#1-查看核心数量)
- [2. 查看cpu信息](#2-查看cpu信息)

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