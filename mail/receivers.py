import logging
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from mail.jobs import schedule_mailing
from mail.models import Mailing
from mail.scheduler import scheduler
from mail.utils import get_mailing_period_trigger

logger = logging.getLogger(__name__)


@receiver(post_delete, sender=Mailing)
def delete_job(instance: Mailing, **kwargs):
    job_id = f'schedule_{instance.pk}'
    job = scheduler.get_job(job_id)
    if job:
        scheduler.remove_job(job_id)
        logger.info('Работа %s удалена', job_id)
    else:
        logger.warning('Ошибка работа %s, не найдена ', job_id)


@receiver(post_save, sender=Mailing)
def schedule_job(instance: Mailing, created: bool, **kwargs):
    job_id = f'schedule_{instance.pk}'
    trigger = get_mailing_period_trigger(instance)
    if created:
        if instance.status == Mailing.Status.CREATED:
            # Создать новое задание в планировщике
            scheduler.add_job(
                schedule_mailing,
                id=job_id,
                trigger=trigger,
                args=[instance.pk],
                max_instances=1,
                replace_existing=True,
            )
            logger.info('Job %s created', job_id)
        if instance.status == Mailing.Status.RUNNING:
            # Запустить задание, если статус "Запущена"
            scheduler.add_job(
                schedule_mailing,
                id=job_id,
                trigger=trigger,
                args=[instance.pk],
                max_instances=1,
                replace_existing=True,
            )
            logger.info('Job %s started', job_id)
        if instance.status == Mailing.Status.FINISHED:
            # Удалить задание из планировщика, если статус "Завершена"
            delete_job(instance)
    else:
        logger.info('Работ %s не найдено', job_id)


