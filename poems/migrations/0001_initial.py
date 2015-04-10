# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import poems.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to=poems.models.pub_file_dir, blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Related_Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('url', models.URLField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to=poems.models.pub_file_dir, blank=True, null=True)),
                ('url', models.URLField(max_length=500)),
                ('slug', models.SlugField(unique=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ['title'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Writer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('bio', models.TextField()),
                ('url', models.URLField(max_length=500)),
                ('photo', models.ImageField(upload_to=poems.models.file_dir, blank=True, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='video',
            name='writer',
            field=models.ForeignKey(to='poems.Writer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='publication',
            name='writer',
            field=models.ForeignKey(to='poems.Writer'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='poem',
            name='writer',
            field=models.ForeignKey(to='poems.Writer'),
            preserve_default=True,
        ),
    ]
