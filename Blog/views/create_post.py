from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SelectMultipleField, SubmitField
from wtforms.validators import DataRequired
from flask_login import current_user
from Blog import blog_blue, db
from ..models import User, Post, Post_User

def getAllUserIdentifiers():
    users = User.query.filter(User.id.isnot(current_user.id)).all()
    users_identifiers = [(str(user.id), user.username) for user in users]
    return users_identifiers

def _create_post_entity(userId, post_title, other_writers_id):
        
    first_writer = User.query.filter_by(id=userId).all()[0]
    post = Post(title=post_title)
    first_writer_post_relationship = Post_User(is_first_author=True)
    first_writer_post_relationship.writer = first_writer
    post.writers.append(first_writer_post_relationship)
    other_writers_post_relationships = []
    for other_writer_id in other_writers_id:
        _relationship = Post_User()
        _idInt = int(other_writer_id)
        _relationship.writer = User.query.filter_by(id=_idInt).all()[0]
        post.writers.append(_relationship)
        other_writers_post_relationships.append(_relationship)

    db.session.add_all(other_writers_post_relationships)
    db.session.add(post)    
    db.session.commit()
    return post

class PostAttributeForm(FlaskForm):
    post_title = StringField('博文标题', validators=[DataRequired()])
    abstract = TextAreaField('摘要')
    publish = BooleanField('发布')
    other_writers = SelectMultipleField('其它作者')
    submit_post = SubmitField('提交')

@blog_blue.route('/create_post', methods=['post', 'get'])
def create_post():
    print(current_user)
    form = PostAttributeForm()
    form.other_writers.choices = getAllUserIdentifiers() 
    if form.validate_on_submit():
        other_writers_id = [ writer_id  for writer_id in form.other_writers.data]        
        post = _create_post_entity(current_user.id, form.post_title.data, other_writers_id)    
        return 'ok'
    else:
        return render_template('create_post.html', form=form)

