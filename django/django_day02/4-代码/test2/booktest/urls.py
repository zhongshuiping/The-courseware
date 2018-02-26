from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index), # 首页
    url(r'^create$', views.create), # 添加图书
    url(r'^delete(\d+)$', views.delete), # 删除图书
]