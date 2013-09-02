from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    
class Iteration(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')
    project = models.ForeignKey(Project)
    
class UserStory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project)
    iteration = models.ForeignKey(Iteration)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    time_estimate = models.IntegerField(default=0)
    time_used = models.IntegerField(default=0)
    user_story = models.ForeignKey(UserStory)