from django.db import models

from apps.users.models import User, Assignee


class ProjectStatus(models.TextChoices):
    ACTIVE = "Active"
    COMPLETED = "Completed"
    FAILED = "Failed"


class GeneralStatus(models.TextChoices):
    ACTIVE = "Active"
    COMPLETED = "Completed"


class PriorityStatus(models.TextChoices):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Низкий"


class Project(models.Model):
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(choices=ProjectStatus.choices, max_length=255)
    assignees = models.ManyToManyField(Assignee, through="ProjectAssignee")

    def __str__(self):
        return f"{self.name}"


class ProjectAssignee(models.Model):
    assignee = models.ForeignKey(Assignee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.assignee.first_name}"


class Sprint(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(choices=GeneralStatus.choices, max_length=255)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    status = models.CharField(choices=GeneralStatus.choices, max_length=255)
    priority = models.CharField(choices=PriorityStatus.choices, max_length=255)
    assignee = models.ForeignKey(Assignee, on_delete=models.CASCADE)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
    due_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"