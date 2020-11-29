from flask import render_template, request,redirect,url_for
from app import app
from .request import get_news


# Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''

#     # Getting popular movie
#     latest_news = get_news('latest')
#     print(latest_news)
#     title = 'Home - Welcome to The best Movie Review Website Online'
#     return render_template('index.html', title = title,latest = latest_news)

@app.route('/', methods=['GET'])
def index():

    '''
    view news page function that returns the news details  and its data
    '''
    
    news = get_news()
    # print(news)
    title = "News_Highlight"
    
    return render_template('index.html', news = news, title=title)
    
    