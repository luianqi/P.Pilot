from django.db import models

from apps.users.models import User


class ProjectStatus(models.TextChoices):
    ACTIVE = "Active"
    COMPLETED = "Completed"
    FAILED = "Failed"


class Project(models.Model):
    admin = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              editable=False,
                              related_name="admin_id",
                              blank=True,
                              null=True)
    manager = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    status = models.CharField(choices=ProjectStatus.choices,
                              max_length=255)
    budget = models.CharField(default="0", max_length=150)
    is_archived = models.BooleanField(default=False)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class ProjectFile(models.Model):
    project_id = models.ForeignKey(Project,
                                   on_delete=models.CASCADE,
                                   related_name="files")
    file = models.FileField(default="default.pdf", upload_to="media")

    def __str__(self):
        return f"{self.file}"


class Iteration(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


class Task(models.Model):
    iteration_id = models.ForeignKey(Iteration,
                                     on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    is_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

#
#
# assignees = models.ManyToManyField(Assignee, through="ProjectAssignee")

# class ProjectAssignee(models.Model):
#     assignee = models.ForeignKey(Assignee, on_delete=models.CASCADE)
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.assignee.first_name}"
#
#
# class Sprint(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE)
#     name = models.CharField(max_length=150)
#     description = models.CharField(max_length=255)
#     start_date = models.DateField()
#     end_date = models.DateField()
#     status = models.CharField(choices=GeneralStatus.choices, max_length=255)
#
#     def __str__(self):
#         return f"{self.name}"
#
#
# class Task(models.Model):
#     name = models.CharField(max_length=150)
#     description = models.CharField(max_length=255)
#     status = models.CharField(choices=GeneralStatus.choices, max_length=255)
#     priority = models.CharField(choices=PriorityStatus.choices, max_length=255)
#     assignee = models.ForeignKey(Assignee, on_delete=models.CASCADE)
#     sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE)
#     due_date = models.DateTimeField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.name}"