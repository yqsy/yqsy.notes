---
title: shell
date: 2017-11-03 21:41:00
categories: [linux, 系统管理]
---

<!-- TOC -->

- [1. 特性](#1-特性)
    - [1.1. 快捷键](#11-快捷键)
- [2. 使用场景时](#2-使用场景时)
- [3. 各种符号含义](#3-各种符号含义)
- [4. 运算符号](#4-运算符号)
    - [4.1. 文件类型运算符](#41-文件类型运算符)
    - [4.2. 文件权限运算符](#42-文件权限运算符)
    - [4.3. 比较数字](#43-比较数字)
- [5. 常用语句](#5-常用语句)
- [6. 标注输入输出](#6-标注输入输出)
- [7. sed的常见语法](#7-sed的常见语法)
- [8. xargs/expr/exec](#8-xargsexprexec)

<!-- /TOC -->


<a id="markdown-1-特性" name="1-特性"></a>
# 1. 特性
`/bin/bash`时Linux默认的shell,时GNU计划中重要的工具软件之一

* history可查看输入历史,`~/.bash_history`
* tab命令补全
* 命令别名设置(alias),例如` alias lm='ls -al'`
* 工作控制,前景背景控制 (job control, foreground, background)
* 程序化脚本(shell script)
* 万用字符: (Wildcard)

<a id="markdown-11-快捷键" name="11-快捷键"></a>
## 1.1. 快捷键

* ctrl+u 向前删除字符串
* ctrl+k 向后删除字符串
* ctrl+a 光标移动到最前面
* ctrl+e 光标移动到最后面
* ctrl+s vim画面锁死  strl+q恢复
* ctrl+c 终止目前的命令
* ctrl+d 输入结束(eof),例如邮件结束的时候
* ctrl+m enter
* ctrl+z 暂停目前的命令

<a id="markdown-2-使用场景时" name="2-使用场景时"></a>
# 2. 使用场景时

请记住shell脚本的强项: 强控简单的文件和命令,当你发现你的脚本写得有点繁琐,特别时涉及复杂的字符串或数学处理时,或许你就该实时Python,Perl或awk之类的脚本语言

* https://stackoverflow.com/questions/209470/can-i-use-python-as-a-bash-replacement (使用python替代shell)
* http://plumbum.readthedocs.io/en/latest/ (库)

<a id="markdown-3-各种符号含义" name="3-各种符号含义"></a>
# 3. 各种符号含义

符号|含义
-|-
单引号|保证shell不做任何转换
双引号|同上,只不过shell会对双引号中的所有变量进行扩展
$+数字|单个参数
$#|参数的数量
$@|代表脚本接收的所有参数
$0|脚本名
$?|退出码

注意
* 引号中的任何东西都会被当成一个参数


<a id="markdown-4-运算符号" name="4-运算符号"></a>
# 4. 运算符号

<a id="markdown-41-文件类型运算符" name="41-文件类型运算符"></a>
## 4.1. 文件类型运算符

运算符|用于测试
-|-
-f|普通文件
-d|目录
-h|符号链接
-b|块设备
-c|字符设备
-p|命名管道
-S|套接字


<a id="markdown-42-文件权限运算符" name="42-文件权限运算符"></a>
## 4.2. 文件权限运算符

运算符|用于测试
-|-
-r|可读
-w|可写
-x|可执行
-u|Setuid
-g|Setgid
-k|Sticky

<a id="markdown-43-比较数字" name="43-比较数字"></a>
## 4.3. 比较数字

运算符|当参数一与参数二相比,....时,返回true
-|-
-eq|相等
-ne|不等
-lt|更小
-gt|更大
-le|更小或相等
-ge|更大或相等
 
<a id="markdown-5-常用语句" name="5-常用语句"></a>
# 5. 常用语句

```bash
# 条件判断
if [ $1 = hi ]; then
    echo 'The first argument was "hi"'
else
    echo -n 'The first argument was not "hi" -- '
    echo it was '"'$1'"'
fi

# elif
if [ "$1" = "hi" ]; then
   echo 'The first argument was "hi"'
elif [ "$2" = "bye" ]; then
   echo 'The second argument was "bye"'
else
   echo -n 'The first argument was not "hi" and the second was not "bye"-- '
   echo They were '"'$1'"' and '"'$2'"'
fi

# -f表示普通文件
for filename in *; do
    if [ -f $filename ]; then
        ls -l $filename
        file $filename
    else
        echo $filename is not a regular file.
    fi
done

# case进行字符串匹配
case $1 in
    bye)
        echo Fine, bye.
        ;;
    hi|hello)
        echo Nice to see you.
        ;;
    what*)
        echo Whatever.
        ;;
    *)
       echo 'Huh?'
       ;;
esac

# for循环
for str in one two three four; do
    echo $str
done

# while循环
#!/bin/sh
FILE=/tmp/whiletest.$$;
echo firstline > $FILE
while tail -10 $FILE | grep -q firstline; do
    # add lines to $FILE until tail -10 $FILE no longer prints "firstline"
    echo -n Number of lines in $FILE:' '
    wc -l $FILE | awk '{print $1}'
    echo newline >> $FILE
done

rm -f $FILE
```


<a id="markdown-6-标注输入输出" name="6-标注输入输出"></a>
# 6. 标注输入输出

按`ctrl-d`终止当前终端的标准输入并终止命令.`ctrl-c`终止当前进程的运行.

标准输入和标注输出通常简写为`stdin`和`stdout`,标准错误输出`stderr`

重定向
```bash

# 如果文件不存在,会创建文件,如果文件已经存在,shell会清空文件内容
command > file

# 不想文件内容被清空
command >> file

# 流ID 1是标准输出,2是标准错误输出
# 重定向标准错误输出至标准输出
ls /ffffffff > f 2>&1

# 标准输入重定向
head < /proc/cpuinfo
```

<a id="markdown-7-sed的常见语法" name="7-sed的常见语法"></a>
# 7. sed的常见语法

```bash

# 根据一个正则表达式进行内容替换
sed 's/exp/test/'

# 将/etc/passwd的第一个冒号替换成%
sed 's/:/%/' /etc/passwd

# 将/etc/passwd的所有冒号都换成%,在末尾加上g
sed 's/:/%/g' /etc/passwd

# 读取/etc/passwd,并把三到六行去掉,打印到标准输出
sed 3,6d /etc/passwd
```

<a id="markdown-8-xargsexprexec" name="8-xargsexprexec"></a>
# 8. xargs/expr/exec
当把海量的文件当作一个命令的参数时,该命令或者shell可能会告诉你缓冲不足以容纳这些参数,解决这个问题,可用`xargs`,它能对自身输入流的每个文件名逐个地执行命令

```bash
# 验证.gif是否是真的gif
find . -name '*.gif' -print0 | xargs -0 file

# 或者可以这样写
find . -name '*.gif' -exec file {} \;
```

exec命令时shell内置的,他会用其后的程序的进程来取代你当前的shell进程,当在shell窗口中运行exec cat时,按下ctrl-d或ctrl-c时,shell窗口就会小时,因为没有任何子进程了
