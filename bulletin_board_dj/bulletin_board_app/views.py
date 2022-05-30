from difflib import context_diff
from importlib.resources import contents
from multiprocessing import context
from re import template
from django.shortcuts import render
from .models import Post

def hello(request):
    template = 'bulletin_board_app/index.html'
    result = 16
    context = {
        'template_var': result,
        'numbers': [1,2,3,4],
    }
    return render(request, template, context)

def posts_list(request):
    template = 'bulletin_board_app/posts_list.html'
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, template, context)

def post_detail(request, post_id):
    template = 'bulletin_board_app/posts_info.html'
    post = Post.objects.get(pk=post_id)
    context = {
        'post': post,
    }
    return render(request, template, context)

