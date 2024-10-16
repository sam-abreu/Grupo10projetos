
from django.shortcuts import render, redirect
from .models import Doacao
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Brinquedo


def home(request):
    return render(request, 'home.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('admin')
            else:
                return redirect('home')
            
        else:
            return render(request, 'login.html', {'form': 'invalid'})


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


def add_brinquedo(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        preco = request.POST.get('preco')
        faixaetaria = request.POST.get('faixaetaria')
        material = request.POST.get('material')

        # Cria um novo brinquedo e salva no banco de dados
        novo_brinquedo = Brinquedo(
            nome=nome,
            preco=preco,
            faixaetaria=faixaetaria,
            material=material
        )
        novo_brinquedo.save()

        # Redireciona para a página principal ou onde você desejar
        return redirect('home')  # Certifique-se de que 'home' é o nome correto da URL

    return render(request, 'add_brinquedo.html')  # Renderiza um template para adicionar brinquedos

def comprar_brinquedo(request):
    brinquedos = Brinquedo.objects.all()  # Puxa todos os brinquedos do banco de dados
    return render(request, 'comprar_brinquedo.html', {'brinquedos': brinquedos})  # Passa os brinquedos para o template