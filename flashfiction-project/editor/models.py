from django.db import models

# Create your models here.


class Fiction(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=300)
