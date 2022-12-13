from django.db import models
from .user import User


class Subscription(models.Model):

    follower_id = models.ForeignKey(User, on_delete=models.CASCADE)
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField()
    ended_on = models.DateField()
    