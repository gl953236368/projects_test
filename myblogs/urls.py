from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'myblogs'

urlpatterns = [
    path('', views.get_home, name='home'),
    path('<int:article_id>/detailes', views.get_detail, name='detail'),
    path('<int:article_id>/saveComments', views.save_comments, name='comments'),
    path('<int:article_id>/login', views.login, name='login'),
    path('<int:article_id>/loginOut', views.loginout, name='loginOut')
]