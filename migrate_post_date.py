#!/usr/bin/env python3

import argparse
import logging
import os
import re

DATE_IN_FILENAME_REGEX = r'^(?P<date>\d{4}-\d{2}-\d{2})'
DATE_IN_FILENAME_MATCHER = re.compile(DATE_IN_FILENAME_REGEX)


def generate_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log_level', help='Set logging level', default='WARNING',
                        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'])
    parser.add_argument('paths', nargs='+', type=argparse.FileType('r+'), metavar='path')
    return parser


def parse_arguments():
    parser = generate_argument_parser()
    return parser.parse_args()


def main():
    args = parse_arguments()

    logging.basicConfig(level=logging.getLevelName(args.log_level))

    for file in args.paths:
        file_name = os.path.basename(file.name)
        logging.debug("Operating on: %s", file_name)

        # Determine if date is in file name
        match = DATE_IN_FILENAME_MATCHER.match(file_name)
        logging.debug('Date in filename: %s', bool(match))

        if not match:
            logging.info('No date found in file name, skipping file: %s', file_name)
            continue

        # Extract date from file name
        publish_date = match.group('date')
        logging.debug('Publish date: %s', publish_date)

        # TODO: Load post
        # TODO: Add date to frontmatter
        # TODO: Add lastmod to frontmatter
        # TODO: Create file name without date
        # TODO: Check file name without date doesn't already exist
        # TODO: Write to file name without date
        # TODO: Remove old file


main()
