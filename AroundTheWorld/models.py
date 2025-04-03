from django.db import models
from django.contrib.auth.models import User

class Destination(models.Model):
    name = models.CharField(max_length = 100)
    weather = models.CharField(max_length = 100)
    state = models.CharField(max_length = 100)
    district = models.CharField(max_length = 100)
    google_map_link = models.URLField()
    description = models.TextField()
    image = models.ImageField(null = True,blank = True,upload_to = 'images/')