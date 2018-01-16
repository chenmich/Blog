from flask import render_template, request, redirect, url_for, current_app
from flask_login import login_required, current_user
from Blog import blog_blue, login_manager
from ..models import Post

def can_be_modify_by_current_user(post_title):
    post = Post.query.filter_by(title=post_title).first()
    if post is None: 
        return False
    first_writer = post.first_writer
    if (first_writer.id == current_user.id): 
        return True
    else:
        return False

@blog_blue.route('/editor/<post_title>', methods=['POST', 'GET'])
@login_required
def post_editor(post_title):
    if can_be_modify_by_current_user(post_title) is False:
        return current_app.login_manager.unauthorized()
    if request.method == 'POST':
        print(request.json['markdownDoc'])
        return 'ok'
    return render_template('post_editor.html', post_title=post_title)
