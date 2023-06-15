from clean import clean
from models import load_model, load_model_score
import streamlit as st

type_humour = ['Pun Humor',
              'Dark Humor',
              'Cultural Humor',
              'One-liner Humor',
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

def analyze_text(text):
    # Run your model on the input text
    # Modify this function according to your specific model and analysis
    cleaner = clean(text)
    model = load_model()
    type = model(cleaner,type_humour)
    topic = model(cleaner,topic_humour)
    result_one = st.write("type of humor :", {type['labels'][0]})
    result_two = st.write("topic of humor :", {topic['labels'][0]})

    return result_one, result_two

def classify_text(text):
    model_score = load_model_score()
    cleaner = clean(text)
    result = model_score.predict(cleaner)
    return result
