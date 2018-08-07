import spacy
from spacy import displacy
import pandas as pd
from collections import defaultdict
import operator
indexes = {}
df = pd.read_csv('greek_sentiment_lexicon.tsv',sep='\t')
df = df.fillna('N/A')
for index, row in df.iterrows():
    df.at[index, "Term"] = row["Term"].split(' ')[0]
    indexes[df.at[index, "Term"]] = index


text = '''Έχω μείνει έκπληκτος! Πώς γίνεται αυτό; Η έκπληξη είναι τόσο μεγάλη! Α, τώρα εξηγούνται όλα.'''
subj_scores = {
    'OBJ': 0,
    'SUBJ-': 0.5,
    'SUBJ+': 1,
}

emotion_scores = {
    'N/A': 0,
    '1.0': 0.2,
    '2.0': 0.4,
    '3.0': 0.6,
    '4.0': 0.8,
    '5.0': 1,
}

polarity_scores = {
    'N/A': 0,
    'BOTH': 0,
    'NEG': -1,
    'POS': 1
}

nlp = spacy.load('el')
doc = nlp(text)
subjectivity_score = 0
anger_score = 0
disgust_score = 0
fear_score =  0
happiness_score = 0
sadness_score = 0
surprise_score = 0
matched_tokens = 0
for token in doc:
    lemmatized_token = token.lemma_
    if (lemmatized_token in indexes):
        indx = indexes[lemmatized_token]
        pos_flag = False
        for col in ["POS1", "POS2", "POS3", "POS4"]:
            if (token.pos_ == df.at[indx,col]):
                pos_flag = True
                break
        if (pos_flag == True):
            match_col_index = [int(s) for s in col if s.isdigit()][0]
            subjectivity_score += subj_scores[df.at[indx,'Subjectivity'+str(match_col_index)]]
            anger_score += emotion_scores[str(df.at[indx, 'Anger'+str(match_col_index)])]
            disgust_score += emotion_scores[str(df.at[indx, 'Disgust'+str(match_col_index)])]
            fear_score += emotion_scores[str(df.at[indx, 'Fear'+str(match_col_index)])]
            happiness_score += emotion_scores[str(df.at[indx, 'Happiness'+str(match_col_index)])]
            sadness_score += emotion_scores[str(df.at[indx,'Sadness'+str(match_col_index)])]
            surprise_score += emotion_scores[str(df.at[indx, 'Surprise'+str(match_col_index)])]
            matched_tokens+=1
            for child in token.children:
                print(child, child.dep_)

try:
    print('Subjectivity: ' + str(subjectivity_score/matched_tokens * 100)+'%')
    emotions = {'anger': anger_score, 'disgust': disgust_score, 'fear':fear_score, 'happiness':happiness_score, 'sadness': sadness_score, 'surprise': surprise_score}
    emotion = max(emotions.items(), key=operator.itemgetter(1))[0]
    if (emotions[emotion] == 0):
        print('Unable to detect emotion')
    else:
        print('Main emotion: ' + emotion + '. Emotion score: ' + str(emotions[emotion]*100/matched_tokens) + '%')
except:
    print('No matched tokens')
