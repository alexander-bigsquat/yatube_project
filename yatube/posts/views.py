from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def headers(request):
    template = 'includes/header.html'
    return render(request, template)


def index(request):
    template = 'posts/index.html'
    title = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
    }
    return render(request, template, context)


def group(request):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text
    }
    return render(request, template, context)


def footer(request):
    template = 'includes/footer.html'
    return render(request, template)


def group_posts(request, slug):
    return HttpResponse(f'Тут что-то о Твиксе {slug}')
