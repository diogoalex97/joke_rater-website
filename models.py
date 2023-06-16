from transformers import  pipeline
import streamlit as st
import pickle
# from tensorflow.keras import models

@st.cache_resource
def load_model():
    pipe = pipeline(model="facebook/bart-large-mnli")
    return pipe

@st.cache_resource
def load_model_score():
    # model = models.load_model('data/engagement_model_v1')
    # #word2vec = Word2Vec.load("word2vec_v1.model")
    # with open("data/word2vec_v3", 'rb') as file:
    #     word2vec = pickle.load(file)
    return None
