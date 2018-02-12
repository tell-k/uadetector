"""
    uadetector.wsgi
    ~~~~~~~~~~~~~~~~

    WSGI Middleware for uadetector.

    :author: tell-k <ffk2005 at gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
import logging

from .constants import ENVIRON_KEY
from .useragent import get_useragent


logger = logging.getLogger(__name__)


class UADetector:
    """ WSGI middleware. Set UserAgent object to WSGI environ dict.
    """

    def __init__(self, app, environ_key=ENVIRON_KEY,
                 useragent_class=None):

        self.environ_key = environ_key
        self.ua_class = useragent_class
        self.app = app

    def __call__(self, environ, start_response):
        if 'HTTP_USER_AGENT' not in environ:
            logger.warn(
                'environ["HTTP_USER_AGENT"] is not exists,'
                ' this assign process is skipped.',
            )
            return self.app(environ, start_response)

        if self.environ_key in environ:
            logger.warn(
                'Since "environ[%s]" is already exists,'
                ' this assign process is skipped.',
                self.environ_key
            )
            return self.app(environ, start_response)

        environ[self.environ_key] = get_useragent(
            environ['HTTP_USER_AGENT'],
            self.ua_class
        )
        return self.app(environ, start_response)
