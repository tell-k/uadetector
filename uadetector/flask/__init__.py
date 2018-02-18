"""
    uadetector.flask
    ~~~~~~~~~~~~~~~~~~

    Flask extension for uadatector.

    :author: tell-k <ffk2005 at gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""

import logging

from flask import request

from ..constants import REQUEST_PROPERTY_NAME
from ..useragent import get_useragent

logger = logging.getLogger(__name__)


class UADetector:
    """ Extension for Flask """

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        ua_class = app.config.get('UADETECTOR_USERAGENT_CLASS')
        prop_name = app.config.get('UADETECTOR_REQUEST_PROPERTY_NAME',
                                   REQUEST_PROPERTY_NAME)

        @app.before_request
        def _attach_ua_prop():
            if hasattr(request, prop_name):
                logger.warn(
                    'Since "app.request.%s" is already exists,'
                    'this assign process is skipped.',
                    prop_name
                )
                return

            setattr(
                request,
                prop_name,
                get_useragent(request.headers.get('USER-AGENT', ''), ua_class)
            )
