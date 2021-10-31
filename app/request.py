from app import app
import urllib.request,json

# from app.article_test import Article
from .models import article

#Getting the api key


# Getting the movie base url
base_url_artciles = app.config["SPECIFIC_ARTICLES_BASE_URL"]
base_url_sources=app.config["NEWS_SOURCES_API_BASE_URL"]
news_api_key=app.config["API_KEY"]

def get_articles(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url_artciles.format(category,news_api_key)

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
        title = news_item.get('original_title')
        description = news_item.get('description')
        url = news_item.get('url')
        image = news_item.get('image')
        publishedAt = news_item.get('publishedAt')

        if author:
            news_object = article.Article(author,title,description,url,image,publishedAt)
            news_results.append(news_object)

    return news_results



# GET SOURCES


def get_source(data):
    '''
    Function that gets the json response to our url request
    '''
    get_newsurl = base_url_sources.format(data,news_api_key)

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
            news_object_sources = article.Source(id,name,description,url,category,country)
            news_sources.append(news_object_sources)

    return news_sources