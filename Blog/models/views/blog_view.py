from ..post.post import Post

class BlogView():
    def __init__(self, post):
        self.title = post.title
        self.users = post.users
        
        
