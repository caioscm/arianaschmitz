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

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = reqst.Request(url, data=data)
        response = reqst.urlopen(req, context=ssl.create_default_context(cafile=certifi.where()))
        result = json.loads(response.read().decode())
        ''' End reCAPTCHA validation '''

        if result['success']:
            try:
                print("Entrou no envio")
                print(send_mail(subject="Mensagem do site Ariana Nutricionista",
                          message=message,
                          from_email=email,
                          recipient_list=['vittorvc@gmail.com'],
                          fail_silently=False)
                )
            except BadHeaderError:
                messages.error(request, 'Ocorreu um erro ao enviar a mensagem.')

            return redirect('home')
        else:
            messages.error(request, 'É preciso confirmar o captcha!')
            return redirect('home')
    else:
        return render(request, 'nutri/contato.html')