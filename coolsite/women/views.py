from django.http import HttpResponseNotFound, Http404  # Http404 to raise 404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from .forms import *
from .models import *

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


class WomenHome(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


# def index(request):
#     posts = Women.objects.all()
#     data = {'posts': posts,
#             'cat_selected': 0,
#             'menu': menu,
#             'title': 'Main page'}
#     return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'About us'})


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = AddPostForm()
    data = {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form
    }
    return render(request, 'women/addpage.html', data)


def contact(request):
    ...


def login(request):
    ...


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': post.title,
        'post': post,
        'menu': menu,
        'cat_selected': post.cat_id
    }
    return render(request, 'women/post.html', context=data)


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = f"Категория - {context['posts'][0].cat}"
        context['cat_selected'] = context['posts'][0].cat_id

        return context

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


# def show_category(request, cat_slug):
#     cat = get_object_or_404(Category, slug=cat_slug)
#     posts = Women.objects.filter(cat__slug=cat_slug)
#     data = {'posts': posts,
#             'cat_selected': cat.pk,
#             'menu': menu,
#             'title': 'Отображение по рубрикам'}
#
#     if len(posts) == 0:
#         raise Http404
#     return render(request, 'women/index.html', context=data)


# def categories(request, catid):
#     if request.GET:
#         print(request.GET)
#     if catid > 99:
#         return redirect('home', permanent=True)
#     return HttpResponse(f'<h2>Category {catid}</h2>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
