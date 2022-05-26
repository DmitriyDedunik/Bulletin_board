from difflib import context_diff
from importlib.resources import contents
from multiprocessing import context
from re import template
from django.shortcuts import render

def hello(request):
    template = 'bulletin_board_app/index.html'
    result = 16
    context = {
        'template_var': result,
        'numbers': [1,2,3,4],
    }
    return render(request, template, context)
