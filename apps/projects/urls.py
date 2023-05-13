from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.projects.views import ProjectView, IterationView, TaskView, ProjectFileView

router = DefaultRouter()
router.register('project', ProjectView)
router.register('project-file', ProjectFileView)
router.register('iteration', IterationView)
router.register('task', TaskView)

# router.register('project-assignee', ProjectAssigneeView)
# router.register('sprint', SprintView)
# router.register('task', TaskView)
#
#
urlpatterns = [
    path('', include(router.urls)),
]