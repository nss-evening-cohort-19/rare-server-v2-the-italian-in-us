'''Reactions Model'''
from django.db import models

class Reaction(models.Model):
    '''Reaction Class'''
    label = models.CharField(max_length=50)
    image_url = models.CharField(max_length=100)
    