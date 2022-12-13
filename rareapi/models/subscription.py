from django.db import models


class Subscription(models.Model):

    follower_id = models.IntegerField()
    author_id = models.IntegerField()
    created_on = models.DateField()
    ended_on = models.DateField()
    