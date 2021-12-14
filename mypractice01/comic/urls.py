from django.urls import path

from comic import views

app_name = 'comic'

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("new/", views.post_new, name="post_new"),
    path("<int:pk>/edit/", views.post_edit, name="post_edit"),
    path("<int:post_pk>/review/new", views.review_new, name="review_new"),
    path("<int:post_pk>/review/<int:pk>/edit", views.review_edit, name="review_edit"),
]