Django-Fieldbook-Demo  [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)
=========

Django-Fieldbook-Demo is a demo of [django-fieldbook](https://github.com/bsab/django-fieldbook.git) package that shows how Django interacts with the Fieldbook.com API.

Check out the [Live Demo](https://django-fieldbook.herokuapp.com).

Usage
----

To start you need an API key, to get it see [the getting started guide](https://github.com/fieldbook/api-docs/blob/master/quick-start.md).

In the registration form:

1. Set the password field usign the API secret; 

2. Set the username field using the API key (ex. key-1).

3. Each book has a base URL displayed in the API management panel, like https://api.fieldbook.com/v1/5643be3316c813030039032e.
In the Fieldbook ID field set the last value of the url, in the example is: 5643be3316c813030039032e

4. Fill out the remaining fields with your personal informations.

At complete, use the login form to access to your book'sheets.

Install on local
-----

If you prefer to run it directly on your local machine, I suggest using
[virtualenv](https://virtualenv.pypa.io/en/stable/) (maybe have a look at
[virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/stable/)),
anyway here the commands you have to enter:

    pip install -r requirements.txt

Then:

    python manage.py migrate auth
    python manage.py migrate

## To Do

The add and update methods related to apis haven't been included, otherwise the current API is fully implemented (at least as of June 2017).

## Author

[Sabatino Severino](https://about.me/the_sab), @bsab

## License

Django-Fieldbook-Demo is available under the MIT license. See the LICENSE file for more info.

Notes
------

Feel free to fork and send a pull request.
