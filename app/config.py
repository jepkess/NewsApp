class Config:
    '''
    General configuration parent class
    '''
    API_KEY='530e4717b7f440a7a60851bca8f06680'
    NEWS_ARTICLES_API_BASE_URL='https://newsapi.org/v2/{}?q=tesla&from=2021-09-30&sortBy=publishedAt&apiKey={}'
    NEWS_SOURCES_API_BASE_URL='https://newsapi.org/v2/top-headlines/{}?apiKey={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
