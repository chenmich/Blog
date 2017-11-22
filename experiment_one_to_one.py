from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func, Boolean
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
Base = declarative_base()
engine = create_engine('sqlite://')
Session = sessionmaker()
Session.configure(bind=engine)

class Association(Base):
    __tablename__ = 'association'
    left_id = Column(Integer, ForeignKey('left.id'), primary_key=True)
    right_id = Column(Integer, ForeignKey('right.id'), primary_key=True)
    is_first_author = Column(Boolean, default=False )
    child = relationship("Child", back_populates="parents")
    parent = relationship("Parent", back_populates="children")
    def __repr__(self):
        return '<A %r>' % self.is_first_author
#post
class Parent(Base):
    __tablename__ = 'left'
    id = Column(Integer, primary_key=True)
    children = relationship("Association", back_populates="parent")
    def __repr__(self):
        return '<Parent %r>' % self.id
#user
class Child(Base):
    __tablename__ = 'right'
    id = Column(Integer, primary_key=True)
    parents = relationship("Association", back_populates="child")
    def __repr__(self):
        return '<Child %r>' % self.id



Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)
sess = Session()

childern = []
parents = []
a_first_authors = []

for i in range(0, 10):
    parent = Parent()
    a = Association(is_first_author=True)
    child = Child()
    a.child = child
    parent.children.append(a)
    parents.append(parent)
    childern.append(child)
    a_first_authors.append(a)

sess.add_all(parents)
sess.add_all(childern)
sess.add_all(a_first_authors)


a = Association()
a.child = childern[1]
parents[0].children.append(a)

print(parents[0].children)
sess.add(a)
sess.commit()
print(parents[0].children)

other_a = Association()

other_a.child = childern[2]
parents[0].children.append(other_a)
sess.add(other_a)
sess.commit()

print(parents[0].children)






























