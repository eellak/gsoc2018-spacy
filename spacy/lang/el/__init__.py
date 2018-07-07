from __future__ import unicode_literals
from .stop_words import STOP_WORDS
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .lex_attrs import LEX_ATTRS
from .tag_map import TAG_MAP
from .lemmatizer import LEMMA_RULES, LEMMA_INDEX, LOOKUP, LEMMA_EXC
from .morph_rules import MORPH_RULES
from .syntax_iterators import SYNTAX_ITERATORS
from .norm_exceptions import NORM_EXCEPTIONS
from .tokenizer import GreekTokenizer
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
    # lemma_lookup= LOOKUP
    lemma_rules = LEMMA_RULES
    lemma_index = LEMMA_INDEX
    lemma_exc = LEMMA_EXC
    morph_rules = MORPH_RULES
    syntax_iterators = SYNTAX_ITERATORS

    @classmethod
    def create_tokenizer(cls, nlp=None):
        rules = cls.tokenizer_exceptions
        token_match = cls.token_match
        prefix_search = (util.compile_prefix_regex(cls.prefixes).search
                         if cls.prefixes else None)
        suffix_search = (util.compile_suffix_regex(cls.suffixes).search
                         if cls.suffixes else None)
        infix_finditer = (util.compile_infix_regex(cls.infixes).finditer
                          if cls.infixes else None)
        vocab = nlp.vocab if nlp is not None else cls.create_vocab(nlp)
        return GreekTokenizer(vocab, rules=rules,
                         prefix_search=prefix_search,
                         suffix_search=suffix_search,
                         infix_finditer=infix_finditer,
                         token_match=token_match)

class Greek(Language):
    lang = 'el'
    Defaults = GreekDefaults

__all__ = ['Greek']
