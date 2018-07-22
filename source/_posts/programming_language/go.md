---
title: go
date: 2017-12-1 21:47:45
categories: [编程语言]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 其他](#2-其他)

<!-- /TOC -->

# 1. 资料

* http://www.ctolib.com/cheatsheets-go-project.html (开源项目速查)
* https://tour.golang.org/welcome/1 (a tour of go)
* https://github.com/golang/go/wiki/GoGetProxyConfig (go get 使用代理)
* https://www.zhihu.com/question/20862617 (routine 实现)

# 2. 其他

关优化编译
```bash
go install  -gcflags "-N -l"
```


环境变量
```bash

cat >> ~/.profile << EOF
# go godoc gofmt
export PATH=\$PATH:/usr/local/go/bin
# custom location
export GOPATH=\$HOME/go
export PATH=\$PATH:\$GOPATH/bin
EOF
```

