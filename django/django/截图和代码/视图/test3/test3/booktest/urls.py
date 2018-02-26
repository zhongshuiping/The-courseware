from django.conf.urls import url
import views
import views1

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(?P<p2>\d+)/(?P<p3>\d+)/(?P<p1>\d+)/$',views.detail,name='detail'),
    url(r'^getTest1/$',views.getTest1),
    url(r'^getTest2/$', views.getTest2),
    url(r'^getTest3/$', views.getTest3),

    url(r'^postTest1/$',views.postTest1),
    url(r'^postTest2/$', views.postTest2),

    url(r'^cookieTest/$', views.cookieTest),

    url(r'^redTest1/$', views.redTest1),
    url(r'^redTest2/$', views.redTest2),

    url(r'^session1/$', views.session1),
    url(r'^session2/$', views.session2),
    url(r'^session2_handle/$', views.session2_handle),
    url(r'^session3/$', views.session3),

]
