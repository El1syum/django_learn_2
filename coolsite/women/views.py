from django.http import HttpResponseNotFound, Http404  # Http404 to raise 404
from django.shortcuts import render

from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def index(request):
    posts = Women.objects.all()
    cats = Category.objects.all()
    data = {'posts': posts,
            'cats': cats,
            'cat_selected': 0,
            'menu': menu,
            'title': 'Main page'}
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
    post = Women.objects.get(pk=post_id)
    data = {
        'title': f'{post.title}',
        'post': post
    }
    return render(request, 'women/post.html', context=data)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()
    data = {'posts': posts,
            'cats': cats,
            'cat_selected': cat_id,
            'menu': menu,
            'title': 'Отображение по рубрикам'}

    if len(posts) == 0:
        raise Http404
    return render(request, 'women/index.html', context=data)


# def categories(request, catid):
#     if request.GET:
#         print(request.GET)
#     if catid > 99:
#         return redirect('home', permanent=True)
#     return HttpResponse(f'<h2>Category {catid}</h2>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
