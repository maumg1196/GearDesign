# Generated by Django 2.2.1 on 2019-06-04 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0013_auto_20190603_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='HBg',
            field=models.FloatField(null=True, verbose_name='Dureza Brinell para el engrane'),
        ),
        migrations.AddField(
            model_name='gear',
            name='HBp',
            field=models.FloatField(null=True, verbose_name='Dureza Brinell para el piñón'),
        ),
    ]
