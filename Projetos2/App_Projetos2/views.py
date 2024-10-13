
from django.shortcuts import render, redirect
from .models import Doacao

def home(request):
    return render(request, 'home.html')

def add_doacao(request):
    if request.method == 'POST':
        nome_doador = request.POST.get('nome_doador')
        email_doador = request.POST.get('email_doador')
        telefone_doador = request.POST.get('telefone_doador')
        tipo_doacao = request.POST.get('tipo_doacao')
        descricao = request.POST.get('descricao')

        doacao = Doacao(
            nome_doador=nome_doador,
            email_doador=email_doador,
            telefone_doador=telefone_doador,
            tipo_doacao=tipo_doacao,
            descricao=descricao
        )
        doacao.save()

        return redirect('home')  # Redireciona para a página inicial após a doação ser cadastrada

    return render(request, 'doar.html')
