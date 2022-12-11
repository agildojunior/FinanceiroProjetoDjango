from django.http.response import  HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from.models import Categoria, Despesa, Receita
from django.core.paginator import Paginator
from django.shortcuts import render
import re


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


@login_required
def senhaEdit(request):
    senha = request.POST.get('senha')
    user = request.user
    user.set_password(senha)
    user.save()
    return redirect('perfil')


@login_required
def userEdit(request):
    user = request.user
    username = request.POST.get('username')
    # --- Verifica se o username ja existe ---
    username2 = User.objects.filter(username=username).first()
    if username != user.username:
        if username2:
            return HttpResponse('Esse usuario esta indisponivel')
    # ----------------------------------------
    email= request.POST.get('email')
    User.objects.filter(id=user.id).update(username=username,email=email)
    return redirect('inicio')


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
    totalreceita = 0
    totaldespesa = 0
    for receit in receitas:
        totalreceita += receit.valor
    for despes in despesas:
        totaldespesa += despes.valor
        
    # --- paginação ---
    paginator1 = Paginator(receitas, 7)
    paginator2 = Paginator(despesas, 7)
    
    page_number = request.GET.get('page')

    page_obj1 = paginator1.get_page(page_number)
    page_obj2 = paginator2.get_page(page_number)
    
    # --- /paginação ---
    return render(request, 'inicio/inicio.html',{'despesas':page_obj2,'receitas':page_obj1,'categorias':categorias,'totalreceita':totalreceita,'totaldespesa':totaldespesa,'saldo':totalreceita-totaldespesa})


@login_required(login_url="/auth/login/")
def grafico(request): 
    categorias = Categoria.objects.all
    despesas = Despesa.objects.filter( user = request.user )
    receitas = Receita.objects.filter( user = request.user )
    totalreceita = 0
    totaldespesa = 0
    for receit in receitas:
        totalreceita += receit.valor
    for despes in despesas:
        totaldespesa += despes.valor
        
    return render(request, 'grafico/grafico.html',{'despesas':despesas,'receitas':receitas,'categorias':categorias,'totalreceita':totalreceita,'totaldespesa':totaldespesa,'saldo':totalreceita-totaldespesa})


@login_required(login_url="/auth/login/")
def editperfil(request): 
    user = request.user
    return render(request, 'perfil/perfil.html',{'user':user})



@login_required
def deslogar(request):
    logout(request)
    return redirect('login')


@login_required
def receitaAdd(request):
    valor = float(re.sub('[^0-9]', '', request.POST.get('valor')))/100
    descricao = request.POST.get('descricao')
    idcategoria = request.POST.get('categoria')
    categoria = Categoria.objects.filter( id = idcategoria ).first()

    Receita.objects.create(descricao=descricao, categoria=categoria, valor=valor, user=request.user)

    return redirect('inicio')


@login_required
def despesaAdd(request):
    valor = float(re.sub('[^0-9]', '', request.POST.get('valor')))/100
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


@login_required
def receitaEdit(request, id):
    receita = Receita.objects.filter(id=id).first()
    categorias = Categoria.objects.all
    return render(request, 'editar/editReceitas.html',{'receita':receita,'categorias':categorias})
@login_required
def receitaEdit2(request, id):
    idcategoria = request.POST.get('categoria')
    valor = float(re.sub('[^0-9]', '', request.POST.get('valor')))/100
    descricao = request.POST.get('descricao')
    categoria = Categoria.objects.filter( id = idcategoria ).first()
    Receita.objects.filter(id=id).update(valor=valor,descricao=descricao,categoria=categoria)
    return redirect('inicio')


@login_required
def despesaEdit(request, id):
    despesa = Despesa.objects.filter(id=id).first()
    categorias = Categoria.objects.all
    return render(request, 'editar/editDespesas.html',{'despesa':despesa,'categorias':categorias})
@login_required
def despesaEdit2(request, id):
    idcategoria = request.POST.get('categoria')
    valor = float(re.sub('[^0-9]', '', request.POST.get('valor')))/100
    descricao = request.POST.get('descricao')
    categoria = Categoria.objects.filter( id = idcategoria ).first()
    Despesa.objects.filter(id=id).update(valor=valor,descricao=descricao,categoria=categoria)
    return redirect('inicio')