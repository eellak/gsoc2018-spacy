import spacy
from nltk import Tree
nlp = spacy.load('el')
doc = nlp("η δημοκρατία είναι το πιο ανθρώπινο πολίτευμα.")


for token in doc:
    print('Token:{}, DEP tag: {}'.format(token,token.dep_))
def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
      return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
      return node.orth_
[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
