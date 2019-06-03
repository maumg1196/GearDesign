# Generated by Django 2.2.1 on 2019-06-03 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0005_auto_20190602_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='Eg',
            field=models.FloatField(null=True, verbose_name='Módulo de elasticidad del engrane'),
        ),
        migrations.AddField(
            model_name='gear',
            name='Ep',
            field=models.FloatField(null=True, verbose_name='Módulo de elasticidad del piñón'),
        ),
        migrations.AddField(
            model_name='gear',
            name='L',
            field=models.FloatField(null=True, verbose_name='Vida del componente'),
        ),
        migrations.AddField(
            model_name='gear',
            name='Ncg',
            field=models.FloatField(null=True, verbose_name='Vida del engrane en ciclos'),
        ),
        migrations.AddField(
            model_name='gear',
            name='Ncp',
            field=models.FloatField(null=True, verbose_name='Vida del piñón en ciclos'),
        ),
        migrations.AddField(
            model_name='gear',
            name='Vg',
            field=models.FloatField(null=True, verbose_name='Cte de poison del engrane'),
        ),
        migrations.AddField(
            model_name='gear',
            name='Vp',
            field=models.FloatField(null=True, verbose_name='Cte de poison del piñón'),
        ),
        migrations.AddField(
            model_name='gear',
            name='hrs',
            field=models.FloatField(null=True, verbose_name='Horas de trabajo por día'),
        ),
        migrations.AddField(
            model_name='gear',
            name='q',
            field=models.FloatField(null=True, verbose_name='Aplicaciones de carga por rev'),
        ),
    ]