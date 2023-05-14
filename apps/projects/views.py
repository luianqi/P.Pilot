from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.projects.models import Project, Iteration, Task, ProjectFile
from apps.projects.serializers import ProjectSerializer, IterationSerializer, TaskSerializer, ProjectFileSerializer


class ProjectFileView(ModelViewSet):
    serializer_class = ProjectFileSerializer
    queryset = ProjectFile.objects.all()


class ProjectView(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    parser_class = [MultiPartParser, FormParser, JSONParser]


class IterationView(ModelViewSet):
    serializer_class = IterationSerializer
    queryset = Iteration.objects.all()
    filterset_fields = ["project"]


class TaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filterset_fields = ["iteration_id"]
