from django.urls import path
from django.shortcuts import redirect
from diary import views

app_name = "diary"

def root(request):
    return redirect("diary:post_list")

urlpatterns = [
    path("", views.post_list, name="post_list"),
]