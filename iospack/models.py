from django.db import models

# Create your models here.

class AppInfo(models.Model):
    name = models.CharField(max_length=32)
    icon = models.URLField(max_length=200)
    launcher = models.URLField(max_length=200)
    version = models.CharField(max_length=32)
    bundle_id = models.CharField(max_length=100)
