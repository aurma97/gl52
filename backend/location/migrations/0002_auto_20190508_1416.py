# Generated by Django 2.2.1 on 2019-05-08 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='current_location',
            field=models.TextField(default=None, max_length=1000),
        ),
        migrations.AlterField(
            model_name='location',
            name='last_location',
            field=models.TextField(default=None, max_length=1000),
        ),
    ]
