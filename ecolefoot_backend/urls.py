from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from api import admin_urls  # importe ton nouveau fichier


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('admin/', include(admin_urls)),  # redirige vers le fichier avec logout personnalisé
    path('api/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
