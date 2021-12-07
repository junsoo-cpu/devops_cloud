# view 함수와 url의 매핑
from django.shortcuts import redirect
from django.urls import path

from diary import views

app_name = "diary"

#TODO : 편의상 여기에 root를 구현하지만 차후
# RedirectView CBV를 써서 이 구현을  제거할 예정
def root(request):
    return redirect("diary:post_list")

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path('', root, name="root"),
]
