from django.apps import AppConfig


class ReposterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vk_scripts.reposter'

    def ready(self):
        from .scheduler import scheduler
        scheduler.start()
