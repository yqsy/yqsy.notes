---
title: 从git迁移至svn
date: 2018-01-01 15:10:36
categories: [版本管理]
---

<!-- TOC -->

- [1. 资料](#1-资料)
- [2. 实践](#2-实践)
- [3. 创建git历史](#3-创建git历史)
- [4. 创建一个svn仓库以及checkout](#4-创建一个svn仓库以及checkout)
- [5. 将git的历史回归到svn](#5-将git的历史回归到svn)

<!-- /TOC -->

<a id="markdown-1-资料" name="1-资料"></a>
# 1. 资料

* https://zxtechart.com/2017/07/16/use-two-remote-repos-of-svn-and-git-at-the-same-time-for-the-same-project/ 
* https://superuser.com/questions/486683/setting-up-local-repository-with-tortoisesvn-in-windows


<a id="markdown-2-实践" name="2-实践"></a>
# 2. 实践
由于公司比较保守,不愿意使用分布式版本管理工具,而我一直使用git来管理版本,所以离职时要将git的提交历史回归到svn上

<a id="markdown-3-创建git历史" name="3-创建git历史"></a>
# 3. 创建git历史
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

<a id="markdown-4-创建一个svn仓库以及checkout" name="4-创建一个svn仓库以及checkout"></a>
# 4. 创建一个svn仓库以及checkout
```
cd C:\work\testrepo
svnadmin create svn-repos
svn co file:///C:/work/testrepo/svn-repos svn-client
cd svn-client/
mkdir trunk branches tags
svn add *
svn ci -m "Added trunk, branches and tags."
```

<a id="markdown-5-将git的历史回归到svn" name="5-将git的历史回归到svn"></a>
# 5. 将git的历史回归到svn

我还是觉得git svn是将svn的历史转到git,而不是git的历史转到svn,(或者可以,但是我这边尝试下来各种报错,这种很傻的事情没必要投入大量的精力尝试)
所以我得改变思路
```bash
cd C:\work\testrepo\local-git-repos

# --stdlayout 没加,加了报错
git svn init C:/work/testrepo/svn-repos/ --prefix=svn/

# 这个指令应该是svn -> git的
git rebase --onto remotes/svn/trunk --root master
```

* http://blog.ploeh.dk/2013/10/07/verifying-every-single-commit-in-a-git-branch/ (参考这个)

