import os
import sys
sys.path.append('.')
import unittest
from config import basedir
from Blog import db, app
from Blog.models import Role, role_name, Permission, permission_name, User, Post, Post_User

class test_user_post_relationship(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
        #'sqlite:///' + os.path.join(basedir, 'test.dat') 
        
        app.config['WTF_CSRF_ENABLED'] = False
        app.testing = True        
        self.app = app.test_client()
        db.create_all()
        self._create_base_row()
    def tearDown(self):
        db.session.remove()
        db.drop_all()
    def _create_base_row(self):    
        #roles
        admin_role = Role(rolename=role_name.admin)
        anonymous_role = Role(rolename=role_name.anonymous)
        common_role = Role(rolename=role_name.common)
        moderator_role = Role(rolename=role_name.moderator)

        #permission
        follow_permission = Permission(permission=permission_name.follow)
        comment_permission = Permission(permission=permission_name.comment)
        writing_permission = Permission(permission=permission_name.writing)
        moderate_comment_permission = Permission(permission=permission_name.moderate_comment)
        admin_permission = Permission(permission=permission_name.admin)

        #admin_role Authentication
        admin_role.permissions.append(admin_permission)
        admin_role.permissions.append(follow_permission)
        admin_role.permissions.append(comment_permission)
        admin_role.permissions.append(writing_permission)
        admin_role.permissions.append(moderate_comment_permission)

        #moderator_role Authentication
        moderator_role.permissions.append(follow_permission)
        moderator_role.permissions.append(writing_permission)
        moderator_role.permissions.append(comment_permission)
        moderator_role.permissions.append(moderate_comment_permission)

        #common_role Authentication
        common_role.permissions.append(follow_permission)
        common_role.permissions.append(writing_permission)
        common_role.permissions.append(comment_permission)

        #There are no Authentications for anonymous_role

        db.session.add(admin_role)
        db.session.add(moderator_role)
        db.session.add(common_role)
        db.session.add(anonymous_role)

        db.session.add(admin_permission)
        db.session.add(moderate_comment_permission)
        db.session.add(follow_permission)
        db.session.add(comment_permission)
        db.session.add(writing_permission)


        micheal = User(username='micheal', 
                        email='micheal@163.com', 
                        password='111111',
                        role=admin_role)

        lrq = User(username='lrq',
                    email='lrq@163.com',
                    password='111111',
                    role=admin_role
                )

        kfl = User(username='kfl',
                    email='kfl@163.com',
                    password='111111',
                    role=admin_role
                )

        zyq = User(username='zyq',
                    email='zyq@163.com',
                    password='111111',
                    role=admin_role
        )

        zl = User(username='zl',
                   email='zl@163.com',
                   password='111111',
                   role=moderator_role
        )

        ny = User(username='ny',
                   email='ny@163.com',
                   password='111111',
                   role=moderator_role
        )

        lzj = User(username='lzj',
                    email='lzj@163.com',
                    password='111111',
                    role=common_role
        )
        
        db.session.add_all([micheal, lrq, zyq, 
                            kfl, zl, ny, lzj])
        db.session.commit()

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