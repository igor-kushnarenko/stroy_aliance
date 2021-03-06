# Generated by Django 3.2.9 on 2021-11-12 15:48

import board.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0008_alter_rate_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rate',
            name='price',
            field=models.FloatField(default=100, validators=[board.models.min_max_validator], verbose_name='Стоимость'),
        ),
    ]
