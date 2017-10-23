---
title: centos搭建pyqt开发环境
date: 2017-10-23 14:26:38
categories: [linux]
---

<!-- TOC -->

- [1. iso版本](#1-iso版本)
- [2. 设置网络](#2-设置网络)
- [3. 设置清华源](#3-设置清华源)
- [4. 安装开发环境](#4-安装开发环境)

<!-- /TOC -->

# 1. iso版本
安装的是`CentOS-7-x86_64-Minimal-1611.iso`

# 2. 设置网络
```bash
sudo sed -i "s/ONBOOT=no/ONBOOT=yes/g" /etc/sysconfig/network-scripts/ifcfg-ens33
sudo systemctl restart network
```

# 3. 设置清华源
* https://mirrors.tuna.tsinghua.edu.cn/help/centos/

```bash
# 备份
sudo mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak

# 拷贝网页的

# 更新缓存
sudo yum makecache
```


# 4. 安装开发环境
```bash
sudo yum update -y
sudo yum install vim -y
yum -y groups install "GNOME Desktop" 

echo "exec gnome-session" >> ~/.xinitrc
# 启动GNOME
startx

# 安装python3.5.3
yum groupinstall 'Development Tools' -y
yum install zlib-devel bzip2-devel openssl-devel ncurese-devel -y

wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tgz
tar -xvzf Python-3.5.3.tgz
cd Python-3.5.3
./configure --enable-shared --enable-optimizations
make
sudo make install

# 添加环境变量(启动python需要)
echo 'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH' >> ~/.bashrc

# 安装pyqt5
pip3 install pyqt5

git clone git@gitlab.com:yqsy021/spx_client_test.git
```
