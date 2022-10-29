import os
from django.conf import settings
from django.db import models

# Create your models here.

def images_path():
    return os.path.join(settings.BASE_DIR, 'images')

class Categories(models.Model):
    category_title = models.CharField(max_length=128, unique=True)

class Status(models.Model):
    status_name = models.CharField(max_length=128, unique=True)

class Tags(models.Model):
    tag = models.CharField(max_length=128)

class Animal(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Categories, to_field='category_title', on_delete=models.SET_NULL, null=True)
    pic_URL = models.FilePathField(max_length=256, path=images_path)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, to_field='status_name', null=True)
    tags = models.ManyToManyField(Tags)
