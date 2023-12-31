# Generated by Django 3.2.18 on 2023-09-13 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20230913_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='total_nds',
            field=models.IntegerField(default=0, verbose_name='НДС в рублях'),
        ),
        migrations.AlterField(
            model_name='document',
            name='total_price',
            field=models.IntegerField(default=0, verbose_name='Полная стоимость с учётом НДС'),
        ),
        migrations.AlterField(
            model_name='documenthistory',
            name='time',
            field=models.TimeField(default=datetime.time(20, 57, 41, 752868), verbose_name='Время'),
        ),
    ]
