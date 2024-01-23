from django.shortcuts import render
from rest_framework import viewsets
from .models import Projects, Tasks
from .serializer import ProjectsSerializer, TaskSerializer

# Create your views here.


class ProjectsView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
