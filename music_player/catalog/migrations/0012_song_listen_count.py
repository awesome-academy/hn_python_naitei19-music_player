# Generated by Django 4.2.5 on 2023-09-24 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_song_content_alter_song_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='listen_count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
