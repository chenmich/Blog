from Blog import app
from Blog import db

permissions = db.Table('permissions',
    db.Column('role_id', db.Integer, db.ForeignKey('role.id')),
    db.Column('permission_id', db.Integer, db.ForeignKey('permission.id'))
)


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rolename= db.Column(db.String(20))
    permissions = db.relationship('Permission', secondary=permissions, lazy='subquery',
        backref=db.backref('role', lazy=True))

class Permission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    permission = db.Column(db.String(20))

