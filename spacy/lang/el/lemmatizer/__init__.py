# coding: utf8
from __future__ import unicode_literals

from .lookup import LOOKUP
from ._adjectives import ADJECTIVES
from ._adverbs import ADVERBS
from ._nouns import NOUNS
from ._verbs import VERBS
from ._lemma_rules import ADJECTIVE_RULES, NOUN_RULES, VERB_RULES, PUNCT_RULES


LEMMA_INDEX = {'adj': ADJECTIVES, 'adv': ADVERBS, 'noun': NOUNS, 'verb': VERBS}


LEMMA_RULES = {'adj': ADJECTIVE_RULES, 'noun': NOUN_RULES, 'verb': VERB_RULES,
               'punct': PUNCT_RULES}
