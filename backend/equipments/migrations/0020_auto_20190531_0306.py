# Generated by Django 2.2.1 on 2019-05-31 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0019_auto_20190531_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked',
            name='start',
            field=models.DateField(),
        ),
    ]
