from django.db import models
import json
from django.core import serializers
from datetime import datetime
import django.utils.timezone as timezone
# Create your models here.
# python manage.py createsuperuser


class User(models.Model):
    name = models.CharField(max_length=200, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=200)
    birthDay = models.DateTimeField()
    updateTime = models.DateTimeField('更新时间', auto_now=True)
    createTime = models.DateTimeField('创建时间', default=timezone.now)
    # phoneNumber = models.CharField(max_length=200)
    # password = models.CharField(max_length=200)

    def __str__(self):
        return self.name
