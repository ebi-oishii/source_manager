# Generated by Django 5.1 on 2024-11-14 22:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('research_projects', '0007_post_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='research_projects.project', verbose_name='project'),
        ),
    ]
