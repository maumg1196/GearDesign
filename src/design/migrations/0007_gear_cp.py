# Generated by Django 2.2.1 on 2019-06-03 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0006_auto_20190602_1934'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='Cp',
            field=models.FloatField(null=True, verbose_name='Constante de elasticidad'),
        ),
    ]
