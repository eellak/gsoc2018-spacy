# coding: utf8
from __future__ import unicode_literals

# import symbols – if you need to use more, add them here
from ...symbols import ORTH, LEMMA, TAG, NORM, ADP, DET


# Add tokenizer exceptions
# If an exception is split into more than one token, the ORTH values combined always
# need to match the original string.

# Exceptions should be added in the following format:

_exc = {
    "don't": [
        {ORTH: "do", LEMMA: "do"},
        {ORTH: "n't", LEMMA: "not", TAG: "RB"}]
}




TOKENIZER_EXCEPTIONS = _exc