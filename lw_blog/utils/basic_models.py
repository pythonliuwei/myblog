from django.db import models


class BaseModel(models.Model):
    crt_ts = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    upd_ts = models.DateTimeField(verbose_name='更新时间', auto_now=True, null=True)

    class Meta:
        abstract = True
