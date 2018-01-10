from Blog import db
from .user import User

class BasePost():
    @property
    def title(self):
        raise NotImplementedError("The title property is not impletemented!")
    @property
    def first_writer(self):
        raise NotImplementedError("The first_writer property is not impletemented!")
    @property
    def other_writers(self):
        raise NotImplementedError("The first_writer property is not impletemented!")
    @property
    def first_paragraph(self):
        raise NotImplementedError("The firs_tparagraph property is not impletemented!")
    @property
    def post_content(self):
        raise NotImplementedError("The post_content property is not impletemented!")
class Post_User(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    is_first_author = db.Column(db.Boolean(), default=False)
    writer = db.relationship("User", back_populates='posts')
    post = db.relationship("Post", back_populates='writers')

    def __repr__(self):
        return '< Post_User {0},{1}>'.format(self.writer.username, self.post.title)
    

class Post(db.Model, BasePost):
    id = db.Column(db.Integer, primary_key=True)
    writers = db.relationship('Post_User', back_populates='post')
    #i can think that the property tilte is defined 
    title = db.Column(db.String(256), nullable=False)
    @property
    def first_writer(self):
        for writer in self.writers:
            if writer.is_first_author:
                return writer.writer
        return None
    @property
    def other_writers(self):
        _writers = []
        for  writer in self.writers:
            if writer.is_first_author is not True:
                _writers.append(writer.writer)
        return _writers


    def __repr__(self):
        return '<Post  %r>'%self.title


