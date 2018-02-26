from django.conf.urls import url
import views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^pro/$',views.pro),
    url(r'^city(\d+)/$',views.city),
    url(r'^htmlEditor/$',views.htmlEditor),
    url(r'^htmlEditorHandle/$', views.htmlEditorHandle),
    url(r'^cache1/$',views.cache1),
    url(r'^mysearch/$',views.mysearch),
    url(r'^celeryTest/$',views.celeryTest),

]