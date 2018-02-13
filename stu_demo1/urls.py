from django.conf.urls import url
from stu_demo1 import views

urlpatterns = [
    url('login', views.login),
    url('home', views.home),
    url('detail/(d*)', views.detail, name='indexx'),
]
