# Generated by Django 5.1 on 2024-11-18 08:25

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('papers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='project id')),
                ('short_project_id', models.CharField(editable=False, max_length=8, unique=True, verbose_name='project_id')),
                ('name', models.TextField(verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('project_url', models.URLField(blank=True, max_length=255, null=True, verbose_name='project URL')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('is_public', models.BooleanField(default=False, verbose_name='is_public')),
                ('is_visible', models.BooleanField(default=True, verbose_name='is_visible')),
                ('members', models.ManyToManyField(related_name='projects', to=settings.AUTH_USER_MODEL, verbose_name='member')),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='content')),
                ('posted_on', models.DateTimeField(auto_now_add=True, verbose_name='posted_on')),
                ('contributer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='contributer')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='research_projects.project', verbose_name='project')),
            ],
            options={
                'db_table': 'post',
            },
        ),
        migrations.CreateModel(
            name='PapersIndices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(verbose_name='index')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papers.paper')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='papers_indices', to='research_projects.project')),
            ],
            options={
                'db_table': 'papers_indices',
                'constraints': [models.UniqueConstraint(fields=('index', 'project'), name='unique_index_project'), models.UniqueConstraint(fields=('paper', 'project'), name='unique_paper_project')],
            },
        ),
    ]
