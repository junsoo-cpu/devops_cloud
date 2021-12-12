from django import forms

from comic.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
            "photo",
            "tag_set",
        ]