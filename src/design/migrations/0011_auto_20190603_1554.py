# Generated by Django 2.2.1 on 2019-06-03 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0010_auto_20190603_1536'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='Stg',
            field=models.FloatField(null=True, verbose_name='Esfuerzo de flexión en el engrane'),
        ),
        migrations.AddField(
            model_name='gear',
            name='Stp',
            field=models.FloatField(null=True, verbose_name='Esfuerzo de flexión en el piñón'),
        ),
    ]