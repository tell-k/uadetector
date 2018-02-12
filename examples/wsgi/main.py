import json
from wsgiref.simple_server import make_server

from uadetector import UADetector, ENVIRON_KEY


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    ua = environ.get(ENVIRON_KEY)
    content = json.dumps({
        'device_type': ua.device_type,
        'os': ua.os,
        'browser': ua.browser,
        'from_pc': ua.from_pc,
        'from_smartphone': ua.from_pc,
    }, indent=2)
    return [content.encode('utf-8')]


application = UADetector(app)

if __name__ == "__main__":
    with make_server('127.0.0.1', 8000, application) as server:
        print("Serving on port 8000...")
        server.serve_forever()
