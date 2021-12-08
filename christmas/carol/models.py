from django.db import models


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Post(TimeStamp):
    title = models.CharField(max_length=100, db_index=True)
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to="carol/%Y/%m/%d")
    tag_set = models.ManyToManyField("Tag")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "캐롤"
        verbose_name_plural = "캐롤 목록"


class Comment(TimeStamp):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"


class Tag(TimeStamp):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"
