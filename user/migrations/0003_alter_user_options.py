# Generated by Django 4.2.15 on 2024-09-17 20:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_is_block'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': [('set_user', 'Блокировка пользователей')], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
