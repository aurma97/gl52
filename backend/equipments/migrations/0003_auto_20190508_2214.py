# Generated by Django 2.2.1 on 2019-05-08 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0002_equipments_last_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked',
            name='end',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
