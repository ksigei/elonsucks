from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('forum/', include('forum.urls')),
    path('support/', include('support.urls')),
    path('userprofile/', include('userprofile.urls')),
    path('', include('elonsucks.urls')),
]

# Add static and media URL patterns
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
