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





class Command(BaseCommand):
    help = (
        'Load Firefox logged in instagram session fool instagram blocking crawler bot'
    )


    def handle(self, *args, **options):

        p = ArgumentParser()
        p.add_argument("-c", "--cookiefile")
        p.add_argument("-f", "--sessionfile")
        args = p.parse_args()
        try:
            import_session(get_cookie_file(), args.sessionfile)
        except (ConnectionException, OperationalError) as e:
            raise SystemExit("Cookie import failed: {}".format(e))

        self.stdout.write(
            self.style.SUCCESS(
                'Vector Database successfully created in {}'.format(
                    os.getenv('CHROMA_PERSIST_DIRECTORY')
                )
                + '\nNow the {} collection is accessible'.format(
                    os.getenv('COLLECTION_NAME')
                )
            )
        )










