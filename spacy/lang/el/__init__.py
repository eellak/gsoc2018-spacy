from __future__ import unicode_literals
from .stop_words import STOP_WORDS
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .lex_attrs import LEX_ATTRS
from .tag_map import TAG_MAP
from .lemmatizer import LEMMA_RULES, LEMMA_INDEX, LOOKUP, LEMMA_EXC
from .morph_rules import MORPH_RULES
from .syntax_iterators import SYNTAX_ITERATORS
from .norm_exceptions import NORM_EXCEPTIONS
# Default imports
from ..tokenizer_exceptions import BASE_EXCEPTIONS
from ..norm_exceptions import BASE_NORMS
from ...language import Language
from ...attrs import LANG, NORM
from ...util import update_exc, add_lookups

class GreekDefaults(Language.Defaults):
    lex_attr_getters = dict(Language.Defaults.lex_attr_getters)
    lex_attr_getters.update(LEX_ATTRS)
    lex_attr_getters[LANG] = lambda text: 'el'
    lex_attr_getters[NORM] = add_lookups(Language.Defaults.lex_attr_getters[NORM],
                                         BASE_NORMS, NORM_EXCEPTIONS)
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)
    tag_map= TAG_MAP
    stop_words = STOP_WORDS
    lemma_lookup= LOOKUP
    lemma_rules = LEMMA_RULES
    lemma_index = LEMMA_INDEX
    lemma_exc = LEMMA_EXC
    morph_rules = MORPH_RULES
    syntax_iterators = SYNTAX_ITERATORS

class Greek(Language):
    lang = 'el'
    Defaults = GreekDefaults

__all__ = ['Greek']
