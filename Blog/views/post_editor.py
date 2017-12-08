from flask import render_template, request

from Blog import app
from ..models import Post

@app.route('/<post_title>', methods=['GET', 'POST'])

@app.route('/editor/<post_title>')
def post_editor(post_title):
    print(request.args.get('a'))
    return render_template('post_editor.html', post_title=post_title)