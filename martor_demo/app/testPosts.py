from app.models import Post
from django.test import TestCase


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="My Title", description="Blurb", wiki="Post Body")
        self.assertEqual(post.title, "My Title")
        self.assertEqual(post.description, "Blurb")
        self.assertEqual(post.wiki, "Post Body")