from django.conf.urls import url
from . import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^save_data/$', views.save_data, name='save_data'),
    url(r'^$', views.index, name='index'),
    url(r'^levels.html/$', views.get_list_levels, name='get_list_levels'),
    url(r'^levels.html/sort$', views.sort_levels, name='sort_levels'),
    url(r'^levels.html/level.html$', views.get_level, name='get_level'),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns() + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)