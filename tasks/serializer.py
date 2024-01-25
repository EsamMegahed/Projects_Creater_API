from rest_framework import serializers
from .models import Projects, Tasks
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password']
        #extra_kwargs = {'password':{'write_only':True,'required':True}}

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"


class ProjectsSerializer(serializers.ModelSerializer):
    task_project = TaskSerializer(many=True)

    class Meta:
        model = Projects
        fields = [
            "id",
            "user",
            "title",
            "project_description",
            "date",
            "task_project",
            "project_complete",
        ]

    # def create(self, validated_data):
    #     tasks_data = validated_data.pop("tasks")
    #     project = Projects.objects.create(**validated_data)
    #     for task_data in tasks_data:
    #         Tasks.objects.create(project=project, **task_data)
    #     return project
