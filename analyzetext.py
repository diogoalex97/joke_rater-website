from cleaner import cleaner_class, clean_score
from models import load_model, load_model_score
import numpy as np
from functools import cache
import streamlit as st
type_humour = ['Pun Humor',
              'Dark Humor',
              'Cultural Humor',
            #   'One-liner Humor',
              'Dad Humor',
              'Knock-knock Humor',
              'Sexual Humor'
              ]

topic_humour = ['Animals Jokes',
                'Bar Jokes',
                'Sports Jokes',
                'Relationships Jokes',
                'Technology Jokes',
                'Politics Jokes',
                'Religious Jokes',
                'Celebrity Jokes'
                ]

def remove_word_from_string(string, word):
    new_string = string.replace(word, '')
    return new_string

def analyze_text(text):
    # Run your model on the input text
    # Modify this function according to your specific model and analysis
    cleaner = cleaner_class(text)
    model = load_model()
    type_ = model(cleaner,type_humour)
    topic = model(cleaner,topic_humour)

    return type_['labels'][0], topic['labels'][0]

def embedding(word2vec, sentences):
    embedded_sentences = [embed_sentence(word2vec, sentence) for sentence in sentences]
    return np.array(embedded_sentences)


def embed_sentence(word2vec, sentence):
    words = [word.lower() for word in sentence.split()]
    embedded_sentence = [word2vec.wv[word]
                             for word in words
                             if word in word2vec.wv]
    return np.array(embedded_sentence)


@st.cache_resource
def classify_text(text):
    return np.random.rand()
