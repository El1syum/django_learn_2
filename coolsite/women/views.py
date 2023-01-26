from django.http import HttpResponse, HttpResponseNotFound  # Http404 to raise 404
from django.shortcuts import render, redirect

from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def index(request):
    posts = Women.objects.all()
    data = {'posts': posts, 'menu': menu, 'title': 'Main page'}
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About us'})


def add_page(request):
    ...


def contact(request):
    ...


def login(request):
    ...


def show_post(request, post_id):
    return HttpResponse(f'{post_id=}')


# def categories(request, catid):
#     if request.GET:
#         print(request.GET)
#     if catid > 99:
#         return redirect('home', permanent=True)
#     return HttpResponse(f'<h2>Category {catid}</h2>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
