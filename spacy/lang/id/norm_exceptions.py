# coding: utf8
from __future__ import unicode_literals

<<<<<<< HEAD
_exc = {
    "Rp": "$",
    "IDR": "$",
    "RMB": "$",
    "USD": "$",
    "AUD": "$",
    "GBP": "$",
}
=======
_exc = {}
>>>>>>> 14d9007efd2ca457c6e6549d5599e460e198904c

NORM_EXCEPTIONS = {}

for string, norm in _exc.items():
    NORM_EXCEPTIONS[string] = norm
    NORM_EXCEPTIONS[string.title()] = norm
