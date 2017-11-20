from Blog import app
from flask import render_template
from .utility import get_post_views
from flask_login import current_user

@app.route('/')
def index():
    blog_views = get_post_views()
    print(current_user)
    return render_template('post_list.html', blog_views=blog_views)
