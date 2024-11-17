# Generated by Django 5.1 on 2024-11-14 23:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('papers', '0001_initial'),
        ('research_projects', '0009_remove_project_papers_paperscitationindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='PapersIndices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(verbose_name='index')),
                ('paper', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='papers.paper')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='papers_indices', to='research_projects.project')),
            ],
            options={
                'db_table': 'papers_indices',
            },
        ),
        migrations.DeleteModel(
            name='PapersCitationIndex',
        ),
        migrations.AddConstraint(
            model_name='papersindices',
            constraint=models.UniqueConstraint(fields=('index', 'project'), name='unique_index_project'),
        ),
        migrations.AddConstraint(
            model_name='papersindices',
            constraint=models.UniqueConstraint(fields=('paper', 'project'), name='unique_paper_project'),
        ),
    ]
