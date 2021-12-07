from django.db import models


class TimestampedModel(models.Model):  # 상속
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 추상 클래스로서 DB 테이블이 생기지 않는다.


class Post(TimestampedModel):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200, db_index=True)  # db_index가 생성되어 있어야 검색 가능
    content = models.TextField()
    photo = models.ImageField(upload_to="diary/post/%Y/%m/%d")  # media 바로 밑에 저장, upload to 를 통해 경로 설정
    tag_set = models.ManyToManyField('Tag')  # 참조가 아니어서 Tag를 문자열로 지정 django app에서 Tag를 찾아줌

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "포스팅"
        verbose_name_plural = "포스팅 목록"


class Comment(TimestampedModel):
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"


class Tag(TimestampedModel):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"
