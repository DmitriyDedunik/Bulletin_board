from importlib.resources import contents
from multiprocessing import context
from re import template
from django.shortcuts import render

def hello(request):
    template = 'bulletin_board_app/index.html'
    context = {}
    return render(request, template, context)
