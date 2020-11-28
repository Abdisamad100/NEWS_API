class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey=327160e4a65c4bcba046b6288b52f9c0'




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True