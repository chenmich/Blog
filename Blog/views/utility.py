from ..models.post import BasePost

class FakePost(BasePost):    
    def __init__(self, title, first_writer, other_writers, first_paragraph):
        self._title = title
        self._first_writer = first_writer
        self._other_writers  = other_writers
        self._first_paragraph = first_paragraph

    @property
    def title(self):
        return self._title
    @property
    def first_writer(self):
        return self._first_writer
    @property
    def other_writers(self):
        return self._other_writers
    @property
    def first_paragraph(self):
        return self._first_paragraph

    def __repr__(self):
        return '<FakePost {}>'.format(self.title)
    
def get_posts(writer=None):
    pass

def get_fake_posts(writer=None):
    post_titles = ['First', 'Second', 'Third', 'Fouth', 'Fifth',
                    'Sixth', 'Seventh', 'Eight', 'Nineth', 'Tenth']
    post_writers = ['micheal', 'kfl', 'lrq', 'zl', 'zyq',
                            'ny', 'lzj', 'xzr', 'zs', 'ls']
    post_content = "Build responsive, mobile-first projects on the web with the world's most popular front-end component library.\nBootstrap is an open source toolkit for developing with HTML, CSS, and JS. Quickly prototype your ideas or build your entire app with our Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful plugins built on jQuery."
    fake_posts = []
    _index = 0
    if writer is not None:
        _index = post_writers.index(writer)
    for i in range(_index ,10):
        _post = FakePost(post_titles[i] + "   Post", 
                        first_writer=post_writers[i],
                        other_writers=post_writers[i+1:],
                        first_paragraph = post_content)
        fake_posts.append(_post)
    return fake_posts
    
        
        
