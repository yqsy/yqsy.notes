---
title: asio
date: 2017-12-12 21:33:05
categories: [网络相关]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 一些实践](#2-一些实践)
- [3. 一些发现](#3-一些发现)
    - [多线程](#多线程)

<!-- /TOC -->



<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料
* http://www.boost.org/doc/libs/1_57_0/doc/html/boost_asio.html (main page)
* http://www.boost.org/doc/libs/1_57_0/doc/html/boost_asio/overview/networking/bsd_sockets.html (BSD api)
* http://www.boost.org/doc/libs/1_57_0/doc/html/boost_asio/overview/networking/iostreams.html (iostream)
* http://www.boost.org/doc/libs/1_57_0/doc/html/boost_asio/reference/ip__tcp/iostream.html (iostream)
* http://www.boost.org/doc/libs/1_57_0/doc/html/boost_asio/overview/core/reactor.html (居然也可以reactor)
* http://www.boost.org/doc/libs/1_57_0/doc/html/boost_asio/tutorial.html (简单的例子把)
* site:http://www.boost.org/doc/libs/1_57_0 (搜素用这个)
* http://www.boost.org/doc/libs/1_57_0/doc/html/boost_asio/reference.html (所有的类)
* https://github.com/opensvn/test/blob/master/Boost-Asio-C-Network-Programming-Cookbook-1-md.md (一些example,可以稍微参考一下)

<a id="markdown-2-一些实践" name="2-一些实践"></a>
# 2. 一些实践

```
tcp 类

根据模板生成类
ip::tcp::acceptor  <- typedef basic_socket_acceptor<tcp> acceptor;
ip::tcp::endpoint  <- typedef basic_endpoint<tcp> endpoint;
ip::tcp::iostream  <- typedef basic_socket_iostream<tcp> iostream;
ip::tcp::resolver  <- typedef basic_resolver<tcp> resolver;
ip::tcp::socket    <- typedef basic_stream_socket<tcp> socket;


关于地址
http://www.boost.org/doc/libs/1_57_0/doc/html/boost_asio/reference/ip__basic_endpoint/basic_endpoint.html

client需要hostname,构造函数:
basic_endpoint(
    const boost::asio::ip::address & addr,
    unsigned short port_num);


dns解析,需要query
https://stackoverflow.com/questions/5486113/how-to-turn-url-into-ip-address-using-boostasio 

iterator resolve(
    const query & q,
    boost::system::error_code & ec);


ip::tcp::resolver 自身包含了:
typedef typename InternetProtocol::endpoint endpoint_type;
typedef basic_resolver_query<InternetProtocol> query;
typedef basic_resolver_iterator<InternetProtocol> iterator;
typedef basic_resolver_results<InternetProtocol> results_type;


函数返回的iterator是typedef basic_resolver_iterator<InternetProtocol> iterator;
*iter是 const basic_resolver_entry< InternetProtocol > & operator *() const;

basic_resolver_entry可以直接这样转,吓死我了 = =
66    /// Convert to the endpoint associated with the entry.
67    operator endpoint_type() const
68    {
69      return endpoint_;
70    }

阻塞I/O写明确的bytes
http://www.boost.org/doc/libs/1_57_0/doc/html/boost_asio/reference/write.html
```


<a id="markdown-3-一些发现" name="3-一些发现"></a>
# 3. 一些发现

<a id="markdown-多线程" name="多线程"></a>
## 多线程
```
      asio::thread* new_thread = new asio::thread(
          boost::bind(&asio::io_context::run, &ioc));

都在跑全局的 asio::io_context ioc;  run 函数上

里面有一把锁 mutex::scoped_lock lock(mutex_);

```
