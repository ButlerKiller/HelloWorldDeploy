from django.urls import path, include
from django.http import HttpResponse
import os


def HelloWorldView(request):
    return HttpResponse('<h1>КИТИС - это пиздец, а не anal. Скоро здесь появится ремастер расписания. (•ω•`)o</h1>')


urlpatterns = [
    path('', HelloWorldView),
]

if os.environ.get('DJANGO_SETTINGS_MODULE') == 'config.settings.dev':
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls))
    ]