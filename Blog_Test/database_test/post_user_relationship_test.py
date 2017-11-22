import os
import sys
sys.path.append('.')

import unittest


from config import basedir
from Blog import db, app
from Blog.models.post.post import Post
from Blog.models.user.user import User
from Blog.models.user.role import Role, role_name, Permission, permission_name


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
    
    def test_role_user_relationship(self):
        admin_role = Role.query.filter_by(rolename=role_name.admin).first()
        self.assertEqual(len(admin_role.users), 4)
        micheal = User.query.filter_by(username='micheal').first()
        self.assertEqual(micheal.role.rolename, role_name.admin)

    def test_role_permission_relationship(self):
        common_role = Role.query.filter_by(rolename=role_name.common).first()
        self.assertEqual(len(common_role.permissions), 3)
        self.assertIsInstance(common_role.permissions[0], Permission)

    def test_otherwriters_post_relationship(self):
        micheal = User.query.filter_by(username='micheal').first()
        lrq = User.query.filter_by(username='lrq').first()
        kfl = User.query.filter_by(username='kfl').first()
        zyq = User.query.filter_by(username='zyq').first()
        zl = User.query.filter_by(username='zl').first()
        ny = User.query.filter_by(username='ny').first()
        lzj = User.query.filter_by(username='lzj').first()

        posts = []
        post_titles = ['the first post', 'the second post', 'the third post',
                        'the fouth post', 'the fifth post', 'the sixth post',
                        'the seventh post', 'the eigth post', 'the nineth post', 
                        'the tenth post'] 
        
        for i in range(0, 9):
            post = Post(title=post_titles[i])
            posts.append(post)     

        posts[0].other_writers.append(micheal)
        posts[0].other_writers.append(zyq)
        posts[1].other_writers.append(lrq)
        posts[1].other_writers.append(micheal)

        db.session.add_all(posts)
        db.session.commit()

        self.assertEqual(len(posts[0].other_writers), 2)
        self.assertEqual(len(micheal.posts), 2)

        


if __name__ == '__main__':
    unittest.main()