from django.urls import path, include
from django.http import HttpResponse
import os


def HelloWorldView(request):
    return HttpResponse('Hello world!')


urlpatterns = [
    path('', HelloWorldView),
]

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.dev':
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]