from Blog import app, db
from Blog.models.user import User, Role

from flask import render_template, redirect
from flask_wtf.form import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email,EqualTo

class userRegisterForm(FlaskForm):
    name = StringField(label='用户名称', validators=[DataRequired()])
    password = PasswordField(label='登录密码')
    check_password = PasswordField(label='确定密码')
    e_mail = StringField(label='电子邮件', validators=[Email()])


@app.route('/register', methods=['GET','POST'])
def user_register():
    form = userRegisterForm()    
    if form.validate_on_submit():
        user =  User.query.filter_by(username=form.name.data).first()
        if user is  None:
            role = Role(name="general user")
            user = User(username=form.name.data, 
                        e_mail=form.e_mail.data,
                        role=role)
            user.password_hash = form.password.data
            
            db.session.add(user)
            db.session.commit()
            return redirect('/')
        else:
            return '该用户名已存在'
    return render_template('user_register.html', form=form)
