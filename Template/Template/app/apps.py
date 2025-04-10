from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'


class YourAppConfig(AppConfig):
    name = 'app'

    def ready(self):
        import app.signals