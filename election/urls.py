from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'', views.vote, name='vote')
    url(r'^(?P<question_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^login',views.logon_page,name='logon_page'),
    url(r'^logout',views.logout_page,name='logout')
]
