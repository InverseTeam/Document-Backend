# Generated by Django 3.2.18 on 2023-09-13 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0009_auto_20230913_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenthistory',
            name='time',
            field=models.TimeField(default=datetime.time(21, 50, 1, 605580), verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='product',
            name='nds',
            field=models.FloatField(verbose_name='НДС'),
        ),
    ]
