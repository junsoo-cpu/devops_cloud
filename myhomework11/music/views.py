from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from music.models import List


def index(request):
    return render(request, "music/index.html")

def list_list(request: HttpRequest) -> HttpResponse:
    # request.GET # QueryString Values
    # request.POST # Post 요청 Values
    # request.FILES # Post 요청에서 파잃 Values

    qs = List.objects.all()
    qs = qs.order_by("-pk")
    # blog/templates/blog/post_list.html

    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, "music/list_list.html", {
        "list_list" : qs,
    })

def list_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # pk = 1
    list = List.objects.get(pk=pk)
    return render(request, "music/list_detail.html", {
        "list": list,
    })
