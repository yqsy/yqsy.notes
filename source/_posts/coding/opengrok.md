---
title: opengrok
date: 2017-12-10 12:03:28
categories: [coding]
---



<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 我的实践](#2-我的实践)

<!-- /TOC -->



<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://github.com/OpenGrok/OpenGrok/wiki/How-to-install-OpenGrok
* http://algopadawan.blogspot.co.uk/2012/07/installing-opengrok-on-windows.html (windows 没下载的) 
* http://moroienius.blogspot.com/2012/07/how-to-setup-opengrok.html (windows)
* https://www.zhihu.com/question/33505693/answer/132224974 (韦易笑的)
* http://zhuanlan.zhihu.com/p/28285996 (知乎简单的安装手册)
* http://mazhuang.org/2016/12/14/rtfsc-with-opengrok/ (多项目)


<a id="markdown-2-我的实践" name="2-我的实践"></a>
# 2. 我的实践

```bash
# jre
https://www.java.com/zh_CN/download/

# 环境变量
JRE_HOME=C:/Program Files/Java/jre1.8.0_151

tomcat
http://tomcat.apache.org/

# ctags(下载完了放到环境变量)
https://github.com/universal-ctags/ctags-win32/releases

opengrok
https://github.com/OpenGrok/OpenGrok/releases


tar -xvzf opengrok-1.1-rc17.tar.gz
copy D:/tools/opengrok/opengrok-1.1-rc17/lib/source.war to D:/tools/apache-tomcat-8.5.24/webapps

# start tomcat 

# 会生成该目录
D:/tools/apache-tomcat-8.5.24/webapps/source

# 修改
D:/tools/apache-tomcat-8.5.24/webapps/source/WEB-INF/web.xml

<param-value>/var/opengrok/etc/configuration.xml</param-value>
# 成
<param-value>D:/tools/opengrok/opengrok-1.1-rc17/data/configuration.xml</param-value>

# 生成索引
java -jar  D:/tools/opengrok/opengrok-1.1-rc17/lib/opengrok.jar -P -S -v -s D:/reference/refer/muduo -d D:/tools/opengrok/opengrok-1.1-rc17/data -W D:/tools/opengrok/opengrok-1.1-rc17/data/configuration.xml

# 多个源码
cd D:/reference/opengrok_projects

mklink /J muduo D:\reference\refer\muduo
mklink /J muduo-examples-in-go D:\reference\refer\muduo-examples-in-go
mklink /J libevent D:\reference\refer\libevent
mklink /J libev D:\reference\refer\libev
mklink /J shadowsocks-libev D:\reference\refer\shadowsocks-libev
mklink /J shadowsocks D:\reference\refer\shadowsocks
mklink /J linux_include D:\reference\refer\usr\include
mklink /J asio D:\reference\refer\asio
mklink /J WebBench D:\reference\refer\WebBench
mklink /J redis D:\reference\refer\redis
mklink /J protobuf D:\reference\refer\protobuf
mklink /J nginx D:\reference\refer\nginx
mklink /J libzmq D:\reference\refer\libzmq
mklink /J memcached D:\reference\refer\memcached
mklink /J leveldb D:\reference\refer\leveldb
mklink /J ace D:\reference\refer\ACE-src-6.4.6\ACE_wrappers
mklink /J brpc D:\reference\refer\brpc
mklink /J rabbitmq-server D:\reference\refer\rabbitmq-server

java -jar  D:/tools/opengrok/opengrok-1.1-rc17/lib/opengrok.jar -P -S -v -s D:/reference/opengrok_projects -d D:/tools/opengrok/opengrok-1.1-rc17/data -W D:/tools/opengrok/opengrok-1.1-rc17/data/configuration.xml
```