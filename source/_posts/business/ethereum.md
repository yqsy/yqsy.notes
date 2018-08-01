---
title: ethereum
date: 2018-07-12 14:29:58
categories: [business]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 缺陷](#2-缺陷)
- [3. solidity](#3-solidity)
- [4. 智能合约](#4-智能合约)
- [5. 实践](#5-实践)
- [6. 代币](#6-代币)
- [7. 详细介绍](#7-详细介绍)
    - [7.1. 场景](#71-场景)
    - [7.2. 开源项目](#72-开源项目)
    - [7.3. 架构](#73-架构)
    - [7.4. 钱包](#74-钱包)
    - [7.5. 存储](#75-存储)
    - [7.6. 防止ASCI的算法](#76-防止asci的算法)
    - [7.7. GAS 价格换算](#77-gas-价格换算)
    - [7.8. 交易包含的信息](#78-交易包含的信息)
    - [7.9. 公有链,私有链,联盟链](#79-公有链私有链联盟链)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明

* https://github.com/ZtesoftCS/go-ethereum-code-analysis (源码分析!!!)
* https://www.ethereum.org/greeter (开发入门)
* https://ethereum.org/cli (安装cli)
* http://ethdocs.org/en/latest/contracts-and-transactions/contracts.html (什么是合约)
* https://solidity.readthedocs.io/en/latest/ (所用语言,类似js)
* https://www.cnblogs.com/tinyxiong/p/7878468.html (什么是智能合约?)
* https://github.com/ethereum/wiki/wiki/White-Paper (以太坊白皮书)
* https://github.com/ethereum/dapp-bin (示例)
* https://blog.csdn.net/huangshulang1234/article/details/79374085 (讲的蛮清楚)
* https://ethfans.org/posts/a-gentle-introduction-to-ethereum (基础介绍)

```
# 拉代码
go get -u github.com/ethereum/go-ethereum

cd ~/go/src/github.com/ethereum/go-ethereum
cloc ./ --exclude-dir=tests,vendor
```


<a id="markdown-2-缺陷" name="2-缺陷"></a>
# 2. 缺陷

* http://baijiahao.baidu.com/s?id=1596196077071413605&wfr=spider&for=pc


---

* 以太坊网络的效率低容易造成网络堵塞,容易受到DDOS的攻击致使主网瘫痪
* 暂时采用POW,造成了大量的网络资源浪费
* 真实世界的数据上链的难度较大,且数据上链的成本较高

以太坊创始人v神也意识到了这些问题,已经提出了使用
* 分片（Sharding)
* 侧链(Plasma)
* 雷电网络(Radien Network)




<a id="markdown-3-solidity" name="3-solidity"></a>
# 3. solidity

* http://wiki.jikexueyuan.com/project/solidity-zh/introduction-smart-contracts.html (简单学习)
* http://solidity.readthedocs.io/en/v0.4.24/solidity-by-example.html (原版教程)
* http://wiki.jikexueyuan.com/project/solidity-zh/units-globally-available-variables.html (全局变量)

```solidity
contract Coin {
//关键字“public”使变量能从合约外部访问。
    address public minter;
    mapping (address => uint) public balances;

//事件让轻客户端能高效的对变化做出反应。
    event Sent(address from, address to, uint amount);

//这个构造函数的代码仅仅只在合约创建的时候被运行。
    function Coin() {
        minter = msg.sender;
    }
    function mint(address receiver, uint amount) {
        if (msg.sender != minter) return;
        balances[receiver] += amount;
    }
    function send(address receiver, uint amount) {
        if (balances[msg.sender] < amount) return;
        balances[msg.sender] -= amount;
        balances[receiver] += amount;
        Sent(msg.sender, receiver, amount);
    }
}
```

```
address public minter;
```

* adderss: 声明了一个可公开访问的状态变量,160bits. 存储`合约的地址`或`其他人的公钥私钥`
* public: `为其修饰的状态变量生成访问函数.`没有public的关键字无法被其他的合约访问

```bash
# public生成的代码
function minter() returns (address) { return minter; }
```

```
mapping (address => uint) public balances;
```

* mapping 哈希表
* address => uint 将一些address映射到无符号整数

```bash
# public生成的代码
function balances(address _account) returns (uint balance) {
    return balances[_account];
}
```

```
event Sent(address from, address to, uint amount);
```

* event: 事件. 由send函数最后一行代码出发,`客户端,服务端都适用`.用很低的开销监听由这些区块链触发的事件.事件触发时,监听者会同时接收到`from,to,value`这些参数值.


```
function Coin() {
    minter = msg.sender;
}
```

* Coin(): 在合约创建的时候运行,之后就无法被调用.它会永久得存储合约创建者的地址.
* msg: 一个神奇的`全局变量`,包含了一些可以被合约代码访问的属`于区块链的属性`.
* msg.sender: 总是存放着`当前函数的外部调用者`的地址

```
function mint(address receiver, uint amount) {
    if (msg.sender != minter) return;
    balances[receiver] += amount;
}
function send(address receiver, uint amount) {
    if (balances[msg.sender] < amount) return;
    balances[msg.sender] -= amount;
    balances[receiver] += amount;
    Sent(msg.sender, receiver, amount);
}

```

* 真正被用户或者其他合约调用. 用来`完成本合约`功能的函数是`mint和send`.
* 如果合约创建者之外的其他人调用mint,什么都不会发生
* send可以被任何人`(拥有一定数量的代币)`调用,发送一些币给其他人  
* 注意: 通过合约发送一些带代币到某个地址,在区块链浏览器中查询该地址将什么也看不到.!!因为发送代币导致的余额变化只存储在该`代币合约`的数据存储中,通过事件我们可以很容易创建一个可以追踪新币交易和余额的区块链浏览器


---


<a id="markdown-4-智能合约" name="4-智能合约"></a>
# 4. 智能合约

区块链是一个全局共享的,事务性的数据库.  = = 没仔细说清楚,是关系型数据库的ACID吗?

区块链以一个相当规律的时间间隔加入到链上,对于以太坊,`这个间隔大致是17秒`

你的交易可能被删除,也可能被回滚,但是你`等待`的时间`越久`,这种情况发生的`概率越小`.

以太坊虚拟机`EVM`是以太坊中智能合约的运行环境,他不仅被沙箱封装起来,事实上也被`完全隔离`.运行在EVM内部的代码不能接触到网络,文件系统或者其他进程,甚至智能合约与其他智能合约只有有限的接触


账户:
* 外部账户: 被公钥-私钥控制,由公钥决定,
* 合约账户: 被存储在账户中的代码控制, 创建合约时确定,

`合约账户存储代码`,外部账户则没有,除了这两点之外,这两类账户对于EVM来说是一致的

每个账户都有一个以太币余额


交易:
* 从一个账户发到另一个账户
* 可以是二进制数据也可以是以太币

---
* 如果目标账户包含代码,该代码就会执行
* 如果目标账户是零账户,交易就会创建一个新的合约


GAS:
* 以太坊的每笔交易都会收取一定数量的GAS,GAS的目的是限制执行交易所需的工作量
* 无论执行到什么位置,一旦gas被耗尽,将会触发一个out-of-gas异常,当前调用帧所有状态修改都将会被回滚

存储:

* 持久化内存区域,形式为key-value,key,value均为256比特,在合约里,不能遍历账户的存储
* 主存,每次消息调用时,都有一块新的,被清除过的主存.按字节粒度寻址,读写粒度为32字节(256比特

EVM不是基于寄存器,而是基于栈的虚拟机.因此所有的计算都在一个被成为栈的区域执行.栈`最多`有`1024个元素`,每个元素`256比特`,对栈的访问只限于其顶端.

无法只访问栈上面的指定深度的那个元素,在那之前必须要把指定深度的所有元素从栈中移除才行.


消息调用:??

合约可以通过消息调用的方式来调用其他合约或者发送以太币到非合约账户上.


代码调用和库: ??

存在一种特殊类型的消息调用,被成为callcode,只是`加载自目标地址的代码将在发起调用的合约上下文运行`

这使得Solidity可以实现"库 ",可复用的库代码可以应用在一个合约的存储上,`可以用来实现复杂的数据结构???`.


<a id="markdown-5-实践" name="5-实践"></a>
# 5. 实践

* https://remix.ethereum.org
* https://metamask.io/

```
sudo su - root

export http_proxy=http://localhost:1080
export https_proxy=http://localhost:1080

npm install solc -g
```
<a id="markdown-6-代币" name="6-代币"></a>
# 6. 代币

* https://ethereum.org/token#the-code (货币)
* https://ethereum.org/crowdsale#the-code (去中心知识库)
* https://www.jianshu.com/p/a5158fbfaeb9 (ERC20)

<a id="markdown-7-详细介绍" name="7-详细介绍"></a>
# 7. 详细介绍

<a id="markdown-71-场景" name="71-场景"></a>
## 7.1. 场景

* Golem 创造一个全球空闲计算资源的产消市场
* CryptoKitties 基于以太坊区块链的养猫娱乐DApp
* Augur 预测未来真实事件的市场预测平台
* Bancor  以太坊代币之间兑换的交易所DApp  代币是BNT, 有经济学的换算公式, 使得各种代币均能根据其现有价格,总市值等标准与BNT进行交换
* KyberNetwork 数字货币交易所App 跨区块链之间的各种代币之间的交易


`KyberNetwork`

去中心化,无需新人的交易所,内部机制主要由以太坊智能合约实现,代币兑换都是链上交易

* 用户希望向其他用户转账A代币
* 接收方希望收到B代币

用户可以向KyberNetwork的智能合约发送A代币,KyberNetwork在其去中心化的代币存储池中实现兑换出相应价值B代币发送给接收方

链上交易,兑换过程可被立即确认,过程结束后也可追溯,并且用户无需更改以太坊底层协议或其他智能合约协议


<a id="markdown-72-开源项目" name="72-开源项目"></a>
## 7.2. 开源项目
开源项目:
* Go-ethereum: `Geth` 目前使用最为广泛的以太坊客户端,又称Geth
* CPP-ethereum: C++语言实现实现的版本. Windows,Linux和OS X等各个版本的操作系统以及多种硬件平台
* Parity: Rust语言实现的版本
* Pyethapp: python语言实现的版本


浏览器:
* Mist: 以太坊官方开发的工具,浏览各类 DApp的项目
* MetaMask: 浏览器插件, 只需通过MetaMask便可在浏览器上连接以太坊网络,和运行以太坊DApp

以太坊开发工具: 
* `Web3.js`: 兼容以太坊核心功能的JavaScript库
* Remix: 网页终端整合了Solidity代码的编写,调试和运行等功能
* Truffle: 针对以太坊Dapp的开发框架, 对Solidity智能合约的开发,测试,部署等进行全流程的管理,帮助开发者更专业地开发以太坊DAPP
* ENS-register: Ethereum name service 为以太坊账户提供域名注册服务

<a id="markdown-73-架构" name="73-架构"></a>
## 7.3. 架构

![](http://ouxarji35.bkt.clouddn.com/c98ff12076232f60ddccda38376baf1ffd4fe309.jpeg)

账户:  
* 外部账户: 由人存储的,可以存储以太币,是由公钥和私钥控制的账户
* 合约账户: 由`外部账户创建`的账户

外部账户(EOA)由私钥来控制,拥有一对公私钥,地址由公钥来决定,外部账户`不能包含以太坊虚拟机(EVN)代码`

可以用Geth指令创建一个外部账户,生成一个账户地址的过程:
* 设置账户的`私钥`,也就是通常意义的用户密码
* 使用加密算法由`私钥生成对应的公钥`  `secp256k1椭圆曲线密码算法`
* 根据公钥得出相应的账户地址 `SHA3`

合约账户和普通账户最大的不同就是它`还存有智能合约` 

私钥的三种形态: Private Key , Keystore & Password, Memonic code
* 256位数字,私钥最初始的状态
* 以太坊官方钱包,`私钥和公钥`将会以`加密`的方式保存一份JSON文件,存储在keystore目录下,用户需要同事`备份Keystore`和`对应的Password`
* BIP 39 ,随机生成12~24个比较容易记住的单词,该种子通过BIP-0032提案的方式生成确定性钱包??

<a id="markdown-74-钱包" name="74-钱包"></a>
## 7.4. 钱包

钱包:  

目前有多种以太坊钱包, 如Mist以太坊钱包,Parity钱包,Etherwall钱包,Brain钱包等

<a id="markdown-75-存储" name="75-存储"></a>
## 7.5. 存储  

比特币中保存了一棵Merkle树, 以太坊对三种对象设计了3棵Merkle Patrcia树,融合了Merkle树和Trie树的优点
* 状态树
* 交易树
* 收据树

这3三种树帮助以太坊客户端做一些简易的查询,如查询某个账户的余额,某笔交易是否被包含在区块中

`区块,交易`等数据最终存储在`levelDB`数据库中.

以太坊去块头不是只包括一棵MPT树,而是为三种对象设计了3棵树. 分别是 
* 交易树(Transaction Tree): 每个键是交易的序号,值是交易的内容
* 状态树 (State Tree): 状态树用来记录各个账户的状态的树,它需要经常进行更新
* 收据树(Receipt Tree): 代表每笔交易相应的收据

客户端可以轻松地查询以下的内容: 
* 某笔`交易`是否被包含`在特定的区块`中   -> `交易树`
* 查询某个地址在过去的30天中发出某种类型事件的所有实例 -> `收据树`
* 目前某个`账户的余额` -> `状态树`
* 一个`账户是否存在` -> `状态树`
* 假如在某个合约中进行一笔交易,`交易的输出`是什么 -> `状态树`


<a id="markdown-76-防止asci的算法" name="76-防止asci的算法"></a>
## 7.6. 防止ASCI的算法
共识算法:

以太坊有一个专门设计的PoW算法,Ethash算法 `(抵制ASIC)`

为什么能抵制ASCI?   
* https://zhuanlan.zhihu.com/p/35326901
* https://zhuanlan.zhihu.com/p/28830859


<a id="markdown-77-gas-价格换算" name="77-gas-价格换算"></a>
## 7.7. GAS 价格换算

大概就是使用种子产生一个16MB的伪随机缓存,基于缓存再生成一个1GB的数据集,称为DAG,挖矿可以概括为矿工从DAG中`随机`选择元素`并对其进行散列的过程`,DAG也可以理解为一个完整的搜索空间.

价格表:

单位|维值
-|-
wei|1 wei
Kwei|1e3 wei
Mwei|1e6 wei
Gwei|1e9 wei
microether|1e12 wei
milliether|1e15 wei
ether|1e18 wei

Gas(汽油) 是用来衡量一笔交易锁消耗的计算资源的基本单位,当以太坊节点执行一笔交易所需的计算步骤越多,那么这笔交易消耗的Gas越多

一笔普通的转账交易会消耗21,000Gas,而一个创建智能合约的交易可能会消耗几万,甚至几百万Gas

目前以太坊客户端默认的GasPrice是0.000000001 Ether/Gas

Gas Limit:  

保护用户免收错误代码影响以致消耗过多的交易费, 如果Gas Used小于Gas Limit,那么矿工执行过程中会发现`Gas已被耗尽`而`交易没有执行完成`,此时矿工会`回滚到程序执行前的状态`

换句话说 `GasPrice * GasLimit` 表示用户愿意为一笔交易支付的`最高金额`, 因为如果没有Gas Limit限制,那么某些恶意的用户可能会发送一个`数十亿步骤的交易`并且没有人能够处理它,所以会导致拒绝服务攻击.

<a id="markdown-78-交易包含的信息" name="78-交易包含的信息"></a>
## 7.8. 交易包含的信息

一条交易内容包含以下的信息:

* from: 交易`发送者的地址` `必填`
* to: 交易`接收者的地址` 如果`为空`意味这是一个`智能合约`的交易
* value: 发送者要转移给接收者的以太币数量
* data: 如果存在,则表明该交易是一个`创建`或者`调用智能合约交易`
* Gas Limit: 这个交易允许消耗的最大Gas数量
* GasPrice : 表示发送者愿意支付给矿工的Gas价格
* nonce: 区别同一用户发出的不同交易的标记
* hash: 以上信息生成的散列值,`作为交易的ID`
* r,s,v: 交易签名的三个部分,由`发送者的私钥`对交易hash进行签名生成


以太坊中包含3种交易:
* 转账交易: 指定交易的发送者,接收者,转移的以太币数量
* `创建`智能合约交易: 指将合约部署在区块链上,`to`字段是一个空字符串,在`data`字段中指定初始化合约的二进制代码
* `执行`智能合约交易: 需要将`to`字段指定为要调用的智能合约的地址,通过`data`字段指定要调用的方法以及向该方法传递参数

接口
* JSON-RPC
* Web3.JavaScript.API


以太坊域名服务 Ethereum Name Service

以太坊推出了可以将散列地址"翻译"成一个简短易记的地址的ENS命名服务,ENS很像我们平时所熟知的DNS服务,比如A要给B转一笔钱,`当A发起交易时,在收款人地址处不用再填写B的散列地址`.填写B的简单易记的钱包域名`B.myetherwallet.eth`也能正常交易


用户注册域名需要完成以下过程:
* 用户通过交易执行智能合约,`向合约提供自己想要注册的域名`
* 1. 域名被注册 -> 重新提交 || 买域名 2. 正在被竞拍 -> 参加竞标,投入比其他竞标者更高的竞价金  3. 没有被注册或竞拍 -> 用户发起竞拍
* 用户只有一次出价机会,竞价匿名
* 竞价截止后进入揭示环节,所有参加竞标的用户必须揭标. 否则竞价金的99.5%都会进入黑洞
* 揭示之后. 出价最高的用户获得竞标胜利,并将`以第二竞价`的金额获得该域名,多余金额将会退回该账户的钱包
* 在域名持有期内,用户可以将域名绑定到自己的以太坊地址,转移域名的使用权,添加设置子域名等,甚至还可以转让域名的所有权


<a id="markdown-79-公有链私有链联盟链" name="79-公有链私有链联盟链"></a>
## 7.9. 公有链,私有链,联盟链

以太坊公有链,联盟链,私有链特点对比

-|公有链|联盟链|私有链
-|-|-|-
可信权威|(依赖代码)|特定联盟|特定团体
挖矿节点成本|挖矿奖励(以太币)|由特定联盟规定|由特定团体规定
虚拟货币|`用于奖励挖矿节点(以太币)`|`不需要`|`不需要`
结算|可行|可行(如果有虚拟货币)|可行(如果有虚拟货币)
共识算法|工作量证明|使用拜占庭容错算法|权威证明
区块链实现|以太坊协议(比特币核心)|企业级以太坊|企业级以太坊
商业价值|高可用性,低成本的分布式账本|高可用性,低成本的分布式账本,无需中间保证金,透明结算|无需中间保证金,透明结算,直接结算

