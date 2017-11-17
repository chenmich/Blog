from Blog import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    