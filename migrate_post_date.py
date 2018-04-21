#!/usr/bin/env python3

import argparse
import datetime
import logging
import os
import re

import frontmatter

DATE_STRFTIME_FORMAT = '%Y-%m-%d'
DATE_IN_FILENAME_REGEX = r'^(?P<date>\d{4}-\d{2}-\d{2})'
DATE_IN_FILENAME_MATCHER = re.compile(DATE_IN_FILENAME_REGEX)


def generate_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log_level', help='Set logging level', default='WARNING',
                        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'])
    parser.add_argument('paths', nargs='+', metavar='path')
    return parser


def parse_arguments():
    parser = generate_argument_parser()
    return parser.parse_args()


def add_date_to_post_frontmatter(post, date):
    """
    Adds (but does not overwrite) `date` and `lastmod` fields to `post`'s
    frontmatter with corresponding `date`.
    """
    if 'date' not in post:
        post['date'] = date

    if 'lastmod' not in post:
        post['lastmod'] = date


def main():
    args = parse_arguments()

    logging.basicConfig(level=logging.getLevelName(args.log_level))

    for source_file_path in args.paths:
        source_file_name = os.path.basename(source_file_path)
        logging.debug("Operating on: %s", source_file_path)

        # Determine if date is in file name
        match = DATE_IN_FILENAME_MATCHER.match(source_file_name)
        logging.debug('Date in filename: %s', bool(match))

        if not match:
            logging.info('No date found in file name, skipping file: %s', source_file_name)
            continue

        # Extract date from file name
        publish_date_string = match.group('date')
        # Parse the date to ensure value is written to frontmatter without quotes
        publish_date = datetime.datetime.strptime(publish_date_string, DATE_STRFTIME_FORMAT).date()
        logging.debug('Publish date: %s', publish_date)

        # Load post for modification
        post = frontmatter.load(source_file_path)
        logging.debug(post.metadata)

        add_date_to_post_frontmatter(post.metadata, publish_date)
        logging.debug(post.metadata)

        # Write post to same file
        destination_file_path = source_file_path

        frontmatter.dump(post, destination_file_path)

        # TODO: Create file name without date
        # TODO: Check file name without date doesn't already exist
        # TODO: Write to file name without date
        # TODO: Remove old file


main()
