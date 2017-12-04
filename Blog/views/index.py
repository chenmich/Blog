from flask import render_template

from Blog import app

from ..models import Post
from .utility import get_posts, get_fake_posts


@app.route('/')
def index():
    #for production
    #posts = get_posts()
    #for development
    posts = get_fake_posts()
    return render_template('index.html', posts=posts)
