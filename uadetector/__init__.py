"""
    uadetector
    ~~~~~~~~~~~

    :author: tell-k <ffk2005 at gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""

from .wsgi import UADetector
from .useragent import UserAgent, get_useragent
from .constants import ENVIRON_KEY

__version__ = '0.1.0'
