from rest_framework.viewsets import ModelViewSet

from apps.projects.models import Project, Iteration
from apps.projects.serializers import ProjectSerializer, IterationSerializer


class ProjectView(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class IterationView(ModelViewSet):
    serializer_class = IterationSerializer
    queryset = Iteration.objects.all()
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
