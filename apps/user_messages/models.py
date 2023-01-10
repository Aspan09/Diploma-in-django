from django.db import models
from profiles.models import UserNet
from django.core.exceptions import ValidationError
from django.utils import timezone


class Message(models.Model):
    sender = models.ForeignKey(UserNet, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(UserNet, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)

    data_send = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Сообщение",
        verbose_name_plural = "Сообщения"
        ordering = ('data_send',)

    def __str__(self):
        return f"Пользователь {self.sender} отправил сообщение {self.receiver}"

    def save(self, *args, **kwargs):
        if self.sender == self.receiver:
            raise ValidationError("Пользователи не могут писать самим себе.")
        super().save(*args, **kwargs)
