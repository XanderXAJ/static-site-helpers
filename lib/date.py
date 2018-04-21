import datetime


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