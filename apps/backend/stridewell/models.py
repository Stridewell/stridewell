from django import utils
from django.db import models

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
    
class WorkoutSet(models.Model):
    workout = models.ForeignKey(to=Workout, on_delete=models.CASCADE),
    order = models.IntegerField(default=1),
    name = models.CharField(max_length=200),
    repeat_amount = models.IntegerField(default=1),

    def __str__(self):
        return self.name
    
DURATION_TYPE_CODES = (
    ('DISTANCE', 'Distance'),
    ('TIME', 'Time'),
)

TARGET_TYPE_CODES = (
    ('SPEED', 'Speed'),
    ('HEART_RATE', 'Heart rate'),
    ('CADENCE', 'Cadence'),
)
    
class WorkoutStep(models.Model):
    workout = models.ForeignKey(to=Workout, on_delete=models.CASCADE),
    set = models.ForeignKey(to=WorkoutSet, on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField(default=1),
    name = models.CharField(max_length=200),
    duration_type = models.CharField(choices=DURATION_TYPE_CODES),
    duration_value = models.IntegerField(default=1)
    target_type = models.CharField(choices=TARGET_TYPE_CODES),
    target_value = models.IntegerField(default=1)

    def __str__(self):
        return self.name