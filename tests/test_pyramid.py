import webtest

from .constants import UA_STRING
from .testapp.pyramid import make_app


class TestPyramedAddRequestMethod:

    def test_set_useragent_object(self):
        app = webtest.TestApp(make_app())

        res = app.get('/view1', headers={'User-Agent': UA_STRING})
        assert res.status_code == 200
        assert res.body == b'iPhone'  # request.ua.os

    def test_change_useragent_class(self):
        app = webtest.TestApp(make_app(ua_class='tests.CustomUserAgent'))

        res = app.get('/view2')
        assert res.body == b'CustomUserAgent'

    def test_change_request_property_name(self):
        app = webtest.TestApp(make_app(prop_name='ua_obj'))

        res = app.get('/view3', headers={'User-Agent': UA_STRING})
        assert res.body == b'iPhone'  # request.ua_obj.os
