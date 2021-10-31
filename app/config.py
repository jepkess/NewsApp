class Config:
    '''
    General configuration parent class
    '''
    API_KEY='530e4717b7f440a7a60851bca8f06680'
    SPECIFIC_ARTICLES_BASE_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
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
