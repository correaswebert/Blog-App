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

import nltk
from nltk.stem import WordNetLemmatizer 

# Plotting tools
import pyLDAvis
import pyLDAvis.gensim  # don't skip this
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(subset='train', shuffle = True)
newsgroups_test = fetch_20newsgroups(subset='test', shuffle = True)


# In[8]:


print(list(newsgroups_train.target_names))


# In[13]:


(newsgroups_train.data[:1])


# In[12]:


def preprocess(text):
    return [w for w in gensim.utils.simple_preprocess(text) if w not in gensim.parsing.preprocessing.STOPWORDS and len(w)>3]
def lemmatize(text):
    return [WordNetLemmatizer().lemmatize(w) for w in text]


# In[33]:


preproc_doc = []
for s in newsgroups_train.data:
    preproc_doc.append(lemmatize(preprocess(s)))
    


# In[27]:


len(preproc_doc[0])


# In[34]:


dwords = gensim.corpora.Dictionary(preproc_doc)


# In[35]:


c = 0
for k,v in dwords.iteritems():
    c+=1
    print(k,v)
    if c==10:
        break


# In[36]:


dwords.filter_extremes(no_below=15, no_above=0.5, keep_n=100000)


# In[38]:


bow = [dwords.doc2bow(s) for s in preproc_doc]


# In[52]:


from gensim import corpora, models
tfidf = models.TfidfModel(bow)
corpus_tfidf = tfidf[bow]
from pprint import pprint
for doc in corpus_tfidf:
    pprint(doc)
    break


# In[54]:


lda_model_tfidf = gensim.models.LdaMulticore(corpus_tfidf, num_topics=20, id2word=dwords, passes=2, workers=4)
for idx, topic in lda_model_tfidf.print_topics(-1):
    print('Topic: {} Word: {}'.format(idx, topic))


# In[57]:


bow_test = dwords.doc2bow(lemmatize(preprocess(newsgroups_test.data[0])))

for index, score in sorted(lda_model_tfidf[bow_test], key=lambda tup: -1*tup[1]):
    print("Score: {}\t Topic: {}".format(score, lda_model_tfidf.print_topic(index, 10)))


# In[58]:


print(newsgroups_test.target[0])


# In[61]:


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


df_topic_sents_keywords = format_topics_sentences(ldamodel=lda_model_tfidf, corpus=bow, texts=preproc_doc)

# Format
df_dominant_topic = df_topic_sents_keywords.reset_index()
df_dominant_topic.columns = ['Document_No', 'Dominant_Topic', 'Topic_Perc_Contrib', 'Keywords', 'Text']
df_dominant_topic.head(10)


# In[82]:


for x in df_dominant_topic[df_dominant_topic['Dominant_Topic']==8]['Document_No']:
    print(newsgroups_train.data[x])


# In[62]:


pyLDAvis.enable_notebook()
vis = pyLDAvis.gensim.prepare(lda_model_tfidf, bow, dictionary=lda_model_tfidf.id2word)
vis


# In[ ]:




