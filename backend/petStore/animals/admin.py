from django.contrib import admin

# Register your models here.
from .models import Categories, Status, Tags, Animal

admin.site.register(Categories)
admin.site.register(Status)
admin.site.register(Tags)
admin.site.register(Animal)