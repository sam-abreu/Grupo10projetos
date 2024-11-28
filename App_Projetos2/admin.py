from django.contrib import admin
from .models import Brinquedo, Doacao, Inscricao, Profile
# Register your models here.

admin.site.register(Brinquedo)
admin.site.register(Doacao)
admin.site.register(Inscricao)
admin.site.register(Profile)