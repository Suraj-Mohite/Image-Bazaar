from django.db import models

# Create your models here.

class imageModel(models.Model):
    photo=models.ImageField(upload_to='upload')
    date=models.DateField(auto_now_add=True)