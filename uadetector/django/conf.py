"""
    uadetector.django.conf
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005 at gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""

from django.conf import settings as django_settings

from .. import constants


class Settings:

    def __init__(self, app_prefix):
        self.app_prefix = app_prefix

    def __getattr__(self, name):
        name = name.upper()
        if not hasattr(constants, name):  # pragma: no cover
            return self.__getattribute__(name)

        default_value = getattr(constants, name)
        setting_name = '{}_{}'.format(self.app_prefix, name)
        return getattr(django_settings, setting_name, default_value)


settings = Settings('UADETECTOR')
