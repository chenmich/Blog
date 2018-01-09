from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired
from flask_login import current_user
from Blog import app, db
from ..models import User, Post, Post_User

def getAllUserIdentifiers():
    users = User.query.all()
    users_identifiers = [(str(user.id), user.username) for user in users]
    return users_identifiers

def _create_post_entity(userId, post_title, other_writers_id):
    first_writer = User.query.all().filter_by(id=userId)
    other_writers = [User.query.all().filter_by(id=int(_id)) for _id in other_writers_id]
    post = Post(post_title=post_title)

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
        _create_post_entity(current_user.id, form.post_title, form.other_writers)    
        return 'ok'
    else:

        return render_template('create_post.html', form=form)

