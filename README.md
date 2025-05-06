# Preprocessing for Sentiment Analysis

This Python library provides a function to clean and preprocess a provided dataset stored in a pandas DataFrame.

## Features

Introduces a method `preprocess_dataframe` that takes a DataFrame as input:
- Cleans text by removing non-alphabetic characters
- Converts all words to lowercase
- Removes stopwords (except `"not"`)
- Applies Porter stemming to reduce words to root forms
- Saves the processed results to a CSV file with a new column: `Processed_Review` to the original DataFrame

## Requirements

- `pandas`
- `nltk`

## Installation

Install the preprocessing package:

```pip install git+https://github.com/remla2025-team10/lib-ml.git```