from Blog import app
from flask import render_template, redirect

from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from Blog.models.user import User, Role

class userRegisterForm(FlaskForm):
    name = StringField(label='用户名称', validators=[DataRequired()])
    password = PasswordField(label='登录密码', validators=[DataRequired()])
    check_password = PasswordField(label='确定密码', validators=[DataRequired()])
    e_mail = StringField(label='电子邮件', validators=[Email()])
   


@app.route('/register', methods=['GET','POST'])
def user_register():
    form = userRegisterForm()    
    if form.validate_on_submit():
        return redirect('/')
    return render_template('user_register.html', form=form)