# Generated by Django 2.2.5 on 2019-12-12 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas', '0004_auto_20191212_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hora',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hora',
            name='telefono',
            field=models.CharField(max_length=12),
        ),
    ]
