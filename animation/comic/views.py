from django.shortcuts import render

from django.http import HttpRequest, HttpResponse

from comic.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, "comic/post_list.html", {
        "post_list": qs,
    })

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)

    return render(request, "comic/post_detail.html", {
        "post": post,

    })