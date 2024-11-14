
from django.contrib import admin
from django.urls import path
from App_Projetos2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_login, name='login'),
    path('cadastro_user/', views.cadastro_user, name='cadastro_user'),
    path('home/', views.home, name='home'),
    path('adminpage/', views.adminpage, name='adminpage'),
    path('doar/', views.add_doacao, name='doar'),
    path('gerar-relatorio/', views.gerar_relatorio_doacoes, name='gerar_relatorio'),
    path('visualizar_doacao/', views.visualizar_doacao, name='visualizar_doacao'),
    path('comprar/', views.comprar_brinquedo, name='comprar_brinquedo'),
    path('add-brinquedo/', views.add_brinquedo, name='add_brinquedo'),
    path('sugestao_brinquedo', views.sugestao_brinquedo, name='sugestao_brinquedo'),
    path('residuos/', views.residuos, name='residuos'),
    path('trabalhe-conosco/', views.trabalhe_conosco, name='trabalhe_conosco'),
]
