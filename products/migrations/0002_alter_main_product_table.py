# Generated by Django 4.2.3 on 2023-09-09 22:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='main_product',
            table='products_main_product',
        ),
    ]
