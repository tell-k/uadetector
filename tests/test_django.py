from .constants import UA_STRING
from .testapp import django  # NOQA


class TestDjangoMiddleware:

    def test_set_useragent_object(self, client):
        res = client.get('/view1', **{'HTTP_USER_AGENT': UA_STRING})
        assert res.status_code == 200
        assert res.content == b'iPhone'  # request.ua.os

    def test_change_useragent_class(self, client, settings):
        settings.UADETECTOR_USERAGENT_CLASS = 'tests.CustomUserAgent'
        res = client.get('/view2')
        assert res.content == b'CustomUserAgent'

    def test_change_request_property_name(self, client, settings):
        settings.UADETECTOR_REQUEST_PROPERTY_NAME = 'ua_obj'
        res = client.get('/view3', **{'HTTP_USER_AGENT': UA_STRING})
        assert res.content == b'iPhone'  # request.ua_obj.os
