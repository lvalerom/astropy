# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Support for ``typing`` py3.9+ features while min version is py3.8.
"""

try:  # py 3.9+
    from typing import Annotated
except (ImportError, ModuleNotFoundError):  # optional dependency
    try:
        from typing_extensions import Annotated
    except (ImportError, ModuleNotFoundError):

        Annotated = NotImplemented

HAS_ANNOTATED = Annotated is not NotImplemented
