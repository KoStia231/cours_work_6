from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=255, verbose_name='имя')
    comment = models.TextField(blank=True, default='', verbose_name='комментарий')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.email


class Message(models.Model):
    title = models.CharField(max_length=255, verbose_name='тема письма')
    content = models.TextField(verbose_name='письмо')

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'

    def __str__(self):
        return self.title


class Mailing(models.Model):
    class Period(models.TextChoices):
        CUSTOM = 'C', 'кастомный'
        DAILY = 'D', 'каждый день'
        WEEKLY = 'W', 'каждую неделю'
        MONTHLY = 'M', 'каждый месяц'

    class Status(models.TextChoices):
        CREATED = 'C', 'создана'
        RUNNING = 'R', 'запущена'
        FINISHED = 'F', 'остановлена'

    start_date = models.DateTimeField(verbose_name='дата старта')
    period = models.CharField(choices=Period.choices, max_length=1, verbose_name='период рассылки')
    status = models.CharField(choices=Status.choices, max_length=1, default=Status.CREATED,
                              verbose_name='статус рассылки')
    clients = models.ManyToManyField(Client)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='mailings', verbose_name='сообщение')

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        return f'{self.get_period_display()} рассылка {self.message.title}'


class Attempt(models.Model):
    class Status(models.IntegerChoices):
        SUCCESS = 1, 'Удачно'
        FAILURE = 0, 'Провал'

    mailings = models.ForeignKey(Mailing, on_delete=models.CASCADE, related_name='attempts', verbose_name='Рассылка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='создана')
    status = models.SmallIntegerField(choices=Status.choices, verbose_name='статус')
    server_response = models.TextField(blank=True, default='', verbose_name='ответ от сервера')

    def __str__(self):
        return f'{self.mailings} attempt at {self.created_at}'

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылки'
