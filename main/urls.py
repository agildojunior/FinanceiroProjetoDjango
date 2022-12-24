from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'), 
    path('login/', views.logar, name='login'),
    path('inicio/', views.inicio, name='inicio'), 
    path('grafico/', views.grafico, name='grafico'), 
    path('perfil/', views.editperfil, name='perfil'), 
    path('deslogar/', views.deslogar, name='deslogar'), 
    path('receitaAdd/', views.receitaAdd, name='receitaAdd'), 
    path('despesaAdd/', views.despesaAdd, name='despesaAdd'), 
    path('categoriaAdd/', views.categoriaAdd, name='categoriaAdd'), 
    path('receitaDel/<int:id>', views.receitaDel, name='receitaDel'),
    path('despesaDel/<int:id>', views.despesaDel, name='despesaDel'),
    path('categoriaDel/<int:id>', views.categoriaDel, name='categoriaDel'),
    path('receitaEdit/<int:id>', views.receitaEdit, name='receitaEdit'),
    path('receitaEdit2/<int:id>', views.receitaEdit2, name='receitaEdit2'),
    path('despesaEdit/<int:id>', views.despesaEdit, name='despesaEdit'),
    path('despesaEdit2/<int:id>', views.despesaEdit2, name='despesaEdit2'),
    path('userEdit', views.userEdit, name='userEdit'),
    path('senhaEdit', views.senhaEdit, name='senhaEdit'),
]
