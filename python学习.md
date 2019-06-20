## django搭建web项目

参考官方教程：[https://docs.djangoproject.com/zh-hans/2.1/intro/tutorial01/](https://docs.djangoproject.com/zh-hans/2.1/intro/tutorial01/)

 #### 一、创建项目
**第一步**

	cd到想要创建项目的目录下执行
	$ django-admin startproject [项目名字]
	如果执行不了百度搜索解决方案
**第二步**
		
	python manage.py runserver
	如果你想更换服务器的监听端口，请使用命令行参数。举个例子
	下面的命令会使服务器监听 8080 端口：
	python manage.py runserver 8080
**第三步**
```
创建应用：
python manage.py startapp [应用名字]
```
**第四步**
```
设置路由：
应用文件夹中新建urls.py
	from django.urls import path
	from . import views
	urlpatterns = [
	    path('', views.index, name='index'),
	]
views.py中:
	from django.http import HttpResponse
	def index(request):
	    return HttpResponse("Hello, world. You're at the index.")
在项目文件urls.py中：
	from django.contrib import admin
	from django.urls import include, pathÏ
	urlpatterns = [
	    path('polls/', include('[应用名字].urls')),
	    path('admin/', admin.site.urls),
	]		    
```
至此项目骨架搭建完成
 #### 二、项目数据库配置
 参考：[https://docs.djangoproject.com/en/2.2/ref/settings/#databases](https://docs.djangoproject.com/en/2.2/ref/settings/#databases)
 **配置**
```python
#settings.py中以mysql为例子
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'polls',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': 'localhost',
		'PORT': '3306',
	}
}
可能出现问题：
1.django.core.exceptions.ImproperlyConfigured: Error loading MySQLdb module: No module named 'MySQLdb'.
Did you install mysqlclient or MySQL-python?
解决方法：
项目__init__.py中添加
import pymysql
pymysql.install_as_MySQLdb()
其他问题：
1、raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__) 　　　
django.core.exceptions.ImproperlyConfigured: mysqlclient 1.3.13 or newer is required; you have 0.9.3. 
　　
解决办法：C:\Python37\Lib\site-packages\django\db\backends\mysql（python安装目录）打开base.py，
注释掉以下内容： 　　　　　　　
if version < (1, 3, 13): 　　　　　　　　　　
	raise ImproperlyConfigured('mysqlclient 1.3.13 or newer is required; you have %s.' % Database.__version__) 
	　　
2、File "C:\Python37\lib\site-packages\django\db\backends\mysql\operations.py", line 146, 
in last_executed_query 　　 
	query = query.decode(errors='replace') 　　
	AttributeError: 'str' object has no attribute 'decode' 
	　　
解决办法：打开此文件把146行的decode修改为encode
```
**模型创建实例**
```python
在应用文件的models.py中
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=200)
    birth = models.DateTimeField('date published')
	age = models. models.IntegerField()
```
**激活模型**
```python
# setting.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	#若应用名为polls，增加下一行
	'polls.apps.PollsConfig',
]

之后执行
$ python manage.py makemigrations polls
返回类似输出
Migrations for 'polls':
  polls/migrations/0001_initial.py:
    - Create model Choice
    - Create model Question
    - Add field question to choices

再执行
$ python manage.py migrate
返回类似输出
Operations to perform:
 Apply all migrations: admin, auth, contenttypes, polls, sessions
Running migrations:
 Rendering model states... DONE
 Applying polls.0001_initial... OK
```
**创建管理员账号**
```
$ python manage.py createsuperuser
```
键入你想要使用的用户名，然后按下回车键：
```
Username: admin
```
然后提示你输入想要使用的邮件地址：
```
Email address: admin@example.com
```
最后一步是输入密码。你会被要求输入两次密码，第二次的目的是为了确认第一次输入的确实是你想要的密码。
```
Password: **********
Password (again): *********
Superuser created successfully.
```
最后启动服务器，并访问http://127.0.0.1:8000/admin
**在管理页面中加入表格**
打开 `[应用名字]/admin.py` 文件，把它编辑成下面这样：
```python
from django.contrib import admin

from .models import Person

admin.site.register(Person)
```
就能在管理页面中操作该表格，增删改查等

#### 三、Restful传参实例
`[应用名称]/views.py`里添加函数
```python
def hello(request, req_name):
    return HttpResponse("Hello %s!" % req_name)
```
`[应用名称].urls` 模块里
```python
from django.urls import path

from . import views

urlpatterns = [
    path('hello/<str:req_name>/', views.helloÏ, name='hello'),
]
```
快捷函数render以及前面出现问题
参考：[https://docs.djangoproject.com/zh-hans/2.1/intro/tutorial03/](https://docs.djangoproject.com/zh-hans/2.1/intro/tutorial03/)



***
***
只考虑后端代码，前端html模版templates不进行学习
***
### 操作mongodb数据库
参考：

1. [https://blog.csdn.net/weixin_42042483/article/details/83083926#1mongodb__mongoengine_2](https://blog.csdn.net/weixin_42042483/article/details/83083926#1mongodb__mongoengine_2)
2. [https://blog.csdn.net/w18211679321/article/details/83065209](https://blog.csdn.net/w18211679321/article/details/83065209)
