#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import numpy as np
import pandas as pd
from pprint import pprint

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

import pickle


# In[2]:


lda_model=pickle.loads(open('LDA_Model', 'rb').read())


# In[12]:


from gensim.parsing.preprocessing import STOPWORDS
import nltk
from nltk.stem import WordNetLemmatizer


# In[4]:


def preprocess(text):
    return [w for w in gensim.utils.simple_preprocess(text) if w not in STOPWORDS and len(w)>3]
def lemmatize(text):
    return [WordNetLemmatizer().lemmatize(w) for w in text]


# In[6]:


def format_topics_sentences(ldamodel, corpus, texts):
    # Init output
    sent_topics_df = pd.DataFrame()

    # Get main topic in each document
    for i, row_list in enumerate(ldamodel[corpus]):
        row = row_list[0] if ldamodel.per_word_topics else row_list            
        # print(row)
        row = sorted(row, key=lambda x: (x[1]), reverse=True)
        # Get the Dominant topic, Perc Contribution and Keywords for each document
        for j, (topic_num, prop_topic) in enumerate(row):
            if j == 0:  # => dominant topic
                wp = ldamodel.show_topic(topic_num)
                topic_keywords = ", ".join([word for word, prop in wp])
                sent_topics_df = sent_topics_df.append(pd.Series([int(topic_num), round(prop_topic,4), topic_keywords]), ignore_index=True)
            else:
                break
    sent_topics_df.columns = ['Dominant_Topic', 'Perc_Contribution', 'Topic_Keywords']

    # Add original text to the end of the output
    contents = pd.Series(texts)
    sent_topics_df = pd.concat([sent_topics_df, contents], axis=1)
    return(sent_topics_df)


#df_topic_sents_keywords = format_topics_sentences(ldamodel=lda_model_tfidf, corpus=bow, texts=preproc_doc)

# Format
#df_dominant_topic = df_topic_sents_keywords.reset_index()
#df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']
#df_dominant_topic.head(10)


# In[13]:


def generate_tags(s):
    preproc_doc = []
    preproc_doc.append(lemmatize(preprocess(s)))
    dwords = gensim.corpora.Dictionary(preproc_doc)
    bow = [dwords.doc2bow(s) for s in preproc_doc]
    df_topic_sents_keywords = format_topics_sentences(ldamodel=lda_model, corpus=bow, texts=preproc_doc)
    df_dominant_topic = df_topic_sents_keywords.reset_index()
    df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']
    return df_dominant_topic.loc[0,'Keywords']

    


# In[ ]:




