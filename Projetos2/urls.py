
from django.contrib import admin
from django.urls import path
from App_Projetos2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.add_brinquedo, name='add_brinquedo'),
    path('cadastro_user/', views.cadastro_user, name='cadastro_user'),
    path('home/', views.home, name='home'),
    path('doar/', views.add_doacao, name='doar'),
    path('comprar/', views.comprar_brinquedo, name='comprar_brinquedo'),
    path('add-brinquedo/', views.add_brinquedo, name='add_brinquedo'),
]
