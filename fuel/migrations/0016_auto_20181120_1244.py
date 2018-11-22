# Generated by Django 2.1.3 on 2018-11-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0015_auto_20181120_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockvariation',
            name='iniial_qty',
            field=models.PositiveIntegerField(default=0, help_text='The quantity left of the inventory on previous day.', verbose_name='Initial Quantity'),
        ),
        migrations.AlterField(
            model_name='stockvariation',
            name='minimum_qty',
            field=models.PositiveIntegerField(default=0, help_text="The threshold quantity that can't be consumed.", verbose_name='Threshold'),
        ),
        migrations.AlterField(
            model_name='stockvariation',
            name='qty_added',
            field=models.PositiveIntegerField(default=0, help_text='The quantity added from supply.', verbose_name='Quantity Supplied'),
        ),
        migrations.AlterField(
            model_name='stockvariation',
            name='qty_left',
            field=models.PositiveIntegerField(default=0, help_text='The quantity left before consumption.', verbose_name='Quantity on Hand'),
        ),
        migrations.AlterField(
            model_name='stockvariation',
            name='qty_removed',
            field=models.PositiveIntegerField(default=0, help_text='The quantity to be consumed.', verbose_name='Quantity Consumed'),
        ),
    ]
