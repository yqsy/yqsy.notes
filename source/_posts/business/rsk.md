---
title: rsk
date: 2018-09-06 10:33:42
categories: [business]
---

<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 双向锚定的问题](#2-双向锚定的问题)
- [3. docker搭建](#3-docker搭建)
- [4. 简单测试](#4-简单测试)
- [5. 部署到实际测试网络](#5-部署到实际测试网络)
- [6. 其他指令](#6-其他指令)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* https://github.com/rsksmart/rskj (源码)
* https://github.com/rsksmart/artifacts/tree/master/Dockerfiles/RSK-Node (docker的readme)
* https://github.com/rsksmart/rskj/wiki (wiki)


部署节点   
* https://github.com/rsksmart/rskj/wiki/Install-RskJ-and-join-the-RSK-Orchid-Mainnet-Beta (安装)
* https://github.com/rsksmart/rskj/wiki/Compile-and-run-a-RSK-node-locally (编译)
* https://github.com/rsksmart/rskj/wiki/rsk-public-nodes (公有链)


---
* ubuntu package (x)
* jar (x)
* docker (✓)
* aws Marketplace AMI (x)
* azure (x) 
* 编译源码 (✓)
* 公有链 (✓)


创建账号
* https://github.com/rsksmart/rskj/wiki/Get-an-RSK-account

手段一: **MyCrypto**
* https://mycrypto.com/account
* https://download.mycrypto.com/

手段二: Jaxx
* https://jaxx.io/downloads.html

手段三: RPC  (下载js的node)
* https://github.com/rsksmart/utilities/tree/master/console

手段四:   
* https://iancoleman.io/bip39/ (BIP39)

---

工具栈:  
* https://solidity.readthedocs.io/en/develop/  (工具栈)

方式:
* remix
* Truffle framework
* rsk console https://github.com/rsksmart/rskj/wiki/RSK-Console
* rpc postman 

编写智能合约:  
* https://github.com/rsksmart/tutorials/wiki/Developing-Smart-Contracts-in-RSK


挖矿:
* https://github.com/rsksmart/rskj/wiki/JSON-RPC-API (rpc)
* https://github.com/rsksmart/rskj/wiki/Configure-your-RSK-node-to-be-used-from-a-merge-mining-pool (节点挖,参与到矿池)
* https://github.com/rsksmart/rskj/wiki/Running-your-own-mining-local-network (本地出矿网络)


浏览器:  
* https://explorer.testnet.rsk.co/
* https://explorer.rsk.co/

双向锚定:
* https://github.com/rsksmart/rskj/wiki/BTC-SBTC-conversion

比特币私钥 -> rsk私钥:  
* https://utils.rsk.co/

json-prc接口:
* https://github.com/rsksmart/rskj/wiki/JSON-RPC-API-compatibility-matrix


给地址充钱:
* https://github.com/rsksmart/tutorials/wiki/Module-3-%E2%80%93-Smart-contract-on-RSK-(40-minutes)
* https://faucet.testnet.rsk.co/

可以搭配其他的:

* https://github.com/rsksmart/rskj/wiki/Configure-Metamask-to-connect-with-RSK (meta mask)
* https://github.com/rsksmart/rskj/wiki/Configure-Truffle-to-connect-with-RSK (truffle)
* https://github.com/rsksmart/rskj/wiki/Configure-Remix-to-connect-with-RSK (remix)
* https://github.com/rsksmart/rskj/wiki/RSK-with-MyCrypto (mycrypto)
* https://github.com/rsksmart/rskj/wiki/Tree-view-of-the-blockchain (treeview)
* https://github.com/rsksmart/rskj/wiki/RSK-Smart-monitor-app (monitor)

<a id="markdown-2-双向锚定的问题" name="2-双向锚定的问题"></a>
# 2. 双向锚定的问题

个人理解:   
前提知识: 数据库的原子性(强调事务的整体,不可分割),一致性(强调没有中间过程).

双向锚定解决的问题是两根链上数据的交换,带来的问题是数据的原子性和一致性的问题.

管理人(中心化):
* 单一保管人: 交易所担保托管锁定比特币和执行监管解锁等量第二层链代币
* 多重签名联邦: 由一组公证人控制的多重签名

(去中心):
* 侧链
* 区块链纠缠
* 驱动链
* `混合型`: 第二层区块链使用`侧链`, 第一层使用`驱动链`

在`中心化和安全性之间`的一种权衡,最终的根链双向锚定设计可以被称为`驱动链 + 公证人/侧链`

* 前期: 公证人投票
* 中期: 矿工和公证人投票
* 后期: 仅有矿工投票 (驱动链)



<a id="markdown-3-docker搭建" name="3-docker搭建"></a>
# 3. docker搭建
```bash
cd /mnt/disk1/linux/reference/refer

git clone https://github.com/rsksmart/artifacts
cd artifacts/Dockerfiles/RSK-Node

docker build -t testnet -f Dockerfile.TestNet .
docker run -d --name testnet-node-01  -p 4444:4444 -p 50505:50505 testnet
```


<a id="markdown-4-简单测试" name="4-简单测试"></a>
# 4. 简单测试

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

<a id="markdown-5-部署到实际测试网络" name="5-部署到实际测试网络"></a>
# 5. 部署到实际测试网络

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

<a id="markdown-6-其他指令" name="6-其他指令"></a>
# 6. 其他指令

```bash
# 获取SBTC的余额??
 curl -X POST --data '{"method":"eth_getBalance", "params":["0x439a98b4b529a681687e4aac288b786662cc9b0e"], "jsonrpc":"2.0", "id":1}' https://public-node.testnet.rsk.co:443

```
