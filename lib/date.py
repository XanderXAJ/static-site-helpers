import datetime
import typing


def parse_date(date_string: str, matcher_strftime_format: str) -> datetime.date:
    """
    Uses `matcher` to parse `date` string.
    Return a tuple of (True, parsed_date) on match, or (False, None).

    The `matcher_regex` must supply a date group (e.g. `(?P<date>...)`).

    Note: The date format matched by `matcher_regex` and `matcher_strftime_format`
    must be equivalent, otherwise this function will not behave as expected.
    """
    # Parse the date in to datetime to ensure value is written to frontmatter without quotes
    parsed_date = datetime.datetime.strptime(date_string, matcher_strftime_format).date()

    return parsed_date
