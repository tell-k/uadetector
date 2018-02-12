"""
    uadetector.utils
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :author: tell-k <ffk2005 at gmail.com>
    :copyright: tell-k. All Rights Reserved.
"""

import pydoc
import inspect


def import_class(klass, default):
    """ import class utility function """

    target = klass or default
    if inspect.isclass(target):
        return target
    else:
        return pydoc.locate(target)
