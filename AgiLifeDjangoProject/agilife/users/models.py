from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from django.db import models

# Create your models here.
class UserEvent(models.Model):
    creator = models.ForeignKey(User)
    name = models.CharField(max_length=100)
    weight = models.FloatField(null=True, blank=True)
    timePreference = models.IntegerField(default=0)
    timeStart = models.DateTimeField(auto_now=False,auto_now_add=False)
    timeEnd = models.DateTimeField(auto_now=False,auto_now_add=False)
    eventLength = models.FloatField(default=0)
    isDynamic = models.BooleanField(default=False)

class GroupEvent(models.Model):
    creator = models.ForeignKey(Group)
    name = models.CharField(max_length=100)
    weight = models.FloatField(null=True, blank=True)
    timePreference = models.IntegerField(default=0)
    timeStart = models.DateTimeField(auto_now=False,auto_now_add=False)
    timeEnd = models.DateTimeField(auto_now=False,auto_now_add=False)
    eventLength = models.FloatField(default=0)
    isDynamic = models.BooleanField(default=False)


