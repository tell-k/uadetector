
from ..useragent import get_useragent


def ua_prop(ua_class=None):
    """ Generate property function for config.add_request_method """

    def _ua_prop(request):
        return get_useragent(request.user_agent or '', ua_class)
    return _ua_prop
