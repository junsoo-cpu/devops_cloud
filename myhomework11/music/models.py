from django.db import models
from music.upload_to import uuid_name_upload_to

class List(models.Model):
    name = models.CharField(max_length=100, verbose_name="제목")
    singer = models.CharField(max_length=100, verbose_name="가수명")
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField(verbose_name="한줄 평")  # FK키를 쓰는 게 적절
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    updated_at = models.DateTimeField(auto_now=True)


    # upload_to
    # - 문자열 : 파일이 저장되는 폴더의 경로


