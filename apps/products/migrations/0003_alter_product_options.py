# Generated by Django 4.2.6 on 2023-11-06 11:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
