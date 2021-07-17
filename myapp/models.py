from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=200)

class Username(models.Model):
    username = models.CharField(max_length=200)

class Message(models.Model):
    sent_user = models.CharField(max_length=200)
    value = models.TextField(blank=True)
    room = models.CharField(max_length=200)
    create_at = models.DateTimeField(default=datetime.now)