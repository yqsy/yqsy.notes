---
title: Memcached
date: 2018-1-7 22:41:03
categories: [微服务]
---

<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 搭建](#2-搭建)
- [3. 代码阅读整理](#3-代码阅读整理)

<!-- /TOC -->

<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源

* https://memcached.org/
* https://github.com/memcached/memcached (推荐看1.2.8版本)
* https://hub.docker.com/_/memcached/ (docker)
* https://github.com/docker-library/memcached/blob/master/alpine/Dockerfile (docker file)
* https://www.tutorialspoint.com/memcached/memcached_set_data.htm (turtoial)
<a id="markdown-2-搭建" name="2-搭建"></a>
# 2. 搭建

```bash

docker run --name my-memcache -p 11211:11211 -d memcached

```

<a id="markdown-3-代码阅读整理" name="3-代码阅读整理"></a>
# 3. 代码阅读整理

```
  5857 total
  3104 ./memcached.c
   694 ./thread.c
   624 ./assoc.c
   546 ./items.c
   437 ./slabs.c
   365 ./stats.c
    87 ./daemon.c
```
