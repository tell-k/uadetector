import logging

from werkzeug.utils import cached_property

from ..constants import REQUEST_PROPERTY_NAME
from ..useragent import get_useragent

logger = logging.getLogger(__name__)


class UADetector:
    """ Extension for Flask """

    def __init__(self, app=None):
        ua_class = app.config.get('UADETECTOR_USERAGENT_CLASS')
        prop_name = app.config.get('UADETECTOR_REQUEST_PROPERTY_NAME', REQUEST_PROPERTY_NAME)

        if hasattr(app.request_class, prop_name):
            logger.warn(
                'Since "app.request.%s" is already exists,'
                'this assign process is skipped.',
                prop_name
            )
            return

        @cached_property
        def ua_prop(self):
            return get_useragent(self.headers.get('USER-AGENT', ''), ua_class)

        setattr(app.request_class, prop_name, ua_prop)
