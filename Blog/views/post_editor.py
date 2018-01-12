from flask import render_template, request
from Blog import blog_blue
from ..models import Post



@blog_blue.route('/editor/<post_title>', methods=['POST', 'GET'])
def post_editor(post_title):
    if request.method == 'POST':
        print(request.json['markdownDoc'])
        return 'OK'
    return render_template('post_editor.html', post_title=post_title)