WSGI Middleware and web framework extensions for handling User-Agent. Thanks to `woothee <https://github.com/woothee/woothee-python>`_ , UADetector supports various User-Agents. This library respects to `k0kubun/rack-user_agent <https://github.com/k0kubun/rack-user_agent>`_ .

|travis| |coveralls| |version| |license|

Installation
===================

::

 $ pip install uadetector


Usage
=====================

WSGI middleware
----------------------

This middleware provides a ``uadetector.useragent.UserAgent`` object to handling User-agents. 

.. code-block:: python

 from wsgiref.simple_server import make_server

 # import middleware
 from uadetector import UADetector

 def app(environ, start_response):
     start_response('200 OK', [('Content-Type', 'text/plain')])

     # get 'UserAgent' object from environ dict.
     ua = environ.get('uadetector.useragent')

     ua.user_agent       #=> "Mozilla/5.0 (Macintosh; ..."
     ua.device_type      #=> "pc"
     ua.os               #=> "Mac OSX"
     ua.browser          #=> "Chrome"
     ua.from_pc          #=> True
     ua.from_smartphone  #=> False

     return [ua.os.encoding('utf-8')]

 # Apply middleware
 application = UADetector(app)

 if __name__ == "__main__":
     with make_server('127.0.0.1', 8000, application) as server:
         print("Serving on port 8000...")
         server.serve_forever()

You can also replace the key of ``environ`` or the ``UserAgent`` class.

.. code-block:: python

 from uadetector.useragent import UserAgent

 class MyUserAgent(UserAgent):
      # Write your custom codes.

 # Apply middleware
 application = UADetector(
    app,
    envorion_key='your.favorite.key'
    useragent_class='path.to.MyUserAgent'
 )

See also `WSGI example <https://github.com/tell-k/uadetector/blob/master/examples/wsgi/>`_.

Web framework extensions
--------------------------------

Some web frameworks provide a way to extend in a different way from WSGI Middleware. We provide shortcuts according to that way.

**Caution: I do not actively support individual frameworks. If you are worried, you should use WSGIMiddleware.**

Django
~~~~~~~~~

You can use Django's ``MIDDLEWARE``.

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

Customize property name of request object and replace UserAgent class.

.. code-block:: python

 # settings.py

 UADETECTOR_REQUEST_PROPERTY_NAME = 'agent' # => You can use "request.agent"
 UADETECTOR_USERAGENT_CLASS = 'path.to.MyUserAgent'

See also `Dajngo example <https://github.com/tell-k/uadetector/blob/master/examples/django/>`_.

Pyramid
~~~~~~~~~

You can use ``config.add_request_method``.

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

Customize property name of request object and replace UserAgent class.

.. code-block:: python

 config.add_request_method(
     ua_prop('path.to.MyUserAgent'),
     name='agent',  # => You can use "request.agent"
     reify=True
 )

See also `Pyramid example <https://github.com/tell-k/uadetector/blob/master/examples/pyramid/>`_.

Flask
~~~~~~~~~

You can use ``Flask Extension``.

.. code-block:: python

 from flask import Flask, request
 from uadetector.flask import UADetector

 app = Flask(__name__)
 UADetector(app)

 @app.route('/')
 def index():
     print(request.ua.from_smartphone) # => True or False
     # ... omit ...

Customize property name of request object and replace UserAgent class.

.. code-block:: python

 app = Flask(__name__)

 app.config['UADETECTOR_USERAGENT_CLASS'] = 'path.to.MyUserAgent'
 app.config['UADETECTOR_REQUEST_PROPERTY_NAME'] = 'agent' # => You can use "request.agent"

 UADetector(app)

See also `Flask example <https://github.com/tell-k/uadetector/blob/master/examples/flask/>`_.

Tornado
~~~~~~~~~

You can use custom ``RequestHandler``.

.. code-block:: python

  from uadetector.tornado.web import RequestHandler

  class IndexHandler(RequestHandler):

      def get(self):
          print(self.request.ua.from_smartphone) # => True or False
          # ... omit ...

Customize property name of request object and replace UserAgent class.

.. code-block:: python

 from tornado.options import define
 from uadetector.tornado.web import RequestHandler

 define(
     'uadetector_request_property_name',
     default='agent', # => You can use "self.request.agent"
 )
 define(
     'uadetector_useragent_class',
     default='path.to.MyUserAgent'
 )

 class IndexHandler(RequestHandler):

See also `Tornado example <https://github.com/tell-k/uadetector/blob/master/examples/tornado/>`_.

UserAgent
===================

List of properties of ``uadetector.useragent.UserAgent`` object.

attrs
-----------

* UserAgent.device_variant
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

Tips
===================

If you want a ``UserAgent`` object simply from the User-Agent string, Please use ``get_useruseragent``.

.. code-block:: python

 from uadetector import get_useragent

 ua_string = "Mozilla/5.0 (iPhone; CPU iPhone OS ..."

 ua = get_useragent(ua_string)
 us.from_smartphone # => True

 # Use custom useragent class
 ua = get_useragent(ua_string, useragent_class='path.to.MyUserAgent')

Support
========

Support latest 3 minor versions.

* Python 3.4, 3.5, 3.6
* Django 1.10, 1.11, 2.0
* Pyramid 1.7, 1.8, 1.9
* Flask 0.10, 0.11, 0.12
* Tornado 4.5, 4.6, 4.7

License
========

MIT License

Authors
=======

* tell-k <ffk2005 at gmail.com>

History
=======

0.1.2(Feb 19, 2018)
---------------------

* First release


.. |travis| image:: https://travis-ci.org/tell-k/uadetector.svg?branch=master
    :target: https://travis-ci.org/tell-k/uadetector

.. |coveralls| image:: https://coveralls.io/repos/tell-k/uadetector/badge.png
    :target: https://coveralls.io/r/tell-k/uadetector
    :alt: coveralls.io

.. |version| image:: https://img.shields.io/pypi/v/uadetector.svg
    :target: http://pypi.python.org/pypi/uadetector/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/uadetector.svg
    :target: http://pypi.python.org/pypi/uadetector/
    :alt: license
