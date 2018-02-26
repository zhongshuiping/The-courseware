from django.contrib import admin
from booktest.models import BookInfo, HeroInfo
# Register your models here.

# 注册模型类
admin.site.register(BookInfo)
admin.site.register(HeroInfo)
