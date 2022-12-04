from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('main.urls')),
    path('', views.logar, name='login'),
]
