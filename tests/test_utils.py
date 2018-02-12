
class TestImportClass:

    def _call_fut(self, klass, default):
        from uadetector.utils import import_class
        return import_class(klass, default)

    def test_import(self):
        cls = self._call_fut('tests.dummy.Dummy', 'tests.dummy.Dummy2')
        assert cls.__name__ == 'Dummy'

    def test_fallback_import(self):
        cls = self._call_fut(None, 'tests.dummy.Dummy2')
        assert cls.__name__ == 'Dummy2'

    def test_is_aready_class(self):
        from tests.dummy import Dummy
        cls = self._call_fut(Dummy, 'tests.dummy.Dummy2')
        assert cls.__name__ == 'Dummy'
