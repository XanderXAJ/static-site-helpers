import datetime
import typing


def parse_date(source: str, matcher_regex: typing.Pattern, matcher_strftime_format: str)\
        -> typing.Tuple[bool, typing.Union[type(None), datetime.date]]:
    """
    Uses `matcher` to parse `date` string.
    Return a tuple of (True, parsed_date) on match, or (False, None).

    The `matcher_regex` must supply a date group (e.g. `(?P<date>...)`).

    Note: The date format matched by `matcher_regex` and `matcher_strftime_format`
    must be equivalent, otherwise this function will not behave as expected.
    """
    match = matcher_regex.match(source)

    if not match:
        return False, None

    date_string = match.group('date')
    # Parse the date in to datetime to ensure value is written to frontmatter without quotes
    parsed_date = datetime.datetime.strptime(date_string, matcher_strftime_format).date()

    return True, parsed_date
