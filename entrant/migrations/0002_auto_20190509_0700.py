# Generated by Django 2.2 on 2019-05-09 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anketa',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='anketa',
            name='date_sr_obr',
            field=models.DateField(),
        ),
    ]
