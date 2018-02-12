WSGI middleware for handling User-Agent. Thanks to `woothee <https://github.com/woothee/woothee-python>`_ , UADetector supports various User-Agents. This is heavily inspired by `k0kubun/rack-user_agent <https://github.com/k0kubun/rack-user_agent>`_ . Thanks :)

Installation
===================

::

 $ pip install uadetector


Usage
=====================

WSGI middleware
----------------------

This middleware provides a `uadetector.useragent.UserAgent` object to handling User-agents.

.. code-block:: python

 import json
 from wsgiref.simple_server import make_server

 # import middleware
 from uadetector import UADetector

 def app(environ, start_response):
     start_response('200 OK', [('Content-Type', 'text/plain')])

     # get 'uadetector.useragent.UserAgent' object from environ dict.
     ua = environ.get('uadetector.useragent')

     content = json.dumps({
         'device_type': ua.device_type,
         'os': ua.os,
         'browser': ua.browser,
         'from_pc': ua.from_pc,
         'from_smartphone': ua.from_pc,
     }, indent=2)
     return [content.encode('utf-8')]

 # apply middleware
 application = UADetector(app)

 if __name__ == "__main__":
     with make_server('127.0.0.1', 8080, application) as server:
         print("Serving on port 8000...")
         server.serve_forever()

You can also replace the key of environ_dict or the UserAgent class.

.. code-block:: python

 from uadetector.useragent import UserAgent

 class MyUserAgent(UserAgent):
      # Write your custom codes.

 # apply middleware
 application = UADetector(
    app,
    envorion_key='your.favorite.key'
    useragent_class='xxxx.MyUserAgent'
 )

Web Frameworks 
----------------------

Some Web frameworks provide a way to extend in a different way from WSGI Middleware. We provide shortcuts according to that way.

** Caution: I don't intend to actively respond to the framework. If you are worried, you should use WSGIMiddleware. **

Django
~~~~~~~~~

You can use Django's `MIDDLEWARE`. like this.

.. code-block:: python

 # settings.py 

 MIDDLEWARE = [
    # Add UADetecorMiddleware
    'uadetector.django.middleware.UADetectorMiddleware',
    # ... omit ...
 ]

.. code-block:: python

 # views.py 

 def index_view(request):
     print(request.ua.from_smartphone) # => True or False
     # ... omit ...


Pyramid
~~~~~~~~~

You can use `config.add_request_method`.

.. code-block:: python

 from uadetector.pyramid import ua_prop


 def index(request):
     print(request.ua.from_smartphone) # => True or False
     # ... omit ...


 with Configurator() as config:
     config.add_route('index', '/')
     config.add_view(index, route_name='index')

     config.add_request_method(ua_prop(), name='ua', reify=True)
     # ... omit ...


Flask
~~~~~~~~~

You can use `Flask Extension`.

.. code-block:: python

 from flask import Flask, request
 from uadetector.flask import UADetector

 app = Flask(__name__)
 UADetector(app)

 @app.route('/')
 def index():
     print(request.ua.from_smartphone) # => True or False
     # ... omit ...


Tornado
~~~~~~~~~

You can use custom `RequestHandler`.

.. code-block:: python 

  from uadetector.tornado.web import RequestHandler

  class IndexHandler(RequestHandler):

      def get(self):
          print(self.request.ua.from_smartphone) # => True or False
          # ... omit ...


UserAgent object
===================

attrs
-----------

* UserAgent.device_type
* UserAgent.os
* UserAgent.os_version
* UserAgent.browser
* UserAgent.browser_version
* UserAgent.browser_vendor

helpers
-----------

* UserAgent.from_pc
* UserAgent.from_smartphone
* UserAgent.from_mobilephone
* UserAgent.from_appliance
* UserAgent.from_crawler

detectors
-----------

* UserAgent.smartphone_version
* UserAgent.from_iphone
* UserAgent.from_ipad
* UserAgent.from_ipod
* UserAgent.from_android
* UserAgent.from_android_tablet
* UserAgent.from_windows_phone
* UserAgent.from_ios
* UserAgent.from_android_os

License
========

MIT License

Authors
=======

* tell-k <ffk2005 at gmail.com>

History
=======

0.1.0(Feb 12, 2018)
---------------------

* First release
