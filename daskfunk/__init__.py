from __future__ import absolute_import, division, print_function

from .core import compile

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
