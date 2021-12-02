from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView

from catube.models import Video

# class Based View (CBV)
index = ListView.as_view(model=Video,
                         template_name="catube/index.html")

# Function Based View (FBV)
# def index(request: HttpRequest) -> HttpResponse:
#     qs = Video.objects.all()  # qs -> lazy(게으르다) 값이 필요한 시점에 찾아와서
#     return render(request, "catube/index.html", {
#         "video_list": qs,
#     })


def video_detail(request: HttpRequest, pk: int) -> HttpResponse:
    video = Video.objects.get(pk=pk)
    return render(request, "catube/video_detail.html", {
        "video": video,
    })
