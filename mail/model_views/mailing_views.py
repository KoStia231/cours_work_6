from django.http import Http404
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    DeleteView, UpdateView, DetailView,
)

from mail.forms import MailingFormCreate, MailingFormUpdate, MailingFormUpdateManager
from mail.models import Mailing, Attempt
from users.views import MyLoginRequiredMixin


class MailingDetailView(MyLoginRequiredMixin, DetailView):
    """Отображение информации о рассылке"""
    model = Mailing
    template_name = 'mail/mailing_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получение попыток отправки писем для текущей рассылки
        context['attempt_list'] = Attempt.objects.filter(mailings=self.object)
        context['client_list'] = self.object.clients.all()
        return context


class MailingCreateView(MyLoginRequiredMixin, CreateView):
    """Страничка создания новой рассылки"""
    model = Mailing
    form_class = MailingFormCreate
    success_url = reverse_lazy('mail:mailing_detail')
    template_name = 'mail/object_form.html'

    def form_valid(self, form):
        """Сохранение с автором"""
        product = form.save(commit=False)
        product.autor = self.request.user
        product.save()
        return super().form_valid(form)

    def get_success_url(self):
        """Перенаправление на страницу рассылки после создания рассылки"""
        return reverse('mail:mailing_detail', args=[self.object.pk])

    def get_form_kwargs(self):
        """Привязка автора и фильтрация клиентов к форме"""
        kwargs = super().get_form_kwargs()
        # Фильтрация клиентов по пользователю
        kwargs['user'] = self.request.user
        return kwargs


class MailingDeleteView(MyLoginRequiredMixin, DeleteView):
    """Страничка удаления рассылки"""
    model = Mailing
    success_url = reverse_lazy('mail:index')
    template_name = 'mail/object_confirm_delete.html'

    def get_object(self, queryset=None):
        """Проверка, что создана текущем пользователем"""
        obj = super().get_object(queryset)

        if obj.autor != self.request.user:
            raise Http404("У вас нет прав на удаление этой рассылки")
        return obj


class MailingUpdateView(MyLoginRequiredMixin, UpdateView):
    """Страничка редактирования рассылки"""
    model = Mailing
    success_url = reverse_lazy('mail:index')
    template_name = 'mail/object_form.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # Проверка, что пользователь является автором
        if obj.autor != self.request.user and not self.request.user.has_perm('mail.manager'):
            raise Http404("Вы не являетесь автором этой рассылки")
        return obj

    def get_form_class(self):
        user = self.request.user
        if user == self.object.autor:
            return MailingFormUpdate
        if user.has_perm('mail.manager'):
            return MailingFormUpdateManager

