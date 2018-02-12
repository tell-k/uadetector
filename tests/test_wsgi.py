

class DummyWSGIApp:

    def __call__(self, environ, start_response):
        return environ, start_response


class TestUADetector:

    def _get_target_class(self):
        from uadetector.wsgi import UADetector
        return UADetector

    def _make_one(self, app, environ_key=None, useragent_class=None):
        from uadetector.constants import ENVIRON_KEY
        if environ_key is None:
            environ_key = ENVIRON_KEY
        return self._get_target_class()(app, environ_key, useragent_class)

    def test_set_useragent_object(self):
        from uadetector.constants import ENVIRON_KEY

        app = self._make_one(DummyWSGIApp())
        environ, _ = app({'HTTP_USER_AGENT': 'dummy'}, 'dummy')

        assert ENVIRON_KEY in environ

    def test_change_environ_key(self):
        environ_key = 'uadetector:newuseragent'
        app = self._make_one(DummyWSGIApp(), environ_key=environ_key)
        environ, _ = app({'HTTP_USER_AGENT': 'dummy'}, 'dummy')

        assert environ_key in environ

    def test_change_useragent_class(self):
        from uadetector.constants import ENVIRON_KEY
        from uadetector.useragent import UserAgent

        class CustomUserAgent(UserAgent):
            pass

        app = self._make_one(DummyWSGIApp(), useragent_class=CustomUserAgent)
        environ, _ = app({'HTTP_USER_AGENT': 'dummy'}, 'dummy')

        assert environ[ENVIRON_KEY].__class__.__name__ == 'CustomUserAgent'

    def test_missing_http_user_agent(self):
        from uadetector.constants import ENVIRON_KEY

        app = self._make_one(DummyWSGIApp())
        environ, _ = app({}, 'dummy')

        assert ENVIRON_KEY not in environ

    def test_aleady_exists_environ_key(self):
        from uadetector.constants import ENVIRON_KEY

        app = self._make_one(DummyWSGIApp())
        environ, _ = app({
            'HTTP_USER_AGENT': 'dummy',
            ENVIRON_KEY: 'already_exists'
        }, 'dummy')

        assert environ[ENVIRON_KEY] == 'already_exists'
