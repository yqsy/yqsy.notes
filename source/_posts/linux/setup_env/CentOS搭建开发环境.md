---
title: CentOS搭建开发环境
date: 2017-10-23 14:26:38
categories: [linux, 搭建环境]
---

<!-- TOC -->

- [1. iso版本](#1-iso版本)
- [2. 设置网络](#2-设置网络)
- [3. 设置证书](#3-设置证书)
- [4. 设置清华源](#4-设置清华源)
- [5. 安装开发环境](#5-安装开发环境)

<!-- /TOC -->

<a id="markdown-1-iso版本" name="1-iso版本"></a>
# 1. iso版本
安装的是`CentOS-7-x86_64-Minimal-1611.iso`

<a id="markdown-2-设置网络" name="2-设置网络"></a>
# 2. 设置网络
```bash
sudo sed -i "s/ONBOOT=no/ONBOOT=yes/g" /etc/sysconfig/network-scripts/ifcfg-ens33
sudo systemctl restart network
```

<a id="markdown-3-设置证书" name="3-设置证书"></a>
# 3. 设置证书
```bash
# 好像国内默认会选择163的了?
sudo yum install wget -y 

wget https://raw.githubusercontent.com/yqsy/linux_script/master/id_rsa.pub

mkdir /root/.ssh
chmod 700 /root/.ssh
touch ~/.ssh/authorized_keys
chmod 600 ~/.ssh/authorized_keys
cat id_rsa.pub >>  ~/.ssh/authorized_keys
systemctl restart sshd
```

<a id="markdown-4-设置清华源" name="4-设置清华源"></a>
# 4. 设置清华源
* https://mirrors.tuna.tsinghua.edu.cn/help/centos/

```bash
# 备份
sudo mv /etc/yum.repos.d/CentOS-Base.repo /etc/yum.repos.d/CentOS-Base.repo.bak

# 拷贝网页的

# 更新缓存
sudo sudo yum makecache
```


<a id="markdown-5-安装开发环境" name="5-安装开发环境"></a>
# 5. 安装开发环境

```bash
sudo yum update -y
sudo yum install vim -y
sudo yum install net-tools -y
sudo yum -y groups install "GNOME Desktop" 

echo "exec gnome-session" >> ~/.xinitrc
# 启动GNOME
startx

# 安装python3.5.3
sudo yum groupinstall 'Development Tools' -y
sudo yum install zlib-devel bzip2-devel openssl-devel ncurese-devel -y

wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tgz
tar -xvzf Python-3.5.3.tgz
cd Python-3.5.3
./configure --enable-shared --enable-optimizations
make
sudo make install

# 添加环境变量(启动python需要)
echo 'LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH' >> ~/.bashrc

# cgdb
sudo yum install ncurses-devel ncurses -y
sudo yum install texinfo -y
sudo yum install readline-devel -y

wget https://cgdb.me/files/cgdb-0.7.0.tar.gz
tar -xvzf cgdb-0.7.0.tar.gz
cd cgdb-0.7.0
./configure --prefix=/usr/local
make
sudo make install

# 安装pyqt5
pip3 install pyqt5

git clone git@gitlab.com:yqsy021/spx_client_test.git
```
