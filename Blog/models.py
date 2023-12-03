from django.contrib.auth.models import User
from django.db import models


class Tags(models.Model):
    tag_name = models.CharField(max_length=100, verbose_name="Тег")

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"


class Posts(models.Model):
    tags = models.ManyToManyField(to=Tags, verbose_name="Теги", default=None)
    created_by = models.ForeignKey(
        to=User, on_delete=models.CASCADE, verbose_name="Создатель"
    )
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Основной контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан в")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
