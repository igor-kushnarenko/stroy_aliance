# Generated by Django 3.2.9 on 2021-11-12 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30, verbose_name='Имя')),
                ('second_name', models.CharField(default='', max_length=30, verbose_name='Фамилия')),
                ('uuid', models.TextField(default='', verbose_name='uuid')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='День рождения')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.AlterField(
            model_name='auth',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='auth', to='board.profile', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='bill', to='board.profile', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='userdevices',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='UserDevices', to='board.profile', verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='visit', to='board.profile', verbose_name='Пользователь'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
