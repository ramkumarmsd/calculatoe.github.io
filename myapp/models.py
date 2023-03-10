from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class calculator(models.Model):
    number1 = models.IntegerField(default='')
    number2 = models.IntegerField(default='')
    answer = models.CharField(default='',max_length=100)

         