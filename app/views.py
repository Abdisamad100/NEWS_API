from flask import render_template, request,redirect,url_for
from app import app
from .request import get_news


# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    news = get_news()
    
    title = 'News Headlines'
    return render_template('index.html', title = title, news = news)