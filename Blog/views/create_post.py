from flask import render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, TextAreaField, SelectMultipleField, SubmitField

from flask_login import current_user
from Blog import app

class PostAttributeForm(FlaskForm):
    post_title = StringField('博文标题')
    abstract = TextAreaField('摘要')
    publish = BooleanField('发布')
    other_writers = SelectMultipleField('其它作者', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
    submit_post = SubmitField('提交')

@app.route('/create_post', methods=['post', 'get'])
def create_post():
    form = PostAttributeForm()
    form.abstract.data='''###摘要
    '''
    
    if request.method == 'POST':
        print('The method is post')
        print(form.other_writers.data)
    return render_template('create_post.html', form=form)
