from django.db import models

# Create your models here.
# 定义模型类


class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称, CharField说明是字符串类型，max_length指定字符串的最大长度
    btitle = models.CharField(max_length=20)
    # 出版日期, DateField说明是日期类型
    bpub_date = models.DateField()


# 英雄人物模型类HeroInfo
# 英雄名称 hname
# 英雄性别 hgender
# 英雄备注 hcomment
# 关系属性

# 一本图书包含很多个英雄人物
# 在一对多关系中，需要在多端对应的表中加外键
# 两个模型类存在一对多关系时，需要在多端的类中定义关系属性

class HeroInfo(models.Model):
    """英雄人物模型类"""
    hname = models.CharField(max_length=20) # 名称
    hgender = models.BooleanField(default=False) # 性别，default设置默认值为False, 代表男
    hcomment = models.CharField(max_length=200) # 备注
    hbook = models.ForeignKey('BookInfo') # 关系属性，建立BookInfo和HeroInfo之间一对多的关系
