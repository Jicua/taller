# Generated by Django 2.2.5 on 2019-12-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horas', '0002_auto_20191212_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hora',
            name='dia',
            field=models.PositiveIntegerField(blank=True),
        ),
    ]
