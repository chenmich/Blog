from Blog import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))

    def __repr__(self):
        return '<Post %r>' % self.title