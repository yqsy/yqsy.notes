---
title: samba
date: 2018-02-01 13:29:12
categories: [linux, 搭建环境]
---


<!-- TOC -->

- [1. 资源](#1-资源)
- [2. 安装](#2-安装)

<!-- /TOC -->

<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源
* https://www.howtoforge.com/samba-server-installation-and-configuration-on-centos-7
* https://serverfault.com/questions/368340/how-to-configure-samba-to-allow-root-user-for-full-control-to-the-particular-sha (allow root)

<a id="markdown-2-安装" name="2-安装"></a>
# 2. 安装

```bash
yum install samba samba-client samba-common -y
mv /etc/samba/smb.conf /etc/samba/smb.conf.bak

echo "
[vm1]
    comment = Admin Config Share  - Whatever
    path = /
    valid users = srijan
    force user = root
    force group = root
    # invalid users = xxx
    # admin users = xxx
    writeable = Yes
" > /etc/samba/smb.conf

# mkdir -p /samba/anonymous
systemctl enable smb.service
systemctl enable nmb.service
systemctl restart smb.service
systemctl restart nmb.service

groupadd smbgrp
useradd srijan -G smbgrp
smbpasswd -a srijan

# mkdir -p /samba/secured
# chmod -R 0777 /samba/secured

systemctl restart smb.service
systemctl restart nmb.service

# windows:
# 清空会话
net use * /del /y
```
