from django.db import models

# Create your models here.
class Film(models.Model):
    nickname = models.CharField(max_length=40)
    description = models.TextField(null=True)
    release_date = models.DateField()
    director = models.CharField(max_length=40)
