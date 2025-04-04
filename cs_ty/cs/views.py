from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404

def index(request):
    return HttpResponse("Главная страница CS_TY")

def category(request, cat_id):
    return HttpResponse(f"Категория ID: {cat_id}")

def category_slug(request, cat_slug):
    if request.GET:
        print(request.GET.get('param'))
    return HttpResponse(f"Slug: {cat_slug}")

def custom_404(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена (CS_TY)</h1>")

def archive(request, year):
    if year > 2023:
        return redirect('home')
    return HttpResponse(f"Архив за {year} год")