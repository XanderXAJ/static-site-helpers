import argparse


def generate_argument_parser(parser=None):
    if parser is None:
        parser = argparse.ArgumentParser()
    parser.add_argument('--log_level', help='Set logging level', default='WARNING',
                        type=str.upper,
                        choices=['CRITICAL', 'ERROR', 'WARNING', 'INFO', 'DEBUG'])
    parser.add_argument('paths', nargs='+', metavar='path')
    return parser


def parse_arguments(args=None, parser=None):
    parser = generate_argument_parser(parser=parser)
    return parser.parse_args(args)
