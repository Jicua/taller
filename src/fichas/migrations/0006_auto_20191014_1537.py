# Generated by Django 2.2.5 on 2019-10-14 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fichas', '0005_auto_20191014_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atencion',
            name='fecha_entrada',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='atencion',
            name='fecha_salida',
            field=models.DateField(blank=True, null=True),
        ),
    ]
