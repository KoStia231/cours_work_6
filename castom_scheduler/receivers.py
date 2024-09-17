import logging

from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from castom_scheduler.jobs import schedule_mailing
from castom_scheduler.scheduler import scheduler
from castom_scheduler.utils import get_mailing_period_trigger
from mail.models import Mailing

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Mailing)
def schedule_job(instance: Mailing, created: bool, **kwargs):
    job_id = f'schedule_{instance.pk}'
    status = instance.status
    trigger = get_mailing_period_trigger(instance)
    print(status)  # надо было

    if status == 'R':
        scheduler.add_job(
            schedule_mailing,
            id=job_id,
            trigger=trigger,
            args=[instance.pk],
            max_instances=1,
            replace_existing=True,
        )


        logger.info('Job %s CREATE', job_id)
    if status == 'F':
        scheduler.remove_job(job_id)
        logger.info('Job %s DELETE', job_id)


@receiver(post_delete, sender=Mailing)
def delete_job(instance: Mailing, **kwargs):
    job_id = f'schedule_{instance.pk}'
    job = scheduler.get_job(job_id)
    if job:
        scheduler.remove_job(job_id)
        logger.info('Работа %s удалена', job_id)
    else:
        logger.warning('Ошибка работа %s, не найдена ', job_id)
