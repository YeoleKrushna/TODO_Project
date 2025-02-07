from django.db import models

# Create your models here.
class Books(models.Model):
    name = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    desc = models.TextField()
    prize = models.IntegerField()
    def __str__(self):
       return self.name
