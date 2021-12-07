from django.contrib import admin
from .models import imageModel

# Register your models here.
@admin.register(imageModel)
class imageAdmin(admin.ModelAdmin):
    list_display=['id','photo','date']