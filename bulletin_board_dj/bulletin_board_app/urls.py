from django.urls import path
from . import views

app_name = 'test_app'
urlpatterns = [
    path('hello/', views.hello, name='hello'),
    path('', views.hello, name='hello'),
    path('posts/', views.posts_list, name='posts'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
    # path('group/<int:group_id>/', views.group, name='group'),
    path('groups/', views.groups_list, name='groups'),
    ]