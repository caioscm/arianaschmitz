import json
import urllib
import certifi
import ssl
from urllib import request as reqst

from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail, BadHeaderError
from django.core.paginator import Paginator
from django.conf import settings
from django.contrib import messages
from .models import Receitas

# Create your views here.

def home(request):
    return render(request, 'nutri/home.html')


def sobre(request):
    return render(request, 'nutri/sobre.html')


def contato(request):
    return render(request, 'nutri/contato.html')


def receitas(request):
    receitas = Receitas.objects.order_by('-update_at')

    paginator = Paginator(receitas, 3)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina,
    }

    return render(request, 'nutri/receitas.html', dados)


def receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    ingredientes = receita.ingredientes.split('\n')

    receita_a_exibir = {
        'receita': receita,
        'ingredientes': ingredientes
    }

    print(ingredientes)

    return render(request, 'nutri/receita.html', receita_a_exibir)


def send_message(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        texto_mensagem = request.POST['mensagem']
        message = f"O usuário {nome} mandou esta mensagem: {texto_mensagem}.\nPara respondê-la, envie um e-mail para" \
                  f" {email}"

        print("Entrou no envio")
        print(send_mail(subject="Mensagem do site Ariana Nutricionista",
                  message=message,
                  from_email=email,
                  recipient_list=['vittorvc@gmail.com'],
                  fail_silently=False)
        )
        return redirect('home')
    else:
        return render(request, 'nutri/contato.html')