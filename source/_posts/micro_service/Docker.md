---
title: Docker
date: 2018-01-03 13:29:51
categories: [微服务]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 安装](#2-安装)

<!-- /TOC -->


<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://hujb2000.gitbooks.io/docker-flow-evolution/content/cn/index.html (Docker入门与实战)
* https://docs.docker.com/engine/getstarted/ (官方文档)
* http://www.docker.org.cn/book/docker/what-is-docker-16.html (docker中文社区)
* https://stackoverflow.com/questions/30494050/how-do-i-pass-environment-variables-to-docker-containers (传递环境变量给docker)
* https://docs.docker.com/engine/admin/volumes/volumes/ (manager data in docker)


<a id="markdown-2-安装" name="2-安装"></a>
# 2. 安装

* https://mirrors.tuna.tsinghua.edu.cn/help/docker-ce/ (到这里安装?清华源?不对)
* https://www.docker-cn.com/registry-mirror (中国官方的源)


```bash
# 改变源

mkdir -p /etc/docker
echo \
"{
  \"registry-mirrors\": [\"https://registry.docker-cn.com\"]
}" > /etc/docker/daemon.json
```

```bash
yum install docker -y
systemctl start docker
systemctl enable docker

systemctl status docker
```

