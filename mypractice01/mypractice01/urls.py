from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path, include

def root(request):
    return redirect("comc:post_list")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('comic/', include("comic.urls")),
    path('', root, name="root"),
]

urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
