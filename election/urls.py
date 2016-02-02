from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # url(r'', views.vote, name='vote')
    url(r'^(?P<question_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^logout',views.logout_page,name='logout'),
    url(r'^login',views.login_page,name='login')
]
