from django.shortcuts import render
from django.views.generic import TemplateView

from mail.models import Mailing


class MailIndexView(TemplateView):
    template_name = 'mail/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['test_var'] = Mailing.objects.all()
        return context
# Create your views here.
