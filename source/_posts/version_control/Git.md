---
title: Git
date: 2017-11-15 12:23:39
categories: [版本管理]
---


<!-- TOC -->

- [1. 删除本地以及remote的分支](#1-删除本地以及remote的分支)
- [2. push 所有分支](#2-push-所有分支)
- [3. 文本文件行尾LF](#3-文本文件行尾lf)
- [4. 切换到最新的master](#4-切换到最新的master)
- [5. clone windows目录](#5-clone-windows目录)
- [6. 设置用户名和邮箱](#6-设置用户名和邮箱)
- [7. 清理文件夹](#7-清理文件夹)

<!-- /TOC -->


<a id="markdown-1-删除本地以及remote的分支" name="1-删除本地以及remote的分支"></a>
# 1. 删除本地以及remote的分支
* https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-both-locally-and-remotely

```bash
# -D表示强制删除
git branch -D branch1
git push origin --delete branch1
```

<a id="markdown-2-push-所有分支" name="2-push-所有分支"></a>
# 2. push 所有分支
```
git push --all origin
```

<a id="markdown-3-文本文件行尾lf" name="3-文本文件行尾lf"></a>
# 3. 文本文件行尾LF
.gitattributes
```
*.sqc text eol=lf
```

<a id="markdown-4-切换到最新的master" name="4-切换到最新的master"></a>
# 4. 切换到最新的master
```
git fetch && git reset --hard origin/master
```

<a id="markdown-5-clone-windows目录" name="5-clone-windows目录"></a>
# 5. clone windows目录
```bash
git clone file:////10.243.141.8/git/cache
```

<a id="markdown-6-设置用户名和邮箱" name="6-设置用户名和邮箱"></a>
# 6. 设置用户名和邮箱
```
git config --global user.email "yqsy021@126.com"
git config --global user.name "yqsy"
```

<a id="markdown-7-清理文件夹" name="7-清理文件夹"></a>
# 7. 清理文件夹

```bash
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
