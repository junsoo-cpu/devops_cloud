from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from catube.views import index, video_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catube/', index),
    path('catube/<int:pk>/', video_detail),
]

urlpatterns += static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
# static은 그자체가 리스트여서 리스트 씌우지 않는다


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]