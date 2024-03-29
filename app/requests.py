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
    
def get_source(category):
    '''
    Function that gets the json response to our url request
    '''
    get_source_url = base_url.format(category,api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        source_results = None

        if get_source_response['sources']:
            source_results_list = get_source_response['sources']
            source_results  = process_results(source_results_list)


    return source_results
def process_results(source_list):
    '''
    Function  that processes the source result and transform them to a list of Objects

    Args:
        source_list: A list of dictionaries that contain source details

    Returns :
        sources_results: A list of news objects
    '''
    source_results = []
    for source_item in source_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        source_object = Source(id,name,description,url,category,language,country)
        source_results.append(source_object)

    return source_results
def get_articles(source_id):
    '''
    Function that gets the json response to our url request
    '''
    get_article_url =articles_url.format(source_id,api_key)
    print(get_article_url)

    with urllib.request.urlopen(get_article_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        
 
        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_articles(articles_list):
    '''
    Function  that processes the article result and transform them to a list of Objects
    '''
    articles_result = []
    for article_item in articles_list:
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        urlToImage = article_item.get('urlToImage')
        publishedAt = article_item.get('publishedAt')
        
        if urlToImage:
            article_object = Articles(author,title,description,url,urlToImage,publishedAt)
            articles_result.append(article_object)
    return articles_result

