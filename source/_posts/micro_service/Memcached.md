---
title: Memcached
date: 2018-1-7 22:41:03
categories: [微服务]
---

<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 搭建](#2-搭建)
- [3. 代码阅读整理](#3-代码阅读整理)
- [4. 接口/使用](#4-接口使用)

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

* 使用的是libevent
* 多线程(pthread_create)

```
main
void thread_init(int nthreads, struct event_base *main_base)
static void create_worker(void *(*func)(void *), void *arg) 
pthread_create

线程跑的函数是
worker_libevent

LIBEVENT_THREAD 作为函数

用这个struct event_base *base;作为参数

event_base_loop(me->base, 0); 让线程跑event loop!

threads[0].base = main_base;  为什么只设置了线程数组的第1个元素的base???

可得知threads[0]跑的是main函数栈上面的 event_base, 其余的会用event_init再次创建

而且注意!! 诡异的是,线程数组第1个元素不会去pthread_create,也不知道这根线程是做啥的?

每根线程在接受到read之后跑的是thread_libevent_process (listen的read事件)

client的read回调函数应该是event_handler -> drive_machine

conn 是连接,有多种不同的状态

连接是用queue管理的

setsockopt
* SO_SNDBUF 给发送缓冲区扩容 https://www.zhihu.com/question/67833119/answer/257061904 (没必要别设置)
* SO_REUSEADDR 
* SO_KEEPALIVE (缺省120分钟?) https://www.zhihu.com/search?type=content&q=SO_KEEPALIVE
* SO_LINGER (延迟关闭时间,应该不需要)
* TCP_NODELAY 
```



<a id="markdown-4-接口使用" name="4-接口使用"></a>
# 4. 接口/使用

存储
* set (强行设置)
* add (如果有key,则返回NOT_STORED)
* replace (替换value)
* append (字符串追加)
* prepend (前向追加)
* CAS (Check-And-Set)

检索数据
* get 
* gets
* incr 自增
* decr 自减

统计数据
* stats
* stats items
* stats slabs
* stats sizes
* flush_all
