from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from Blog import app
from ..models import Post

class PostEditor(FlaskForm):
    title = StringField('文章标题', validators=[DataRequired()])
    post_doc = TextAreaField(_name='post-markdown-doc')
    post_html = TextAreaField(_name='post-html-code')
    publish = BooleanField('请求发布')
    save = SubmitField('存储文章')

@app.route('/editor/<post_title>')
def post_editor(post_title):
    form = PostEditor()
    
    return render_template('post_editor.html', form=form)