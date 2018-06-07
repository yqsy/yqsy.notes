---
title: p2p
date: 2018-06-07 18:54:33
categories: [网络相关]
---

<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* http://blog.51cto.com/wangbojing/1968118
* http://www.goto.info.waseda.ac.jp/~wei/file/wei-apan-v10.pdf


简单整理下来,有这么几种

* Full Cone NAT ,对端任意ip port
* Restricted Cone NAT 对端`unique ip`,任意port
* Port Restricted Cone NAT
* Symmetric NAT, 对端`unique ip`, `unique port`


打洞方法我的梳理:


```
   server
 |       |
NATA     NATB
 |       |
 PCA     PCB
```

简单的就是锥形模式,server处有A/B(ip,port),让AB得知各自的(ip,port)即可穿透NAT  


但是对称模式如何打洞呢?只能靠猜测了,AB得知各自的ip地址后, port怎么办?靠猜测,或者预测nat产生port的规律

