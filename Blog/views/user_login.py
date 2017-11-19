from flask import redirect, render_template
from flask_login import login_user, current_user
from flask_wtf.form import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

from Blog import app, db
from Blog.models.user import User

class userLoginForm(FlaskForm):
    name = StringField('用户名称', validators=[DataRequired()])
    password = PasswordField('用户密码', validators=[DataRequired()])
    remember_me = BooleanField('请记住我')


@app.route('/login', methods=['GET','POST'])
def user_login():
    form = userLoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            pass
                   
    return render_template('user_login.html', form=form)
        

