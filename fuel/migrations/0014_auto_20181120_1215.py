# Generated by Django 2.1.3 on 2018-11-20 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fuel', '0013_auto_20181115_1320'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stockvariation',
            options={'verbose_name': 'Variation', 'verbose_name_plural': 'Varations'},
        ),
        migrations.RemoveField(
            model_name='storageunit',
            name='iniial_qty',
        ),
        migrations.RemoveField(
            model_name='storageunit',
            name='minimum_qty',
        ),
        migrations.RemoveField(
            model_name='storageunit',
            name='qty_added',
        ),
        migrations.RemoveField(
            model_name='storageunit',
            name='qty_left',
        ),
        migrations.RemoveField(
            model_name='storageunit',
            name='qty_removed',
        ),
        migrations.AddField(
            model_name='stockvariation',
            name='iniial_qty',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stockvariation',
            name='minimum_qty',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stockvariation',
            name='qty_added',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stockvariation',
            name='qty_left',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='stockvariation',
            name='qty_removed',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stockvariation',
            name='record_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='stockvariation',
            name='storage_unit',
            field=models.ForeignKey(help_text='The record changes in inventory.', on_delete=django.db.models.deletion.CASCADE, to='fuel.Storageunit', verbose_name='Inventory changes'),
        ),
    ]