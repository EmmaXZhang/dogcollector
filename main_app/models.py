from django.db import models
from django.urls import reverse

MEALS = (
    # tuple, using shortcut to save data space
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=256)
    breed = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    age = models.IntegerField()

    def __str__(self):
        return self.name
    

    def get_absolute_url(self):
        return reverse('detail',kwargs={'dog_id':self.id})
    

class Feeding(models.Model):
    date = models.DateField("feeding date")
    meal = models.CharField(max_length=1, choices = MEALS, default = MEALS[0][0])
    
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"
    
    class Meta:
        ordering =['-date']