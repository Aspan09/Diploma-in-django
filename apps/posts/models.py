from django.db import models
from profiles.models import UserNet


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