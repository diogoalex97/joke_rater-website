import streamlit as st
import pandas as pd

def display_dataframe_from_csv():
    # Load the CSV file into a DataFrame
    df = pd.read_csv("data/r_class_dict_diogo.csv")

    return df


def filter_and_get_top(df, column1, value1, column2, value2):
    filtered_df = df[(df[column1] == value1) & (df[column2] == value2)]
    sorted_df = filtered_df.sort_values(by="thread_rate", ascending=False)
    top3_rows = sorted_df.head(3)['thread_joke']
    return top3_rows

def calculate_average(df, column, column1, value1, column2, value2):
    filtered_df = df[(df[column1] == value1) & (df[column2] == value2)]
    average = filtered_df[column].mean()
    return average
