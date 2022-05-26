from django.urls import path
from . import views

app_name = 'test_app'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.hello, name='hello'),
    path('posts', views.posts_list, name='posts'),
    ]