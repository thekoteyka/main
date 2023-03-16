from django.core.management.base import BaseCommand

from rating.models import Rating

class Command(BaseCommand):
    help = 'adding some entires to Rating model'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        from random import randint
        count = options.get('count', 1)
        for i in range(count):
            r = Rating(name=i, text='created from command line', rate=randint(1, 5))
            r.save()