from ..models.post import BasePost

class FakePost(BasePost):    
    def __init__(self, title, first_writer,
                other_writers, first_paragraph,
                post_content):
        self._title = title
        self._first_writer = first_writer
        self._other_writers  = other_writers
        self._first_paragraph = first_paragraph
        self._post_content=post_content

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
    @property
    def post_content(self):
        return self._post_content

    def __repr__(self):
        return '<FakePost {}>'.format(self.title)
    
def get_posts(writer=None):
    pass

post_titles = ['First', 'Second', 'Third', 'Fouth', 'Fifth',
                    'Sixth', 'Seventh', 'Eight', 'Nineth', 'Tenth']
post_writers = ['micheal', 'kfl', 'lrq', 'zl', 'zyq',
                        'ny', 'lzj', 'xzr', 'zs', 'ls']
first_paragraph = '###About the responsive mobilt-first web'
first_paragraph = first_paragraph + "Build responsive, mobile-first projects on the web with the world's most popular front-end component library.\nBootstrap is an open source toolkit for developing with HTML, CSS, and JS. Quickly prototype your ideas or build your entire app with our Sass variables and mixins, responsive grid system, extensive prebuilt components, and powerful plugins built on jQuery."

post_content ='##About SQL database'
post_content = post_content + "SQL databases behave less like object collections the more size and performance start to matter; object collections behave less like tables and rows the more abstraction starts to matter. SQLAlchemy aims to accommodate both of these principles.\n"
post_content = post_content + "SQLAlchemy considers the database to be a relational algebra engine, not just a collection of tables. Rows can be selected from not only tables but also joins and other select statements; any of these units can be composed into a larger structure. SQLAlchemy's expression language builds on this concept from its core.\n"
post_content = post_content + "SQLAlchemy is most famous for its object-relational mapper (ORM), an optional component that provides the data mapper pattern, where classes can be mapped to the database in open ended, multiple ways - allowing the object model and database schema to develop in a cleanly decoupled way from the beginning.\n"
post_content = post_content + "SQLAlchemy's overall approach to these problems is entirely different from that of most other SQL / ORM tools, rooted in a so-called complimentarity- oriented approach; instead of hiding away SQL and object relational details behind a wall of automation, all processes are fully exposed within a series of composable, transparent tools. The library takes on the job of automating redundant tasks while the developer remains in control of how the database is organized and how SQL is constructed.\n"
post_content = post_content + "###why the SQLAlchemy"
post_content = post_content + "The main goal of SQLAlchemy is to change the way you think about databases and SQL!\n"
post_content = post_content + "Read some key features of SQLAlchemy, as well as what people are saying about SQLAlchemy.\n"

def get_fake_posts(writer=None):
    fake_posts = []
    _index = 0
    if writer is not None:
        _index = post_writers.index(writer)
    for i in range(_index ,10):
        _post = FakePost(post_titles[i] + "Post", 
                        first_writer=post_writers[i],
                        other_writers=post_writers[i+1:],
                        first_paragraph=first_paragraph,
                        post_content=post_content)
        fake_posts.append(_post)
    return fake_posts
    
def get_fake_post(post_title):
    _index = post_titles.index(post_title.split("P")[0])
    return FakePost(post_titles[_index] + "Post",
                    first_writer=post_writers[_index],
                    other_writers=post_writers[_index + 1:],
                    first_paragraph=first_paragraph,
                    post_content=post_content)
        
