from django.db import models

class Tide(models.Model):

    location = models.CharField(max_length=20)
