from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, BooleanField, SubmitField
from wtforms.validators import DataRequired

from Blog import app
from ..models import Post

class PostEditor(FlaskForm):
    title = StringField('请输入文章标题', validators=[DataRequired()])
    post_markdown_doc = TextAreaField()
    post_html_code = TextAreaField()
    publish = BooleanField('请求发布')
    save = SubmitField('存储文章')

@app.route('/editor/<post_title>')
def post_editor(post_title):
    form = PostEditor()
    
    if form.validate_on_submit():
        print(form.publish.data)
        print("=====================================================")
        

    return render_template('post_editor.html', form=form)