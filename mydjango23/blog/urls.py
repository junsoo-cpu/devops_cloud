from django.urls import path

from blog.views import fbv as views       # 함수 기반
# from blog.views import cbv as views         # 클래스 기반


app_name = "blog"

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path("subscriber/new/", views.subscriber_new, name="subscriber_new"),
]