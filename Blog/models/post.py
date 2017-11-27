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
        raise NotImplementedError("The firstparagraph property is not impletemented!")

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
    _title = db.Column("title", db.String(256), nullable=False)
    writers = db.relationship('Post_User', back_populates='post')

    @property
    def title(self):
        return self.title
    @property
    def first_writer(self):
        for writer in self.writers:
            if writer.is_first_author:
                return writer
        return None
    @property
    def other_writers(self):
        _writers = []
        for  writer in self.writers:
            if writer is not True:
                _writers.append(writer)
        return writer


    def __repr__(self):
        return '<Post  %r>'%self.title


