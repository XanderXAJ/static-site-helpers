#!/usr/bin/env python3

import logging

import frontmatter
import os
import re

import lib.arg
import lib.date
import lib.post

# Note: The regex and strftime expressions must match the same date format.
DATE_STRFTIME_FORMAT = '%Y-%m-%d'
DATE_IN_FILENAME_REGEX = r'^(?P<date>\d{4}-\d{2}-\d{2})-(?P<title>.*)$'
DATE_IN_FILENAME_MATCHER = re.compile(DATE_IN_FILENAME_REGEX)


def main():
    args = lib.arg.parse_arguments()

    logging.basicConfig(level=logging.getLevelName(args.log_level))

    for source_file_path in args.paths:
        source_file_name = os.path.basename(source_file_path)
        logging.debug("Operating on: %s", source_file_path)

        match = re.fullmatch(DATE_IN_FILENAME_REGEX, source_file_name)
        if not match:
            logging.info('File name did not match regex %s, skipping file: %s',
                         DATE_IN_FILENAME_REGEX, source_file_name)
            continue

        tokens = match.groupdict()
        if not ('date' in tokens and 'title' in tokens):
            logging.info('Did not match date and title, skipping %s', source_file_path)
            continue
        logging.debug('Matched tokens: %s', tokens)

        publish_date = lib.date.parse_date(tokens['date'], DATE_STRFTIME_FORMAT)
        logging.debug('Publish date: %s', publish_date)

        # Load post for modification
        post = frontmatter.load(source_file_path)
        logging.debug("Frontmatter before: %s", post.metadata)

        lib.post.update_frontmatter_with_date(post.metadata, publish_date)
        logging.debug("Frontmatter after: %s", post.metadata)

        # Write post to same file
        destination_file_path = source_file_path

        frontmatter.dump(post, destination_file_path)

        # TODO: Create file name without date
        # TODO: Check file name without date doesn't already exist
        # TODO: Write to file name without date
        # TODO: Remove old file


main()
