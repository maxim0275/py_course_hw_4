from django.db import models


class MailRecipient(models.Model):
    email = models.CharField(max_length=100, verbose_name="Адрес электронной почты", null=False, unique=True)
    full_name = models.CharField(max_length=100, verbose_name="Полное имя", null=False)
    comment = models.CharField(max_length=100, verbose_name="Комментарий")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'
        ordering = ['email']
        db_table = 'recipients'


class Message(models.Model):
    topic = models.CharField(max_length=100, verbose_name="Тема письма", null=False)
    body = models.TextField(verbose_name="Тело письма", null=False)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['topic']
        db_table = 'messages'


class MailManage(models.Model):
    STATUS_CHOICES = [
        ('CREATED', 'Создана'),
        ('STARTED', 'Запущена'),
        ('ENDED', 'Завершена')
    ]

    date_first_send = models.DateField(verbose_name='Дата и время первой отправки', null=False)
    date_last_send = models.DateField(verbose_name='Дата и время окончания отправки', null=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CREATED', verbose_name='Статус')
    message = models.ForeignKey(Message, on_delete=models.PROTECT, related_name='mailing_manage')
    recipient = models.ManyToManyField(MailRecipient)

    def __str__(self):
        recipients = ', '.join([str(recipient) for recipient in self.recipient.all()])
        return str(self.message) + ', ' + recipients

    class Meta:
        verbose_name = 'Пользователи_и_рассылки'
        verbose_name_plural = 'Пользователи_и_рассылки'
        ordering = ['message']
        db_table = 'mail_manage'


class MailAtt(models.Model):
    STATUS_CHOICES = [
        ('SUCC', 'Создана'),
        ('FAIL', 'Запущена')
    ]

    date_time_att = models.DateField(verbose_name='Дата и время попытки отправки', null=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='CREATED', verbose_name='Статус')
    server_answer = models.TextField(verbose_name="Ответ почтового сервера", null=False)
    mailing = models.ForeignKey(MailManage, on_delete=models.PROTECT, related_name='mail_att')

    def __str__(self):
        return str(self.mailing) + ', ' + str(self.date_time_att)

    class Meta:
        verbose_name = 'Попытка_рассылки'
        verbose_name_plural = 'Попытки_рассылки'
        ordering = ['date_time_att']
        db_table = 'mail_att'
