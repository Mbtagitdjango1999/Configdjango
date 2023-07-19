from django.test import TestCase
import random

from sageteam.blog.models import Post
from sageteam.blog.repository.generator import BlogDGL

class TestPostModel(TestCase):
    
    def setUp(self):
        DGL = BlogDGL()
        self.categories = DGL.create_post_categories(10)
        self.posts = DGL.create_posts(self.categories,50)
    
    def test_str_method(self):
        for i in range(50):
            post = self.posts[i]
            actual = str(post)
            expected = post.title
            # self.assertEqual(str(post),post.title) 
            self.assertEqual(actual,expected,
                             msg=f"we expected {expected} but actual {actual} "
                             )
            
    # def test_verbose_name(self):
    #     self.assertEqual(first,second)        