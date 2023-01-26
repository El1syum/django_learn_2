from django.http import HttpResponse, HttpResponseNotFound  # Http404 to raise 404
from django.shortcuts import render, redirect

from .models import *

menu = ['О сайте', 'Добавить статью', 'Обратная связь', 'Войти']


def index(request):
    posts = Women.objects.all()
    return render(request, 'women/index.html', {'posts': posts, 'menu': menu, 'title': 'Main page'})


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About us'})


def categories(request, catid):
    if request.GET:
        print(request.GET)
    if catid > 99:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h2>Category {catid}</h2>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
