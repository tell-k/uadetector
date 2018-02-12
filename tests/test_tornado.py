from tornado.testing import AsyncHTTPTestCase

from .constants import UA_STRING
from .testapp.tornado import make_app


class TestView1Handler(AsyncHTTPTestCase):

    def get_app(self):
        return make_app()

    def test_exists_useragent_object(self):
        res = self.fetch('/view1', method='GET',
                         headers={'User-Agent': UA_STRING})
        assert res.code == 200
        assert res.body == b'iPhone'  # request.ua.os


class TestView2Handler(AsyncHTTPTestCase):

    def get_app(self):
        return make_app(ua_class='tests.CustomUserAgent')

    def test_change_useragent_class(self):
        res = self.fetch('/view2', method='GET')
        assert res.body == b'CustomUserAgent'


class TestView3Handler(AsyncHTTPTestCase):

    def get_app(self):
        return make_app(prop_name='ua_obj')

    def test_change_request_property_name(self):
        res = self.fetch('/view3', method='GET',
                         headers={'User-Agent': UA_STRING})
        assert res.body == b'iPhone'  # request.ua_obj.os
