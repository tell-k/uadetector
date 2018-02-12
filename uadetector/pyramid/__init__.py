"""
    uadetector.pyramid
    ~~~~~~~~~~~~~~~~~~~~~

    Generate request property function for pyramid.

    :author: tell-k <ffk2005 at gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""

from ..useragent import get_useragent


def ua_prop(useragent_class=None):
    """ Generate property function for config.add_request_method """

    def _ua_prop(request):
        return get_useragent(request.user_agent or '', useragent_class)
    return _ua_prop
