# from rest_framework.serializers import ModelSerializer
#
# from apps.projects.models import Project, ProjectAssignee, Sprint, Task
#
#
# class ProjectSerializer(ModelSerializer):
#     class Meta:
#         model = Project
#         fields = ["id",
#                   "manager",
#                   "name",
#                   "description",
#                   "notes",
#                   "status",
#                   "assignees",
#                   ]
#         read_only_fields = ["assignees"]
#
#
# class ProjectAssigneeSerializer(ModelSerializer):
#     class Meta:
#         model = ProjectAssignee
#         fields = ["id", "assignee", "project"]
#
#
# class SprintSerializer(ModelSerializer):
#     class Meta:
#         model = Sprint
#         fields = ["id",
#                   "project",
#                   "name",
#                   "description",
#                   "start_date",
#                   "end_date",
#                   "status"
#                   ]
#
#
# class TaskSerializer(ModelSerializer):
#     class Meta:
#         model = Task
#         fields = ["id",
#                   "name",
#                   "description",
#                   "status",
#                   "priority",
#                   "assignee",
#                   "sprint",
#                   "due_date",
#                   "created_at"
#                   ]
#         read_only_fields = ["created_at"]
