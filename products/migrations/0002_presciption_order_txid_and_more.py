# Generated by Django 4.2.5 on 2023-11-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='presciption_order',
            name='TxID',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='presciption_order',
            name='paymentMobile',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]