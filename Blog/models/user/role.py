from Blog import app
from Blog import db

from Blog.models.user.user  import User

class role_name():
    admin = 'Administrator'
    anonymous = 'Anonymous'
    common = 'Common'
    moderator ='Moderator'

class permission_name():
    follow = 'FOLLOW'
    comment = 'COMMENT'
    writing = 'WRITING'
    moderate_comment ='MODERATE_COMMENT'
    admin ='ADMINSTER'

permissions = db.Table('permissions',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'), primary_key=True)
)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rolename= db.Column(db.String(20))
    permissions = db.relationship('Permission', secondary=permissions, lazy='subquery',
        backref=db.backref('role', lazy=True))
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.rolename

class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permission = db.Column(db.String(20))

