import unittest

import lib.post as post


class TestPost(unittest.TestCase):
    def test_update_post_frontmatter_with_date_adds_fields(self):
        test_post = {}
        post.update_post_frontmatter_with_date(test_post, '2018-04-16')
        expected = {'date': '2018-04-16', 'lastmod': '2018-04-16'}
        self.assertEqual(test_post, expected)

    def test_update_post_frontmatter_with_date_respects_date_field(self):
        test_post = {'date': '2017-01-01'}
        post.update_post_frontmatter_with_date(test_post, '2018-04-16')
        expected = {'date': '2017-01-01', 'lastmod': '2018-04-16'}
        self.assertEqual(test_post, expected)

    def test_update_post_frontmatter_with_date_respects_lastmod_field(self):
        test_post = {'lastmod': '2017-01-01'}
        post.update_post_frontmatter_with_date(test_post, '2018-04-16')
        expected = {'date': '2018-04-16', 'lastmod': '2017-01-01'}
        self.assertEqual(test_post, expected)
