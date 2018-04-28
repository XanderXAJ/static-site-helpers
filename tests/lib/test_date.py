import datetime
import unittest

import re

import lib.date

YYYY_MM_DD_REGEX = re.compile(r'^(?P<date>\d{4}-\d{2}-\d{2})')
YYYY_MM_DD_STRFTIME = '%Y-%m-%d'


class TestDate(unittest.TestCase):
    def test_parse_date_no_date_raises_exception(self):
        string = 'no-date-in-this-string'

        with self.assertRaises(ValueError):
            lib.date.parse_date(
                string, YYYY_MM_DD_STRFTIME)

    def test_parse_date_matches_date_string(self):
        string = '2018-04-28'

        parsed_date = lib.date.parse_date(
            string, YYYY_MM_DD_STRFTIME)

        self.assertEqual(parsed_date, datetime.date(2018, 4, 28))

    def test_parse_date_with_extra_data_raises_exception(self):
        string = '2018-04-28-post-title'

        with self.assertRaises(ValueError):
            lib.date.parse_date(
                string, YYYY_MM_DD_STRFTIME)
