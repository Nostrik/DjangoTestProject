from tabnanny import verbose
from django.db import models


class Vacancy(models.Model):
    is_active = models.BooleanField(default=False, verbose_name='Активность')
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    descripton = models.TextField(default='', verbose_name='Описание')
    publisher = models.CharField(max_length=30, verbose_name='Кто опубликовал')
    created_at =models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    published = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)

    class Meta:
        verbose_name = 'вакансия'
        verbose_name_plural = 'вакансии'
        permissions = (
            ("can_publish", "может опубликовать"),
        )

    def __str__(self):
        return self.title


class Summary(models.Model):
    title = models.CharField(max_length=30, verbose_name='Заголовок')
    created_at =models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    published = models.DateTimeField(verbose_name='Дата публикации', blank=True, null=True)


    class Meta:
        verbose_name = 'резюме'
        verbose_name_plural = 'резюме'
        permissions = (
            ("can_publish", "может опубликовать"),
        )

    def __str__(self):
        return self.title