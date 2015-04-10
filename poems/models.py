from django.db import models
from django_markdown.models import MarkdownField

import os
# Create your models here.

def file_dir(instance, file_name):
    # /writers/writer.slug/filename
    return '/'.join(['writers', instance.slug, file_name])


def pub_file_dir(instance, file_name):
    # /publications/writer.slug/publications.slug/filename
    return '/'.join(['publications', instance.writer.slug, instance.slug, file_name])


class Writer(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    bio = MarkdownField()
    url = models.CharField(max_length=500)
    photo = models.ImageField(upload_to=file_dir, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Meta:
    ordering = ['name']


class Poem(models.Model):
    name = models.CharField(max_length=200)
    body = MarkdownField()
    writer = models.ForeignKey(Writer)
    slug = models.SlugField(max_length=50, unique=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Publication(models.Model):
    title = models.CharField(max_length=200)
    publisher = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=pub_file_dir, null=True, blank=True)
    writer = models.ForeignKey(Writer)
    slug = models.SlugField(max_length=50, unique=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Related_Link(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    # url = models.CharField(max_length=500)
    url = models.CharField(max_length=500)

    description = models.TextField()


    def __str__(self):
        return self.name


    class Meta:
        ordering = ['name']


class Video(models.Model):
    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to=pub_file_dir, null=True, blank=True)
    url = models.CharField(max_length=500)
    writer = models.ForeignKey(Writer)
    slug = models.SlugField(max_length=50, unique=True, )
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
