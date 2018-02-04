---
title: https
date: 2017-11-28 22:44:46
categories: [微服务]
---



<!-- TOC -->

- [1. 资源](#1-资源)
- [2. docker示例](#2-docker示例)
- [3. 免费签名](#3-免费签名)
- [4. 梳理](#4-梳理)
- [5. 所有文件后缀的含义](#5-所有文件后缀的含义)

<!-- /TOC -->


<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源

* https://en.wikipedia.org/wiki/HTTPS (wiki)
* http://www.ituring.com.cn/book/1734 (HTTPS权威指南)
* https://www.zhihu.com/question/21518760/answer/19698894 (解释的很生动) 
* https://www.nginx.com/resources/wiki/start/topics/examples/SSL-Offloader/ (nginx 配置)
* http://nginx.org/en/docs/http/configuring_https_servers.html (nginx如何配置)
* https://developers.google.com/web/fundamentals/security/encrypt-in-transit/enable-https (说明)
* https://www.nginx.com/blog/nginx-https-101-ssl-basics-getting-started/ (https入门)
* http://nginx.org/en/docs/http/ngx_http_ssl_module.html (nginx官方文档配置)
* https://certbot.eff.org/ (这个好像可以直接生成证书)
* https://segmentfault.com/a/1190000005797776 (cerbot快速入门)
* https://hub.docker.com/r/certbot/certbot/ (docker)

<a id="markdown-2-docker示例" name="2-docker示例"></a>
# 2. docker示例

* https://github.com/jwilder/nginx-proxy (默认只EXPOSE80端口,需要反向443)
* https://github.com/JrCs/docker-letsencrypt-nginx-proxy-companion
* https://github.com/fatk/docker-letsencrypt-nginx-proxy-companion-examples
* https://github.com/SteveLTN/https-portal (就是这个了)
* https://hub.docker.com/r/steveltn/https-portal/ (同上docker hub的)

<a id="markdown-3-免费签名" name="3-免费签名"></a>
# 3. 免费签名

* https://letsencrypt.org/
* https://bruceking.site/2017/07/12/how-letsencrypt-works/ (letsencrypt原理)

<a id="markdown-4-梳理" name="4-梳理"></a>
# 4. 梳理
> Web browsers know how to trust HTTPS websites based on certificate authorities that come pre-installed in their software. Certificate authorities (such as Symantec, Comodo, GoDaddy, GlobalSign and Let's Encrypt) are in this way being trusted by web browser creators to provide valid certificates. 


<a id="markdown-5-所有文件后缀的含义" name="5-所有文件后缀的含义"></a>
# 5. 所有文件后缀的含义

* https://www.zhihu.com/question/29620953 

* X.509 DER 编码(ASCII)的后缀是： .DER .CER .CRT
* X.509 PAM 编码(Base64)的后缀是： .PEM(也可能是key) .CER .CRT
* 私钥：.key
* 证书请求：.csr

