from os import urandom

from werkzeug.security import check_password_hash, generate_password_hash

from Blog import app, db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    email = db.Column(db.String(128))

    password_hash = db.Column(db.String(128), nullable=False)
    

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    
    def __repr__(self):
        return '<Role %r>' % self.username
