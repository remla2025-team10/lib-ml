import re
import nltk
import pandas as pd

nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

def preprocess_dataframe(df: pd.DataFrame, output_path: str = "processed_reviews.csv") -> pd.DataFrame:
    """
    cleans and preprocesses the 'Review' column in the provided df dataset.
    saves the result to a CSV file, returns processed dataframe.

    Args:
        df (pd.DataFrame): input DataFrame with a 'Review' column.
        output_path (str): path to save the processed corpus as CSV.

    Returns:
        pd.DataFrame: dataFrame with a new column 'Processed_Review'.
    """

    ps = PorterStemmer()

    all_stopwords = set(stopwords.words('english'))
    all_stopwords.discard('not')

    processed_reviews = []

    for review in df['Review']:
        review = re.sub('[^a-zA-Z]', ' ', str(review))
        review = review.lower().split()
        review = [ps.stem(word) for word in review if word not in all_stopwords]
        cleaned = ' '.join(review)
        processed_reviews.append(cleaned)

    df['Processed_Review'] = processed_reviews
    df.to_csv(output_path, index=False)

    return df
