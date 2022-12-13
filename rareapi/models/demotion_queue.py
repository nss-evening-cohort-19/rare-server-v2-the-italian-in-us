from django.db import models
from .user import User

class DemotionQueue(models.Model):

    action = models.CharField(max_length=100)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    approver_one_id = models.ForeignKey(User, on_delete=models.CASCADE)
