Closeness Project
=================

Platform to serve content near to the user, using geolocation information. Made with Django and Python 3 with :heart:

.. image:: https://travis-ci.org/theroomofcode/closeness.svg?branch=master
    :target: https://travis-ci.org/theroomofcode/closeness

Environment variables
---------------------

For local development:

.. code-block:: bash

    export DATABASE_URL="postgis://postgres:potato@localhost:5432/closeness"
    export DJANGO_SETTINGS_MODULE="config.settings.local"

Import countries
----------------

To import countries as Places, just run this command:

.. code-block:: bash

    $ ./manage.py import_countries

Run tests
---------

.. code-block:: bash

    $ py.test




