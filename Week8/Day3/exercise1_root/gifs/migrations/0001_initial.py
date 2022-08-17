# Generated by Django 4.1 on 2022-08-14 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gif_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('uploader_name', models.CharField(max_length=50)),
                ('created_at', models.DateField(default=datetime.datetime(2022, 8, 14, 9, 9, 30, 379550))),
            ],
        ),
        migrations.CreateModel(
            name='Category_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gif', models.ManyToManyField(blank=True, related_name='categories', to='gifs.gif_model')),
            ],
        ),
    ]