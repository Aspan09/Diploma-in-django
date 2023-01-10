from django.contrib.auth.models import AbstractUser
from django.db import models


GENDER_CHOICES = [
    ['male', u"Мужской"],
    ['female', u"Женский"],
]

REL_CHOICES = [
    ['none', u"Не определенно"],
    ['single', u"Холост"],
    ['in_a_rel', u"В отношениях"],
    ['engaged', u"Помолвлен(а)"],
    ['married', u"Женат/Замужем"],
    ['in_love', u"Влюблен(а)"],
    ['complicated', u"Все сложно"],
]


class UserNet(AbstractUser):
    """Custom user model"""
    
    first_login = models.DateTimeField(verbose_name='Первый вход', auto_now=True)
    phone = models.CharField(verbose_name='Номер телефона', max_length=20)
    avatar = models.ImageField(verbose_name='Фото пользователя', null=False, upload_to='resource')

    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"О себе")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Город")
    birth_date = models.DateField(null=True, blank=True, verbose_name=u"Дата рождения")
    gender = models.CharField(max_length=10, verbose_name=u"Пол", choices=GENDER_CHOICES, default="male")
    relationship = models.CharField(max_length=20, verbose_name=u"Статус отношений", choices=REL_CHOICES, default="none")

    class Meta:
        verbose_name = "Юзер"
        verbose_name_plural = "Юзеры"

