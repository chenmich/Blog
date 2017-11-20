import os
import sys
sys.path.append('.')

import tempfile
import unittest

import Blog
from  Blog.views.user_register import _create_register_user
from Blog.models.user.role import Role, role_name
from Blog.models.user.user import User


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        Blog.app.testing = True
        self.app = Blog.app.test_client()
        

    def tearDown(self):
        pass
    
    def register_test(self):
        pass

    def test_create_user(self):
        common_role = Role.query.filter_by(rolename=role_name.common).first()
        self.assertEqual(common_role.id, 3)
        email='张三@163.com'
        username='张三'
        password='111111'
        user = _create_register_user(
            username=username,
            email=email,
            password=password,
            role=common_role)
        self.assertIsInstance(user, User)
        self.assertEqual(user.role.id, common_role.id)
        
if __name__ == '__main__':
    unittest.main()
