# Generated by Django 2.2.1 on 2019-05-31 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gear',
            name='Av',
            field=models.IntegerField(null=True, verbose_name='Calidad'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='C',
            field=models.FloatField(null=True, verbose_name='distancia entre centros'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Cpf',
            field=models.FloatField(null=True, verbose_name='factor de proporción del piñón'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Dp',
            field=models.FloatField(null=True, verbose_name='paso diametral del piñón'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='F',
            field=models.FloatField(null=True, verbose_name='ancho de la cara'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Ft',
            field=models.FloatField(null=True, verbose_name='fuerza transmitida'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='HP',
            field=models.FloatField(null=True, verbose_name='potencia de motor'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Ng',
            field=models.FloatField(null=True, verbose_name='dientes del engrane'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Np',
            field=models.FloatField(null=True, verbose_name='dientes del piñón'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Pd',
            field=models.FloatField(null=True, verbose_name='paso diametral del engrane'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='PotD',
            field=models.FloatField(null=True, verbose_name='potencia de diseño'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Vt',
            field=models.FloatField(null=True, verbose_name='velocidad tangencial'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Wg',
            field=models.FloatField(null=True, verbose_name='RPMs del engrane'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Wp',
            field=models.FloatField(null=True, verbose_name='RPMs del piñón'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='angle',
            field=models.FloatField(null=True, verbose_name='ángulo'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='fs',
            field=models.FloatField(null=True, verbose_name='factor de servicio'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='kv',
            field=models.FloatField(null=True),
        ),
    ]
