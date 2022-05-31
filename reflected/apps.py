from django.apps import AppConfig


class ReflectedConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reflected'
