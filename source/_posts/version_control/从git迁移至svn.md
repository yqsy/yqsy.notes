---
title: 从git迁移至svn
date: 2018-01-01 15:10:36
categories: [版本管理]
---

<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 实践](#2-实践)
- [创建git历史](#创建git历史)
- [创建一个svn仓库以及checkout](#创建一个svn仓库以及checkout)
- [将git的历史回归到svn](#将git的历史回归到svn)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://zxtechart.com/2017/07/16/use-two-remote-repos-of-svn-and-git-at-the-same-time-for-the-same-project/ 
* https://superuser.com/questions/486683/setting-up-local-repository-with-tortoisesvn-in-windows


<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践
由于公司比较保守,不愿意使用分布式版本管理工具,而我一直使用git来管理版本,所以离职时要将git的提交历史回归到svn上

<a id="markdown-创建git历史" name="创建git历史"></a>
# 创建git历史
```
mkdir local-git-repos
cd local-git-repos/
git init
touch test.txt
git add test.txt
git commit -am "Added test.txt."
echo aaaa >> test.txt
git commit -am "Added aaaa."
echo bbbb >> test.txt
git commit -am "Added bbbb."
```

<a id="markdown-创建一个svn仓库以及checkout" name="创建一个svn仓库以及checkout"></a>
# 创建一个svn仓库以及checkout
```
cd C:\work\testrepo
svnadmin create svn-repos
svn co file:///C:/work/testrepo/svn-repos svn-client
cd svn-client/
mkdir trunk branches tags
svn add *
svn ci -m "Added trunk, branches and tags."
```

<a id="markdown-将git的历史回归到svn" name="将git的历史回归到svn"></a>
# 将git的历史回归到svn
```
cd C:\work\testrepo\local-git-repos

# --stdlayout 没加,加了报错
git svn init C:/work/testrepo/svn-repos/ --prefix=svn/
git rebase --onto remotes/svn/trunk --root master
```
