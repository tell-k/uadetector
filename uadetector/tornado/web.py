"""
    uadetector.tornado.web
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Request handler for uadatector.

    :author: tell-k <ffk2005 at gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""

import logging

from tornado.web import RequestHandler as BaseRequestHandler
from tornado.options import options

from ..constants import REQUEST_PROPERTY_NAME
from ..useragent import get_useragent


logger = logging.getLogger(__name__)


class RequestHandler(BaseRequestHandler):
    """ RequestHandler for Tornado """

    def initialize(self):
        super().initialize()

        options_dict = options.as_dict()
        ua_class = options_dict.get('uadetector_useragent_class')
        prop_name = options_dict.get('uadetector_request_property_name',
                                     REQUEST_PROPERTY_NAME)

        if hasattr(self.request, prop_name):
            logger.warn(
                'Since "self.request.%s" is already exists,'
                ' this assign process is skipped.',
                prop_name
            )
            return

        setattr(
            self.request,
            prop_name,
            get_useragent(
                self.request.headers.get('User-Agent', ''),
                ua_class
            )
        )
