from django.db import models
from .tags import Tags
from .post import Post

class PostTags(models.Model):
  
  tag = models.ForeignKey(Tags, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
