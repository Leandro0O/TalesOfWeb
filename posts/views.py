from django.views.generic import DetailView, ListView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import *


class PostDetailView(DetailView):
    model = Post


def PostList(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)

    return render(request, 'posts/post_list.html', {'post_list': post_list})


def Home(request):
    busca = request.GET.get('busca')
    if busca:
        post_list = Post.objects.filter(title__icontains=busca)

    else:    

        post_list = Post.objects.all()

        paginator = Paginator(post_list, 4)

    return render(request, 'posts/index.html', {'post_list': post_list})


def Sobre(request):

    return render(request, 'posts/sobre.html')    


class ImagensView(DetailView):
    model = Imagens
