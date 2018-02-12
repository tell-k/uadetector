import tornado.web
from tornado.options import define

from uadetector.tornado.web import RequestHandler


class View1Handler(RequestHandler):

    def get(self):
        # Skip re-assign useragent object to request object.
        self.initialize()
        self.write(self.request.ua.os)


class View2Handler(RequestHandler):

    def get(self):
        self.write(self.request.ua.__class__.__name__)


class View3Handler(RequestHandler):

    def get(self):
        self.write(self.request.ua_obj.os)


def make_app(ua_class=None, prop_name=None):

    if ua_class:
        define('uadetector_useragent_class', default=ua_class)
    if prop_name:
        define('uadetector_request_property_name', default=prop_name)

    return tornado.web.Application([
        (r'/view1', View1Handler),
        (r'/view2', View2Handler),
        (r'/view3', View3Handler),
    ])
