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
