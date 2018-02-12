"""
    uadetector.django.middleware
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Django middleware class for uadatector.

    :author: tell-k <ffk2005 at gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""

import logging

from ..useragent import get_useragent

from .conf import settings

logger = logging.getLogger(__name__)


class UADetectorMiddleware:
    """ Middleware for Django """

    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        self.process_request(request)
        return self.get_response(request)

    def process_request(self, request):
        prop_name = settings.REQUEST_PROPERTY_NAME
        if hasattr(request, prop_name):
            logger.warn(
                'Since "request.%s" is already exists,'
                ' this assign process is skipped.',
                prop_name
            )
            return

        setattr(
            request,
            prop_name,
            get_useragent(
                request.META.get('HTTP_USER_AGENT', ''),
                settings.USERAGENT_CLASS,
            )
        )
