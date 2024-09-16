from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from mail.apps import MailConfig
from mail.views import (
    MailIndexView
)

app_name = MailConfig.name

urlpatterns = [
                  path('', MailIndexView.as_view(), name='index'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
