import json

import spacy
from prodigy.components.db import connect
from prodigy.util import split_evals
from spacy.gold import GoldCorpus, minibatch, biluo_tags_from_offsets, tags_to_entities


def prodigy_to_spacy(nlp, dataset):
    """Create spaCy JSON training data from a Prodigy dataset.

    See https://spacy.io/api/annotation#json-input.
    """
    db = connect()
    examples = db.get_dataset(dataset)

    offsets = []
    for eg in examples:
        if eg['answer'] == 'accept':
            entities = [(span['start'], span['end'], span['label'])
                        for span in eg['spans']]
            offsets.append((eg['text'], {'entities': entities}))

    docs = docs_from_offsets(nlp, offsets)
    trees = docs_to_trees(docs)
    return trees


def docs_from_offsets(nlp, gold):
    """Create a sequence of Docs from a sequence of text, entity-offsets pairs."""
    docs = []
    for text, entities in gold:
        doc = nlp(text)
        entities = entities['entities']
        tags = biluo_tags_from_offsets(doc, entities)
        if entities:
            for start, end, label in entities:
                span = doc.char_span(start, end, label=label)
                if span:
                    doc.ents = list(doc.ents) + [span]
        if doc.ents:  # remove to return documents without entities too
            docs.append((doc, tags))
    return docs


def docs_to_trees(docs):
    """Create spaCy JSON training data from a sequence of Docs."""
    doc_trees = []
    for d, doc_tuple in enumerate(docs):
        doc, tags = doc_tuple
        try:
            tags_to_entities(tags)
        except AssertionError:
            print('Dropping {}'.format(d))
            continue
        if not tags:
            print('Dropping {}'.format(d))
            continue
        sentences = []
        for s in doc.sents:
            s_tokens = []
            for t in s:
                token_data = {
                    'id': t.i,
                    'orth': t.orth_,
                    'tag': t.tag_,
                    'head': t.head.i - t.i,
                    'dep': t.dep_,
                    'ner': tags[t.i],
                }
                s_tokens.append(token_data)
            sentences.append({'tokens': s_tokens})
        doc_trees.append({
            'id': d,
            'paragraphs': [
                {
                    'raw': doc.text,
                    'sentences': sentences,
                }
            ]
        })
    return doc_trees

nlp = spacy.load('el_core_web_sm')
doc_trees = prodigy_to_spacy(nlp, 'ner_train')

train, dev, _ = split_evals(doc_trees, .2)
with open('train.json', 'wt') as f:
    json.dump(train, f)
with open('dev.json', 'wt') as f:
    json.dump(dev, f)
