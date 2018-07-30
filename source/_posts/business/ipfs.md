---
title: ipfs
date: 2018-07-13 13:11:45
categories: [business]
---


<!-- TOC -->

- [1. 说明](#1-说明)
- [2. 再介绍](#2-再介绍)
- [3. 安装ipfs](#3-安装ipfs)
- [4. 存储原理](#4-存储原理)
- [5. 实践](#5-实践)
- [6. ipld](#6-ipld)
- [7. filecoin](#7-filecoin)
- [8. ipfs私人网络](#8-ipfs私人网络)

<!-- /TOC -->

<a id="markdown-1-说明" name="1-说明"></a>
# 1. 说明


* http://ipfser.org/2018/06/27/r45/ (书)
* https://github.com/ipfs/ipfs (官方文档)
* https://ipfs.io/docs/examples/ (常用场景,看完了)
* https://www.youtube.com/watch?v=h73bd9b5pPA (indeep-turtoial)
* https://github.com/ipfs/specs (协议规范)
* https://github.com/ipfs/reading-list (阅读列表)
* http://ipfser.org/author/wendury/ (汉化文章)
* http://ipfser.org/ (国内官网)
* https://github.com/filecoin-project (file-coin源码)

IPFS提供了一个p2p的网络传输层用于终端之间基于文件名称发现和共享文件,但是IPFS不提供和保证文件的存储,托管和带宽.

IPFS团队为了解决这个文件,发布了`FileCoin区块链`,使用区块链的支付系统来`激励`拥有剩余存储空间的`人帮助提供稳定可靠文件的存储,托管和带宽`.

EOS的问题,EOS设计性能需要达到百万级,这个设计如果每秒进行100W次交易,每次交易产生100字节,那么`每秒钟就有100M的数据`记录.如果每个区块节点都要存储一份这样的数据,那么时间稍久数据量就是一个天文数字.对于一些只能合约天然就有存储数据的需要,比如需要`存储文字,图片,声音,和视频等等数据`.这些数据更`不可能存储在区块链上`了

EOS的存储问题,看似IPFS解决了,但是`IPFS使用FileCoin让终端用户自己为存储和带宽付费`. EOS自己设计了一套方案:

文件系统智能合约,发行了一个token叫TOK,允许每个用户定义一个目录结构,所有文件都链接了一个IPFS文件,也就是TOK存储IPFS的文件链接和人类可读的文件名 `?? 不理解`

区块生产者们代表的是至少20个独立的个人或组织,每一个生产者可以复制和托管全球不同辖区的数据,只要这20个区块生产者有一个在线并提供文件,那么这个文件就可以提供给所有人

`EOS的存储经济系统`


持有TOK的人将有每年5%的EOS通胀来支付.  激励系统的不同.


* http://blog.sina.com.cn/s/blog_e99bfe2f0102xyf6.html (实现)

实现:  

用分布式的计算范式(类似于ETH,EOS,chain等底层平台) + (分布式的存储) 构建一个世界共享的分布式超级计算机

* 文件索引,每个文件将根据哈希映射从而得到一个独特的指纹
* 文件存储,区块化分发到网络中不同的节点上,网络中的`每个节点将会存储一部分文件`,并维护文件的指纹,以方便其他用户读取文件
* 文件修改,IPFS会采用`Git类似的机制来记录文件的修改`,而不是每次修改后,拷贝整个文件,并使用`梅克尔树(Merkle DAG)`来验证文件的完整性

FileCoin采用`时空证明共识`机制`(Proof of Spacetime)`,证明了在`该段时间内矿工存储了特定的数据`,其算力就是硬盘的存储量,能够节省因为POW产生的巨大能源消耗  

其他(PoSt是基于复制证明(`PoRep`,Proof-of-Repbublican))


共存机制:

client(有需求客户,个人,组织)`支付代币`将文件存储在区块链上.  
miner(矿工: 分为`存储矿工`和`检索矿工`)为挖矿的方式提供存储能力,或者检索而获得Filecoin

* 存储市场: Filecoin Storage Market,  越多的硬盘空间,挖矿能力就越高, `存储市场采用的就是 PoS(Power of Storage)证明`
* 检索市场: Filecoin's Retrieval Market,矿工提供网络带宽帮助用户提取已经保存的内容,根据带宽来分配FIL

新技术取代老的技术,无非就两点: 第一,提供系统效率 第二,降低系统成本.  IPFS是目前的过渡方案? `最典型的应用就是EOS`

EOS引以为傲的是支持百万级别TPS,其中除了DPFS共识机制的功劳外,还归功于其底层存储设计时`采取IPFS`来解决大型数据的传输效率


* http://www.ipfs.cn/news/info-100091.html   说的非常好

区块链已经产生很多风口,就像一棵树结很多种子,第一个果子是比特币,第二个果子ICO,`第三个果子是内容和文件`.

存储项目有很多技术问题需要攻克, `货币和ICO`只要把一份`文件存储在所有节点`上就可以了,但是存储项目:

第一个难点:
* 把N个文件放在M个节点上进行存储
* 区块链的节点是有下线的可能的
* 区块链的节点上的文件损坏了


第二个难点:
* 经济激励模式和收益分配

下一波牛市会由内容和文件存储的项目所引爆,2019年,或在2020年项目都会有比较可用的程度

`第四个风口`可能是产权在区块链上的交易,有一些东西抵押登记在区块链上,区块链上也有相应的货币可以`实现产权与数字货币的交易`,政府不仅不能控制甚至连税都收不了了

P2P技术还是比较完善的,只需要把这些`完善的技术以一种市场化的方法组合起来`,完善里面的经济激励就足够了.


<a id="markdown-2-再介绍" name="2-再介绍"></a>
# 2. 再介绍


2017年8月区块链项目Filecoin吸收了来自红杉资本,联合广场创投以及另外多家风险投资公司累计`5200万美元的预售轮ICO`,短短一个余额,又再次募集到了2亿美金等值的加密数字货币资产,累计`2亿5700万美金`.

把云存储变为一个算法市场,代币(FIL)在是`沟通`资源(存储和检索)`使用者`和资源的`提供者`(Filecoin矿工)的中介桥梁.越来越多的区块链项目采取了IPFS作为`存储解决方案`,提供了更加便宜,安全,稳定的存储解决方案


搭建全球化分布式存储网络之前有 BitTorrent,Kazaa,Napster,这些虽然用户多,但是自始至终没有出现一个能实现全球范围内,`低延时,并且完全去中心化的通用分布式文件系统`

HTTP协议问题:
* 高度中心化,容易被攻击,防范攻击成本高
* 存储成本高
* 泄露风险,twitter,五角大楼,Linkedln.机锋.都有被泄露
* 大规模数据存储难题,如何存储和分发PB级别的大数据

IPFS为解决这些问题诞生
* `下载速度快`,从中心化的传输方式变为点对点的传输,并且`节省大量的网络流量`
* 优化全球存储,由于FileCoin技术的使用,`数据的存储成本`将会逐步下降
* 更加安全,与中心化的云存储相比,可以使得数据存储`更安全`,并且抵挡黑客攻击
* 数据的永久保存,IPFS提供了一种使得互联网数据可以被`永久保存`可能性方式,并且提供数据的历史版本(Git)`回溯`功能

整合了多种技术的优点
* 分布式哈希表DHT (Kademlia)
* BitTorrent -> Bitswap  (p2p) ICE NAT traversal -> STUN,TURN
* Git -> DAG
* SFS 自验证文件系统Self-Certifying File System
* FileCoin


轻钱包:  
我们只需要下载与自己钱包对应的交易信息,需要验证的时候,只需要找一条从交易信息的叶节点到根节点的哈希路径即可,而`不需要`下载区块链的`全部数据`.

IPFS项目里:
数据分块存放在`有向无环图`中,如果数据被修改了,那么只需要修改对应默克尔的有向无环图的点,而不需要向网络重新更新整个文件.


`区块链`处理的本分问题:  

* 去中心化
* 没有中心机构下达成共识,共同维护一个账本
* 设计动机本不是为了高效,低能耗,和扩展性  (如果追求这些,中心化程序可能是更好的选择)

IPFS与区块链协同工作,能够补充区块链的两大缺陷:
* 区块链`存储效率低`,`成本极高`
* 跨链需要各个链之间协同配合,难以协调

对于第一个问题,我们假设这样一个场景:  
全网有1万个矿工,即便我们希望在网路保存`1M信息`,`全网消耗的存储资源是10GB!!`

IPFS的解决方法:  
1. 我们可以用IPFS存储文件数据,并将唯一永久可用的`IPFS地址`放置到区块链事务中,而不将数据本身放在区块链中
2. IPFS能协助各个不同的区块链网络传递信息和文件,IPLD??

Filecoin:  
代币上限为2亿枚,使用复制证明`(Proof of Replication).` 防止攻击矿工实际存储的数据大小要比声称的存储大小少

![](http://ouxarji35.bkt.clouddn.com/201803301400091513.jpg)

* 身份层, 路由层: 每个加入这个DHT网络的人都要声称自己的`身份信息`
* 网络层: `LibP2P`支持任意传输层协议
* 交换层: 对BitTorrent进行创新性修改,叫做`Bitswap`,利用信用和账单体系来`激励`节点去分享,如果用户只下载数据而不分享数据,信用分则会越来越低
* 对象和文件层: 大部分数据对象都是以Merkle Dag的结构存在,为内容寻址和去重.文件层是一个新的数据结构,`和DAG并列,`采用git一样的数据结构来支持版本快照
* 命名层: 验证用户发布对象的真实性,.?
* 应用层: 基于IPFS的CDN,应用可以快速下载数据

![](http://ouxarji35.bkt.clouddn.com/201803301400341605.jpg)



其他:

* Burst: 容量证明(Proof-of-capacity)
* Sia: 让云存储去中心化,倾向于在P2P和企业级领域与现有存储解决方案进行竞争
* Storj: 去中心化的基于区块链的分布式云存储西永,主要功能与中心化的Dropbox,Onedrive类似. 相较于Filecoin,基于ERC2.0的以太坊众筹币种.
* Bluzella: 很小,大小固定,按照数组,集合等数据结构的数据字段进行结构化存储

![](http://ouxarji35.bkt.clouddn.com/QQ%E5%9B%BE%E7%89%8720180725093735.png)

![](http://ouxarji35.bkt.clouddn.com/QQ%E6%88%AA%E5%9B%BE20180725094636.png)

<a id="markdown-3-安装ipfs" name="3-安装ipfs"></a>
# 3. 安装ipfs

```bash
go get -u -d github.com/ipfs/go-ipfs
cd $GOPATH/src/github.com/ipfs/go-ipfs

# 这个通过ipfs网络下载不到? 被墙了(因为官网被墙了)?
make install

cd /home/yq/installpack
wget https://dist.ipfs.io/go-ipfs/v0.4.16/go-ipfs_v0.4.16_linux-amd64.tar.gz
tar -xvzf go-ipfs_v0.4.16_linux-amd64.tar.gz
cd go-ipfs
sudo cp ipfs /usr/bin

# 创建默认的配置文件
ipfs init   

# 查看readme
ipfs cat /ipfs/QmS4ustL54uo8FzR9455qaxZwuMiUhyvMcX9Ba8nUH4uVv/readme

```

<a id="markdown-4-存储原理" name="4-存储原理"></a>
# 4. 存储原理

* http://ipfser.org/2018/01/25/r20/ (ipfs版本管理 DAG)
* https://blog.csdn.net/yichigo/article/details/79655922 (原理简述)
* https://github.com/ChainBook/IPFS-For-Chinese (国人积累的资料)
* http://mochain.info/wordpress/index.php/2018/03/12/qian_xi_ipfs_de_cun_chu_yu_du_qu/ (存储/检索 文件/目录树基本)

数据结构: Merkle DAG 

![](http://ouxarji35.bkt.clouddn.com/file_split.png)

单文件存储:

* 把单个文件拆分成若干个`256KB`大小的块 (block,可以理解为扇区)
* 逐块(block)计算block hash,hashn = hash(blockn)
* 把所有block hash拼凑成一个数组,再计算一次hash得到了文件的最终hash.并将`文件hash`和`block hash`数组捆绑起来成一个对象,把这个对象当成一个索引结构. 
* 把`block`和`索引结构`全部上传给IPFS节点,文件便同步到了IPFS的网络了
* 把hash file 打印出来,读的时候有用

小文件:  
* 小文件(小于1KB),IPFS会把数据内容直接和hash放在一起上传给ipfs节点,不会再占用一个block的大小

大文件的增量存储:  
* 文件是分块存储的,hash相同的block,只会存储一次.

Merkle DAG:  
* 内容可寻址: 所有的内容都是被多重hash校验和来唯一识别的,包括links
* 无法篡改: 所有的内容都用它的校验和来做验证,如果数据被篡改或篡改,IPFS会检测    到
* 重复数据删除

简单来说就是 `分块存储 (256kb) + Merkle DAG`,和git还是有区别的: `文件分开存储  + Merkle DAG (冗余用gc来解决)`


文件树存储???什么鬼要分析源码:  

1. 把目录下的所有的文件同步到IPFS网络中去,`为所有的文件hash建立一个别名,`这个别名其实就是本地文件名,把`hash`和`别名`捆绑在一起组建一个名为IPFSLink的对象
2. 把该目录下的所有的`IPFSLink对象`组成一个`数组`,对该数组计算一个`目录hash`,并将数组和目录hash拼成一个结构体,同步到IPFS网络
3. 如果上层还有目录结构,则为目录hash建立一个别名,把目录hash和别名捆绑在一起组成一个IPFSLink的对象
4. 把目录hash打印出来,读取的时候用

单文件读取:

1. 根据`hash`搜索该文件的`hash的索引结构`,即找到该文件的block hash数组(这一步是矿工做的)
2. 得到了block的索引,根据block hash,搜索block 所在的节点的位置,下载下来
3. 本地拼装block,根据block hash数组的顺序,把文件拼装好


文件树读取:

1. 根据hash搜索该hash的索引结构,找到该目录的IPFSLink对象数组,即目录下的子列表
2. 遍历数组,如果IPFSLink对象是文件,则取出文件的hash下载该文件
3. 如果是目录 ... 递归向下

支持的潜在的数据结构:
* 键值对存储(key-value stores)
* 关系型数据库(traditional relatioinal database)
* 三元组存储 (Linked Data triple stores)
* 文档发布系统 (Linked document publishing systems)
* 通信平台 (Linked communication platforms)
* 加密货币区块链 (cryptocurrency blockchains)



<a id="markdown-5-实践" name="5-实践"></a>
# 5. 实践

基础实践
```bash
# 初始化全局配置
ipfs init 

# 上传当前整个目录
ipfs add -r .

# 使用ipfs cat打印
ipfs cat /ipfs/QmeV1kwh3333bsnT6YRfdCRrSgUPngKmAhhTa4RrqYPbKT

# 连接到互联网
ipfs daemon

# 查看peers
ipfs swarm peers

# 本地inspector:
http://127.0.0.1:5001/webui

# 本地直接的浏览
http://127.0.0.1:8080/ipfs/QmeV1kwh3333bsnT6YRfdCRrSgUPngKmAhhTa4RrqYPbKT

#　如果开启了daemon 那么会传输到星际网络
https://gateway.ipfs.io/ipfs/QmeV1kwh3333bsnT6YRfdCRrSgUPngKmAhhTa4RrqYPbKT

# 这个也可以吗?
https://ipfs.io/ipfs/QmeV1kwh3333bsnT6YRfdCRrSgUPngKmAhhTa4RrqYPbKT

# 查看文件分片
ipfs ls QmQn14QTMctBUp8GVhSamP1cz1NbnsqfcGm9nJWzqQV47u

# 直接创建分片
echo "This is some data" | ipfs block put

# 获取分片
ipfs block get QmfQ5QAjvg4GtA3wg3adpnDJug8ktA1BxurVqBD8rtgVjM

# 主动连接 swarm
ipfs swarm connect /ip4/104.236.176.52/tcp/4001/ipfs/QmSoLnSGccFuZQJzRadHn95W2CrSFmZuTdDWP8HXaHca9z

# 寻找peer
ipfs dht findpeer QmSoLnSGccFuZQJzRadHn95W2CrSFmZuTdDWP8HXaHca9z

# 防止gc
ipfs pin


# 本地映射
sudo mkdir /ipfs /ipns
sudo chown `whoami` /ipfs /ipns

ipfs mount

```

ipns 名字空间!!!!
```bash
echo 'Let us have some mutable fun!' | ipfs add

# 发布
ipfs name publish QmYuWGLtu2fwTBMyt9LWJw212PBdMm2uDchub4rHqkHPg3

# 解析自己的(hash是自己的node id)
ipfs name resolve QmRxvVhBA9p1CTamqzyfPbqS4QsdnihYaMnm6sLY2utW6D

# 为何不是目录树,而直接是文本呢?
https://ipfs.io/ipns/QmRxvVhBA9p1CTamqzyfPbqS4QsdnihYaMnm6sLY2utW6D

echo 'Look! Things have changed!' | ipfs add

# 绑定节点名(绑定到自己的!)
# 主要解决问题是每次修改文件后add都会返回不同的hash,对于网站来说没法访问
ipfs name publish QmSb8DSVmu4Qip56jcqPVz1Cx9RJ3vTf3d1Gf9ixaG2tWg

```

bootstrap(初始化引导列表把)
```
ipfs bootstrap list
```

ipfs 配置
```
"Addresses": {
    "Swarm": [  
      "/ip4/0.0.0.0/tcp/4001" # 公网地址给别人dial的
    ],
    "API": "/ip4/127.0.0.1/tcp/5001", # 提供http API,操控daemon,本机用
    "Gateway": "/ip4/127.0.0.1/tcp/8080" # 网关地址,本机用
  }
```

Graphing Objects 画图哦
```
yq@yq-PC:~/resource/test% tree shit
shit
├── cat.jpg
└── test
    ├── bar
    ├── baz
    │   ├── b
    │   └── f
    └── foo

graphmd Qma2m3f9w345iMWX32ormPsNwq8PWa5Pmm94N9WiErMqHY | dot -Tpng > graph.png

```

git more distributed

```bash
git clone --bare https://github.com/yqsy/testipfs

# 往ipfs上扔的时候
git update-server-info

# 可选
cp objects/pack/*.pack .
git unpack-objects < ./*.pack
rm ./*.pack

ipfs add -r .


git clone http://127.0.0.1:8080/ipfs/QmaUufWKhav51hZHT9BMHSVGwTg4ksiSwKXd8cPH9D8sXP myrepo

# 直接可以这样用
import (
    mylib "gateway.ipfs.io/ipfs/QmX679gmfyaRkKMvPA4WGNWXj9PtpvKWGPgtXaF18etC95"
)

```

websites

```bash
mkdir testhtml
cd testhtml
echo "<h> hello world</h>" > index.html
ipfs add -r .

# 访问
http://127.0.0.1:8080/ipfs/QmZfycqAQViYGJ4eH2e63cgAD7J57VRcPeD3NkHfkxdbT8/
```


<a id="markdown-6-ipld" name="6-ipld"></a>
# 6. ipld


* https://ipld.io/
* https://github.com/ipld/ipld 

<a id="markdown-7-filecoin" name="7-filecoin"></a>
# 7. filecoin

* https://filecoin.io/
* https://filecoin.io/blog/update-2017-q4/ (博客)
* http://chainx.org/paper/index/index/id/13.html (中文白皮书)
* http://ipfser.org/2017/12/28/r12/ (证明机制)

应用:
* https://d.tube


大概梳理:

* 去中心化存储网络(Decentralized Storage Network)(DSN)
* 新型的存储证明 1.复制证明”（`Proof-of-Replication` PoRep  2.`“时空证明”（Proof-of-Spacetime）` PoSt
* 可验证市场,确保服务被正常提供的时候执行支付请求
* 有效的工作量证明(Proof-of-work), 在时空证明的基础上构建一个可以在共识协议上的有效工作证明,矿工们不需要浪费计算能力来开采区块.

具体做啥?:

* Filecoin协议是构建于区块链和`带有原生令牌的去中心化存储网络`。客户`花费令牌`来`存储`数据和`检索`数据，而`矿工们`通过提供存储和检索数据来`赚取`令牌。
* Filecoin `DSN` 分别通过`两个可验证市场`来处理存储请求和检索请求：`存储市场`和`检索市场`。客户和矿工设定所要求服务的价格和提供服务的价格，并将其`订单`提交到`市场`。
* 市场由Filecoin网络来操作，该网络采用了`“时空证明”`和`“复制证明”`来确保矿工们正确存储他们承诺存储的数据。

参与者:

* 客户: 在DSN中通过Put和Get请求存储数据或者检索数据,并为此付费
* 存储矿工为网络提供数据存储,存储矿工通过提供他们的磁盘空间和响应Pug请求来参与Filecoin.
* 检索矿工为网络提供数据检索服务

数据结构:

* `碎片`是客户在DSN所存储数据的一部分: 数据可以`划分为许多片`,每片都可以有不同集合的存储矿工来存储
* `扇区`: `存储矿工`向网络`提供`的一些`磁盘空间`,矿工将客户数据的碎片存储到扇区,并通过服务赚取令牌
* `分配表`: `跟踪碎片`和其分配的扇区
* `订单`: 订单式请求或提供服务的意向声明,客户向市场提交投标来请求服务
* `订单簿`: 订单的集合
* `抵押`: 网络提供存储的承诺

存储会面临到的攻击手段?:

* 女巫攻击 (Sybil Attacks): 利用n个身份，承诺存储n份数据D，`而实际上存储小于n份`（比如1份），但是`却提供了n份存储证明`，攻击成功
* 外部数据源攻击 (Outsourcing Attacks): 攻击者矿工收到检验者要求提供数据D的证明的时候，`攻击者矿工从别的矿工那里生成证明`，证明自己一直存储了数据D，而实际上没有存储，攻击成功
* 生成攻击 (Generation Attacks):  `攻击者A可以使用某种方式生成数据D`，当检验者验证的时候，攻击者A就可以重新生成数据D来完成存储证明，攻击成功

其他共识?

* 数据持有性证明(Provable Data Possession,PDP): 用户发送数据给矿工进行存储,矿工`证明数据已经被自己存储`,用户重复检查矿工是否还在存储自己的数据
* 可检索证明(Proof-of-Retrievablity,PoRet): 和PDP过程比较类似,证明矿工存储的数据是可以用来查询的

---
* 存储证明(Proof-of-Storage,PoS): 利用存储空间进行的证明,工作量证明的一种,FileCoin上一篇论文一直使用这个名字,`新的论文则升级为PoRep`
* 复制证明(Proof-of-Replication,`PoRep`): 新的PoS(Proof-of-storage),`PoRep可以保证每份数据都是独立的`.可以防止女巫攻击,外源攻击和生成攻击
* 时空证明(Proof-of-Spacetime,`PoSt`): 证明自己花费了spacetime的资源,`一定时间内的存储使用`,`PoSt是基于PoRep实现的`

---
* 工作量证明(Proof-of-Work,`PoW`): 证明者向校验者证明自己花费了一定的资源.
* 空间证明(Proof-of-Space,PoSpace): `PoSpace是PoW的一种`,不同的是PoW是用的是`计算的资源`,而PoSpace使用的是`存储的资源`


<a id="markdown-8-ipfs私人网络" name="8-ipfs私人网络"></a>
# 8. ipfs私人网络

* https://blog.csdn.net/oscube/article/details/80598790
* https://github.com/ipfs/go-ipfs/blob/master/docs/experimental-features.md#private-networks

```bash

```
