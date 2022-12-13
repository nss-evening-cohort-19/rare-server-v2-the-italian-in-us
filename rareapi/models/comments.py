'''Comments Model'''

from django.db import models

class Comment(models.Model):
    '''Coment Model'''
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)
    created_on = models.DateField()
    

    