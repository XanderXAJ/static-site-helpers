import argparse
import unittest

import lib.arg


class TestException(Exception):
    """Exception to be deliberately thrown as part of tests."""


class RaiseArgumentParser(argparse.ArgumentParser):
    """ArgumentParser that raises an exception instead of exiting the process."""

    def error(self, message):
        raise TestException(message)


class TestArgIntegration(unittest.TestCase):
    def test_no_path_fails(self):
        with self.assertRaises(TestException):
            lib.arg.parse_arguments([], parser=RaiseArgumentParser())

    def test_single_path(self):
        args = lib.arg.parse_arguments(['./file'])

        self.assertEqual(args.paths, ['./file'])

    def test_multiple_paths(self):
        args = lib.arg.parse_arguments(['./file1', './file2'])

        self.assertEqual(args.paths, ['./file1', './file2'])

    def test_log_level_parsed(self):
        args = lib.arg.parse_arguments(['--log_level', 'DEBUG', './file'])

        self.assertEqual(args.log_level, 'DEBUG')

    def test_log_level_parsed_case_insensitive(self):
        args = lib.arg.parse_arguments(['--log_level', 'debug', './file'])

        self.assertEqual(args.log_level, 'DEBUG')
