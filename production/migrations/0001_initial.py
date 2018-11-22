# Generated by Django 2.1.3 on 2018-11-22 10:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fuel', '0017_remove_powerplant_available_power'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_consumer', models.CharField(help_text='The name of power consumer.', max_length=256, verbose_name='Power Consumer')),
                ('power_units', models.BigIntegerField(default=0, help_text='Amount of power that can be generated', verbose_name='Power Available')),
                ('unit_measurement', models.CharField(help_text='The unit of measurement in which power is quantified', max_length=256, verbose_name='Unit of measurement')),
                ('date_recorded', models.DateField(default=datetime.datetime.today)),
                ('time_recorded', models.TimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Consumer',
                'verbose_name_plural': 'Consumers',
            },
        ),
        migrations.CreateModel(
            name='Generators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_number', models.PositiveIntegerField(default=1, help_text='Number given to identify the generator', verbose_name='Generator Number')),
                ('power_units', models.BigIntegerField(default=0, help_text='Amount of power that can be generated', verbose_name='Power Available')),
                ('location', models.CharField(help_text='The power plant ocation of the generator', max_length=256, verbose_name='Plant Location')),
                ('date_recorded', models.DateField(default=datetime.datetime.today)),
                ('time_recorded', models.TimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Power Plant Generator',
                'verbose_name_plural': 'Power Plant Generators',
            },
        ),
        migrations.CreateModel(
            name='PowerAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_units', models.BigIntegerField(default=0, help_text='Amount of power that can be generated', verbose_name='Power Available')),
                ('location', models.CharField(help_text='The power plant ocation of the generator', max_length=256, verbose_name='Plant Location')),
                ('date_recorded', models.DateField(default=datetime.datetime.today)),
                ('time_recorded', models.TimeField(auto_now_add=True)),
                ('power_plant', models.ForeignKey(help_text='The power plant making declaration', on_delete=django.db.models.deletion.CASCADE, to='fuel.Powerplant', verbose_name='Power Plant')),
            ],
            options={
                'verbose_name': 'Total Power Available',
                'verbose_name_plural': 'Total Power Available',
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('power_units', models.BigIntegerField(default=0, help_text='Amount of power that can be generated', verbose_name='Power Available')),
                ('location', models.CharField(help_text='The power plant ocation of the generator', max_length=256, verbose_name='Plant Location')),
                ('date_recorded', models.DateField(default=datetime.datetime.today)),
                ('time_recorded', models.TimeField(auto_now_add=True)),
                ('power_plant', models.ForeignKey(help_text='The power plant making declaration', on_delete=django.db.models.deletion.CASCADE, to='fuel.Powerplant', verbose_name='Power Plant')),
            ],
            options={
                'verbose_name': 'Total Power Available',
                'verbose_name_plural': 'Total Power Available',
            },
        ),
    ]
