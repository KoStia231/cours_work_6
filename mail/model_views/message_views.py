from django.http import Http404
from django.views.generic import (
    CreateView, DetailView,
    DeleteView, UpdateView, ListView,
)

from mail.forms import MessageFormCreate, MessageFormUpdate
from mail.model_views.utils import ProfileSuccessUrl
from mail.models import Message
from users.views import MyLoginRequiredMixin


class MessageListView(MyLoginRequiredMixin, ListView):
    """Отображение списка клиентов"""
    model = Message
    template_name = 'mail/list_message.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(autor=self.request.user)
        return queryset


class MessageDetailView(MyLoginRequiredMixin, DetailView):
    """Отображение одного клиента"""
    model = Message
    template_name = 'mail/detail_message.html'


class MessageCreateView(ProfileSuccessUrl, MyLoginRequiredMixin, CreateView):
    """Страничка создания нового клиента"""
    model = Message
    form_class = MessageFormCreate
    template_name = 'mail/object_form.html'

    def form_valid(self, form):
        """Сохранение с автором"""
        product = form.save(commit=False)
        product.autor = self.request.user
        product.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        """привязка автора к форме """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class MessageDeleteView(ProfileSuccessUrl, MyLoginRequiredMixin, DeleteView):
    """Страничка удаления клиента"""
    model = Message
    template_name = 'mail/object_confirm_delete.html'

    def get_object(self, queryset=None):
        """Проверка, что создана текущем пользователем"""
        obj = super().get_object(queryset)

        if obj.autor != self.request.user:
            raise Http404("Вы не являетесь автором")
        return obj


class MessageUpdateView(ProfileSuccessUrl, MyLoginRequiredMixin, UpdateView):
    """Страничка редактирования клиента"""
    model = Message
    form_class = MessageFormUpdate
    template_name = 'mail/object_form.html'

    def form_valid(self, form):
        """Сохранение рассылки с автором"""
        version = form.save(commit=False)
        version.autor = self.request.user
        version.save()
        return super().form_valid(form)

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Проверка, что пользователь является автором версии
        if obj.autor != self.request.user:
            raise Http404("Вы не являетесь автором")
        return obj
