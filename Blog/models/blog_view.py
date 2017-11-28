from .post import BasePost

class blog_view(BasePost):
    """
    post: a instance of Post
    """
    def __init__(self, post):
        self._post = post
    
    @property
    def title(self):
        return self._post.title
    @property
    def first_writer(self):
        return self._post.first_writer.username
    @property
    def other_writers(self):
        return [writer.username for writer in self._post.other_writers]
    @property
    def first_paragraph(self):
        return self._post.first_paragraph