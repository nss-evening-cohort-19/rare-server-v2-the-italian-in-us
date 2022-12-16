from django.db import models


class User(models.Model):

    uid = models.CharField(max_length=50, default="X2B6BcDVXNbCHo1svFqlGmBpMWl1")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.CharField(max_length=280)
    profile_image_url = models.CharField(max_length=50)
    email = models.EmailField()
    created_on = models.DateField(auto_now_add=True)
    active = models.BooleanField()
    is_staff = models.BooleanField()
