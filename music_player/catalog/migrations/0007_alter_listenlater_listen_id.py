# Generated by Django 4.2.5 on 2023-09-22 09:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_remove_listenlater_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listenlater',
            name='listen_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.song'),
        ),
    ]
