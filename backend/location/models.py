from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(default=None, max_length=80, unique=True)

    def __str__(self):
        return self.name