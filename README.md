# Static Site Helpers

Utilities for helping maintain static sites.

## Usage

```bash
# Migrates dates from the file name to the post's frontmatter
./migrate_post_date.py <post_files>
```

## Development

This project uses `python3`.

This project uses `pipenv` to isolate its environment.  Install it with:

```bash
python3 -m pip install --user pipenv
```

Then install the project's dependencies:

```bash
pipenv install
```

This project uses `unittest` for testing.  To run the tests:

```bash
pipenv run python -m unittest
```

Use `pipenv run` to run commands inside the virtualenv from outside the virtualenv.
Use `pipenv shell` to get a shell inside the virtualenv.

### Writing tests

The tests use Python's built-in `unittest` module.
Add new files prefixed with `test_` to the `tests` directory.
Mirror the structure of the code.

### Running Tests

From the root of the repository, run:

```bash
# Outside the virtualenv
pipenv run python -m unittest
# Inside the virtualenv
python -m unittest
```

To run a specific module, specify it after the command:

```bash
# Outside the virtualenv
pipenv run python -m unittest tests/lib/test_post.py
# Inside the virtualenv
python -m unittest tests/lib/test_post.py
```

[Refer to the unittest docs][unittest-docs] or use the `--help` option to get further help.

[unittest-docs]: https://docs.python.org/3/library/unittest.html
