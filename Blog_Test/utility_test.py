import unittest
from Blog.views.utility import get_post_views


class test_get_blog_views(unittest.TestCase):
    def test_return_value(self):
        views = get_post_views()
        self.assertEqual(views.count, 4)

if __name__ == '__main__':
    unittest.main()