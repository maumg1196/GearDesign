# Generated by Django 2.2.1 on 2019-06-02 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('design', '0004_auto_20190602_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='gear',
            name='SF',
            field=models.FloatField(default=1.0, verbose_name='Factor de seguridad'),
        ),
        migrations.AddField(
            model_name='gear',
            name='kb',
            field=models.FloatField(default=1.0, verbose_name='Factor de espesor de la corona'),
        ),
        migrations.AddField(
            model_name='gear',
            name='kr',
            field=models.FloatField(default=1.0, verbose_name='Factor de confiabilidad'),
        ),
        migrations.AddField(
            model_name='gear',
            name='ks',
            field=models.FloatField(null=True, verbose_name='Factor de tamaño'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='C',
            field=models.FloatField(null=True, verbose_name='Distancia entre centros'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Cpf',
            field=models.FloatField(null=True, verbose_name='Factor de proporción del piñón'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Dg',
            field=models.FloatField(null=True, verbose_name='Diametro de paso del engrane'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Dp',
            field=models.FloatField(null=True, verbose_name='Diametro de paso del piñón'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='F',
            field=models.FloatField(null=True, verbose_name='Ancho de la cara'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Ft',
            field=models.FloatField(null=True, verbose_name='Fuerza transmitida'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='HP',
            field=models.FloatField(null=True, verbose_name='Potencia de motor'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Ng',
            field=models.FloatField(null=True, verbose_name='Dientes del engrane'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Np',
            field=models.FloatField(choices=[(12.0, 12.0), (18.0, 18.0), (32.0, 32.0)], null=True, verbose_name='Dientes del piñón'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Pd',
            field=models.FloatField(null=True, verbose_name='Paso diametral'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='PotD',
            field=models.FloatField(null=True, verbose_name='Potencia de diseño'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='Vt',
            field=models.FloatField(null=True, verbose_name='Velocidad tangencial'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='angle',
            field=models.FloatField(null=True, verbose_name='Ángulo'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='fs',
            field=models.FloatField(null=True, verbose_name='Factor de servicio'),
        ),
        migrations.AlterField(
            model_name='gear',
            name='kv',
            field=models.FloatField(null=True, verbose_name='Factor dinámico'),
        ),
    ]
