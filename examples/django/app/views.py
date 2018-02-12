import json

from django.http import HttpResponse


def index(request):
    content = json.dumps({
        'device_type': request.ua.device_type,
        'os': request.ua.os,
        'browser': request.ua.browser,
        'from_pc': request.ua.from_pc,
        'from_smartphone': request.ua.from_pc,
    }, indent=2)
    return HttpResponse(content, content_type="text/plain")
