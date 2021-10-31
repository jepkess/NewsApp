# from app import app
import urllib.request,json
from .models import Article,Source

Source = Source

Article = Article

api_key = None

news_sources_url = None

articles_url = None

#Getting the api key


# Getting the movie base url
# base_url_articles = app.config["SPECIFIC_ARTICLES_BASE_URL"]
# base_url_sources=app.config["NEWS_SOURCES_API_BASE_URL"]
# news_api_key=app.config["API_KEY"]

def configure_request(app):
    global api_key,news_sources_url,articles_url
    #Getting api key
    api_key = app.config['NEWS_API_KEY']

    news_sources_url = app.config["NEWS_SOURCES_API_BASE_URL"]

    articles_url = app.config["SPECIFIC_ARTICLES_BASE_URL"]


def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = articles_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['articles']:
            news_results_list = get_news_response['articles']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_results = []
    for news_item in news_list:
      
        author = news_item.get('author')
        title = news_item.get('title')
        description = news_item.get('description')
        url = news_item.get('url')
        image = news_item.get('urlToImage')
        publishedAt = news_item.get('publishedAt')

        if author:
            news_object = Article(author,title,description,url,image,publishedAt)
            news_results.append(news_object)

    return news_results



# GET SOURCES


def get_source(data):
    '''
    Function that gets the json response to our url request
    '''
    get_newsurl = news_sources_url.format(data,api_key)

    with urllib.request.urlopen(get_newsurl) as url:
        get_source_data = url.read()
        get_source_response = json.loads(get_source_data)

        news_sources = None

        if get_source_response['sources']:
            news_source_list = get_source_response['sources']
            news_sources = process_sources(news_source_list)


    return news_sources

def process_sources(source_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    news_sources = []
    for source_item in source_list:
      
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        country = source_item.get('country')

        if name:
            news_object_sources = Source(id,name,description,url,category,country)
            news_sources.append(news_object_sources)

    return news_sources