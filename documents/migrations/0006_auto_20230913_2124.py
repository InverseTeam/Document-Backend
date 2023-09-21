# Generated by Django 3.2.18 on 2023-09-13 16:24

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_auto_20230913_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documenthistory',
            name='time',
            field=models.TimeField(default=datetime.time(21, 24, 42, 304053), verbose_name='Время'),
        ),
        migrations.AlterField(
            model_name='documentstatus',
            name='status_id',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)], verbose_name='ID статуса'),
        ),
    ]
