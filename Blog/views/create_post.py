from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired
from flask_login import current_user
from Blog import app, db
from ..models import User

def getAllUserIdentifiers():
    users = User.query.all()
    users_identifiers = [(str(user.id), user.username) for user in users]
    return users_identifiers


class PostAttributeForm(FlaskForm):
    post_title = StringField('博文标题', validators=[DataRequired()])
    abstract = TextAreaField('摘要')
    publish = BooleanField('发布')
    other_writers = SelectMultipleField('其它作者', choices=getAllUserIdentifiers())
    submit_post = SubmitField('提交')

@app.route('/create_post', methods=['post', 'get'])
def create_post():
    form = PostAttributeForm()    
    if form.validate_on_submit():        
        return 'ok'
    else:
        print(form.post_title.errors)
        return render_template('create_post.html', form=form)
