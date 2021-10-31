from flask import render_template
from app import app
from .request import get_articles,get_source

# Views
#displaying the source on the homepage
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data

    '''
    response=get_source('sources')
    title = "news"
    return render_template('index.html',title=title,sources=response)

@app.route('/articles/<source>',methods=['GET']) # get method to get data from the api
def articles(source):

    '''
    View root page function that returns the index page and its data

    '''
    articles=get_articles(source)
   
    title = " HOME-Welcome to the best News online website"
    return render_template('articles.html',title=title,articles=articles,source=source)

# @app.route('/')
# def sources():

#     '''
#     View root page function that returns the index page and its data

#     '''
  
#     news_sources=get_source('sources')
#     title = " HOME-Welcome to the best News online website"
#     return render_template('sources.html',title=title,news_sources=news_sources)





