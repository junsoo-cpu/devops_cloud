from django.core.validators import RegexValidator
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimestampedModel):
    title = models.CharField(max_length=100, db_index=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="comic/post/%Y/%m/%d")
    tag_set = models.ManyToManyField('Tag', blank=True)
    ip = models.GenericIPAddressField()

    def __str__(self) -> str:
        return f"[{self.pk}] {self.title}"


class Comment(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()


class Tag(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name
