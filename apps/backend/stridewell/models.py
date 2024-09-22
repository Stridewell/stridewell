from django import utils
from django.db import models

# Create your models here.

class Runner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()

class Workout(models.Model):
    name = models.CharField(max_length=200)
    runner = models.ForeignKey(to=Runner, on_delete=models.CASCADE)
    date = models.DateTimeField(default=utils.timezone.now)

    def __str__(self):
        return self.name
    
class WorkoutStep(models.Model):
    workout = models.ForeignKey(to=Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name