from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=280)
    profile_image_url = models.CharField(max_length=50)
    email = models.EmailField()
    created_on = models.DateField()
    active = models.BooleanField()
    is_staff = models.BooleanField()
