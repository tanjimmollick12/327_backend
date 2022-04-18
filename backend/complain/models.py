from django.db import models
from account.models import User


# Create your models here.
class Complain(models.Model):
    author = models.CharField(max_length=100)
    role = models.CharField(max_length=10,   default='')
    description = models.TextField(max_length=1000)
    reply = models.TextField(max_length=500,   default='')
    created_at = models.DateTimeField(auto_now_add=True)

