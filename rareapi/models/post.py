from django.db import models
from .user import User
from .category import Category

class Post(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_author')
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    image_url = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    approved = models.BooleanField()

    @property
    def edited_on(self):
        return self.__edited_on
    
    @edited_on.setter
    def edited_on(self, value):
        self.__edited_on = value
            