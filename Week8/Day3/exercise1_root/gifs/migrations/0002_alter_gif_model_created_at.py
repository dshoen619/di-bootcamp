# Generated by Django 4.1 on 2022-08-14 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gif_model',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2022, 8, 14, 9, 10, 0, 859563)),
        ),
    ]