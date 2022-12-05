from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.logar, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('deslogar/', views.deslogar, name='deslogar'),
    path('receitaAdd/', views.receitaAdd, name='receitaAdd'),
    path('despesaAdd/', views.despesaAdd, name='despesaAdd'),
    path('categoriaAdd/', views.categoriaAdd, name='categoriaAdd'),
    path('receitaDel/<int:id>', views.receitaDel, name='receitaDel'),
    path('despesaDel/<int:id>', views.despesaDel, name='despesaDel'),
    path('categoriaDel/<int:id>', views.categoriaDel, name='categoriaDel'),
]
