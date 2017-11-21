from Blog import db

class CommentForPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    