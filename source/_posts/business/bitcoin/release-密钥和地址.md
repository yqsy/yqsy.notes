---
title: 密钥和地址
date: 2018-02-01 13:29:12
categories: [business, bitcoin]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. libbitcoin梳理P2PKH地址的关系](#2-libbitcoin梳理p2pkh地址的关系)
- [3. libbitcoin梳理P2SH地址的关系](#3-libbitcoin梳理p2sh地址的关系)
- [4. BIP38 私钥加密](#4-bip38-私钥加密)
- [5. 参考资料](#5-参考资料)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

比特币的转账是基于密码学的,借助于`unspent transaction output (UTXO)`(未花费输出),`Secp256k1 with ECDSA`(椭圆曲线数字签名)等技术,完成了货币的支付职能.类比于传统中心化系统的`帐号,密码,账户+密码验证->转账`,在比特币中变成了`公钥,私钥,私钥签名+公钥认证->转账`.本文简单讲述一下,私钥,公钥,公钥哈系,钱包地址之间的关系,并提供shell指令以供方便使用.

关系:  
![](./pic/relation.png)

流程图:  
![](./pic/address-generation-extra.png)

(图片来源: 互联网)

![](https://en.bitcoin.it/w/images/en/4/48/Address_map.jpg)

(图片来源: https://en.bitcoin.it/wiki/Address)

<a id="markdown-2-libbitcoin梳理p2pkh地址的关系" name="2-libbitcoin梳理p2pkh地址的关系"></a>
# 2. libbitcoin梳理P2PKH地址的关系
安装libbitcoin-explorer:
```bash
wget https://github.com/libbitcoin/libbitcoin-explorer/releases/download/v3.2.0/bx-linux-x64-qrcode
sudo mv bx-linux-x64-qrcode /usr/local/bin/bx
chmod +x /usr/local/bin/bx
```

提供以下shell脚本方便日常使用:  

* parse_privkey 解析私钥
* parse_privkeywif 解析私钥wif
* parse_pubkey_uncompressed 解析未压缩公钥
* parse_pubkey_compressed 解析压缩公钥
* parse_pubkeyhash 公钥哈系 -> 钱包地址
* parse_address  钱包地址 -> 公钥哈系

```bash
# 私钥 -> 公钥 -> 公钥哈系 -> 钱包地址:
parse_privkey() {
    PRIKEY=$1
    PRIKEY_WIF_UNCOMPRESSED=`bx ec-to-wif -u $PRIKEY`
    PUBKEY_UNCOMPRESSED=`bx wif-to-public $PRIKEY_WIF_UNCOMPRESSED`
    PUBKEYHASH_UNCOMPRESSED=`bx sha256 $PUBKEY_UNCOMPRESSED | bx ripemd160`
    P2PKHADDRESS_UNCOMPRESSED=`bx address-encode -v 0 $PUBKEYHASH_UNCOMPRESSED`
    URI_UNCOMPRESSED=`bx uri-encode $P2PKHADDRESS_UNCOMPRESSED`
    QRCODE_UNCOMPRESSED=`bx qrcode -p $P2PKHADDRESS_UNCOMPRESSED`

    echo "[未压缩]" &&
    echo 私钥: $PRIKEY &&
    echo 私钥WIF: $PRIKEY_WIF_UNCOMPRESSED &&
    echo 公钥: $PUBKEY_UNCOMPRESSED &&
    echo 公钥hash: $PUBKEYHASH_UNCOMPRESSED &&
    echo P2PKH地址: $P2PKHADDRESS_UNCOMPRESSED &&
    echo URI: $URI_UNCOMPRESSED 

    echo $QRCODE_UNCOMPRESSED > /tmp/uncompressed.png

    PRIKEY_WIF_COMPRESSED=`bx ec-to-wif $PRIKEY`
    PUBKEY_COMPRESSED=`bx wif-to-public $PRIKEY_WIF_COMPRESSED`
    PUBKEYHASH_COMPRESSED=`bx sha256 $PUBKEY_COMPRESSED | bx ripemd160`
    P2PKHADDRESS_COMPRESSED=`bx address-encode -v 0 $PUBKEYHASH_COMPRESSED`
    URI_COMPRESSED=`bx uri-encode $P2PKHADDRESS_COMPRESSED`
    QRCODE_COMPRESSED=`bx qrcode -p $P2PKHADDRESS_COMPRESSED`

    echo "[压缩]" &&
    echo 私钥: $PRIKEY &&
    echo 私钥WIF: $PRIKEY_WIF_COMPRESSED &&
    echo 公钥: $PUBKEY_COMPRESSED &&
    echo 公钥hash: $PUBKEYHASH_COMPRESSED &&
    echo P2PKH地址: $P2PKHADDRESS_COMPRESSED &&
    echo URI: $URI_COMPRESSED 

    echo $QRCODE_COMPRESSED > /tmp/compressed.png
} 

# 私钥wif -> 私钥 -> 公钥 -> 公钥哈系 -> 钱包地址:
parse_privkeywif() {
    PRIKEYWIF=$1
    parse_privkey `bx wif-to-ec $PRIKEYWIF`
}

# 公钥[未压缩] -> 公钥哈系 -> 钱包地址
parse_pubkey_uncompressed() {
    PUBKEY_UNCOMPRESSED=$1
    PUBKEYHASH_UNCOMPRESSED=`bx sha256 $PUBKEY_UNCOMPRESSED | bx ripemd160`
    P2PKHADDRESS_UNCOMPRESSED=`bx address-encode -v 0 $PUBKEYHASH_UNCOMPRESSED`
    URI_UNCOMPRESSED=`bx uri-encode $P2PKHADDRESS_UNCOMPRESSED`
    echo "[未压缩]" &&
    echo 公钥: $PUBKEY_UNCOMPRESSED &&
    echo 公钥hash: $PUBKEYHASH_UNCOMPRESSED &&
    echo P2PKH地址: $P2PKHADDRESS_UNCOMPRESSED &&
    echo URI: $URI_UNCOMPRESSED 
}

# 公钥[压缩] -> 公钥哈系 -> 钱包地址
parse_pubkey_compressed() {
    PUBKEY_COMPRESSED=$1
    PUBKEYHASH_COMPRESSED=`bx sha256 $PUBKEY_COMPRESSED | bx ripemd160`
    P2PKHADDRESS_COMPRESSED=`bx address-encode -v 0 $PUBKEYHASH_COMPRESSED`
    URI_COMPRESSED=`bx uri-encode $P2PKHADDRESS_COMPRESSED`
    echo "[压缩]" &&
    echo 公钥: $PUBKEY_COMPRESSED &&
    echo 公钥hash: $PUBKEYHASH_COMPRESSED &&
    echo P2PKH地址: $P2PKHADDRESS_COMPRESSED &&
    echo URI: $URI_COMPRESSED 
}

# 公钥哈系 -> 钱包地址
parse_pubkeyhash() {
    PUBKEYHASH=$1
    P2PKHADDRESS=`bx address-encode -v 0 $PUBKEYHASH`
    URI=`bx uri-encode $P2PKHADDRESS`
    echo 公钥hash: $PUBKEYHASH &&
    echo P2PKH地址: $P2PKHADDRESS &&
    echo URI: $URI 
}

# 钱包地址 -> 公钥哈系
parse_address() {
    P2PKHADDRESS=$1
    PUBKEYHASH=`bx address-decode  $P2PKHADDRESS`
    URI=`bx uri-encode $P2PKHADDRESS`
    echo 公钥hash: $PUBKEYHASH &&
    echo P2PKH地址: $P2PKHADDRESS &&
    echo URI: $URI 
}

# 创建新私钥
parse_privkey `bx seed | bx ec-new`
```

<a id="markdown-3-libbitcoin梳理p2sh地址的关系" name="3-libbitcoin梳理p2sh地址的关系"></a>
# 3. libbitcoin梳理P2SH地址的关系

```bash
echo "dup hash160 [e0a9980de27a65fc49069fce46fefbff9d6990ce] equalverify checksig" |  bx script-encode  | bx sha256 | bx ripemd160 | bx base58check-encode --version 5
```

<a id="markdown-4-bip38-私钥加密" name="4-bip38-私钥加密"></a>
# 4. BIP38 私钥加密

上文直接下载的bx二进制在这里失去了作用,所以我们要从源码编译bx,加上开启`icu`的选项
```bash
wget https://raw.githubusercontent.com/libbitcoin/libbitcoin-explorer/version3/install.sh

mkdir /home/yq/libbitcoin-build
chmod +x install.sh
./install.sh --with-icu --with-png --with-qrencode --build-icu --build-zlib --build-png --build-qrencode --build-boost --build-zmq --prefix=/home/yq/libbitcoin-build

# 把之前的删除
sudo rm -rf /usr/local/bin/bx

# 环境变量添加
cat >> ~/.profile << EOF
# bx
export PATH=/home/yq/libbitcoin-build/bin:\$PATH
EOF
```

```bash
# 私钥,对称密钥 -> 加密私钥
encryptkey() {
    PRIKEY=$1
    PASSPHRASE=$2
    bx ec-to-ek $PASSPHRASE $PRIKEY
}

# 加密私钥,对称密钥 -> 私钥
decryptkey() {
    ENCRYPTED_PRIKEY=$1
    PASSPHRASE=$2
    bx ek-to-ec $PASSPHRASE $ENCRYPTED_PRIKEY
}

# 实验
encryptkey 1801f9286f5a71eb77534f26804b37a24abe54ea3dc0933a3568e89076dd9d4d abc123456

decryptkey 6PYWxXWVyd4xBdcgSEpcXL378fg49FnvSmgbQZwr8EEKKKng62qwVBzawd abc123456
```

<a id="markdown-5-参考资料" name="5-参考资料"></a>
# 5. 参考资料

上文命令行参考:  

* https://github.com/libbitcoin/libbitcoin-explorer (libbitcoin-explorer)
* https://github.com/libbitcoin/libbitcoin-explorer/wiki/Wallet-Commands (libbitcoin-explorer command)

地址生成工具:  

* https://www.bitaddress.org/ (web地址生成)

原理解释:  

* https://en.bitcoin.it/wiki/Wallet_import_format (私钥->wif, wif->私钥)
* https://en.bitcoin.it/wiki/Technical_background_of_version_1_Bitcoin_addresses (生成比特币地址)

便捷查询:  

* https://en.bitcoin.it/wiki/List_of_address_prefixes (prefix)

书籍参考:  

* http://book.8btc.com/books/6/masterbitcoin2cn/_book/ch04.html (精通比特币第四章)
