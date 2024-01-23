# Generated by Django 5.0.1 on 2024-01-22 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_tasks_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_project', to='tasks.projects'),
        ),
    ]