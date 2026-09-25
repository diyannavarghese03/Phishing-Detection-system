from urllib.parse import urlparse
import pandas as pd


def preprocess_url(url):
    """Clean and standardize URL"""
    url = url.lower().strip()
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    return url


def load_data():
    """Load and combine datasets"""
    data = pd.read_excel("data/data_bal - 20000.xlsx")
    urls = data['URLs'].tolist()
    labels = data['Labels'].tolist()
    return urls, labels
