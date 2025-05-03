from setuptools import setup, find_packages

setup(
    name='preprocess-sentiment-analysis',
    version='0.0.2', # TODO: Automatic versioning
    packages=find_packages(),
    install_requires=['nltk', 'pandas'],
    author='REMLA 2025 Team 10',
    description='Preprocessing logic for Restaurant Sentiment Analysis',
    include_package_data=True,
    python_requires='>3.8'
)
