def update_post_frontmatter_with_date(post, date):
    """
    Adds (but does not overwrite) `date` and `lastmod` fields to `post`'s
    frontmatter with corresponding `date`.
    """
    if 'date' not in post:
        post['date'] = date

    if 'lastmod' not in post:
        post['lastmod'] = date
