from django.db import models
from django.utils import timezone

"""
Run migrations everytime you modify the models

python manage.py makemigrations

python manage.py migrate
"""
# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=255)

    
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    release_year = models.IntegerField()
    price = models.FloatField()
    image_url = models.TextField()
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE) 
    
    def __str__(self):
        return self.title + "|"+ str(self.release_year) + "|" + str(self.price)