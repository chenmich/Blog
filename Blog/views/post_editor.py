from flask import render_template, request
from Blog import app
from ..models import Post

@app.route('/<post_title>', methods=['POST'])
def recieve_post(post_title):
    if request.method == 'GET':
        print('ok')
    return 'OK'

@app.route('/editor/<post_title>', methods=['POST', 'GET'])
def post_editor(post_title):
    if request.method == 'POST':
        pass
    return render_template('post_editor.html', post_title=post_title)