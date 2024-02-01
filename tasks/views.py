from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Projects, Tasks
from .serializer import ProjectsSerializer, TaskSerializer,UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password


# Create your views here.

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     if 'password' in serializer:
    #         password = make_password(self.request.data['password'])
    #         serializer.save(password=password)
    #     else:
    #         serializer.save()
        
    #     self.perform_create(serializer)
    #     token,created = Token.objects.get_or_create(user = serializer.instance)

    #     return Response({'token':token.key},status=status.HTTP_400_BAD_REQUEST)
    
    def perform_create(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

    def perform_update(self, serializer):
        # Hash password but passwords are not required
        if ('password' in self.request.data):
            password = make_password(self.request.data['password'])
            serializer.save(password=password)
        else:
            serializer.save()

class ProjectsView(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]



class TasksView(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]