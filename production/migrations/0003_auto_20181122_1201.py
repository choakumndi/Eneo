# Generated by Django 2.1.3 on 2018-11-22 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production', '0002_auto_20181122_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demand',
            name='time_recorded',
            field=models.TimeField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='generators',
            name='time_recorded',
            field=models.TimeField(default=datetime.datetime.today),
        ),
        migrations.AlterField(
            model_name='poweravailable',
            name='time_recorded',
            field=models.TimeField(default=datetime.datetime.today),
        ),
    ]
