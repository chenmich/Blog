from flask import render_template

from Blog import app

from ..models import Post
from .utility import get_posts, get_fake_post

@app.route('/post_show/<post_title>')
def post_show(post_title):
    #for development
    post = get_fake_post(post_title)
    return render_template('post_show.html', post=post)