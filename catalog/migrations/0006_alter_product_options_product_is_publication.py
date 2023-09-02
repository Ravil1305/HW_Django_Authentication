# Generated by Django 4.2.3 on 2023-09-02 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_product_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'permissions': [('set_published', 'Can publish product')], 'verbose_name': 'продукт', 'verbose_name_plural': 'продукты'},
        ),
        migrations.AddField(
            model_name='product',
            name='is_publication',
            field=models.BooleanField(default=False, verbose_name='признак публикации'),
        ),
    ]
