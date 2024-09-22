from itertools import count

from django.views.generic import TemplateView
from django.db.models import Count

from blog.models import BlogEntry
from mail.models import Mailing, Client


class MailIndexView(TemplateView):
    """Отображение главной страницы сайта"""
    template_name = 'mail/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blog_list'] = BlogEntry.objects.order_by('-id')[:3]
        context['count_mailing_r'] = Mailing.objects.filter(status='R').count()
        context['count_mailing'] = Mailing.objects.all().count()
        context['clients'] = Client.objects.all().count()
        return context
