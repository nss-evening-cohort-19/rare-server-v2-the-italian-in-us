''''Post Reaction model'''

from django.db import models
from .reaction import Reaction
from .post import Post
from .user import User

class PostReaction(models.Model):
    '''Post Reactions class'''
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    reaction_id = models.ForeignKey(Reaction, on_delete=models.CASCADE)
