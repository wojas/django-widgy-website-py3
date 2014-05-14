Example project for using Widgy with Django 1.6 and Python 3.4.

WARNING: Widgy currently does not support Python 3 and many other 
dependencies require bleeding edge and/or patched versions referenced
in requirements.txt here. This gets the project so far as running and
having some working Widgy functionality. Many bugs remain, so do not 
use this for anything other than Widgy development (yet).


Installation instructions
=========================

Requirements: Python 3.4+

Create a venv:

    python3 -m venv ~/widgy-py3
    . ~/widgy-py3/activate

Install dependencies:

    pip install -r requirements.txt
    ./manage.py validate

Initialize the database:

    ./manage.py syncdb
    ./manage.py migrate

Make sure to set the site correctly when asked, because Widgy 
depends on it. Set to 'localhost:8000' for local development.

Run the server:

    ./manage.py runserver


Using PostgreSQL instead of SQLite3
===================================

Optional for PostgreSQL:

    pip install -r dev-requirements.txt

If you want to develop against PostgreSQL using pgrunner, set PGRUNNER 
to True in settings.py.

