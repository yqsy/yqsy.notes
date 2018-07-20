---
title: Git
date: 2017-11-15 12:23:39
categories: [版本管理]
---


<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 删除本地以及remote的分支](#2-删除本地以及remote的分支)
- [3. push 所有分支](#3-push-所有分支)
- [4. 文本文件行尾LF](#4-文本文件行尾lf)
- [5. 切换到最新的master](#5-切换到最新的master)
- [6. clone windows目录](#6-clone-windows目录)
- [7. 设置用户名和邮箱](#7-设置用户名和邮箱)
- [8. 清理文件夹](#8-清理文件夹)
- [9. windows lf](#9-windows-lf)
- [10. 底层](#10-底层)
- [11. 继续整理](#11-继续整理)
- [12. 大文本文件是怎么做存储的?](#12-大文本文件是怎么做存储的)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://git-scm.com/book/zh/v2 (git book)
* http://backlogtool.com/git-guide/cn/intro/intro1_1.html (猴子都能看的懂)
* https://www.quora.com/What-version-control-systems-do-large-companies-use (大公司用什么版本管理工具)
* https://github.com/xirong/my-git (学习资料)
* http://www.cnblogs.com/ShaYeBlog/p/5712839.html (托管商)

<a id="markdown-2-删除本地以及remote的分支" name="2-删除本地以及remote的分支"></a>
# 2. 删除本地以及remote的分支
* https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-both-locally-and-remotely

```bash
# -D表示强制删除
git branch -D branch1
git push origin --delete branch1
```

<a id="markdown-3-push-所有分支" name="3-push-所有分支"></a>
# 3. push 所有分支
```
git push --all origin
```

<a id="markdown-4-文本文件行尾lf" name="4-文本文件行尾lf"></a>
# 4. 文本文件行尾LF
.gitattributes
```
*.sqc text eol=lf
```

<a id="markdown-5-切换到最新的master" name="5-切换到最新的master"></a>
# 5. 切换到最新的master
```
git fetch && git reset --hard origin/master
```

<a id="markdown-6-clone-windows目录" name="6-clone-windows目录"></a>
# 6. clone windows目录
```bash
git clone file:////10.243.141.8/git/cache
```

<a id="markdown-7-设置用户名和邮箱" name="7-设置用户名和邮箱"></a>
# 7. 设置用户名和邮箱
```
git config --global user.email "yqsy021@126.com"
git config --global user.name "yqsy"
```

<a id="markdown-8-清理文件夹" name="8-清理文件夹"></a>
# 8. 清理文件夹

```bash
# 回退修改但没有commit的内容
git reset --hard

# 清理忽视/未被忽视/文件夹
git clean -fxd

# 清理未被忽视/文件夹
git clean -fd

# 删除已经提交但是ignore的文件 (漏掉了.cache?)
git ls-files -ci --exclude-standard

git ls-files -ci --exclude-standard -z | xargs -0 git rm --cached
```
<a id="markdown-9-windows-lf" name="9-windows-lf"></a>
# 9. windows lf

```bash
git config --global core.autocrlf false
```

说明|指令
-|-
忽视	|-fX
未被忽视	|-f
忽视+未被忽视	|-fx
文件夹	|-d

<a id="markdown-10-底层" name="10-底层"></a>
# 10. 底层

* https://www.cnblogs.com/gscienty/p/7904518.html (csdn的)

```bash
# 文件 
COMMIT_EDITMSG  # 最近一次的commit message,git系统都不会用到,给用户一个参考
config          # git 仓库的配置文件
description     # 主要给gitweb等git托管文件使用
HEAD            # 映射到ref引用,能够找到下一次commitd的前一次hash值
index           # 暂存区,一个二进制文件

# 路径
branches
hooks            # 存放脚本
info             # 存放仓库信息
ipfs             
ipld
logs             # !!!保存所有更新的引用记录  (分支)
objects          # !!!所有git对象
refs             # !!!保存最近一次提交的hash值

```

git系统中的三个实体
* 提交节点实体  核心实体,`节点`与`节点`之间的`继承关系`
* 节点内容实体  本次提交的`文件名`和所`对应`的`hash`
* 文件内容实体 用于`具体记录文件的内容`,所有的历史都有备份

存储时采用`deflate`对原始文件内容进行压缩, key 根据`原始文件内容`,`文件大小`等数据生成的消息摘要

在当前版本的git中,主要采用SHA1算法,将`文件格式`与`文件长度`组成`头部`,将`文件内容`作为`尾部`,由头部和尾部拼接作为原文,经过SHA1算法计算之后得到该文件的160位长的SHA1签名.一般用`长度为40`的字符串来表示,将字符串的前两个字符作为文件夹,后38个字符作为文件名进行存储

计算差异使用`pack`算法: https://github.com/git/git/blob/master/Documentation/technical/pack-heuristics.txt

merkle dag


实验

```
mkdir testipfs
cd testipfs
git init

# 一次提交两个文件
echo "this is readme" > readme.md
echo "hello" > 1.txt
git add .  && git commit -a -m "1"

# 已有两个文件再提交第三个文件
echo "world" > 2.txt
git add .  && git commit -a -m "2"

# 三个文件都存在,修改其中一个文件(增)
echo ", thar is readme too" >> readme.md
git commit -a -m "3"

# 修改增加很多字呢(不可能是全量的吧)
echo "123123123123123123123213213" >> readme.md
git commit -a -m "4"

```

```bash
# 查看hash值的方法
git cat-file -p SHA1
```


<a id="markdown-11-继续整理" name="11-继续整理"></a>
# 11. 继续整理

* https://www.youtube.com/watch?v=P6jD966jzlk
* https://github.com/pluralsight/git-internals-pdf

![](http://ouxarji35.bkt.clouddn.com/20180719210954.png)

对象类型
* Commit - Author,message,pointer to a tree of changes
* Tree - Pointer to file names, content , other trees
* Blob - Data (source code,pictures,video, etc.)


知识点:
* git是一个 Directed acyclic graph (有向无环图)
* commits都会引用父亲节点
* 分支是commit的引用
* master是权威的主线分支
* HEAD 是特殊的指针,指向最新的提交

![](http://ouxarji35.bkt.clouddn.com/20180719225914.png)


```bash
# 观察文件夹变化
watch -n 1 -d find .


```

<a id="markdown-12-大文本文件是怎么做存储的" name="12-大文本文件是怎么做存储的"></a>
# 12. 大文本文件是怎么做存储的?

例如一个1MB的源码文件(假设),其中只做了一行修改不可能整个文件copy一遍把,我要做个实验

```bash
mkdir testipfs 
cd testipfs
for i in $(seq 1 100000); do echo $i >> 1.txt; done
git add .
git commit -a -m "new"

```

这个功能应该是gc

