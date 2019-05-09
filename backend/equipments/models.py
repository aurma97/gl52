from django.db import models
from django.contrib.auth.models import User
from ..location.models import Location
# Create your models here.

class EquipmentType(models.Model):
    title = models.CharField(default="Aucune catégorie", max_length=100)

    def __str__(self):
        return self.title

#use_cond = condition generale d'utilisation
#last_check = date de dernière maintenance
class Equipments(models.Model):
    name = models.CharField(max_length=100)
    date_purchase = models.DateField()
    description = models.TextField(max_length=1000)
    use_cond = models.TextField(max_length = 1000)
    last_check = models.DateField(default=None)
    type_id = models.ForeignKey(EquipmentType, default=None, on_delete=models.PROTECT)
    location = models.ForeignKey(Location, default=None, on_delete=models.PROTECT)
    last_location = models.CharField(default=None, max_length=100)
    reservation = models.ManyToManyField(User, through='Booked')

    def __str__(self):
        return self.name
    
class Booked(models.Model):
    id = models.AutoField(primary_key=True)
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(auto_now=True)
    status_choice = (
        ('0', 'En cours'),
        ('1', 'Terminé'),
    )
    status = models.CharField(max_length=1, choices=status_choice)
    equipment_id = models.ForeignKey(Equipments, on_delete=models.PROTECT, unique=True)
    user_id = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.id)