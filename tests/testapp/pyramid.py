from pyramid.config import Configurator
from pyramid.response import Response
from uadetector.pyramid import ua_prop


def view1(request):
    return Response(request.ua.os)


def view2(request):
    return Response(request.ua.__class__.__name__)


def view3(request):
    return Response(request.ua_obj.os)


def make_app(ua_class=None, prop_name='ua'):
    config = Configurator()
    config.add_route('view1', '/view1')
    config.add_route('view2', '/view2')
    config.add_route('view3', '/view3')
    config.add_view(view1, route_name='view1')
    config.add_view(view2, route_name='view2')
    config.add_view(view3, route_name='view3')

    # add request method
    config.add_request_method(ua_prop(ua_class), name=prop_name, reify=True)
    return config.make_wsgi_app()
