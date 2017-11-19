from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from Blog import app, db, login_manager

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)    
    email = db.Column(db.String(128))
    password_hash = db.Column(db.String(128), nullable=False)
    
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)
    
    

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def get_id(self):
        return self.username

    def __repr__(self):
        return '<Role %r>' % self.username


@login_manager.user_loader
def user_loader(username):
    return User.query.filter_by(username=username).first()
    