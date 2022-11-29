from django.db import models

# Create your models here.
class Club(models.Model):
    name = models.CharField(max_length=60)
    stadium = models.CharField(max_length=3)

    def __str__(self):
        return self.name

class Team(models.Model):
    rank = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    pts = models.CharField(max_length=60)
    gd = models.CharField(max_length=60)
    mp = models.CharField(max_length=60)

    def __str__(self):
        return self.name
