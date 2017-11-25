---
title: TTCP
date: 2017-11-25 20:15:44
categories: [网络相关]
---

<!-- TOC -->

- [1. Why do we re-implement TTCP](#1-why-do-we-re-implement-ttcp)
- [2. 资料](#2-资料)

<!-- /TOC -->

<a id="markdown-1-why-do-we-re-implement-ttcp" name="1-why-do-we-re-implement-ttcp"></a>
# 1. Why do we re-implement TTCP

* Basic Sockets APIS: socket, listen, bind, accept, connect ,read/recv,write/send,shutdown,close,etc.
* protocol is binary, not just byte stream, so it's bnetter than the classic echo exmaple
* Typical behaviors, meaningful results, instead of packets/s
* Service benchmark for programming language as well, by comparing CPU usage (不同语言比较性能)
* Not concurrent (一请求一应答,模拟普通的应用场景)

<a id="markdown-2-资料" name="2-资料"></a>
# 2. 资料
* https://en.wikipedia.org/wiki/Ttcp