import logging

from django.apps import AppConfig

from castom_scheduler.scheduler import scheduler

log = logging.getLogger(__name__)


class MailConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mail'
    verbose_name = 'Приложение рассылки'

    def ready(self):
        from castom_scheduler.scheduler import scheduler
        from castom_scheduler.receivers import delete_job, schedule_job  # noqa
        import sys

        if 'runserver' in sys.argv or 'your_desired_command' in sys.argv:
            if not scheduler.running:
                scheduler.start()
                log.info('Scheduler started')
