from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(default=None, max_length=50)

    def __str__(self):
        return self.name



