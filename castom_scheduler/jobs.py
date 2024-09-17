import logging
import smtplib

from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from mail.models import Mailing, Attempt

logger = logging.getLogger(__name__)


def schedule_mailing(mailing_id: int) -> None:
    mailing = Mailing.objects.get(id=mailing_id)
    for client in mailing.clients.all():
        try:
            send_mail(
                subject=mailing.message.title,
                message=mailing.message.content,
                from_email=EMAIL_HOST_USER,
                recipient_list=[client.email],
                fail_silently=False,  # не ломать приложение при ошибке отправки письма
            )
            logger.info(f"Sending mailing: {mailing.id}")
            Attempt.objects.create(mailings=mailing, status=Attempt.Status.SUCCESS)
            logger.info(f"Mailing {mailing.id} sent successfully.")
        except smtplib.SMTPException as e:
            Attempt.objects.create(mailings=mailing, status=Attempt.Status.FAILURE, server_response=str(e))
            logger.error(f"Failed to send mailing {mailing.id}: {e}")
