# Generated by Django 3.2.18 on 2023-09-14 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0011_auto_20230914_1646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='contractor_categories',
            new_name='contractors_categories',
        ),
        migrations.AlterField(
            model_name='documenthistory',
            name='time',
            field=models.TimeField(default=datetime.time(16, 48, 28, 838088), verbose_name='Время'),
        ),
    ]
