# 应用的urls文件
from django.conf.urls import url
from booktest import views

# index
# index2
urlpatterns = [
    url(r'^index$', views.index), # url地址和视图函数的对应关系
    url(r'^index2$', views.index2),
]