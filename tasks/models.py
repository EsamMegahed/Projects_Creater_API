from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


        
class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    project_description = models.TextField()
    date = models.DateTimeField(auto_now=True)
    project_complete = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class Tasks(models.Model):
    title = models.CharField(max_length=50)
    tsks_description = models.TextField()
    project = models.ForeignKey(
        Projects, on_delete=models.CASCADE, related_name="task_project"
    )

    def __str__(self) -> str:
        return self.title
