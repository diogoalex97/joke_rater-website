import re
import pandas as pd

def clean(sentence):
        # Basic cleaning
        sentence = sentence.strip() ## remove whitespaces
        sentence = sentence.lower() ## lowercase
        sentence = re.sub(r'[^\w]', ' ', sentence)
        sentence = sentence.replace('\n', '')
        return sentence
