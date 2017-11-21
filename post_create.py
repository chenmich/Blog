from Blog import db

from Blog.models.post.post import Post
from Blog.models.user.user import User

users = User.query.all()

db.drop_all()
db.create_all()
post = Post.query.all()
print(post)