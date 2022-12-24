from django.db import models
from profiles.models import UserNet


class Group(models.Model):
    name = models.CharField('Название', max_length=30)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['name']

    def __str__(self):
        return self.name


class UserSendMessageInGroup(models.Model):
    user_sender = models.ForeignKey(
        UserNet,
        on_delete=models.CASCADE,
        verbose_name='От пользователя',
        related_name='sender_group'
    )

    message = models.TextField(max_length=1200)
    receiver_group = models.ManyToManyField(Group)

    class Meta:
        verbose_name = 'Сообщение в группу'
        verbose_name_plural = 'Сообщения в группу'
        ordering = ['message']

    def __str__(self):
        return '{}: {}'.format(self.user_sender, self.message)


