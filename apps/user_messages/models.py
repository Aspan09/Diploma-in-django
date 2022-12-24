from django.db import models
from profiles.models import UserNet
from django.core.exceptions import ValidationError


class Message(models.Model):
    sender = models.ForeignKey(UserNet, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(UserNet, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        verbose_name = "Сообщение",
        verbose_name_plural = "Сообщения"
        ordering = ('timestamp',)

    def __str__(self):
        return f"Пользователь {self.sender} отправил сообщение {self.receiver}"

    def save(self, *args, **kwargs):
        if self.sender == self.receiver:
            raise ValidationError("Пользователи не могут писать самим себе.")
        super().save(*args, **kwargs)
