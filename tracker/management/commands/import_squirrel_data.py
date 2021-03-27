import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from tracker.models import Squirrel

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
                X = dict_['X'],
                Y = dict_['Y'],
                Unique_Squirrel_ID = dict_['Unique Squirrel ID'],
                Hectare = dict_['Hectare'],
                Shift = dict_['Shift'],
                Date = dict_['Date'],
                Hectare_Squirrel_Number = dict_['Hectare Squirrel Number'],
                Age = dict_['Age'],
                Primary_Fur_Color = dict_['Primary Fur Color'],
                Combination_of_Primary_and_Highlight_Color = dict_['Combination of Primary and Highlight Color'],
                Color_notes = dict_['Color notes'],
                Location = dict_['Location'],
                Above_Ground_Sighter_Measurement = dict_['Above Ground Sighter Measurement'],
                Specific_Location = dict_['Specific Location'],
                Running = dict_['Running'],
                Chasing = dict_['Chasing'],
                Climbing = dict_['Climbing'],
                Eating = dict_['Eating'],
                Foraging = dict_['Foraging'],
                Other_Activities = dict_['Other Activities'],
                Kuks = dict_['Kuks'],
                Quaas = dict_['Quaas'],
                Moans = dict_['Moans'],
                Tail_flags = dict_['Tail flags'],
                Tail_twitches = dict_['Tail twitches'],
                Approaches = dict_['Approaches'],
                Indifferent = dict_['Indifferent'],
                Runs_from = dict_['Runs from'],
                Other_Interactions = dict_['Other Interactions'],
                Lat_Long = dict_['Lat/Long']

            ))

        Squirrel.objects.bulk_create(squirrels)
