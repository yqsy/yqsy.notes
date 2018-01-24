---
title: relay
date: 2018-1-24 22:43:23
categories: [网络相关]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 实践](#2-实践)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://unix.stackexchange.com/questions/115897/whats-ssh-port-forwarding-and-whats-the-difference-between-ssh-local-and-remot (tcp relay)
* http://blog.csdn.net/chenjh213/article/details/49795521 (中文介绍)

<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践

```bash
# 暴露了一个端口
http://127.0.0.1:4040

# 在本机上使用ssh tunnel,即可访问
ssh -NL  9001:localhost:4040 root@pi1

-N (Do not execute remote command)
-f (Go to background)
-L (Locally forwarded ports)
-R (Remotely forwarded ports)

# 通过远程机器跳板访问其他机器
ssh -NL 9001:192.168.2.127:22 root@pi1

# 把localhost:4040 映射到 root@192.168.2.157的localhost:9001上
ssh -NR 9001:localhost:4040 root@192.168.2.157

# xxx:4040 映射到 root@192.168.2.157的localhost:9001上
ssh -NR 9001:xxx:4040 root@192.168.2.157

# 动态访问 chrome安装(switchysharp)
ssh -ND 9003 root@gg
```
