from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import User
from datetime import datetime
from django.core import serializers
import django.utils.timezone as timezone
import json
from RAndL.const.errcode import ErrCode
from django.forms.models import model_to_dict
# Create your views here.


def index(request):
    return HttpResponse('Welcome RegistAndLogin!')


def login(request):
    return render(request, 'login.html')


def addUser(request):
    if(request.method == 'POST'):
        try:
            # 获取json字符串
            postBody = json.loads(request.body)
            # 初始化一个user对象
            user = User(**postBody)
            # 处理属性
            user.birthDay = datetime.strptime(user.birthDay, '%Y%m%d')
            # 存入数据库
            user.save()
            result = {
                "code": ErrCode.OK,
                "msg": "存储成功"
            }
            return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")
        except Exception as e:
            result = {
                "code": ErrCode.BadRequest,
                "err": "存储失败"
            }
            return HttpResponse(json.dumps(result, ensure_ascii=False), content_type="application/json")

    else:
        return HttpResponse('wrong!')


def getUsers(request):
    # 转化为list
    data = {}
    users = User.objects.all().values()
    data['data'] = list(users)
    return JsonResponse(data)

    # serializers序列化
    # # 查询所有User对象
    # users = User.objects.all()
    # # 序列化
    # usersJson = serializers.serialize('json', users)
    # # 返回
    # return HttpResponse(usersJson, content_type="application/json")

    # TODO 第三种方法
