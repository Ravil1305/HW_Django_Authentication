from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(**NULLABLE, verbose_name='описание')
    preview = models.ImageField(upload_to='catalog/', **NULLABLE, verbose_name='превью')
    category = models.CharField(max_length=100, verbose_name='категория')
    price = models.IntegerField(verbose_name='цена')
    date_of_creation = models.DateField(verbose_name='дата создания')
    last_modified_date = models.DateField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f'{self.name}: {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.name}: {self.description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
