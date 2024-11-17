# Generated by Django 5.1 on 2024-11-14 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=255, verbose_name='first_name')),
                ('last_name', models.TextField(max_length=255, verbose_name='last_name')),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True, verbose_name='publisher name')),
            ],
            options={
                'db_table': 'publisher',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255, verbose_name='name')),
            ],
            options={
                'db_table': 'university',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(unique=True, verbose_name='title')),
                ('arxiv', models.TextField(unique=True, verbose_name='arxiv_id')),
                ('published_date', models.DateField(verbose_name='published_date')),
                ('authors', models.ManyToManyField(to='papers.author', verbose_name='author')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='papers.publisher', verbose_name='publisher')),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='affiliation',
            field=models.ManyToManyField(blank=True, null=True, to='papers.university', verbose_name='affiliation'),
        ),
    ]
