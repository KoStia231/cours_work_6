from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import TemplateView

from mail.models import  Mailing
from users.models import User
from users.views import MyLoginRequiredMixin


class MailManagerView(MyLoginRequiredMixin, PermissionRequiredMixin,  TemplateView):
    """Отображение главной страницы сайта"""
    permission_required = 'mail.manager'
    template_name = 'mail/manager.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_list'] = User.objects.all()
        context['mailings_list'] = Mailing.objects.all()
        return context
