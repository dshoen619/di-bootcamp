# Generated by Django 4.1 on 2022-08-15 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0004_gif_model_likes_alter_gif_model_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gif_model',
            name='likes',
            field=models.IntegerField(default=False),
        ),
    ]