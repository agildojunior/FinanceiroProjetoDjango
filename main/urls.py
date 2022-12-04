from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('login/', views.logar, name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('deslogar/', views.deslogar, name='deslogar'),
]