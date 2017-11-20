from flask import redirect, render_template
from flask_login import login_user
from flask_wtf.form import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

from Blog import app, db
from Blog.models.user import Role, User, role_name


class userRegisterForm(FlaskForm):
    name = StringField(label='用户名称', validators=[DataRequired()])
    password = PasswordField(label='登录密码', validators=[DataRequired()])
    check_password = PasswordField(label='确定密码', validators=[EqualTo('password', '输入的两个密码不一致')])
    e_mail = StringField(label='电子邮件', validators=[Email()])


@app.route('/register', methods=['GET','POST'])
def user_register():
    form = userRegisterForm()    
    if form.validate_on_submit():
        user =  User.query.filter_by(username=form.name.data).first()
        if user is  None:
            common_role = Role.query.filter_by(rolename=role_name.common).first()            
            register_user = _create_register_user(
                username=form.name.data,
                password=form.password.data,
                email=form.e_mail.data,
                role=common_role
            )
            db.session.add(register_user)            
            login_user(register_user)
            return redirect('/')
        else:
            return '该用户名已存在'
    return render_template('user_register.html', form=form)

def _create_register_user(username, password, email, role):
    user = User(
                username=username,
                password=password,
                email=email,
                role=role
            )
    #user.role_id = role.id
    return user
