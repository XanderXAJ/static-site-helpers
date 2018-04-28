def update_frontmatter_with_date(post, date):
    """
    Mutates (but does not overwrite) `post`'s `date` and `lastmod`
    frontmatter fields with the passed `date`.
    """
    if 'date' not in post:
        post['date'] = date

    if 'lastmod' not in post:
        post['lastmod'] = date
