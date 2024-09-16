from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from mail.models import Mailing


def schedule_mailing(mailing_id: int) -> None:
    mailing = Mailing.objects.get(id=mailing_id)
    for client in mailing.clients.all():
        send_mail(
            subject=mailing.message.title,
            message=mailing.message.content,
            from_email=EMAIL_HOST_USER,
            recipient_list=[client.email],
        )




