from django.db import models
from .user import User

class UserTypeChangeRequest(models.Model):

    action = models.CharField(max_length=100)
    admin_one_id = models.ForeignKey(User,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     related_name="admin_one")
    admin_two_id = models.ForeignKey(User,
                                     on_delete=models.SET_NULL,
                                     null=True,
                                     related_name="admin_two")
    modified_user_id = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    related_name="modified_user")
