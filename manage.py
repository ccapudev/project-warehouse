#!/usr/bin/env python
import os
import sys
import environ

if __name__ == '__main__':
    root = environ.Path(__file__) - 1
    env = environ.Env(
        DJANGO_SETTINGS_MODULE=(str, 'webapp.settings'),
    )
    environ.Env.read_env(os.path.join(root(), 'webapp/.env'))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', env('DJANGO_SETTINGS_MODULE'))
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
