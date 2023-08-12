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

    def get_current_version(self):
        current_version = self.productversion_set.filter(is_current=True).first()
        return current_version if current_version else None

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


class ProductVersion(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    version_number = models.PositiveIntegerField(verbose_name='номер версии')
    version_name = models.CharField(max_length=100, verbose_name='название версии')
    is_current = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product}: {self.version_name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
