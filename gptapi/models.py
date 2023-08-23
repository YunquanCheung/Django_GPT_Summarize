from django.db import models

# Create your models here.


class SUMMARIZES(models.Model):
     timestamp = models.DateTimeField(auto_now=True, verbose_name="请求时间")
     input_text = models.CharField(max_length=1000, verbose_name="输入内容")
     summary = models.CharField(max_length=1000,  verbose_name="总结内容")
     class Meta:
         db_table = "summarizes"
