from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    ratings = models.IntegerField(default=0)
    