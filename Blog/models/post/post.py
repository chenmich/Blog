from Blog import db

post_user = db.Table('post_user',
            db.Column('post_id', db.Integer, db.ForeignKey('post.id'), primary_key=True),
            db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
            )

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))

   
    #perhaps there are a fewer writer for this post
    other_writers = db.relationship('User', secondary=post_user, lazy='subquery',
        backref=db.backref('post', lazy=True))
    
    def __repr__(self):
        return '<Post %r>' % self.title

