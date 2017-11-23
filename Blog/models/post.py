from Blog import db
from .user import User

class Post_User(db.Model):
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    is_first_author = db.Column(db.Boolean(), default=False)
    writer = db.relationship("User", back_populates='posts')
    post = db.relationship("Post", back_populates='writers')
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256), nullable=False)
    writers = db.relationship('Post_User', back_populates='post')

    def __repr__(self):
        return '<Post  %r>'%self.title


