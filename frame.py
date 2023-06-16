import streamlit as st
import pandas as pd

st.cache_data
def load_jokes_data():
    # Load the CSV file into a DataFrame
    df = pd.read_csv("data/r_class_dict_diogo.csv")

    return df


def filter_jokes(df, column1, value1, column2, value2):
    return df[(df[column1] == value1) & (df[column2] == value2)]

def top3_jokes(df, column1, value1, column2, value2):
    filtered_df = filter_jokes(df, column1, value1, column2, value2)
    return filtered_df.sort_values(by="thread_rate", ascending=False).head(3)['thread_joke']

def plot_metrics(df, column, column1, value1, column2, value2):
    filtered_df = filter_jokes(df, column1, value1, column2, value2)
    filtered_df[column].plot.hist(bins=50)
