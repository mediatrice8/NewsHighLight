import urllib.request,json
from .models import Source,Articles

# Source= source.Source
# Getting api key
# api_key = None
# # Getting the movie base url
# base_url = None
# articles_url = None


def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    articles_url = app.config['ARTICLES_BASE_URL']
    # news_headlines_url = app.config['NEWS_HEADLINES_BASE_URL']
    # search_url = app.config['SEARCH_BASE_URL']
