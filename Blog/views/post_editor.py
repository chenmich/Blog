from flask import render_template

from Blog import app
from ..models import Post

@app.route('/editor/<post_title>')
def post_editor(post_title):
    return "<h1>未实现</h1>"