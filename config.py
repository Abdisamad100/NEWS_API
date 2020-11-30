# class Config:
#     '''
#     General configuration parent class
#     '''
#     NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey=327160e4a65c4bcba046b6288b52f9c0'
#     NEWS_ARTICLE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'




# class ProdConfig(Config):
#     '''
#     Production  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''
#     pass


# class DevConfig(Config):
#     '''
#     Development  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''

#     DEBUG = True

import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey=327160e4a65c4bcba046b6288b52f9c0'
    NEWS_ARTICLE_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')



class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
