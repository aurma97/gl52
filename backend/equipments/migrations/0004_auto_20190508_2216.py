# Generated by Django 2.2.1 on 2019-05-08 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0003_auto_20190508_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booked',
            name='id',
            field=models.IntegerField(max_length=100000, primary_key=True, serialize=False),
        ),
    ]
