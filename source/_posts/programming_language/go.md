---
title: go
date: 2017-12-1 21:47:45
categories: [编程语言]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 设置环境变量](#2-设置环境变量)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* http://www.ctolib.com/cheatsheets-go-project.html (开源项目速查)
* https://tour.golang.org/welcome/1 (a tour of go)
* https://github.com/golang/go/wiki/GoGetProxyConfig (go get 使用代理)


<a id="markdown-2-设置环境变量" name="2-设置环境变量"></a>
# 2. 设置环境变量

```bash
cat >> ~/.zshrc << EOF
export GOPATH=\$HOME/go
export PATH=\$PATH:\$GOROOT/bin:$GOPATH/bin
EOF
```
