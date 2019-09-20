import os

class Config:

    SOURCE_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_BASE_URL ='https://newsapi.org/v2/everything?sources={}&apiKey={}'
    # NEWS_HEADLINES_BASE_URL = 'https://newsapi.org/v2/news_headlines?source=abc-news,aftenposten,abc-news-au,al-jazeera-english,ansa,argaam,ars-technica,ary-news,associated-pres,australian-financial-review,independent&pageSize={}&apiKey={}'
    # SEARCH_BASE_URL = 'https://newsapi.org/v2/search?q={}&pageSize={}&apiKey={}'
    SOURCE_API_KEY  = '68df0bb9d5d44acda7ef91bb0d77b229'
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}