from django.conf.urls import url
import views
urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^(\d+)/(\d+)$',views.show,name='show'),
    url(r'^index2$', views.index2, name='index2'),
    url(r'^user1', views.user1, name='user1'),
    url(r'^user2', views.user2, name='user2'),
    url(r'^htmlTest$',views.htmlTest),
    url(r'^csrf1$',views.csrf1),
    url(r'^csrf2$',views.csrf2),
    url(r'^verifyCode$',views.verifyCode),
    url(r'^verifyTest1', views.verifyTest1),
    url(r'^verifyTest2', views.verifyTest2),

]


