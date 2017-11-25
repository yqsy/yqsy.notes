---
title: 搭建ss资料
date: 2017-11-04 15:21:38
categories: [coding]
---

<!-- TOC -->

- [1. ss-libev / kcptun](#1-ss-libev--kcptun)
    - [1.1. 客户端](#11-客户端)
    - [1.2. 各个ss版本的差异](#12-各个ss版本的差异)
- [2. google-bbr](#2-google-bbr)
- [3. openwrt](#3-openwrt)

<!-- /TOC -->

<a id="markdown-1-ss-libev--kcptun" name="1-ss-libev--kcptun"></a>
# 1. ss-libev / kcptun
* https://teddysun.com/ (秋水逸冰)
* https://story.tonylee.name/2016/03/31/yong-shu-mei-pai-da-zao-wu-xian-zhong-ji-ke-xue-shang-wang-lu-you-qi/ (树莓派中继redsocket)
* https://blog.chionlab.moe/2016/01/27/use-haproxy-to-optimize-shadowsocks-on-openwrt/ (haproxy负载均衡)
* https://blog.chionlab.moe/2016/01/27/optimize-shadowsocks-on-openwrt/ (openwrt优化)
* https://www.zhihu.com/question/32229915?from=profile_question_card (无污染dns)
* https://github.com/yqsy/linux_script (我自己的搭建过程mt)

<a id="markdown-11-客户端" name="11-客户端"></a>
## 1.1. 客户端
* https://github.com/xtaci/kcptun/releases
* https://github.com/dfdragon/kcptun_gclient/releases
* https://github.com/shadowsocks/shadowsocks-windows/releases
* https://shadowsocks.org/en/download/clients.html


<a id="markdown-12-各个ss版本的差异" name="12-各个ss版本的差异"></a>
## 1.2. 各个ss版本的差异
* https://github.com/shadowsocks/shadowsocks/wiki/Feature-Comparison-across-Different-Versions


<a id="markdown-2-google-bbr" name="2-google-bbr"></a>
# 2. google-bbr
```bash
wget --no-check-certificate https://raw.githubusercontent.com/teddysun/across/master/bbr.sh
chmod +x bbr.sh
./bbr.sh
```

查看是否开启
```
sysctl net.ipv4.tcp_available_congestion_control
sysctl net.ipv4.tcp_congestion_control
sysctl net.core.default_qdisc
lsmod | grep bbr
```

源码
* https://github.com/google/bbr

<a id="markdown-3-openwrt" name="3-openwrt"></a>
# 3. openwrt
* https://wiki.openwrt.org/toh/hwdata/netgear/netgear_wndr4300_v1
* https://github.com/shadowsocks/openwrt-shadowsocks/releases
* https://github.com/shadowsocks/luci-app-shadowsocks/releases
* http://sourceforge.net/projects/openwrt-dist/files/chinadns/
* http://sourceforge.net/projects/openwrt-dist/files/luci-app/chinadns/
* https://github.com/aa65535/openwrt-dns-forwarder/releases
* https://github.com/aa65535/openwrt-dist-luci/releases
* https://github.com/xtaci/kcptun/releases