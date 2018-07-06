# gsoc2018-spacy
## About the project

This projects aims to achieve the following goals: 
1. Integration of Greek language to spaCy.io platform
2. Natural Language Processing of Greek documents in order to extract valuable information such as named entities, sentiment analysis, tags, etc.

The project got selected for Google Summer of Code 2018 under the auspices of GFOSS organization.

## Problem Statement

We live in the era of data. **Every minute**, 3.8 billion internet users, produce content; more than 120 million emails , 500.000 Facebook comments, 3 million Google searches. If we want to process that amount of data efficiently, we need to process natural language. Open source projects such as spaCy, textblob, or NLTK contribute signifficantly to that direction and thus they need to be reinforced.

This project is about improving the quality of Natural Language Processing of Greek Language. The first step is to integrate Greek Language to spaCy. During that process, innovative approaches will be used. It is of vital importance for the writer and for the mentors of the program to identify which of them are of practical use for spaCy and to share the results in order to support any other open source enthusiast who is interested. In the fortunate scenario of successful integration of Greek Language to spaCy, the greek model will be trained and used for extraction of valuable information such as emotions detection in Greek texts, entity extraction, etc.

## Licensing
The project is forked from spaCy.io so it uses MIT License.



## People

* Google Summer of Code participant: [Ioannis Daras](https://github.com/giannisdaras)
* Mentor: [Markos Gogoulos](https://github.com/mgogoulos)
* Mentor: [Panos Louridas](https://github.com/louridas)

## Setting up the dev environment - a quick reference

**DISCLAIMER**: This is a very short description of steps that you need to reproduce the dev environment. For more detailed information, have a look at ./spacy/lang/el/contribute/

### Initializing model
`cd ./spacy/lang/el/training`
`python3 -m spacy init-model el el_vocab ../stop-words/global-freqs/out.txt --vectors-loc ../res/cc.el.300.vec`

### Training POS/DEP
1. `cd pos_tagger/`

2. Without vectors:
`python3 -m spacy train el small/ el_gdt-ud-train.json el_gdt-ud-dev.json --meta-path small.json --no-entities`

With vectors:
`python3 -m spacy train el big/ el_gdt-ud-train.json el_gdt-ud-dev.json --meta-path big.json --vectors ../el_vocab/ --no-entities`

3. `python3 -m spacy package small/model-final ./ --meta-path small.json`
4. `cd el_small-0.0.0` 
5. `python3 setup.py sdist`
6. `cd dist`
7. `sudo pip3 install el_small-0.0.0.tar.gz`