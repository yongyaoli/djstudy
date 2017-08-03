from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(u'用户名', max_length=100)
    passwd = models.CharField(u'密码', max_length=32)
    age = models.IntegerField(u'年龄')
    email = models.CharField(u'邮箱', max_length=50)
    phone = models.CharField(u'电话', max_length=11)
    add_time = models.DateTimeField(u'添加时间',auto_now_add=True, editable=True)

    def my_pro(self):
        return  self.name+'('+self.phone+')'

    my_pro.short_description='full name'
    full_name = property(my_pro)

    def __str__(self):
        return self.name
