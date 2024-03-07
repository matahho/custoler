import os
from django.core.management.base import BaseCommand
import pathlib
from argparse import ArgumentParser
from crawler.session.firefox import get_cookie_file , import_session
from sqlite3 import OperationalError
try:
    from instaloader import ConnectionException
except ModuleNotFoundError:
    raise SystemExit("Instaloader not found.\n  pip install [--user] instaloader")



'''
    Referenced in here : https://instaloader.github.io/troubleshooting.html
    loading session from firefox database to instaloader 

'''

class Command(BaseCommand):
    help = (
        'Load Firefox logged in instagram session fool instagram blocking crawler bot'
    )


    def handle(self, *args, **options):
        session_file = None
        try:
            import_session(cookie_file=get_cookie_file(), session_file=session_file)
        except (ConnectionException, OperationalError) as e:
            raise SystemExit("Cookie import failed: {}".format(e))

        self.stdout.write(
            self.style.SUCCESS(
                'session successfully loaded and saved in instaloader env vars!'
            )
        )










