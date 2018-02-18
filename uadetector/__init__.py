"""
    uadetector
    ~~~~~~~~~~~

    WSGI Middleware and web framework extensions for handling User-Agent

    :author: tell-k <ffk2005 at gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""

from .wsgi import UADetector  # NOQA
from .useragent import UserAgent, get_useragent  # NOQA
from .constants import ENVIRON_KEY  # NOQA

__version__ = '0.1.2'
