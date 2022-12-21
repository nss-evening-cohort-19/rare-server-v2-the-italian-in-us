from django.db import models
from .user import User


class Subscription(models.Model):

    follower_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    author_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    created_on = models.DateField(auto_now_add=True)    
