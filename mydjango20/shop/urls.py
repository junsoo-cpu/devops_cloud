from shop import views
from django.urls import path

app_name = "shop"

urlpatterns = [
    path("", views.shop_list, name="shop_list"),
    path("<int:pk>/", views.shop_detail, name="shop_detail"),
    path("new/", views.shop_new, name="shop_new"),   # 앞에 shop/로 처리가 되어 있음(기존 url)
]