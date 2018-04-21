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


def update_post_frontmatter_with_date(post, date):
    """
    Adds (but does not overwrite) `date` and `lastmod` fields to `post`'s
    frontmatter with corresponding `date`.
    """
    if 'date' not in post:
        post['date'] = date

    if 'lastmod' not in post:
        post['lastmod'] = date


def parse_date(source, matcher, strftime_format):
    """
    Uses `matcher` to parse `date` string.
    Return a tuple of (match_occurred, parsed_date or None).
    """
    match = matcher.match(source)

    if not match:
        return False, None

    date_string = match.group('date')
    # Parse the date in to datetime to ensure value is written to frontmatter without quotes
    date = datetime.datetime.strptime(date_string, strftime_format).date()

    return True, date


def main():
    args = parse_arguments()

    logging.basicConfig(level=logging.getLevelName(args.log_level))

    for source_file_path in args.paths:
        source_file_name = os.path.basename(source_file_path)
        logging.debug("Operating on: %s", source_file_path)

        match, publish_date = parse_date(source_file_name, DATE_IN_FILENAME_MATCHER, DATE_STRFTIME_FORMAT)
        logging.debug('Date in filename: %s', bool(match))
        logging.debug('Publish date: %s', publish_date)

        if not match:
            logging.info('No date found in file name, skipping file: %s', source_file_name)
            continue

        # Load post for modification
        post = frontmatter.load(source_file_path)
        logging.debug("Frontmatter before: %s", post.metadata)

        update_post_frontmatter_with_date(post.metadata, publish_date)
        logging.debug("Frontmatter after: %s", post.metadata)

        # Write post to same file
        destination_file_path = source_file_path

        frontmatter.dump(post, destination_file_path)

        # TODO: Create file name without date
        # TODO: Check file name without date doesn't already exist
        # TODO: Write to file name without date
        # TODO: Remove old file


main()
