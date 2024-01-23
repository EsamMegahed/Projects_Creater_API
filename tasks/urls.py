from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("projects", views.ProjectsView)

urlpatterns = [
    path("api/", include(router.urls)),
]
