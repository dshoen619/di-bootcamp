# Generated by Django 4.1 on 2022-08-28 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testudo_app', '0002_alter_courselist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='course_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='testudo_app.courselist'),
        ),
    ]