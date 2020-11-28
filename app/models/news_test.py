import unittest
from models import news
News = movie.News

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News(aljazeera-News", "Aljazeera News","Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at AljazeeraNews.com","https://aljazeeranew.go.com","general","us")


    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()