# coding: utf8
from __future__ import unicode_literals

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .stop_words import STOP_WORDS
<<<<<<< HEAD
=======
from .lemmatizer import LOOKUP
>>>>>>> 14d9007efd2ca457c6e6549d5599e460e198904c

from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ..norm_exceptions import BASE_NORMS
from ...language import Language
from ...attrs import LANG, NORM
from ...util import update_exc, add_lookups


class RomanianDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters[LANG] = lambda text: 'ro'
    lex_attr_getters[NORM] = add_lookups(Language.Defaults.lex_attr_getters[NORM], BASE_NORMS)
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    stop_words = STOP_WORDS
<<<<<<< HEAD
=======
    lemma_lookup = LOOKUP
>>>>>>> 14d9007efd2ca457c6e6549d5599e460e198904c


class Romanian(Language):
    lang = 'ro'
    Defaults = RomanianDefaults


__all__ = ['Romanian']

