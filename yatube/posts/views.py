from django.shortcuts import render

# posts/views.py
from django.http import HttpResponse


# Главная страница
def index(request):
    return HttpResponse('Главная страница')

# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()
def group_posts(request, slug):
    return HttpResponse(f'Пост номер {slug}')
