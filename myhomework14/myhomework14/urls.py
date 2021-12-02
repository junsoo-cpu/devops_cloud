from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from music.views import index, video_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('music/', index),
    path("music/<int:pk>/", video_detail),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]
