from Blog import app
from flask import render_template
from flask_login import current_user
from ..models import Post
from .utility import get_posts

@app.route('/')
def index():
    posts = get_posts()
    return render_template('index.html', posts=posts)