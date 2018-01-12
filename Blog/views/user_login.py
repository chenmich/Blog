from flask import redirect, render_template, flash, url_for
from flask_login import login_user, current_user
from flask_wtf.form import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired

from Blog import blog_blue, db
from Blog.models.user import User

class userLoginForm(FlaskForm):
    name = StringField('用户名称', validators=[DataRequired()])
    password = PasswordField('用户密码', validators=[DataRequired()])
    remember_me = BooleanField('请记住我')


@blog_blue.route('/login', methods=['GET','POST'])
def user_login():
    form = userLoginForm()
    if form.validate_on_submit():
        print()
        user = User.query.filter_by(username=form.name.data).first()
        if user is not None  and   user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            return redirect(url_for('blog.index'))
        else:
            flash("用户名称/密码不正确")

    return render_template('user_login.html', form=form)
        

