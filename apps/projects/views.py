from rest_framework.viewsets import ModelViewSet

from apps.projects.models import Project, Iteration, Task
from apps.projects.serializers import ProjectSerializer, IterationSerializer, TaskSerializer


class ProjectView(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class IterationView(ModelViewSet):
    serializer_class = IterationSerializer
    queryset = Iteration.objects.all()
    filterset_fields = ["project"]


class TaskView(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    filterset_fields = ["iteration_id"]
#
#
# class ProjectAssigneeView(ModelViewSet):
#     serializer_class = ProjectAssigneeSerializer
#     queryset = ProjectAssignee.objects.all()
#
#
# class SprintView(ModelViewSet):
#     serializer_class = SprintSerializer
#     queryset = Sprint.objects.all()
#
#
# class TaskView(ModelViewSet):
#     serializer_class = TaskSerializer
#     queryset = Task.objects.all()
#
#
