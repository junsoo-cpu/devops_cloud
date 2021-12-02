from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from catube.models import Video


def index(request: HttpRequest) -> HttpResponse:
    qs = Video.objects.all()  # qs -> lazy(게으르다) 값이 필요한 시점에 찾아와서
    return render(request, "catube/index.html", {
        "video_list": qs,
    })
