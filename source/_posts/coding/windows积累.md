---
title: windows积累
date: 2017-11-06 15:20:00
categories: [coding]
---

<!-- TOC -->

- [1. 常用](#1-常用)
- [2. 穿墙应用](#2-穿墙应用)

<!-- /TOC -->


<a id="markdown-1-常用" name="1-常用"></a>
# 1. 常用

```bash
# telnet安装
pkgmgr /iu:"TelnetClient"

# 刷新dns
ipconfig /flushdns

# 注册/卸载DLL
Regsvr32 /S VA_X.dll
Regsvr32 /S /U VA_X.dll

# 查看静态库
dumpbin.exe -headers glog.lib > export.txt

# 新装网卡驱动时,注意安装官方原版
realtek

# dig
https://www.isc.org/downloads/

# 远程连接
mstsc

# 查看屏幕尺寸
dxdiag

# mstsc full screen on second monitor
http://www.fixedbyvonnie.com/2013/12/how-to-open-full-screen-remote-desktop-session-secondary-monitor-in-windows/#.WUi7XeuGOHs
```

<a id="markdown-2-穿墙应用" name="2-穿墙应用"></a>
# 2. 穿墙应用

```bash
# git(只能代理https,ssh的无效)
git config --global http.proxy 'socks5://127.0.0.1:1080' 
git config --global https.proxy 'socks5://127.0.0.1:1080'

# pip
vim C:\Users\Gong.guochun\pip\pip.ini

[global]
proxy = 127.0.0.1:1080

# atom
apm config set proxy "http://127.0.0.1:1080"
apm config set https_proxy "http://127.0.0.1:1080"

# go get
env `https_proxy` http://127.0.0.1:1080
```
