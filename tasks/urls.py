from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register("projects", views.ProjectsView)
router.register("tasks", views.TasksView)
router.register("User", views.UserView)

urlpatterns = [
    path("api/", include(router.urls)),
    path('api/token-auth/', obtain_auth_token),
]
