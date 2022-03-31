from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, ListView, CreateView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *


class PostDetailView(DetailView):
    model = Post



def PostList(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 4)

    page = request.GET.get('page')
    post_list = paginator.get_page(page)

    return render(request, 'posts/post_list.html', {'post_list': post_list})


def Home(request):
    busca = request.GET.get('busca')
    if busca:
        post_list = Post.objects.filter(title__icontains=busca)

    else:

        post_list = Post.objects.all()

        paginator = Paginator(post_list, 4)

        page = request.GET.get('page')
        post_list = paginator.get_page(page)

    return render(request, 'posts/index.html', {'post_list': post_list})


def WebDesign(request):

    post_list = Post.objects.filter(categoria='Web Design')

    paginator = Paginator(post_list, 4)

    return render(request, 'posts/index.html', {'post_list': post_list})


def ProgramadorWeb(request):

    post_list = Post.objects.filter(categoria='Web Development')

    paginator = Paginator(post_list, 4)

    return render(request, 'posts/index.html', {'post_list': post_list})


def Linguagens(request):

    post_list = Post.objects.filter(categoria='Linguagens de Programação')

    paginator = Paginator(post_list, 4)

    return render(request, 'posts/index.html', {'post_list': post_list})


def Sobre(request):

    return render(request, 'posts/sobre.html')


class ImagensView(DetailView):
    model = Imagens


def Email(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        form.save()
        if form.is_valid():

            messages.success(request, 'Mensagem enviada com sucesso!')
            return redirect('/contato/')
    else:
        form = ContatoForm()
        return render(request, 'posts/contato.html', {'form': form})


            