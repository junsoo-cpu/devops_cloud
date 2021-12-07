from django.db import models


class Timestamped(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(Timestamped):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="diary/post/%Y/%m/%d")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "포스팅"
        verbose_name_plural = "포스팅 목록"


class Comment(Timestamped):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"


class Tag(Timestamped):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"
