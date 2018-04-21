import argparse


def generate_argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--log_level', help='Set logging level', default='WARNING',
                        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'])
    parser.add_argument('paths', nargs='+', metavar='path')
    return parser


def parse_arguments():
    parser = generate_argument_parser()
    return parser.parse_args()