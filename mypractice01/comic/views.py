from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from comic.forms import PostForm, ReviewForm
from comic.models import Post, Category, Review


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    category_qs = Category.objects.all()

    category_id: str = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)

    return render(request, "comic/post_list.html", {
        "post_list": qs,
        "category_list": category_qs
    })


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    review_list = post.review_set.all()
    return render(request, "comic/post_detail.html", {
        "post": post,
        "review_list": review_list,
    })


def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()

            return redirect("comic:post_detail", saved_post.pk)
    else:
        form = PostForm()

    return render(request, "comic/post_form.html", {
        "form": form,
    })


def post_edit(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            saved_post = form.save()
            # shop_detail 뷰를 구현했다면 !!!
            return redirect("comic:post_detail", saved_post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, "comic/post_form.html", {
        "form": form,
    })


def review_new(request, post_pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            review.save()
            return redirect("comic:post_detail", post_pk)
    else:
        form = ReviewForm()
    return render(request, "comic/review_form.html", {
        "form": form,
    })


def root(request):
    return redirect("comic:post_list")


def review_edit(request: HttpRequest, post_pk: int, pk: int) -> HttpResponse:
    review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "성공적으로 저장했습니다.")
            return redirect("comic:post_detail", post_pk)
    else:
        form = ReviewForm(instance=review)

    return render(request, "comic/review_form.html", {
        "form": form,
    })
