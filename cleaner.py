import re

def cleaner_class(sentence):
        # Basic cleaning
        sentence = sentence.strip() ## remove whitespaces
        sentence = sentence.lower() ## lowercase
        # sentence = re.sub(r'[^\w]', ' ', sentence)
        # sentence = re.sub(r'\d+', '', sentence)
        sentence = sentence.replace('\n', '')
        return sentence

def clean_score(sentence):
        # Basic cleaning
        sentence = sentence.strip() ## remove whitespaces
        sentence = sentence.lower() ## lowercase
        sentence = re.sub(r'[^\w]', ' ', sentence)
        sentence = re.sub(r'\d+', '', sentence)
        sentence = sentence.replace('\n', '')
        return sentence
