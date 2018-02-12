import json

import tornado.ioloop
import tornado.web

from uadetector.tornado.web import RequestHandler

# define(
#     'uadetector_request_property_name',
#     default='ua',
#     help='xxx'
# )
# define(
#     'uadetector_useragent_class',
#     default='myuser.MyUserAgent',
#     help='xxx'
# )


class IndexHandler(RequestHandler):

    def get(self):
        content = '<pre>{}</pre>'.format(json.dumps({
            'device_type': self.request.ua.device_type,
            'os': self.request.ua.os,
            'browser': self.request.ua.browser,
            'from_pc': self.request.ua.from_pc,
            'from_smartphone': self.request.ua.from_pc,
        }, indent=2))
        self.write(content)


def make_app():
    return tornado.web.Application([
        (r'/', IndexHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
