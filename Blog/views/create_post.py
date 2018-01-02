from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SelectMultipleField, SubmitField

from flask_login import current_user
from Blog import app

class PostAttributeForm(FlaskForm):
    post_title = StringField('博文标题')
    abstract = TextAreaField('摘要')
    other_writers = SelectMultipleField('其它作者')
    publish = BooleanField('发布')
    other_writers = SelectMultipleField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    submit_post = SubmitField('提交')

@app.route('/create_post', methods=['post', 'get'])
def create_post():
    form = PostAttributeForm()

    return render_template('create_post.html', form=form)
