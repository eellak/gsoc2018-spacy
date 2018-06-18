import unicodedata

def strip_accents(s):
   s=s.lower()
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

ls=defaultdict(lambda: '')
with open('greek_dict.in') as fileinst:
        for line in fileinst:
                tmp_str=line.rstrip()
                ls[strip_accents(tmp_str)]=tmp_str

def get_accent(word):
        try:
                return ls[word]
        except:
                return[word]
