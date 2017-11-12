---
title: Ubuntu搭建开发环境
date: 2017-10-23 14:26:38
categories: [linux, 搭建环境]
---

<!-- TOC -->

- [1. 设置1080p](#1-设置1080p)
- [2. 设置清华源](#2-设置清华源)
- [3. 安装开发环境](#3-安装开发环境)

<!-- /TOC -->

<a id="markdown-1-设置1080p" name="1-设置1080p"></a>
# 1. 设置1080p
* http://blog.csdn.net/u013122625/article/details/52967831

```bash
xrandr --newmode "1920x1080_60.00" 173.00 1920 2048 2248 2576 1080 1083 1088 1120 -hsync +vsync
xrandr --addmode Virtual1 "1920x1080_60.00"
```


<a id="markdown-2-设置清华源" name="2-设置清华源"></a>
# 2. 设置清华源
* https://mirrors.tuna.tsinghua.edu.cn/help/ubuntu/

```bash
sudo cp /etc/apt/sources.list /etc/apt/sources.list.bak

# 拷贝网页的
sudo apt-get update
```

<a id="markdown-3-安装开发环境" name="3-安装开发环境"></a>
# 3. 安装开发环境
* http://1csh1.github.io/2017/06/21/ubuntu16.04-install-wiznote/ (编译说明)

```bash
sudo apt-get install openssh-server -y

# 设置root密码登录
sudo vim /etc/ssh/sshd_config
PermitRootLodin yes

sudo apt-get install vim -y
sudo apt-get install git -y
sudo apt-get install build-essential -y
sudo apt-get install cmake -y
sudo apt-get install zlib1g-dev -y

# 下载/安装qt
http://download.qt.io/official_releases/qt/5.7/5.7.0/qt-opensource-linux-x64-5.7.0.run

chmod +x qt-opensource-linux-x64-5.7.0.run
./qt-opensource-linux-x64-5.7.0.run

# 设置git代理
git config --global http.proxy 'socks5://192.168.2.106:1080' 
git config --global https.proxy 'socks5://192.168.2.106:1080'

# 下载wiz前台代码
cd ~
mkdir WizTeam
cd WizTeam
git clone https://github.com/WizTeam/WizQTClient.git
cd WizQTClient
git checkout v2.5.1

# 缺少的库
sudo apt-get install libgl1-mesa-dev libglu1-mesa-dev -y

# 使用qtcreater打开cmake进行编译吧

# pyqt
sudo apt install python3-pip -y

# setting to qinghua resource
https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

pip3 install pyqt5
```
