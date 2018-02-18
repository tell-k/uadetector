import sys
import os
import re

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ''

    def run_tests(self):
        import shlex
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(shlex.split(self.pytest_args))
        sys.exit(errno)


here = os.path.dirname(__file__)


with open(os.path.join(here, 'uadetector', '__init__.py'), 'r') as f:
    version = re.compile(
        r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)


readme = open(os.path.join(here, 'README.rst')).read()

requires = [
    'woothee',
]

tests_require = [
    'Django',
    'Flask',
    'Pyramid',
    'tornado',
    'pytest-django',
    'pytest-cov',
    'pytest',
    'webtest',
]

classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Software Development :: Libraries',
]

setup(
    name='uadetector',
    version=version,
    description='WSGI Middleware and web framework extensions for handling User-Agent.',  # NOQA
    long_description=readme,
    url='https://github.com/tell-k/uadetector',
    author='tell-k',
    author_email='ffk2005@gmail.com',
    classifiers=classifiers,
    keywords=['user_agent', 'web', 'browser', 'detector', 'handling'],
    install_requires=requires,
    tests_require=tests_require,
    cmdclass={'test': PyTest},
    packages=find_packages(exclude=['tests*']),
    license='MIT',
)
