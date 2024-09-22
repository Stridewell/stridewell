from django.contrib import admin

# Register your models here.
from .models import Workout, WorkoutStep

admin.site.register(Workout)
admin.site.register(WorkoutStep)