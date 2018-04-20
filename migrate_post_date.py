#!/usr/bin/env python3

import argparse
import logging
import os


import frontmatter


def generate_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log_level', help='Set logging level', default='WARNING',
                        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'])
    parser.add_argument('paths', nargs='+', type=argparse.FileType('w'), metavar='path')
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

        # TODO: Determine if date is in file name
        # TODO: Extract date from file name
        # TODO: Load post
        # TODO: Add date to frontmatter
        # TODO: Add lastmod to frontmatter
        # TODO: Create file name without date
        # TODO: Check file name without date doesn't already exist
        # TODO: Write to file name without date
        # TODO: Remove old file


main()
