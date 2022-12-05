from django.http.response import  HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from.models import Categoria, Despesa, Receita


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro/cadastro.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Esse usuario ja existe')

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()

        return render(request, 'login/login.html')


def logar(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login(request, user)
            return redirect('inicio')
        else:
            return render(request, 'login/login.html')


@login_required(login_url="/auth/login/")
def inicio(request): 
    categorias = Categoria.objects.all
    despesas = Despesa.objects.filter( user = request.user )
    receitas = Receita.objects.filter( user = request.user )
    return render(request, 'inicio/inicio.html',{'despesas':despesas,'receitas':receitas,'categorias':categorias})


@login_required
def deslogar(request):
    logout(request)
    return redirect('login')


@login_required
def receitaAdd(request):
    valor = request.POST.get('valor')
    descricao = request.POST.get('descricao')
    idcategoria = request.POST.get('categoria')
    categoria = Categoria.objects.filter( id = idcategoria ).first()

    Receita.objects.create(descricao=descricao, categoria=categoria, valor=valor, user=request.user)

    return redirect('inicio')


@login_required
def despesaAdd(request):
    valor = request.POST.get('valor')
    descricao = request.POST.get('descricao')
    idcategoria = request.POST.get('categoria')
    categoria = Categoria.objects.filter( id = idcategoria ).first()

    Despesa.objects.create(descricao=descricao, categoria=categoria, valor=valor, user=request.user)

    return redirect('inicio')


@login_required
def categoriaAdd(request):
    categoria = request.POST.get('categoria')

    Categoria.objects.create(nome=categoria)

    return redirect('inicio')


@login_required
def receitaDel(request, id):
    receita = Receita.objects.filter(id=id).first()
    receita.delete()
    return redirect('inicio')


@login_required
def despesaDel(request, id):
    despesa = Despesa.objects.filter(id=id).first()
    despesa.delete()
    return redirect('inicio')


@login_required
def categoriaDel(request, id):
    categoria = Categoria.objects.filter(id=id).first()
    categoria.delete()
    return redirect('inicio')
