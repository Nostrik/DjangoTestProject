from django.db import models


class Item(models.Model):
    code = models.CharField(max_length=100, verbose_name='артикул')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')


class NewItem(models.Model):
    name = models.CharField(max_length=10, verbose_name='название')
    code = models.CharField(max_length=10, verbose_name='артикул')
    price = models.CharField(max_length=10, verbose_name='цена')


class File(models.Model):
    file = models.FileField(upload_to='files/')
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
