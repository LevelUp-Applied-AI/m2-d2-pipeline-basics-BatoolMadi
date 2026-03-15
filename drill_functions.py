"""
Module 2 — Drill 2: Pipeline Basics

Write the two functions below from memory.
Remove the TODO: comments and pass statements as you implement each function.
Do not change the function signatures.
"""

import pandas as pd


def clean_column(series):
    
    median_value = series.median()
    cleaned_series = series.fillna(median_value)
    return cleaned_series


def compute_revenue(quantity, price):

    revenue = quantity * price
    return revenue
