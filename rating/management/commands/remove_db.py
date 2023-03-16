from django.core.management.base import BaseCommand
from rating.models import Rating

class Command(BaseCommand):
    help = 'remove addede entires from Rating model'

    def handle(self, *args, **options):
        obj = Rating.objects.filter(text='created from command line')
        obj.delete()