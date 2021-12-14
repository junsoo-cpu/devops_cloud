from django import forms

from comic.models import Post, Tag, Review


class PostForm(forms.ModelForm):
    tags = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:  # 수정 시
            tag_qs = self.instance.tag_set.all()
            tags = ", ".join([tag.name for tag in tag_qs])
            self.fields["tags"].initial = tags

    def save(self):
        saved_post = super().save()

        tag_list = []
        tags = self.cleaned_data.get("tags", "")
        for word in tags.split(","):
            tag_name = word.strip()
            tag, __ = Tag.objects.get_or_create(name=tag_name)
            tag_list.append(tag)

        saved_post.tag_set.clear()
        saved_post.tag_set.add(*tag_list)
        return saved_post

    class Meta:
        model = Post
        fields = ["category",
                  "title",
                  "content",
                  ]


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["name",  "message"]
