from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from comic.forms import PostForm
from comic.models import Post


def tag_detail(request: HttpRequest, tag_name: str) -> HttpResponse:
    qs = Post.objects.all()
    qs = qs.filter(tag_set__name=tag_name)

    return render(request, "comic/tag_detail.html", {
        "tag_name": tag_name,
        "post_list": qs,
    })


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    return render(request, "comic/post_list.html", {
        "post_list": qs,
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    comment_list = post.comment_set.all()
    tag_list = post.tag_set.all()

    return render(request, "comic/post_detail.html", {
        "post": post,
        "comment_list": comment_list,
        "tag_list": tag_list,
    })

def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            print("유효성 검사에 통과했습니다. :", form.cleaned_data)
            form.save()
            return redirect("comic:post_list")
        else:
            pass
    return render(request, "comic/post_form.html", {
        "form": form,
    })