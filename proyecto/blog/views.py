from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)   #crea un ruta en la carpeta blog dentro de templates


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})