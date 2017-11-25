import os
import sys
sys.path.append('.')
import unittest
from Blog import db, app
from Blog.models import Role, role_name, Permission, permission_name, User, Post, Post_User
from create_data_for_test import create_base_row

class test_user_post_relationship(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        #'sqlite:///' + os.path.join(basedir, 'test.dat') 
        
        app.config['WTF_CSRF_ENABLED'] = False
        app.testing = True        
        self.app = app.test_client()
        db.create_all()
        create_base_row(db=db)
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    

    def test_user_role(self):
        #test user to role
        micheal  = User.query.filter_by(username='micheal').first()
        self.assertIsInstance(micheal.role, Role)
        self.assertEqual(micheal.role.rolename, role_name.admin)
        #test role to users
        admin_role = Role.query.filter_by(rolename=role_name.admin).first()
        self.assertGreaterEqual(len(admin_role.users), 1)

    def test_post_user(self):
        #the bidirectory relationship of post_user with extra data is many to many
        #i use a association class Post_User
        #the tests must be for bidirectory
        print()
        post_titles = ['first', 'second', 'third', 'fouth', 'fifth']
        posts = [Post(title=title) for title in post_titles]

        #如果先把posts加入，就可能会引发nullable=False错，所在，post不要先加入
        #db.session.add_all(posts)
        #db.session.commit()
        micheal = User.query.filter_by(username='micheal').first()
        kfl = User.query.filter_by(username='kfl').first()
        
        #micheal have three posts, and is the first author of first post
        #请注意这时posts并没有被add到数据库，更没有commit
        m_first = Post_User(is_first_author=True)
        m_first.writer = micheal
        posts[0].writers.append(m_first)

        m_second = Post_User()
        m_second.writer = micheal
        posts[1].writers.append(m_second)

        m_third = Post_User()
        m_third.writer = micheal
        posts[2].writers.append(m_third)
        
        #kfl have five posts, and is the first autor of the 2~5 posts respectively
        kfl_first = Post_User()
        kfl_first.writer = kfl
        posts[0].writers.append(kfl_first)

        kfl_second = Post_User(is_first_author=True)
        kfl_second.writer = kfl
        posts[1].writers.append(kfl_second)

        kfl_third = Post_User(is_first_author=True)
        kfl_third.writer = kfl
        posts[2].writers.append(kfl_third)

        kfl_fouth = Post_User(is_first_author=True)
        kfl_fouth.writer = kfl
        posts[3].writers.append(kfl_fouth)

        kfl_fifth = Post_User(is_first_author=True)
        kfl_fifth.writer = kfl
        posts[4].writers.append(kfl_fifth)

        db.session.add_all(posts)
        db.session.add_all([m_first, m_second, m_third,
                            kfl_first, kfl_second,
                            kfl_third, kfl_fouth, kfl_fifth])
        db.session.commit()
        

        #from user to post
        self.assertEqual(len(micheal.posts), 3)
        micreal_post_association_first_author = []
        for a in micheal.posts:
            if a.is_first_author:
                micreal_post_association_first_author.append(a)
        micheal_post_first_author = [a.post for a in micreal_post_association_first_author]
        self.assertEqual(micheal_post_first_author[0].title, post_titles[0])

        self.assertEqual(len(kfl.posts), 5)
        kfl_post_association_first_author = []
        for a in kfl.posts:
            if a.is_first_author:
                kfl_post_association_first_author.append(a)
        self.assertEqual(len(kfl_post_association_first_author), 4)
        kfl_post_title_first_author = [a.post.title for a in kfl_post_association_first_author]
        self.assertIn(post_titles[1], kfl_post_title_first_author)
        self.assertIn(post_titles[2], kfl_post_title_first_author)
        self.assertIn(post_titles[3], kfl_post_title_first_author)
        self.assertIn(post_titles[4], kfl_post_title_first_author)
        
        #from post to user
        self.assertEqual(len(posts[0].writers), 2)
        self.assertEqual(len(posts[1].writers), 2)
        self.assertEqual(len(posts[2].writers), 2)
        self.assertEqual(len(posts[3].writers), 1)
        self.assertEqual(len(posts[4].writers), 1)

        post_first_first_author_association = []
        for a in posts[0].writers:
            if a.is_first_author:
                post_first_first_author_association.append(a)
        self.assertEqual(len(post_first_first_author_association), 1)
        _micheal = post_first_first_author_association[0].writer
        self.assertEqual(_micheal.username, micheal.username)




if __name__ == '__main__':
    unittest.main()