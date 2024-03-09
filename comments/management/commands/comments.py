from django.core.management.base import BaseCommand
from comments.models import Comment
import instaloader
from os import environ

try:
    from instaloader import ConnectionException, Instaloader
except ModuleNotFoundError:
    raise SystemExit('Instaloader not found.\n  pip install [--user] instaloader')


class Command(BaseCommand):
    help = 'Save all commands from a post '

    def add_arguments(self, parser):
        parser.add_argument('-p', '--post', type=str, help='url of the post')

    @staticmethod
    def get_post_id_from_url(url):
        parsed = url.split('/')
        post_id_index = parsed.index('p') + 1
        return parsed[post_id_index]

    @staticmethod
    def get_answers(comment):
        answers = {}
        for answer in comment.answers:
            answers[answer.owner.username] = answer.text
        return answers

    def handle(self, *args, **options):
        post_url = options['post']
        post_id = self.get_post_id_from_url(post_url)
        print(environ.get('INSTAGRAM_SESSION_USERNAME'))

        try:
            loader = Instaloader()
            loader.load_session_from_file(environ.get('INSTAGRAM_SESSION_USERNAME'))
            post = instaloader.Post.from_shortcode(loader.context, post_id)

            for comment in post.get_comments():
                Comment.objects.create(
                    id=comment.id,
                    username=comment.owner.username,
                    created=comment.created_at_utc,
                    text=comment.text,
                    likes=comment.likes_count,
                    answers=self.get_answers(comment),
                    post_id=post_id,
                )

            self.stdout.write(self.style.SUCCESS('Comments saved successfully.'))
        except ConnectionException as e:
            raise ConnectionError(f'Connection error: {e}')
