from django.db import models

# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=256)
    breed = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    age = models.IntegerField()

    def __str__(self):
        return self.name