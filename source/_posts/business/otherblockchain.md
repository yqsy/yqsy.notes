---
title: otherblockchain
date: 2018-08-26 21:43:47
categories: [business]
---


<!-- TOC -->

- [1. 星云链](#1-星云链)
- [2. tendermint](#2-tendermint)
- [3. rsk (根链)](#3-rsk-根链)
    - [3.1. 测试](#31-测试)

<!-- /TOC -->

<a id="markdown-1-星云链" name="1-星云链"></a>
# 1. 星云链

* https://nano.nebulas.io/h5/index_h5.html (手机钱包)

<a id="markdown-2-tendermint" name="2-tendermint"></a>
# 2. tendermint

* https://tendermint.com/docs/tendermint.pdf (白皮书))

<a id="markdown-3-rsk-根链" name="3-rsk-根链"></a>
# 3. rsk (根链)

* https://github.com/rsksmart/rskj (源码)
* https://github.com/rsksmart/artifacts/tree/master/Dockerfiles/RSK-Node (docker的readme)
* https://github.com/rsksmart/rskj/wiki (wiki)

docker搭建
```bash
cd /mnt/disk1/linux/reference/refer

git clone https://github.com/rsksmart/artifacts
cd artifacts/Dockerfiles/RSK-Node

docker build -t testnet -f Dockerfile.TestNet .
docker run -d --name testnet-node-01  -p 4444:4444 -p 50505:50505 testnet

```

<a id="markdown-31-测试" name="31-测试"></a>
## 3.1. 测试

简单部署到本地
```bash
truffle init

truffle develop

create contract SimpleStorage

touch ./migrations/2_simple_storage.js

# 输入部署脚本
var SimpleStorage = artifacts.require("./SimpleStorage.sol");

module.exports = function(deployer) {
  deployer.deploy(SimpleStorage);
};

# 编译
compile

# 部署
migrate

# 获取实例
var simpleStorage
SimpleStorage.deployed().then(instance => simpleStorage = instance)

# 调用get接口
simpleStorage.get()

# 转Number
simpleStorage.get().then(bn => bn.toNumber())

# 修改
simpleStorage.set(10)

# 再查看
simpleStorage.get().then(bn => bn.toNumber())

```

部署到rsk测试网络,修改truffle.js文件

```js
var HDWalletProvider = require('truffle-hdwallet-provider')

var mnemonic = ''
var publicNode = 'https://public-node.testnet.rsk.co:443'

module.exports = {
  networks: {
    rsk: {
      provider: () =>
        new HDWalletProvider(mnemonic, publicNode),
      network_id: '*',
      gas: 2500000,
      gasPrice: 183000
    }
  }
}
```

```bash
npm install truffle-hdwallet-provider --save

# truffle develop

# 连接到测试网络
truffle console --network rsk

# 获取区块链高度
web3.eth.getBlockNumber((err, res) => console.log(res))

# 钱包
web3.currentProvider.wallets

# 账户
var account = Object.keys(web3.currentProvider.wallets)[0]

# 获取余额
web3.eth.getBalance(account, (err, res) => console.log(res.toNumber()))

# 编译
compile

# 提交
migrate --reset

# 0xc8d7b165a93c7124758729bea93d4c30e0e7c52a (合约地址)

SimpleStorage.deployed().then(instance => contract = instance)

contract.set(1)

contract.get()
```
