from django.db import models

# Create your models here.


class Bridges(models.Model):
    title = models.CharField(max_length=100)
    long_version = models.CharField(max_length=100)
    short_version = models.CharField(max_length=100)
