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

说明|指令
-|-
忽视	|-fX
未被忽视	|-f
忽视+未被忽视	|-fx
文件夹	|-d
