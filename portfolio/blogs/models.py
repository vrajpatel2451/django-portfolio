from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=20,)
    description = models.TextField()
    ratings = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blogs')
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    appuser = models.OneToOneField('AppUser',on_delete=models.CASCADE)

    def __str__(self):
        return self.title    

class Category(models.Model):
    name = models.CharField(max_length=20) 

    def __str__(self):
        return self.name
class AppUser(models.Model):
    name = models.CharField(max_length=20) 
    email = models.CharField(max_length=40,primary_key=True) 

    def __str__(self):
        return self.email