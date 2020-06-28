from django.db import models

# Create your models here.
from utils.basic_models import BaseModel


class UserInfo(BaseModel):
    username = models.CharField(verbose_name='用户名',unique=True,max_length=12)
    password = models.CharField(verbose_name="密码",max_length=12)
    avatar = models.ImageField(verbose_name="头像")
    phone = models.PositiveSmallIntegerField(verbose_name="手机号",unique=True)
    email = models.EmailField(verbose_name="邮箱",unique=True)
    note = models.TextField(verbose_name="说明")

    class Meta:
        db_table = "user_info"
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name