import unicodedata
from collections import defaultdict

def strip_accents(s):
   s=s.lower()
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

words={}
with open('dictionaries/greek_dict.in') as fileinst:
        for line in fileinst:
                tmp_str=line.rstrip()
                words[strip_accents(tmp_str)]=tmp_str

def get_accent(word):
        try:
          if (words[word]==word):
            return word
          else:
            return words[word]
        except:
          return word
