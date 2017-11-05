from Blog import app
from flask import render_template
from .utility import get_post_views

@app.route('/')
def index():
    blog_views = get_post_views()
    return render_template('post_list.html', blog_views=blog_views)
