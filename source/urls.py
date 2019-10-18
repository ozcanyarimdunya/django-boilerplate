from django.conf import settings
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = settings.SITE_HEADER
admin.site.site_title = settings.SITE_HEADER

urlpatterns = [
    path('', include('source.apps.common.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
