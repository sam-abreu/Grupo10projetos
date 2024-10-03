
from django.contrib import admin
from django.urls import path
from App_Projetos2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # A página inicial será servida por esta URL
]
