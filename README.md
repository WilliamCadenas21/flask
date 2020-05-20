# Flask project

## Set up the python virtual environment

1 Install venv:

    $ apt-get install python3-venv

2 Create virtualenv

    $ python3 -m venv venv

3 Activate the venv

    $ . venv/bin/activate

## Install manually flask and some others dependencies

1 Install flask manually

    $ pip install Flask

2 or install directly all requirements declared in requirements.txt

    $ pip install -r requirements.txt

## For run flask there are some options:

1 one by one

    $ export FLASK_APP=main.py
    $ export FLASK_ENV=development
    $ flask run

1 one line

    $ FLASK_APP=main.py FLASK_ENV=development flask run

3 for more options

    $ flask run --help