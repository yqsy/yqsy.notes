---
title: Django
date: 2018-1-31 22:10:29
categories: [web]
---


<!-- TOC -->

- [1. 资源](#1-资源)
- [2. windows安装](#2-windows安装)

<!-- /TOC -->

<a id="markdown-1-资源" name="1-资源"></a>
# 1. 资源
* https://docs.djangoproject.com/en/2.0/intro/tutorial01/ (初始教学)


<a id="markdown-2-windows安装" name="2-windows安装"></a>
# 2. windows安装

```
Python 3.6.2
pip 9.0.1 from c:\python36\lib\site-packages (python 3.6)

pip install django

# 显示版本
python -m django --version

# 创建一个工程
django-admin startproject mysite

# 运行工程
python manage.py runserver 0:8000

# An app can be in multiple projects.
python manage.py startapp polls


mysite/urls.py -> app polls or admin

path('polls/', include('polls.urls')), 应该是路径 polls -> 找到polls目录下的urls.py文件把

app polls -> urls.py  -> views.py (定义路径函数)
这里面定义为啥要反射? path('', views.index, name='index'),

path() argument: route view kwargs name是别名


安装的app
django.contrib.admin – The admin site. You’ll use it shortly.
django.contrib.auth – An authentication system.
django.contrib.contenttypes – A framework for content types.
django.contrib.sessions – A session framework.
django.contrib.messages – A messaging framework.
django.contrib.staticfiles – A framework for managing static files.


数据库用的是orm技术?

models文件定义数据类型

添加了models如何让manage.py 生成数据库结构呢?
在settings.py里面配置
'polls.apps.PollsConfig', 路径.apps.PollsConfig?

生成数据库结构?是的,可以看到migrations目录中有生成的文件
python manage.py makemigrations polls

生成sql (其实也不用执行啦)
python manage.py sqlmigrate polls 0001

在数据库创建model (默认是sqlite)
python manage.py migrate

交互访问源码模块
python manage.py shell 

导入模块
from polls.models import Question, Choice

表的所有数据
Question.objects.all()

from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.question_text
q.pub_date
q.question_text = "What's up?"
q.save()
Question.objects.all()

Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

q = Question.objects.get(pk=1)
q.was_published_recently()

?这个choice_set是哪里来的呀
q.choice_set.all()

q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
c = q.choice_set.create(choice_text='Just hacking again', votes=0)
c.question
q.choice_set.all()

q.choice_set.count()

创建用户名密码
python manage.py createsuperuser

在poll/admin.py中添加表可以通过web管理

```
