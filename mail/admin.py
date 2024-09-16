from django.contrib import admin

from mail.models import Attempt, Client, Mailing, Message


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    pass


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('id', 'period', 'message', 'start_date', 'status')
    list_filter = ('period', 'status')
    fieldsets = [
        ('Планирование', {'fields': ['start_date', 'period']}),
        ('Настройки', {'fields': ['clients', 'message']}),
        ('Информация', {'fields': ['status']}),
    ]


@admin.register(Attempt)
class AttemptAdmin(admin.ModelAdmin):
    list_display = ('id', 'mailing_id', 'created_at')
    list_filter = ('status',)
