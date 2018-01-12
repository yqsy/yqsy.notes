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
* https://github.com/memcached/memcached/blob/master/doc/protocol.txt (协议)


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

* daemon运行 (这个知识点没深入研究过)
* 使用的是libevent
* 多线程(pthread_create),多线程需要加参数编译(Round-robin)
* 有锁生产者消费者队列 (pthread_mutex_lock)
* hash 算法: http://burtleburtle.net/bob/hash/doobs.html
* slab 内存处理机制,避免大量的初始化和清理操作

```
第一根线程是复用主线程的    main_base = event_init();, 其余线程都会创建新的event_base (可能是把主线程当数组的第一根线程了)
    threads[0].base = main_base;


每一根线程都会有各自的单向pipe
    pipe(fds)

        threads[i].notify_receive_fd = fds[0];
        threads[i].notify_send_fd = fds[1];


除开第一根线程都会pthread_create (入口是worker_libevent)  event_base_loop(me->base, 0);
for (i = 1; i < nthreads; i++) {
    create_worker(worker_libevent, &threads[i]);
}


typedef struct {
    pthread_t thread_id;        /* unique ID of this thread */
    struct event_base *base;    /* libevent handle this thread uses */
    struct event notify_event;  /* listen event for notify pipe */
    int notify_receive_fd;      /* receiving end of notify pipe */  ****   管道读会走到函数 thread_libevent_process, 其实只是接收信号, 用来conn_new的.
    int notify_send_fd;         /* sending end of notify pipe */    ************ 关于谁会写这个管道看下文调用栈
    CQ  new_conn_queue;         /* queue of new connections to handle */  ** 每根线程的新的连接
} LIBEVENT_THREAD;



总结:
主线程创建listen fd ,并用conn_new监听可读事件到达主线程执行的event loop,一旦有新的连接进来,accept,通过dispatch_conn_new 以Round-robin 负载均衡手段将
连接CQ_ITEM(包含fd) push到各个线程的消费队列里,并write至管道,通知到相应线程.相应线程触发conn_new,注册监听事件至event_handler

关键流程 (listenfd和clientfd)conn_new->(注册)event_handler->drive_machin根据状态来处理相应事件

conn_new函数调用确定初始化状态

* conn_listening , 作为Listen套接字,其套接字收到可读信号,都要处理accept
* conn_read , 每根线程得到初始化的套接字时的初始化状态 try_read_command(读已有的缓冲区数据) -> process_command

这是一个双向链表
typedef struct conn_queue CQ;
struct conn_queue {
    CQ_ITEM *head;
    CQ_ITEM *tail;
    pthread_mutex_t lock;
    pthread_cond_t  cond;
};

链接队列

单向链表
typedef struct conn_queue_item CQ_ITEM;
struct conn_queue_item {
    int     sfd;
    int     init_state;
    int     event_flags;
    int     read_buffer_size;
    int     is_udp;
    CQ_ITEM *next;
};


连接
struct conn {
    int    sfd;
    int    state;
    struct event event;
    short  ev_flags;
    short  which;   /** which events were just triggered */

    char   *rbuf;   /** buffer to read commands into */
    char   *rcurr;  /** but if we parsed some already, this is where we stopped */
    int    rsize;   /** total allocated size of rbuf */
    int    rbytes;  /** how much data, starting from rcur, do we have unparsed */

    char   *wbuf;
    char   *wcurr;
    int    wsize;
    int    wbytes;
    int    write_and_go; /** which state to go into after finishing current write */
    void   *write_and_free; /** free this memory after finishing writing */

    char   *ritem;  /** when we read in an item's value, it goes here */
    int    rlbytes;

    /* data for the nread state */

    /**
     * item is used to hold an item structure created after reading the command
     * line of set/add/replace commands, but before we finished reading the actual
     * data. The data is read into ITEM_data(item) to avoid extra copying.
     */

    void   *item;     /* for commands set/add/replace  */
    int    item_comm; /* which one is it: set/add/replace */

    /* data for the swallow state */
    int    sbytes;    /* how many bytes to swallow */

    /* data for the mwrite state */
    struct iovec *iov;
    int    iovsize;   /* number of elements allocated in iov[] */
    int    iovused;   /* number of elements used in iov[] */

    struct msghdr *msglist;
    int    msgsize;   /* number of elements allocated in msglist[] */
    int    msgused;   /* number of elements used in msglist[] */
    int    msgcurr;   /* element in msglist[] being transmitted now */
    int    msgbytes;  /* number of bytes in current msg */

    item   **ilist;   /* list of items to write out */
    int    isize;
    item   **icurr;
    int    ileft;

    char   **suffixlist;
    int    suffixsize;
    char   **suffixcurr;
    int    suffixleft;

    /* data for UDP clients */
    bool   udp;       /* is this is a UDP "connection" */
    int    request_id; /* Incoming UDP request ID, if this is a UDP "connection" */
    struct sockaddr request_addr; /* Who sent the most recent request */
    socklen_t request_addr_size;
    unsigned char *hdrbuf; /* udp packet headers */
    int    hdrsize;   /* number of headers' worth of space is allocated */

    int    binary;    /* are we in binary mode */
    bool   noreply;   /* True if the reply should not be sent. */
    conn   *next;     /* Used for generating a list of conn structures */
};

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
