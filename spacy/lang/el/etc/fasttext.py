# TRAIN FastText with Greek Wikipedia
# needs gensim installed

# Step 1 : get a working environment with gensim installed
# On Ubuntu 16
# apt-get install -y gcc python3-pip python3-dev vim htop
# pip3 install --upgrade pip
# pip3 install setuptools
# pip3 install ipython gensim

# Step 2 : get the wikipedia dump
# wget https://dumps.wikimedia.org/elwiki/latest/elwiki-latest-pages-articles.xml.bz2

# Step 3: train the model. Skip-Gram, negative sampling, 300size dimension and a window of 10 (as of the FastText pre-trained word vectors 
# https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md


import logging
import multiprocessing
from gensim.corpora import WikiCorpus, MmCorpus
from gensim.models.fasttext import FastText
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

wiki = WikiCorpus("/root/elwiki-latest-pages-articles.xml.bz2", dictionary={})

sentences = list(wiki.get_texts())

params = {'sg': 1, 'size': 300, 'window': 10, 'negative': 10, 'min_count': 10, 'workers': max(1, multiprocessing.cpu_count() -1), 'sample': 1E-3}

model = FastText(sentences, **params)

model.save('ft_model')

# Step 4: load the model

from gensim.models import KeyedVectors
model = KeyedVectors.load('ft_model')

