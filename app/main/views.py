from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_source,get_articles
# from .forms import ReviewForm
from ..models import Source, Articles

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sports = get_source('sports')
    entertainment = get_source('entertainment')
    technology = get_source('technology')
    business = get_source('business')
    general = get_source('general')
    health = get_source('health')
    title = ' Welcome to the online Newshighlights'
    return render_template('index.html', title = title, sports =sports, entertainment=entertainment, technology=technology, business=business, general=general,health = health)
@main.route('/source/<int:id>')
def source(id):

    sources = get_source(id)
    # title = f'{id} | All Article'
    return render_template('index.html',source = sources)

@main.route('/article/<source_id>')
def articles(source_id):
    '''
    Function that returns the articles
    '''
    articles_source = get_articles(source_id)
    # title = f'{id}| Articles'
    return render_template('articles.html', articles = articles_source)
