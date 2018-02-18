from unittest import mock

import pytest


class TestUseragent:

    def _get_target_class(self):
        from uadetector.useragent import UserAgent
        return UserAgent

    def _make_one(self, useragent_string):
        return self._get_target_class()(useragent_string)

    def _patch_woothe(self, **kwargs):
        dummy_parsed = {
            'category': 'pc',
            'name': 'Firefox',
            'version': '9.0.1',
            'os': 'Windows 7',
            'vender': 'Microsoft',
            'os_version': 'NT 6.1',
        }
        dummy_parsed.update(kwargs)
        return mock.patch(
            'uadetector.useragent.woothee.parse',
            return_value=dummy_parsed,
        )

    @pytest.mark.parametrize('attr,params,expected', [
        ('device_type', {'category': 'pc'}, 'pc'),
        ('os', {'os': 'Windows'}, 'Windows'),
        ('os_version', {'os_version': 'NT 6.1'}, 'NT 6.1'),
        ('browser', {'name': 'Google Chrome'}, 'Google Chrome'),
        ('browser_version', {'version': '9.01'}, '9.01'),
        ('browser_vendor', {'vendor': 'Microsoft'}, 'Microsoft'),
    ])
    def test_attrs(self, attr, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert getattr(ua, attr) == expected

    def test_attribute_error(self):
        with self._patch_woothe():
            ua = self._make_one('dummy_ua')
            with pytest.raises(AttributeError):
                ua.unkown_attr

    @pytest.mark.parametrize('params,expected', [
        ({'category': 'pc'}, 'pc'),
        ({'category': 'unknown'}, 'unknown'),
    ])
    def test_device_variant(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.device_variant is expected

    @pytest.mark.parametrize('params,expected', [
        ({'category': 'pc'}, True),
        ({'category': 'smartphone'}, False),
    ])
    def test_from_pc(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.from_pc is expected

    @pytest.mark.parametrize('params,expected', [
        ({'category': 'smartphone'}, True),
        ({'category': 'pc'}, False),
    ])
    def test_from_smartphone(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.from_smartphone is expected

    @pytest.mark.parametrize('params,expected', [
        ({'category': 'mobilephone'}, True),
        ({'category': 'pc'}, False),
    ])
    def test_from_mobilephone(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.from_mobilephone is expected

    @pytest.mark.parametrize('params,expected', [
        ({'category': 'appliance'}, True),
        ({'category': 'pc'}, False),
    ])
    def test_from_appliance(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.from_appliance is expected

    @pytest.mark.parametrize('params,expected', [
        ({'category': 'crawler'}, True),
        ({'category': 'pc'}, False),
    ])
    def test_from_crawler(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.from_crawler is expected

    @pytest.mark.parametrize('params,expected', [
        ({'os': 'iPhone'}, True),
        ({'os': 'iPad'}, False),
    ])
    def test_from_iphone(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.from_iphone is expected

    @pytest.mark.parametrize('params,expected', [
        ({'os': 'iPad'}, True),
        ({'os': 'iPhone'}, False),
    ])
    def test_from_ipad(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.from_ipad is expected

    @pytest.mark.parametrize('params,expected', [
        ({'os': 'iPod'}, True),
        ({'os': 'iPhone'}, False),
    ])
    def test_from_ipod(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.from_ipod is expected

    @pytest.mark.parametrize('params,expected', [
        ({'os': 'iPod'}, True),
        ({'os': 'iPhone'}, True),
        ({'os': 'iPad'}, True),
        ({'os': 'iOS'}, True),
        ({'os': 'Android'}, False),
    ])
    def test_from_ios(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.from_ios is expected

    @pytest.mark.parametrize('params,uastring,expected', [
        ({'os': 'Android'}, 'Android Mobile', True),
        ({'os': 'Android'}, 'Android Tablet', False),
    ])
    def test_from_android(self, params, uastring, expected):
        with self._patch_woothe(**params):
            ua = self._make_one(uastring)
            assert ua.from_android is expected

    @pytest.mark.parametrize('params,uastring,expected', [
        ({'os': 'Android'}, 'Android Tablet', True),
        ({'os': 'Android'}, 'Android Mobile', False),
    ])
    def test_from_android_tablet(self, params, uastring, expected):
        with self._patch_woothe(**params):
            ua = self._make_one(uastring)
            assert ua.from_android_tablet is expected

    @pytest.mark.parametrize('params,uastring,expected', [
        ({'os': 'Android'}, 'Android Tablet', True),
        ({'os': 'Android'}, 'Android Mobile', True),
        ({'os': 'iOS'}, 'Android Mobile', False),
    ])
    def test_from_android_os(self, params, uastring, expected):
        with self._patch_woothe(**params):
            ua = self._make_one(uastring)
            assert ua.from_android_os is expected

    @pytest.mark.parametrize('params,expected', [
        ({'os': 'Windows Phone OS'}, True),
        ({'os': 'iPhone'}, False),
    ])
    def test_from_windows_phone(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.from_windows_phone is expected

    @pytest.mark.parametrize('params,expected', [
        ({'os_version': '', 'category': 'pc'}, None),
        ({'os_version': 'NT 6.1', 'category': 'smartphone'}, 'NT 6.1'),
        ({'os_version': 'UNKNOWN', 'category': 'smartphone'}, None),
    ])
    def test_smartphone_version(self, params, expected):
        with self._patch_woothe(**params):
            ua = self._make_one('dummy_ua')
            assert ua.smartphone_version == expected


class TestGetUseragent:

    def _call_fut(self, useragent_string, useragent_class=None):
        from uadetector.useragent import get_useragent
        return get_useragent(useragent_string, useragent_class)

    def test_get_useragen_object(self):
        obj = self._call_fut('dummy_ua')
        assert obj.__class__.__name__ == 'UserAgent'

    def test_replace_useragent_class(self):
        from uadetector.useragent import UserAgent

        class CustomUserAgent(UserAgent):
            pass

        obj = self._call_fut('dummy_ua', CustomUserAgent)
        assert obj.__class__.__name__ == 'CustomUserAgent'
