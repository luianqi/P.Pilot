from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.organizations.views import OrganizationView

router = DefaultRouter()
router.register('organization', OrganizationView)


urlpatterns = [
    path('', include(router.urls)),
]