import os
import sys
sys.path.append('.')
from Blog import db, app


class Association(db.Model):
    __tablename__ = 'association'
    left_id = db.Column(db.Integer, db.ForeignKey('left.id'), primary_key=True)
    right_id = db.Column(db.Integer, db.ForeignKey('right.id'), primary_key=True)
    extra_data = db.Column(db.String(50))
    child = db.relationship("Child", back_populates="parents")
    parent = db.relationship("Parent", back_populates="children")

class Parent(db.Model):
    __tablename__ = 'left'
    id = db.Column(db.Integer, primary_key=True)
    children = db.relationship("Association", back_populates="parent")
    def __repr__(self):
        return '<Parent {}>'.format(self.id)

class Child(db.Model):
    __tablename__ = 'right'
    id = db.Column(db.Integer, primary_key=True)
    parents = db.relationship("Association", back_populates="child")
    def __repr__(self):
        return "<Child  {}>".format(self.id)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        #'sqlite:///' + os.path.join(basedir, 'test.dat') 
        
app.config['WTF_CSRF_ENABLED'] = False
app.testing = True
db.create_all()

ps = [Parent() for i in range(0,10)]
children = [Child() for i in range(0,10)]
print(ps)
print(children)
print("---------------------------------------")
print()

p = ps[0]
a = Association()
a.child = children[0]
p.children.append(a)

db.session.add(a)
db.session.commit()
print(ps)
print(a)
print(children)
