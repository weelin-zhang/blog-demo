from django.db import models

# Create your models here.

from django.db import models


class UserInfo(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'姓名')
    age = models.CharField(max_length=3, verbose_name=u'年龄')

    class Meta:
        verbose_name = u'用户信息表'
        verbose_name_plural = verbose_name
