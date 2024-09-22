from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from mail.apps import MailConfig
from mail import model_views as v


app_name = MailConfig.name

urlpatterns = [
                  path('', v.MailIndexView.as_view(), name='index'),  # главная для обычных пользователей
                  path('manager-online/', v.MailManagerView.as_view(), name='manager'),  # страница только для менеджера
                  path('mailing-detail/<int:pk>', cache_page(300)(v.MailingDetailView.as_view()), name='mailing_detail'),
                  path('mailing-create/', v.MailingCreateView.as_view(), name='mailing_create'),
                  path('mailing-update/<int:pk>', v.MailingUpdateView.as_view(), name='mailing_update'),
                  path('mailing-delete/<int:pk>', v.MailingDeleteView.as_view(), name='mailing_delete'),

                  path('client-list/', v.ClientListView.as_view(), name='client_list'),
                  path('client-create/', v.ClientCreateView.as_view(), name='client_create'),
                  path('client-detail/<int:pk>', cache_page(300)(v.ClientDetailView.as_view()), name='client_detail'),
                  path('client-update/<int:pk>', v.ClientUpdateView.as_view(), name='client_update'),
                  path('client-delete/<int:pk>', v.ClientDeleteView.as_view(), name='client_delete'),

                  path('message-list/', cache_page(300)(v.MessageListView.as_view()), name='message_list'),
                  path('message-create/', v.MessageCreateView.as_view(), name='message_create'),
                  path('message-detail/<int:pk>', cache_page(300)(v.MessageDetailView.as_view()), name='message_detail'),
                  path('message-update/<int:pk>', v.MessageUpdateView.as_view(), name='message_update'),
                  path('message-delete/<int:pk>', v.MessageDeleteView.as_view(), name='message_delete'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
