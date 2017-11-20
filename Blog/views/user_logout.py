from Blog import db, app
from flask_login import logout_user, login_required, current_user
from flask import render_template, redirect

@app.route('/logout')
@login_required
def user_logout():
    logout_user()
    return redirect('/')