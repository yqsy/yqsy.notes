---
title: go
date: 2017-12-1 21:47:45
categories: [编程语言]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 其他](#2-其他)
- [3. 错误处理](#3-错误处理)
- [4. 对于json,bencode如何处理](#4-对于jsonbencode如何处理)
- [5. call graph](#5-call-graph)
- [6. 小知识点](#6-小知识点)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* http://www.ctolib.com/cheatsheets-go-project.html (开源项目速查)
* https://tour.golang.org/welcome/1 (a tour of go)
* https://github.com/golang/go/wiki/GoGetProxyConfig (go get 使用代理)
* https://www.zhihu.com/question/20862617 (routine 实现)

<a id="markdown-2-其他" name="2-其他"></a>
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

<a id="markdown-3-错误处理" name="3-错误处理"></a>
# 3. 错误处理


```
外部输入错误,   1. object无key 2. 类型不对    捕获panic  ??   (范围,数值类型其他判断普通error) ??? 不能捕获的,这是runtime-error!!!
https://blog.golang.org/defer-panic-and-recover

内部处理错误, return error

重要错误,无法挽救 panic
```


<a id="markdown-4-对于jsonbencode如何处理" name="4-对于jsonbencode如何处理"></a>
# 4. 对于json,bencode如何处理

像go这样的静态语言

1. 反射到类型 (标准库)  像bencode,缺点是要实现MarshalBinary, UnmarshalBinary
2. 包一层object来给接口调用 (默认值)  https://github.com/buger/jsonparser
3. 解析到内置类型,并提供检查接口 1. 类型 2. key

像动态语言一样搞不行,大量重复的劳动???可以弄成nodejs那样的检查方式
1. interface{} 类型判断
2. object key 判断


<a id="markdown-5-call-graph" name="5-call-graph"></a>
# 5. call graph

* https://github.com/TrueFurby/go-callvis

```bash
go get -u github.com/TrueFurby/go-callvis
cd $GOPATH/src/github.com/TrueFurby/go-callvis && make

go-callvis github.com/anacrolix/torrent/cmd/torrent
http://localhost:7878/ 
```

不是很理想,还是用goland的吧!

<a id="markdown-6-小知识点" name="6-小知识点"></a>
# 6. 小知识点

```
解析DNS: net.LookupHost 是对协程友好的
```
