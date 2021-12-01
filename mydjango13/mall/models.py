import datetime
from django.db import models

class shop(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    telephone = models.CharField(max_length=13)
    open_time = models.TimeField(default=datetime.time) # datetime.time -> 함수 값(time())을 받는 것이 아닌 함수(time)를 넣음
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)