from django.db import models

# Create your models here.
class Fiction(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=300)

class Bridges(models.Model):
    title = models.CharField(max_length=100)
    long_version = models.CharField(max_length=100)
    short_version = models.CharField(max_length=100)
    