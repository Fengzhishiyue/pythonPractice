import json
from enum import Enum, unique
from django.http import HttpResponse
# Create your models here.
# python manage.py createsuperuser


class ErrCode(object):
    OK = 200
    BadRequest = 400


