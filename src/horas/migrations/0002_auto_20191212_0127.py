# Generated by Django 2.2.5 on 2019-12-12 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hora',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='hora',
            name='nombre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='hora',
            name='telefono',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
