import urllib.request,json
from .models import Source

# Source= source.Source
# Getting api key
api_key = None
# Getting the movie base url
base_url = None


def configure_request(app):
    global api_key,base_url
    api_key = app.config['SOURCE_API_KEY']
    base_url = app.config['SOURCE_API_BASE_URL']
    print('lslsll')
    # print(api_key)
    # print(base_url)
    
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
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain source details

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