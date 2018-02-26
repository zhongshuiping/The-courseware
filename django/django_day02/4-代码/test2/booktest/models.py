from django.db import models

# Create your models here.


# mysql 软删除
class BookInfo(models.Model):
    """图书模型类"""
    btitle = models.CharField(max_length=20, db_column='title')
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0) # 阅读量
    bcomment = models.IntegerField(default=0) # 评论量
    is_delete = models.BooleanField(default=False) # 软删除标记

    # bprice = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    """英雄人物模型类"""
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=200, null=True, blank=False)
    hbook = models.ForeignKey('BookInfo') # 关系属性, 一对多关系
    is_delete = models.BooleanField(default=False)  # 软删除标记

    def __str__(self):
        return self.hname


class NewsType(models.Model):
    """新闻类型类"""
    type_name = models.CharField(max_length=20) # 类型名称
    # 多对多关系属性
    type_news = models.ManyToManyField('NewsInfo')


class NewsInfo(models.Model):
    """新闻类"""
    news_title = models.CharField(max_length=128) # 新闻标题
    news_content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True) # 创建时间
    update_time = models.DateTimeField(auto_now=True) # 更新时间
    # 多对多关系属性
    # news_type = models.ManyToManyField('NewsType')


class EmployeeBasic(models.Model):
    """员工基本信息类"""
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=False)
    # ...
    # 一对一关系属性
    emp_detail = models.OneToOneField('EmployeeDetail')


class EmployeeDetail(models.Model):
    """员工详细信息类"""
    comment = models.CharField(max_length=200)
    # ...
    # 一对一关系属性
    # emp_basic = models.OneToOneField('EmployeeBasic')










