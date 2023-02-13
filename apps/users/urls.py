from django.urls import path, include

from rest_framework.routers import DefaultRouter

from apps.users.views import AssigneeView

router = DefaultRouter()
router.register('assignee', AssigneeView)


urlpatterns = [
    path('', include(router.urls)),
]