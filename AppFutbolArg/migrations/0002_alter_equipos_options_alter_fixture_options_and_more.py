# Generated by Django 4.2.2 on 2023-06-24 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppFutbolArg', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='equipos',
            options={'verbose_name_plural': 'Equipos'},
        ),
        migrations.AlterModelOptions(
            name='fixture',
            options={'verbose_name': 'Fixture'},
        ),
        migrations.AlterModelOptions(
            name='posiciones',
            options={'verbose_name_plural': 'Posiciones'},
        ),
    ]
