from Blog import blog_blue
from flask_login import logout_user, login_required, current_user
from flask import render_template, redirect, url_for

@blog_blue.route('/logout')
def user_logout():
    logout_user()
    return redirect(url_for('blog.index'))