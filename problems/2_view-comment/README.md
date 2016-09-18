# Problem

The user wants a responsive web interface to see a particular comment from the
mySidewalk engagement comments API. Load the comment with ID 100
(https://mysidewalk.com/api/engagement/v1/comments/100.json) from the API,
redirect the window’s location to a path that represents a human friendly
portion of the comment, and display the comment in a device response and
visually pleasing manner.

# Usage

`docker-compose build`
`docker-compose up`

Or, to run on the host, create a virtual environment and install via pip the
packages in requirements.txt.

Then, run: `python manage.py runserver" and view in a browser at `localhost:8000`.

## Run tests

`docker-compose exec app bash -c "python manage.py test"`

Or locally:

`python manage.py test`

# Issues

Tests fail for some reason when executed on running Docker container, perhaps
related to binary stream issue (as indicated by \b character that doesn't appear
when tests are run on the host directly).
