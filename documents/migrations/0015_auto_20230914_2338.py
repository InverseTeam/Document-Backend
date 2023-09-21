# Generated by Django 3.2.18 on 2023-09-14 18:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0014_auto_20230914_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='main_contractor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='documents_main_contractor', to='documents.contractor', verbose_name='Главный контрагент'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='documenthistory',
            name='time',
            field=models.TimeField(default=datetime.time(23, 38, 44, 469243), verbose_name='Время'),
        ),
    ]
