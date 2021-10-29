from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data

    '''
    message ="Welcome to News-App"
    return render_template('index.html',message=message)

@app.route('/articles/<source>')
def articles():
    """
     View articles for a specific source page function that returns the article details page and its data.
    """
    return render_template('article.html')



