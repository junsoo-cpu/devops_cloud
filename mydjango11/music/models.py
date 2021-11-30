from django.db import models


class List(models.Model):
    name = models.CharField(max_length=100, verbose_name="제목")
    singer = models.CharField(max_length=100, verbose_name="가수명")
    date = models.DateTimeField(max_length=100, verbose_name="작성 날짜")
    appraisal = models.TextField(verbose_name="한줄 평")  # FK키를 쓰는 게 적절

    def __str__(self):
        return self.name

