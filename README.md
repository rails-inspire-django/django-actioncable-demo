# README

This is demo project for [django-actioncable](https://github.com/rails-inspire-django/django-actioncable)

## How to use

```bash
$ pip install requirements.txt
$ python manage.py migrate
$ python manage.py runserver
```

Open [localhost:8000](http://localhost:8000/), you should be able to see blank page.

Launch Django shell, and run below code:

```python
>>> from actioncable import cable_broadcast
>>> cable_broadcast("chat_1", message="Hello World")
```

The message should appear on the page.
