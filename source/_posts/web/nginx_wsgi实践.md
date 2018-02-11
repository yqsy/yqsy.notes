---
title: Django
date: 2018-2-4 11:21:21
categories: [web]
---


<!-- TOC -->

- [1. 实践](#1-实践)
- [2. https实践](#2-https实践)
- [3. docker-https proxy实践](#3-docker-https-proxy实践)

<!-- /TOC -->


<a id="markdown-1-实践" name="1-实践"></a>
# 1. 实践

wsgi_server.py
```bash
from wsgiref.simple_server import make_server
from webapp import application

httpd = make_server('', 8000, application)

httpd.serve_forever()
```

webapp.py
```bash
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']
```

nginx.conf
```bash
user root;

worker_processes 4; # 进程数

worker_rlimit_nofile 65535;  # 最大可打开文件数量

events {
    worker_connections 768; # 允许的最大连接数

}

http {

    sendfile on;
    client_header_buffer_size 32k;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    access_log /var/log/nginx/access.log;
    error_log /var/log/nginx/error.log;

    server {
        listen 80;

        root /usr/share/nginx/html;
        index index.html index.htm;
        server_name _;

        location /usr/ {
            proxy_pass http://127.0.0.1:8000;
        }

        error_page 404 /404.html;
    }
}
```

https
```bash
    server {
        listen 443 ssl;
        keepalive_timeout   70;
        
        ssl_protocols       TLSv1 TLSv1.1 TLSv1.2;
        ssl_ciphers         AES128-SHA:AES256-SHA:RC4-SHA:DES-CBC3-SHA:RC4-MD5;

        server_name _;
        ssl_certificate /etc/nginx/fullchain.pem;
        ssl_certificate_key /etc/nginx/privkey.pem;
        
        ssl_session_cache   shared:SSL:10m;
        ssl_session_timeout 10m;
        
        location / {
            proxy_pass http://127.0.0.1:8000;
            #root   /usr/share/nginx/html;
        }
    }
```


```bash

yum install nginx -y
mv /etc/nginx/nginx.conf /etc/nginx/nginx.conf.bak
touch /etc/nginx/nginx.conf

# 全局配置:/etc/nginx/nginx.conf
# 访问日志:/var/log/nginx/access.log
# 错误日志: /var/log/nginx/error.log
# 站点配置: /etc/nginx/sites-enabled/default

python3 wsgi_server.py

```

<a id="markdown-2-https实践" name="2-https实践"></a>
# 2. https实践

书上看到的,貌似有点问题?浏览器不识别?
```bash
yum install openssl -y
yum install openssl-devel -y

# 生成CA密钥
openssl genrsa -out ca.key 2048

# 生成CA证书 (common要输入domain和具体的ip地址)
openssl req -x509 -new -nodes -key ca.key -days 365 -out ca.crt

# 生成服务器证书RSA的密钥对
openssl genrsa -out server.key 2048

# 生成服务端证书CSR
openssl req -new -key server.key -out server.csr

# 生成服务器端证书 ca.crt
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 365

cp server.crt /etc/nginx/server.crt
cp server.key /etc/nginx/server.key
```

再来,参考https://github.com/greyltc/docker-LAMP/blob/master/setupApacheSSLKey.sh (owncloud的)
```bash
openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -out ./privkey.pem

openssl req -new -key ./privkey.pem -out ./server.csr -subj /C=US/ST=CA/L=CITY/O=ORGANIZATION/OU=UNIT/CN=localhost

openssl x509 -req -days 3650 -in ./server.csr -signkey ./privkey.pem -out ./fullchain.pem

cp fullchain.pem /etc/nginx/fullchain.pem
cp privkey.pem /etc/nginx/privkey.pem
```

https权威指南指令
```bash
# 生成rsa密钥


```

certbot实践,参考:https://certbot.eff.org/all-instructions/#centos-rhel-7-nginx
```

wget https://dl.eff.org/certbot-auto
chmod a+x ./certbot-auto
./certbot-auto
```

<a id="markdown-3-docker-https-proxy实践" name="3-docker-https-proxy实践"></a>
# 3. docker-https proxy实践

```bash
docker pull jwilder/nginx-proxy:latest
docker pull jwilder/whoami

docker-compose up -d 

# -d                         Detached mode: Run containers in the background,
#                            print new container names.

dbash httpsproxy_nginx-proxy_1

```
