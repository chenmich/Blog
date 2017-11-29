from flask import render_template
from flask_wtf import FlaskForm

from Blog import app
from ..models import Post

class PostEditor(FlaskForm):
    pass

@app.route('/editor/<post_title>')
def post_editor(post_title):
    return render_template('post_editor.html')