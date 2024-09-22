from django.db import models

# Create your models here.

class Workout(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class WorkoutStep(models.Model):
    workout = models.ForeignKey(to=Workout, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name