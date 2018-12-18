---
title: rsa
date: 2018-01-02 14:15:28
categories: [math]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 参考资料](#2-参考资料)

<!-- /TOC -->


<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

1. 随意选择两个大的`质数`p和q,`N = pq`
2. 根据欧拉函数,求得`φ(N) = (p-1)(q-1)`
3. 选择整数e, 满足`1 < e < φ(N)`,并且e与φ(N)互质
4. 求e关于φ(N)的模逆元,命名为d `(e*d mod φ(N) = 1)`

(N,e)是公钥. (N,d)是私钥. 

对于明文m:  

* 加密: c = (m^e) mod N
* 解密: m = (c^d) mod N

<a id="markdown-2-参考资料" name="2-参考资料"></a>
# 2. 参考资料

* http://code.activestate.com/recipes/578838-rsa-a-simple-and-easy-to-read-implementation/ (python example)
* https://zh.wikipedia.org/wiki/RSA%E5%8A%A0%E5%AF%86%E6%BC%94%E7%AE%97%E6%B3%95 (RSA维基百科)
* https://zh.wikipedia.org/wiki/%E6%AC%A7%E6%8B%89%E5%87%BD%E6%95%B0 (欧拉函数维基百科)
* https://zh.wikipedia.org/wiki/%E6%A8%A1%E5%8F%8D%E5%85%83%E7%B4%A0 (模逆元维基百科)
