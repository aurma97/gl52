# Generated by Django 2.2.1 on 2019-05-08 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('location', '0002_auto_20190508_1416'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True)),
                ('end', models.DateTimeField()),
                ('status', models.CharField(choices=[('0', 'En cours'), ('1', 'Terminé')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Aucune catégorie', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Equipments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_purchase', models.DateField()),
                ('description', models.TextField(max_length=1000)),
                ('use_cond', models.TextField(max_length=1000)),
                ('last_check', models.DateField(default=None)),
                ('location', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='location.Location')),
                ('reservation', models.ManyToManyField(through='equipments.Booked', to=settings.AUTH_USER_MODEL)),
                ('type_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='equipments.EquipmentType')),
            ],
        ),
        migrations.AddField(
            model_name='booked',
            name='equipment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='equipments.Equipments'),
        ),
        migrations.AddField(
            model_name='booked',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
