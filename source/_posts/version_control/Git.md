---
title: Git
date: 2017-11-15 12:23:39
categories: [版本管理]
---


<!-- TOC -->

- [1. 删除本地以及remote的分支](#1-删除本地以及remote的分支)

<!-- /TOC -->


<a id="markdown-1-删除本地以及remote的分支" name="1-删除本地以及remote的分支"></a>
# 1. 删除本地以及remote的分支
* https://stackoverflow.com/questions/2003505/how-do-i-delete-a-git-branch-both-locally-and-remotely

```bash
# -D表示强制删除
git branch -D branch1
git push origin --delete branch1
```
