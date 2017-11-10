import sys
import unittest
sys.path.append('.')

from Blog.views.utility import get_post_views

class test_get_blog_views(unittest.TestCase):
    def test_return_value(self):
        views = get_post_views()
        self.assertEqual(len(views), 4)
        self.assertIsInstance(views[0].title,str)
if __name__ == '__main__':
    unittest.main()
