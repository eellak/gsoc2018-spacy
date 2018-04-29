# coding: utf8
from __future__ import unicode_literals
import unicodedata

# import the symbols for the attrs you want to overwrite
from ...attrs import LIKE_NUM



# probably, without accents and with or without capitalization
_num_words = ['ένα','δύο','δυο','τρία','τέσσερα','πέντε','έξι','επτά','οκτώ','εννέα','εκατομμύριο','δισεκατομμύριο','τρισεκατομμύριο','δις','χιλιάδες','χιλιάδα']


def like_num(text):
    text = text.replace(',', '').replace('.', '')
    if text.isdigit():
        return True
    if text.count('/') == 1:
        num, denom = text.split('/')
        if num.isdigit() and denom.isdigit():
            return True
    if (text.count('^')==1):
        num,denom=text.split('^')
        if (num.isdigit() and denom.isdigit()):
          return True
    if text in _num_words:
        return True
    return False

def has_accents(text):
  False if ( text==unicodedata.normalize('NFD',text) ) else True


# The default lex_attr_getters are updated with this one, 
# so only the functions defined here are overwritten.

LEX_ATTRS = {
    LIKE_NUM: like_num
}