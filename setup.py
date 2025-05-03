from setuptools import setup, find_packages
import os

# read the version
def read_version():
    with open(os.path.join("preprocess_sentiment_analysis", "VERSION"), "r") as file:
        return file.read().strip()

setup(
    name='preprocess-sentiment-analysis',
    version=read_version(),
    packages=find_packages(),
    install_requires=['nltk', 'pandas'],
    author='REMLA 2025 Team 10',
    description='Preprocessing logic for Restaurant Sentiment Analysis',
    include_package_data=True,
    python_requires='>3.8'
)
