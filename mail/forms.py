from django import forms

from mail.models import Mailing, Client, Message
from users.forms import CustomFormMixin


class MailingFormCreate(CustomFormMixin, forms.ModelForm):
    """Форма рассылки"""

    class Meta:
        model = Mailing
        exclude = ('autor', 'status',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MailingFormCreate, self).__init__(*args, **kwargs)
        # Фильтрация клиентов по пользователю
        if user:
            self.fields['clients'].queryset = Client.objects.filter(autor=user)
        if user:
            self.fields['message'].queryset = Message.objects.filter(autor=user)


class MailingFormUpdate(CustomFormMixin, forms.ModelForm):
    """Форма редактирования рассылки"""

    # только два варианта для поля status
    STATUS_CHOICES = [
        ('R', 'запущена'),
        ('F', 'остановлена'),
    ]

    class Meta:
        model = Mailing
        exclude = ['autor']

    status = forms.ChoiceField(choices=STATUS_CHOICES, initial='R', label='статус рассылки')


class MailingFormUpdateManager(CustomFormMixin, forms.ModelForm):
    STATUS_CHOICES = [
        ('F', 'остановлена'),
    ]

    class Meta:
        model = Mailing
        fields = ['status', ]

    status = forms.ChoiceField(choices=STATUS_CHOICES, initial='F', label='статус рассылки')


class MessageFormCreate(CustomFormMixin, forms.ModelForm):
    """Форма создания сообщения"""

    class Meta:
        model = Message
        exclude = ('autor',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(MessageFormCreate, self).__init__(*args, **kwargs)


class MessageFormUpdate(CustomFormMixin, forms.ModelForm):
    """Форма редактирования сообщения"""

    class Meta:
        model = Message
        exclude = ('autor',)


class ClientFormCreate(MessageFormCreate):
    """Форма создания клиента"""

    class Meta:
        model = Client
        exclude = ('autor',)


class ClientFormUpdate(CustomFormMixin, forms.ModelForm):
    """Форма редактирования клиента"""

    class Meta:
        model = Client
        exclude = ('autor',)
