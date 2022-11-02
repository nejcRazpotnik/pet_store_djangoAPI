import os
from django.conf import settings
from django.db import models
from django.forms import ModelForm

# Create your models here.

def images_path():
    return os.path.join(settings.BASE_DIR, 'images')

class Categories(models.Model):
    category_title = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.category_title

class Status(models.Model):
    status_name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.status_name

class Tags(models.Model):
    tag = models.CharField(max_length=128)

    def __str__(self):
        return self.tag

class Picture_URLs(models.Model):
    picture_URL = models.FilePathField(max_length=256, path=images_path, null=True)
    title = models.CharField(max_length=256, null=True)
    picture_file = models.FileField(null=True)

class Animal(models.Model):
    name = models.CharField(max_length=128)
    category = models.ForeignKey(Categories, to_field='category_title', on_delete=models.SET_NULL, null=True)
    pictures = models.ManyToManyField(Picture_URLs, blank=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, to_field='status_name', null=True)
    tags = models.ManyToManyField(Tags, blank=True)


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'category', 'pictures', 'status', 'status', 'tags']