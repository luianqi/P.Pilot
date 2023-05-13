from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer

from apps.projects.models import Project, Iteration, Task, ProjectFile


class ProjectFileSerializer(ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ["id",
                  "project_id",
                  "file"
                  ]


class ProjectSerializer(ModelSerializer):
    files = ProjectFileSerializer(many=True)

    class Meta:
        model = Project
        fields = ["id",
                  "admin",
                  "manager",
                  "name",
                  "description",
                  "status",
                  "files",
                  "is_archived"
                  ]


class IterationSerializer(ModelSerializer):
    project = PresentablePrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        presentation_serializer=ProjectSerializer
    )

    class Meta:
        model = Iteration
        fields = ["id",
                  "project",
                  "start_date",
                  "end_date"
                  ]


class TaskSerializer(ModelSerializer):
    iteration_id = PresentablePrimaryKeyRelatedField(
        queryset=Iteration.objects.all(),
        presentation_serializer=IterationSerializer
    )

    class Meta:
        model = Task
        fields = ["id",
                  "iteration_id",
                  "name",
                  "is_finished"
                  ]
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
