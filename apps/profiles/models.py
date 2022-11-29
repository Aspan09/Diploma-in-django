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


class Post(models.Model):
    datetime = models.DateTimeField(verbose_name="Дата", auto_now_add=True)
    username = models.ForeignKey(UserNet, on_delete=models.CASCADE, verbose_name="Автор", related_name="posts")
    text = models.CharField(max_length=1000, verbose_name="Текст", null=True, blank=True)
    image = models.FileField(verbose_name="Картинка", null=True, blank=True)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-datetime"]


class Comment(models.Model):
    datetime = models.DateTimeField(verbose_name=u"Дата", auto_now_add=True)
    username = models.ForeignKey(UserNet, on_delete=models.CASCADE, verbose_name=u"Автор", related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name=u"Пост", related_name="comments")
    text = models.CharField(max_length=1000, verbose_name=u"Текст", null=True, blank=True)

    class Meta:
        verbose_name = "Коммент"
        verbose_name_plural = "Комментарий"
        ordering = ["datetime"]


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

