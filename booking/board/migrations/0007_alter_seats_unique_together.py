# Generated by Django 3.2.9 on 2021-11-12 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_alter_seats_seat_number'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='seats',
            unique_together={('service', 'seat_number')},
        ),
    ]
