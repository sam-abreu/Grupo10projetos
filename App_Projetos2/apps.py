from django.apps import AppConfig


class AppProjetos2Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'App_Projetos2'

    def ready(self):
        # Aqui você importa os sinais para que eles sejam registrados
        import App_Projetos2.signals
