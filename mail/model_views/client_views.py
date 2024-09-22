from django.views.generic import (
    DetailView,
)

from mail.forms import ClientFormCreate, ClientFormUpdate
from mail.model_views.message_views import (
    MessageCreateView, MessageDeleteView,
    MessageUpdateView, MessageListView
)
from mail.models import Client
from users.views import MyLoginRequiredMixin


class ClientListView(MessageListView):
    """Отображение списка клиентов"""
    model = Client
    template_name = 'mail/list_client.html'


class ClientDetailView(MyLoginRequiredMixin, DetailView):
    """Отображение одного клиента"""
    model = Client
    template_name = 'mail/detail_client.html'


class ClientCreateView(MessageCreateView):
    """Страничка создания нового клиента"""
    model = Client
    form_class = ClientFormCreate
    template_name = 'mail/object_form.html'


class ClientDeleteView(MessageDeleteView):
    """Страничка удаления клиента"""
    model = Client
    template_name = 'mail/object_confirm_delete.html'


class ClientUpdateView(MessageUpdateView):
    """Страничка редактирования клиента"""
    model = Client
    form_class = ClientFormUpdate
    template_name = 'mail/object_form.html'
