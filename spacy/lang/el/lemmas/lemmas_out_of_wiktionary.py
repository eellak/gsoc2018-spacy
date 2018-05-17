import re
import pickle

from gensim.corpora.wikicorpus import extract_pages

regex = re.compile(r'==={{(\w+)\|el}}===')
regex2 = re.compile(r'==={{(\w+ \w+)\|el}}===')

# get words based on the Wiktionary dump
# check only for specific parts

# ==={{κύριο όνομα|el}}===
expected_parts = ['μετοχή', 'ρήμα', 'επίθετο',
                  'επίρρημα',  'ουσιαστικό', 'κύριο όνομα']


def load_pickle(file_path):
    # load file
    with open(file_path, 'rb') as f:
        return pickle.load(f)


def save_obj(obj):
    # save dictionary
    with open('elwiktionary.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


wiktionary_file_path = '/root/elwiktionary-latest-pages-articles.xml'


def get_words(wiktionary_file_path):
    words = {}

    for title, text, pageid in extract_pages(wiktionary_file_path):
        if text.startswith('#REDIRECT'):
            continue
        title = title.lower()
        all_regex = regex.findall(text)
        all_regex.extend(regex2.findall(text))
        for a in all_regex:
            if a in expected_parts:
                words[title] = {}
                words[title]['part_of_speech'] = a
    return words

# generate dictionary with words
# words = get_words(wiktionary_file_path)

# save dictionary
# words_in_model = save_obj(words)

# load dictionary
# words_in_model = load_pickle('elwiktionary.pkl')

# save sorted words
# with open('elwords.txt', 'w') as f:
#    for line in sorted(words_in_model):
#        f.write(line+'\n')
