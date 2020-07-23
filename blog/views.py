from django.shortcuts import render, get_object_or_404
from .models import BlogPost
from django.core.paginator import Paginator
import random



def blog(request):
    postagens = BlogPost.objects.filter(publicada=True).order_by('-data_modificacao')
    destaques = BlogPost.objects.filter(destaque=True).order_by('-data_modificacao')

    paginator = Paginator(postagens, 4)
    page = request.GET.get('page')
    postagens_por_pagina = paginator.get_page(page)

    dados = {
        'postagens': postagens_por_pagina,
        'destaques': destaques
    }

    return render(request, 'blog/blog.html', dados)

def blog_post(request, titulo):
    postagem = get_object_or_404(BlogPost, titulo=titulo)
    destaques = BlogPost.objects.filter(destaque=True).order_by('-data_modificacao')
    if len(destaques) >= 2:
        destaques_a_exibir = destaques[0:2]
    else:
        destaques_a_exibir = destaques

    postagem_e_destaque = {
        'postagem': postagem,
        'destaques': destaques_a_exibir
    }

    return render(request, 'blog/blog-post.html', postagem_e_destaque)
