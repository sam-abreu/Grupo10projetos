
from django.shortcuts import render, redirect
from .models import Doacao, Brinquedo
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def adminpage(request):
    return render(request, 'admin.html')

def home(request):
    return render(request, 'home.html')

def cadastro_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um usuário com esse nome')
        
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
        
    else:
        return render(request, 'cadastro_user.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.is_superuser:
                return redirect('adminpage')
            else:
                return redirect('home')
            
        else:
            return HttpResponse('Usuário ou senha inválidos!')

    else:
        return render(request, 'login.html')


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

def visualizar_doacao(request):
    doacoes = Doacao.objects.all()
    return render(request, 'visualizar_doacao.html', {'doacoes': doacoes})


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