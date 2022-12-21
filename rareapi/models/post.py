from django.db import models
from .user import User
from .category import Category
from django.forms.models import model_to_dict

class Post(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    approved = models.BooleanField()
    
    @property
    def tags_on_post(self):
        db_tags = self.tags.all()
        post_tags = []
        for tag in db_tags:
            single_tag = model_to_dict(tag)
            post_tags.append(single_tag)
        return post_tags
