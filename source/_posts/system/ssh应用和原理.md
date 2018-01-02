---
title: ssh应用和原理
date: 2017-11-25 20:50:00
categories: [系统底层]
---

<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 日常碰到的场景](#2-日常碰到的场景)
- [3. SSH简介](#3-ssh简介)
    - [3.1. SSH Transport Layer Protocol](#31-ssh-transport-layer-protocol)
        - [3.1.1. based on tcp](#311-based-on-tcp)
        - [3.1.2. Encryption](#312-encryption)
        - [3.1.3. Data Integrity](#313-data-integrity)
        - [3.1.4. Key Exchange](#314-key-exchange)
    - [3.2. User Authentication Protocol](#32-user-authentication-protocol)
    - [3.3. Connection Protocol](#33-connection-protocol)
- [4. 中间人攻击](#4-中间人攻击)
- [5. host key](#5-host-key)
- [6. SSL和SSH](#6-ssl和ssh)
- [7. TLS/SSL](#7-tlsssl)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* http://blog.csdn.net/is0501xql/article/details/8158327 (SSL协议详解)
* http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html (SSH 阮一峰)


<a id="markdown-2-日常碰到的场景" name="2-日常碰到的场景"></a>
# 2. 日常碰到的场景
* ssh登陆回话时,服务器的公钥保存在本机
* ssh登陆使用Public Key作为身份校验,私钥存在本机
* https (ssl/tls)

<a id="markdown-3-ssh简介" name="3-ssh简介"></a>
# 3. SSH简介
* https://en.wikipedia.org/wiki/Secure_Shell
* https://tools.ietf.org/html/rfc4251

Secure Shell (SSH) is a protocol for secure remote login and other secure network services over an insecure network. It consists of three major components:

* 1)Transport Layer Protocol  
provides server authentication(认证), confidentiality(保密), and integrity(完整). It may optionally also provide compression. The transport layer will typically be run over a TCP/IP connection,but might also be used on top of any other reliable data stream.
* 2)User Authentication Protocol  
authenticates the client-side user to the server. It runs over the transport layer protocol.
* 3)Connection Protocol  
multiplexes the encrypted tunnel into several logical channels. It runs over the user authentication protocol.


<a id="markdown-31-ssh-transport-layer-protocol" name="31-ssh-transport-layer-protocol"></a>
## 3.1. SSH Transport Layer Protocol
* https://tools.ietf.org/html/rfc4253

The SSH transport layer is a secure, low level transport protocol. It provides strong encryption(强加密), cryptographic host authentication(密码主机认证), and integrity protection(完整性保护).

<a id="markdown-311-based-on-tcp" name="311-based-on-tcp"></a>
### 3.1.1. based on tcp

When used over TCP/IP, the server normally listens for connections onport 22.
```
$ telnet xx.xx.xx.xx
SSH-2.0-OpenSSH_6.6.1
```

<a id="markdown-312-encryption" name="312-encryption"></a>
### 3.1.2. Encryption
`An encryption algorithm and a key will be negotiated during the key exchange.` When encryption is in effect, the packet length, padding length, payload, and padding fields of each packet MUST be encrypted with the given algorithm.

一般采用对称加密算法加密数据吧,通过key exchange协商加密算法.

算法|是否必须|描述
-|-|-
3des-cbc	|REQUIRED	|three-key 3DES in CBC mode
blowfish-cbc	|OPTIONAL	|Blowfish in CBC mode
twofish256-cbc|	OPTIONAL|	Twofish in CBC mode,with a 256-bit key
twofish-cbc	|OPTIONAL|	alias for “twofish256-cbc” (this is being retained for historical reasons)
twofish192-cbc	|OPTIONAL|	Twofish with a 192-bit key
twofish128-cbc	|OPTIONAL|	Twofish with a 128-bit key
aes256-cbc|	OPTIONAL|	AES in CBC mode,with a 256-bit key
aes192-cbc|	OPTIONAL|	AES with a 192-bit key
aes128-cbc|	RECOMMENDED	|AES with a 128-bit key
serpent256-cbc|OPTIONAL	|Serpent in CBC mode, with a 256-bit key
serpent192-cbc|	OPTIONAL|	Serpent with a 192-bit key
serpent128-cbc|	OPTIONAL	|Serpent with a 128-bit key
arcfour|OPTIONAL	|the ARCFOUR stream cipher with a 128-bit key
idea-cbc|	OPTIONAL|	IDEA in CBC mode
cast128-cbc	|OPTIONAL	|CAST-128 in CBC mode
none	|OPTIONAL|	no encryption; NOT RECOMMENDED

<a id="markdown-313-data-integrity" name="313-data-integrity"></a>
### 3.1.3. Data Integrity

消息码认证算法 消息认证码（带密钥的Hash函数）:密码学中，通信实体双方使用的一种验证机制，保证消息数据完整性的一种工具。构造方法由M.Bellare提出，安全性依赖于Hash函数，故也称带密钥的Hash函数。消息认证码是基于密钥和消息摘要所获得的一个值，`可用于数据源发认证和完整性校验`。 在发送数据之前，`发送方首先使用通信双方协商好的散列函数计算其摘要值`。在双方共享的会话密钥作用下，由摘要值获得消息验证码。之后，`它和数据一起被发送`。接收方收到报文后，首先利用会话密钥还原摘要值，同时利用散列函数在本地计算所收到数据的摘要值，并将这两个数据进行比对。若两者相等，则报文通过认证

* https://en.wikipedia.org/wiki/Message_authentication_code

The following MAC algorithms are currently defined

算法|是否必须|描述
-|-|-
hmac-sha1	|REQUIRED	|HMAC-SHA1 (digest length = key length = 20)
hmac-sha1-96	|RECOMMENDED|first 96 bits of HMAC-SHA1 (digest length = 12, key length = 20)
hmac-md5|	OPTIONAL	|HMAC-MD5 (digest length = key length = 16)
hmac-md5-96	|OPTIONAL|	first 96 bits of HMAC-MD5 (digest length = 12, key length = 16)
none|	OPTIONAL	|no MAC; NOT RECOMMENDED


<a id="markdown-314-key-exchange" name="314-key-exchange"></a>
### 3.1.4. Key Exchange
* https://en.wikipedia.org/wiki/Key_exchange
* https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange

The key exchange method specifies how one-time session keys are generated for encryption and for authentication, and how the server authentication is done.

diffie-hellman

* http://baike.baidu.com/link?url=64u53XDmXEOMBh-47ooAmv_i1AT1sB4_frG4dYMmQf0mvZgpIMLFX2_n6VZBfNbdaFb5PhulyaJ_4LkpHycXJ11Yq8CG7rvRcHQDvZXhCdxugNBW1X2VI7X7T2ILMFfn_6Qw0H98qBGVM4JMbiKiiSz127PfKMpTFdUju9zZEti

这个机制的巧妙在于需要安全通信的双方可以用这个方法确定对称密钥。然后可以用这个密钥进行加密和解密。但是注意，这个密钥交换协议/算法只能用于密钥的交换，而不能进行消息的加密和解密。双方确定要用的密钥后，要使用其他对称密钥操作加密算法实际加密和解密消息。

<a id="markdown-32-user-authentication-protocol" name="32-user-authentication-protocol"></a>
## 3.2. User Authentication Protocol
有证书和密码验证
* https://tools.ietf.org/html/rfc4252
* http://blog.chinaunix.net/uid-21854925-id-3082425.html
* http://blog.csdn.net/brandohero/article/details/8475244


<a id="markdown-33-connection-protocol" name="33-connection-protocol"></a>
## 3.3. Connection Protocol
* https://tools.ietf.org/html/rfc4254


<a id="markdown-4-中间人攻击" name="4-中间人攻击"></a>
# 4. 中间人攻击
* https://tlanyan.me/ssh-shadowsocks-prevent-man-in-middle-attack/
* https://www.zhihu.com/question/20744215

TLS的握手依赖于“公开密钥加密算法（也叫非对称算法）”：加密密钥（公钥）和解密密钥（私钥）是不同的，从公钥很难推出私钥。握手是为了双方确定一个用作加密通信的密钥（因为非对称算法很慢，所以只用来做密钥交换）。考虑一种简单的模型：客户端产生一串随机数作为密钥，使用服务器发送过来的公钥加密，再发送给服务器。服务器用对应的私钥解密。这种方式不能抵御中间人攻击，`因为你不知道服务器发来的公钥是不是真的来自服务器。这时候就需要一个可信的第三方来为服务器作证`。证书就是服务器的公钥、服务器的各种信息（比如“我是http://github.com“, 我的这个公钥最多能用到xxxx年x月x日），加上一个可信的第三方对公钥和这些信息的签名。`中间人无法伪造这个签名，也就无法替换服务器的公钥。强行替换的话，只能找另外的机构签名，或者自己给自己签名。`

自己理解: 想要抵御中间人攻击的话,只能让第三方证明了.

<a id="markdown-5-host-key" name="5-host-key"></a>
# 5. host key
存储在`known_hosts`

The server host key is used during key exchange to verify that the client is really talking to the correct server. For this to be possible, `the client must have a priori knowledge of the server's public host key.`

所以第一次使用ssh登录服务器时会提示
```
(xshell)
45.76.104.154(端口:22)的主机密钥未在本地主机密钥数据库中注册.下次若需要身份验证此主机的话必须保存主机密钥.

主机密钥指纹(MD5校验和):
ssh-rsa 2048  xxxxx
接受此主机密钥吗?
```

风险  
`The protocol provides the option that the server name - host key association is not checked when connecting to the host for the first time.` This allows communication without prior communication of host keys or certification. The connection still provides protection against passive listening; however, it becomes vulnerable to active man-in-the-middle attacks.

Implementations SHOULD try to make the best effort to check host keys. An example of a possible strategy is to only accept a host key without checking the first time a host is connected, save the key in a local database, and compare against that key on all future connections to that host.

没啥好的办法防范中间人攻击


<a id="markdown-6-ssl和ssh" name="6-ssl和ssh"></a>
# 6. SSL和SSH
* https://security.stackexchange.com/questions/1599/what-is-the-difference-between-ssl-vs-ssh-which-is-more-secure


<a id="markdown-7-tlsssl" name="7-tlsssl"></a>
# 7. TLS/SSL

* https://en.wikipedia.org/wiki/Transport_Layer_Security
* https://segmentfault.com/a/1190000000476876

The Transport Layer Security protocol aims primarily to provide privacy and data integrity between two communicating computer applications.

Once the client and server have agreed to use TLS, they negotiate a stateful connection by using a handshaking procedure.[6] `The protocols use a handshake with an asymmetric cipher to establish cipher settings and a shared key for a session`(非对称密钥加密对称密钥); the rest of the communication is encrypted using a symmetric cipher and the session key. During this handshake, the client and server agree on various parameters used to establish the connection's security:
