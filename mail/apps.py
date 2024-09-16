from django.apps import AppConfig


class MailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail'
    verbose_name = 'Приложение рассылки'

    def ready(self):
        from .receivers import delete_job, schedule_job  # noqa: F401
