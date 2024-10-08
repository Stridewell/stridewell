# Generated by Django 5.1.1 on 2024-09-23 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stridewell', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkoutSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='workoutstep',
            name='name',
        ),
        migrations.RemoveField(
            model_name='workoutstep',
            name='workout',
        ),
        migrations.AddField(
            model_name='workoutstep',
            name='duration_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='workoutstep',
            name='target_value',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='workoutstep',
            name='set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stridewell.workoutset'),
        ),
    ]
