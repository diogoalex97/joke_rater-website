from transformers import  pipeline
import streamlit as st
import pickle
from gensim.models import Word2Vec
# import tensorflow as tfds
# from tensorflow.keras.preprocessing.text import text_to_word_sequence, Tokenizer
# from tensorflow.keras.preprocessing.sequence import pad_sequences
# from tensorflow.keras import layers, Sequential

@st.cache_resource
def load_model():
    pipe = pipeline(model="facebook/bart-large-mnli")
    return pipe

@st.cache_resource
def load_model_score():
    model = pickle.load(open('engagement_model.sav', 'rb'))
    return model
