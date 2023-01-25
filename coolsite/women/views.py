from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


def index(request):
    return HttpResponse('<h2>Women</h2>')


def categories(request, catid):
    if request.GET:
        print(request.GET)
    if catid > 99:
        return redirect('home', permanent=True)
    return HttpResponse(f'<h2>Category {catid}</h2>')


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
