# Generated by Django 2.2.1 on 2019-05-12 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0015_remove_equipments_last_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipments',
            name='reservation',
        ),
    ]
