from django.conf.urls import include, url
from django.conf.urls.static import static
from main_settings import settings

urlpatterns = [
    url(r'', include('save_data.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

