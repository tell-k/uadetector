import django
from django.http import HttpResponse
from django.conf import settings


def view1(request):
    return HttpResponse(request.ua.os)


def view2(request):
    return HttpResponse(request.ua.__class__.__name__)


def view3(request):
    return HttpResponse(request.ua_obj.os)


if django.VERSION < (2, 0):
    from django.conf.urls import url
    urlpatterns = [
        url(r'^view1', view1),
        url(r'^view2', view2),
        url(r'^view3', view3),
    ]
else:
    from django.urls import path
    urlpatterns = [
        path('view1', view1),
        path('view2', view2),
        path('view3', view3),
    ]


settings.configure(
    ALLOWED_HOSTS=['*'],
    DEBUG=True,
    ROOT_URLCONF=__name__,
    MIDDLEWARE=(
        'django.middleware.common.CommonMiddleware',
        'uadetector.django.middleware.UADetectorMiddleware',
        # Skip re-assign useragent object to request object.
        'uadetector.django.middleware.UADetectorMiddleware',
    )
)
