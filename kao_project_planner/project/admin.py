from django.contrib import admin
from project.models import Project, Iteration, UserStory, Task

admin.site.register(Project)
admin.site.register(Iteration)
admin.site.register(UserStory)
admin.site.register(Task)