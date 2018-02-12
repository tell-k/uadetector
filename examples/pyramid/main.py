import json
from wsgiref.simple_server import make_server

from pyramid.config import Configurator
from pyramid.response import Response

from uadetector.pyramid import ua_prop


def index(request):
    return Response('<pre>{}</pre>'.format(json.dumps({
        'device_type': request.ua.device_type,
        'os': request.ua.os,
        'browser': request.ua.browser,
        'from_pc': request.ua.from_pc,
        'from_smartphone': request.ua.from_pc,
    }, indent=2)))


with Configurator() as config:
    config.add_route('index', '/')
    config.add_view(index, route_name='index')

    # add request method
    config.add_request_method(ua_prop(), name='ua', reify=True)
    app = config.make_wsgi_app()

if __name__ == '__main__':
    with make_server('127.0.0.1', 8000, app) as server:
        print("Serving on port 8000...")
        server.serve_forever()
