# coding: utf8
from __future__ import unicode_literals

from ...symbols import ORTH


_exc = {}


# Source: https://en.wiktionary.org/wiki/Category:Romanian_abbreviations
for orth in [
<<<<<<< HEAD
    "1-a", "1-ul", "10-a", "10-lea", "2-a", "3-a", "3-lea", "6-lea",
    "d-voastră", "dvs.", "Rom.", "str."]:
=======
    "1-a", "2-a", "3-a", "4-a", "5-a", "6-a", "7-a", "8-a", "9-a", "10-a", "11-a", "12-a",
    "1-ul", "2-lea", "3-lea", "4-lea", "5-lea", "6-lea", "7-lea", "8-lea", "9-lea", "10-lea", "11-lea", "12-lea",
    "d-voastră", "dvs.", "ing.", "dr.", "Rom.", "str.", "nr.", "etc.", "d.p.d.v.", "dpdv", "șamd.", "ș.a.m.d."]:
>>>>>>> 14d9007efd2ca457c6e6549d5599e460e198904c
    _exc[orth] = [{ORTH: orth}]


TOKENIZER_EXCEPTIONS = _exc
