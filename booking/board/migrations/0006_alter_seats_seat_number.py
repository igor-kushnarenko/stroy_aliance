# Generated by Django 3.2.9 on 2021-11-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0005_alter_seats_seat_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seats',
            name='seat_number',
            field=models.IntegerField(default='', verbose_name='Номер шезлонга'),
        ),
    ]
