import unicodedata
def strip_accents(s):
   s=s.lower()
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')
