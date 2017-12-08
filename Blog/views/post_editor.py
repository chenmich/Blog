from flask import render_template, request

from Blog import app
from ..models import Post

@app.route('/<post_title>')
def recieve_post(post_title):
    print('ok')
    return 'OK'

@app.route('/editor/<post_title>')
def post_editor(post_title):    
    return render_template('post_editor.html', post_title=post_title)