from cleaner import cleaner_class, clean_score
from models import load_model, load_model_score
from frame import filter_and_get_top, display_dataframe_from_csv
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

def remove_word_from_string(string, word):
    new_string = string.replace(word, '')
    return new_string

def analyze_text(text):
    # Run your model on the input text
    # Modify this function according to your specific model and analysis
    cleaner = cleaner_class(text)
    model = load_model()
    type = model(cleaner,type_humour)
    topic = model(cleaner,topic_humour)
    modified_type= remove_word_from_string(type['labels'][0], 'Humor')
    modified_topic = remove_word_from_string(topic['labels'][0], 'Jokes')
    result_one = st.write("<b>Type of humor :</b>", modified_type, unsafe_allow_html=True)
    result_two = st.write("<b>Topic of the Joke :</b>", modified_topic, unsafe_allow_html=True)
    df = display_dataframe_from_csv()
    result_three = st.write(filter_and_get_top(df,"type humor",type['labels'][0],"topic joke",topic['labels'][0]))
    return result_one, result_two, result_three

def classify_text(text):
    model_score = load_model_score()
    cleaner = clean_score(text)
    result = model_score.predict(cleaner)
    return result
