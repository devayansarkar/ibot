#!/usr/bin/env python
"""importing modules requried"""
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        try:
            import django
            #trying to import django to check everything is fine
        except ImportError:
            raise ImportError(
                "--Unable to import django--"
            )
        raise
    execute_from_command_line(sys.argv)
