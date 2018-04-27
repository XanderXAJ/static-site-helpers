import datetime


def parse_date(source, matcher_regex, matcher_strftime_format):
    """
    Uses `matcher` to parse `date` string.
    Return a tuple of (True, parsed_date) on match, or (False, None).

    Note: The date format matched by `matcher_regex` and `matcher_strftime_format`
    must be equivalent, otherwise this function will not behave as expected.
    """
    match = matcher_regex.match(source)

    if not match:
        return False, None

    date_string = match.group('date')
    # Parse the date in to datetime to ensure value is written to frontmatter without quotes
    date = datetime.datetime.strptime(date_string, matcher_strftime_format).date()

    return True, date
