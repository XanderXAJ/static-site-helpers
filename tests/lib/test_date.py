import unittest
import datetime

import re

import lib.date

YYYY_MM_DD_REGEX = re.compile(r'^(?P<date>\d{4}-\d{2}-\d{2})')
YYYY_MM_DD_STRFTIME = '%Y-%m-%d'


class TestDate(unittest.TestCase):
    def test_parse_date_does_not_match_date_less_string(self):
        string = 'no-date-in-this-string'

        matched, parsed_date = lib.date.parse_date(
            string, YYYY_MM_DD_REGEX, YYYY_MM_DD_STRFTIME)

        self.assertFalse(matched)
        self.assertIsNone(parsed_date)

    def test_parse_date_matches_date_string(self):
        string = '2018-04-28'

        matched, parsed_date = lib.date.parse_date(
            string, YYYY_MM_DD_REGEX, YYYY_MM_DD_STRFTIME)

        self.assertTrue(matched)
        self.assertEqual(parsed_date, datetime.date(2018, 4, 28))

    def test_parse_date_matches_date_substring(self):
        string = '2018-04-28-post-title'

        matched, parsed_date = lib.date.parse_date(
            string, YYYY_MM_DD_REGEX, YYYY_MM_DD_STRFTIME)

        self.assertTrue(matched)
        self.assertEqual(parsed_date, datetime.date(2018, 4, 28))
