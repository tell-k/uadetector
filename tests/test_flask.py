from .testapp.flask import make_app
from .constants import UA_STRING


class TestFlaskExtension:

    def test_set_useragent_object(self, client):
        app = make_app().test_client()

        res = app.get('/view', environ_base={'HTTP_USER_AGENT': UA_STRING})
        assert res.status_code == 200
        assert res.data == b'iPhone'  # request.ua.os

    def test_change_useragent_class(self):
        app = make_app(ua_class='tests.CustomUserAgent').test_client()

        res = app.get('/view2')
        assert res.data == b'CustomUserAgent'

    def test_change_request_property_name(self):
        app = make_app(prop_name='ua_obj').test_client()

        res = app.get('/view3', environ_base={'HTTP_USER_AGENT': UA_STRING})
        assert res.data == b'iPhone'  # request.ua_obj.os
