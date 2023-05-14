from drf_extra_fields.relations import PresentablePrimaryKeyRelatedField
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from apps.projects.models import Project, Iteration, Task, ProjectFile
from apps.users.models import User
from apps.users.serializers import RegisterSerializer


class ProjectFileSerializer(ModelSerializer):
    class Meta:
        model = ProjectFile
        fields = ["id",
                  "project_id",
                  "file",
                  ]


class ProjectSerializer(ModelSerializer):
    files = ProjectFileSerializer(many=True, read_only=True)
    uploaded_files = serializers.ListField(
        child=serializers.FileField(), write_only=True
    )
    manager = PresentablePrimaryKeyRelatedField(
        queryset=User.objects.all(),
        presentation_serializer=RegisterSerializer
    )

    class Meta:
        model = Project
        fields = ["id",
                  "admin",
                  "manager",
                  "name",
                  "description",
                  "status",
                  "files",
                  "uploaded_files",
                  "budget",
                  "start_date",
                  "end_date",
                  "is_archived"
                  ]

    def create(self, validated_data):
        uploaded_files = validated_data.pop("uploaded_files")
        project = Project.objects.create(**validated_data)
        for file in uploaded_files:
            ProjectFile.objects.create(project_id=project, file=file)
        return project

    def update(self, instance, validated_data):
        uploaded_files = validated_data.pop("uploaded_files", [])
        for file in uploaded_files:
            ProjectFile.objects.create(project_id=instance, file=file)
        return super().update(instance, validated_data)


class IterationSerializer(ModelSerializer):
    project = PresentablePrimaryKeyRelatedField(
        queryset=Project.objects.all(),
        presentation_serializer=ProjectSerializer
    )

    class Meta:
        model = Iteration
        fields = ["id",
                  "name",
                  "project",
                  "is_completed",
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
