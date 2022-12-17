from django.db import models
from rest_framework import serializers
import json
from django.forms.models import model_to_dict



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

    @property
    def subscribers(self):
        """other users that have subscribed to this user"""
        db_subs = self.followers.all()
        subs = []
        for sub in db_subs:
            sub = model_to_dict(sub)
            subs.append(sub)
        return subs
    
    @property    
    def posts(self):
        """posts by author"""
        db_posts = self.post_author.all()
        posts = []
        for post in db_posts:
            post = model_to_dict(post)
            posts.append(post)
        return posts
    
    @property
    def following(self):
        """users this user is following"""
        db_users_following = self.author.all()
        users_following = []
        for user in db_users_following:
            user = model_to_dict(user)
            users_following.append(user)
        return users_following
        