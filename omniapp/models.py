from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1048)
    # image_path = models.ImageField(upload_to = '')
    image = models.ImageField(upload_to = 'movies_pics')

    duration = models.IntegerField()
    genre = models.CharField(max_length=40)
    language = models.CharField(max_length=44)
    # mpaaRating = 
    type = models.CharField(max_length=20)
    label = models.CharField(max_length=255)
    userRating = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

