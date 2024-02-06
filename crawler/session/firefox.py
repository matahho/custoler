import os
from glob import glob
from os.path import expanduser
from platform import system
from sqlite3 import OperationalError, connect

try:
    from instaloader import ConnectionException, Instaloader
except ModuleNotFoundError:
    raise SystemExit("Instaloader not found.\n  pip install [--user] instaloader")


def get_cookie_file():
    default_cookie_file = {
        "Windows": os.getenv('WINDOWS_FIREFOX_SESSIONS'),
        "Darwin": os.getenv('DARWIN_FIREFOX_SESSIONS'),
    }.get(system(), os.getenv('DEFAULT_FIREFOX_SESSIONS'))
    cookie_files = glob(expanduser(default_cookie_file))
    if not cookie_files:
        raise SystemExit("No Firefox cookies.sqlite file found. Use -c COOKIEFILE.")
    return cookie_files[0]


def import_session(cookie_file, session_file):
    print("Using cookies from {}.".format(cookie_file))
    conn = connect(f"file:{cookie_file}?immutable=1", uri=True)
    try:
        cookie_data = conn.execute(
            "SELECT name, value FROM moz_cookies WHERE baseDomain='instagram.com'"
        )
    except OperationalError:
        cookie_data = conn.execute(
            "SELECT name, value FROM moz_cookies WHERE host LIKE '%instagram.com'"
        )
    instaloader = Instaloader(max_connection_attempts=1)
    instaloader.context._session.cookies.update(cookie_data)
    username = instaloader.test_login()
    if not username:
        raise SystemExit("Not logged in. Are you logged in successfully in Firefox?")
    print("Imported session cookie for {}.".format(username))
    instaloader.context.username = username
    instaloader.save_session_to_file(session_file)


