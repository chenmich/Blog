from flask import render_template

from Blog import blog_blue

from ..models import Post
from .utility import get_posts, get_fake_posts
from ..models import User
from ..models import blog_view

@blog_blue.route('/post/<username>')
def post_by_user(username):
    
    #for production
    #posts = get_posts(username)
    #for development
    posts = get_fake_posts(username)
    return render_template("index.html", posts=posts)
