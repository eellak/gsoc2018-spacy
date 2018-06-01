import pickle

def load_pickle(file_path):
    # load file
    with open(file_path, 'rb') as f:
        return pickle.load(f)


verbs = load_pickle('elwiktionary_verbs.pkl')
len(verbs)
