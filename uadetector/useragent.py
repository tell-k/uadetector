"""
    uadetector.useragent
    ~~~~~~~~~~~~~~~~~~~~~

    UserAgent class based on woothee.

    :author: tell-k <ffk2005 at gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""
import re

import woothee
from woothee.dataset import VALUE_UNKNOWN

from .constants import USERAGENT_CLASS
from .utils import import_class


UNKNOWN_VARIANT = 'unknown'


def get_useragent(useragent_string, useragent_class=None):
    _class = import_class(useragent_class, USERAGENT_CLASS)
    return _class(useragent_string)


def _suppress_unknown(version):
    if version.lower() == VALUE_UNKNOWN.lower():
        return None
    else:
        return version


class UserAgent:
    """ UserAgent handling, detection based on woothee """

    attr_map = {
        'device_type': 'category',
        'os': 'os',
        'os_version': 'os_version',
        'browser': 'name',
        'browser_version': 'version',
        'browser_vendor': 'vendor',
    }

    def __init__(self, useragent_string):
        self.user_agent = useragent_string
        self._woothee_result = woothee.parse(useragent_string)

    def __getattr__(self, name):
        if name in self.attr_map:
            return self._woothee_result.get(self.attr_map.get(name))
        return self.__getattribute__(name)

    @property
    def device_variant(self):
        if self.device_type.lower() == VALUE_UNKNOWN.lower():
            return UNKNOWN_VARIANT
        return self.device_type

    # helpers --

    @property
    def from_pc(self):
        return self.device_type == 'pc'

    @property
    def from_smartphone(self):
        return self.device_type == 'smartphone'

    @property
    def from_mobilephone(self):
        return self.device_type == 'mobilephone'

    @property
    def from_appliance(self):
        return self.device_type == 'appliance'

    @property
    def from_crawler(self):
        return self.device_type == 'crawler'

    # detectors --

    @property
    def from_iphone(self):
        return self.os.lower() == 'iphone'

    @property
    def from_ipad(self):
        return self.os.lower() == 'ipad'

    @property
    def from_ipod(self):
        return self.os.lower() == 'ipod'

    @property
    def from_ios(self):
        return (
            self.from_iphone
            or self.from_ipad
            or self.from_ipod
            or self.os.lower() == 'ios'
        )

    @property
    def from_android(self):
        return self.os.lower() == 'android' and self._from_andorid_mobile

    @property
    def from_android_tablet(self):
        return self.os.lower() == 'android' and not self._from_andorid_mobile

    @property
    def _from_andorid_mobile(self):
        m = re.search(r'Android.+Mobi(le)?', self.user_agent)
        return True if m else False

    @property
    def from_android_os(self):
        return self.from_android or self.from_android_tablet

    @property
    def from_windows_phone(self):
        return self.os.lower() == 'windows phone os'

    @property
    def smartphone_version(self):
        if not self.from_smartphone:
            return None
        return _suppress_unknown(self.os_version)
