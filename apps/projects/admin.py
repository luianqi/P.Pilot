from django.contrib import admin

from apps.projects.models import Project, ProjectFile, Iteration, Task

admin.site.register(Project)
admin.site.register(ProjectFile)
admin.site.register(Iteration)
admin.site.register(Task)


