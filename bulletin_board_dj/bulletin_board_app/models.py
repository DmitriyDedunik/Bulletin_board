from venv import create
from django.db import models

class Post(models.Model):
    text = models.TextField(verbose_name='Текст поста')
    create = models.DateTimeField(verbose_name='Время создания', auto_now_add=True)

