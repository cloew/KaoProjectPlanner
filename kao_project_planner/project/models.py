from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.title
    
class Iteration(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    project = models.ForeignKey(Project)
    
    def __unicode__(self):
        return self.title
    
class UserStory(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    project = models.ForeignKey(Project)
    iteration = models.ForeignKey(Iteration, blank=True, null=True)
    
    def __unicode__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    time_estimate = models.IntegerField(default=0)
    time_used = models.IntegerField(default=0)
    user_story = models.ForeignKey(UserStory)
    
    def __unicode__(self):
        return self.title