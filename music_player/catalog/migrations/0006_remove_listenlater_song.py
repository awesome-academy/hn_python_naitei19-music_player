# Generated by Django 4.2.5 on 2023-09-21 18:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_listenlater_listen_id_alter_user_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listenlater',
            name='song',
        ),
    ]
