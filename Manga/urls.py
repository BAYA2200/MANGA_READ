from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Manga import settings
from Manga.settings.base import STATIC_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
    path('', include('anime.urls')),
]+ static(settings.base.STATIC_URL, document_url=settings.base.STATIC_URL)

