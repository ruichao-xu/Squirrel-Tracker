import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from adopt.models import Squirrel


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file')

    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

        squirrels = []
        for dict_ in data:
            squirrels.append(Squirrel(
                name=dict_['name'],
                birth_date=None,  # Do date conversion
                vaccinated=dict_['vaccinated'].lower() == 'true'
            ))

        Squirrel.objects.bulk_create(squirrels)
