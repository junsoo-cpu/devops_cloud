from django.db import models

class List(models.Model):
    song = models.CharField(max_length=100)
    singer= models.TextField(blank=True)
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)