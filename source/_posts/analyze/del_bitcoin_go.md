---
title: del_bitcoin_go
date: 2018-09-07 14:58:35
categories: [项目分析]
---



<!-- TOC -->

- [1. 说明](#1-说明)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* https://github.com/btcsuite/btcd (go实现)
* https://github.com/btcsuite/btcd/blob/master/docs/README.md (go实现文档)


```bash

go get -u github.com/Masterminds/glide
git clone https://github.com/btcsuite/btcd $GOPATH/src/github.com/btcsuite/btcd
cd $GOPATH/src/github.com/btcsuite/btcd
glide install
go install . ./cmd/...
```

源码
```bash
.                    133353 
./blockchain         20064 
./txscript           17953 
./wire               17163 
./database           12548 
./btcjson            12190 
./rpcclient          8227 
./btcec              6778 
./mempool            4430 
./peer               4158 
./integration        3707 
./addrmgr            2356 
./chaincfg           2259 
./mining             2077 
./cmd                1802 
./connmgr            1697 
./netsync            1632 
./limits             72 
```
