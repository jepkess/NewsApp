from flask import render_template
from app import app
from .request import get_news,get_source

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data

    '''
    
    title = "news"
    return render_template('index.html',title=title)

@app.route('/articles')
def articles():

    '''
    View root page function that returns the index page and its data

    '''
    technology_news=get_news('everything')
   
    title = " HOME-Welcome to the best News online website"
    return render_template('articles.html',title=title,technology_news=technology_news)

@app.route('/sources')
def sources():

    '''
    View root page function that returns the index page and its data

    '''
  
    news_sources=get_source('sources')
    title = " HOME-Welcome to the best News online website"
    return render_template('sources.html',title=title,news_sources=news_sources)





