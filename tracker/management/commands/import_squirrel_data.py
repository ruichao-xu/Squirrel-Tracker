import csv

from django.core.management.base import BaseCommand
from django.utils import timezone
from tracker.models import Squirrel
from datetime import datetime
from django.utils import timezone
import pytz

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('csv_file')
    
    def handle(self, *args, **options):
        with open(options['csv_file']) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
    
        a = []
        squirrels = []
        for dict_ in data:
            if dict_['Unique Squirrel ID'] in a:
                continue
            else:
                squirrels.append(Squirrel(
                    X = dict_['X'],
                    Y = dict_['Y'],
                    Unique_Squirrel_ID = dict_['Unique Squirrel ID'],
                    Hectare = dict_['Hectare'],
                    Shift = dict_['Shift'],
                    Date = dict_['Date'][4:8]+'-'+ dict_['Date'][0:2]+'-'+ dict_['Date'][2:4],
                    Hectare_Squirrel_Number = dict_['Hectare Squirrel Number'],
                    Age = dict_['Age'],
                    Primary_Fur_Color = dict_['Primary Fur Color'],
                    Highlight_Fur_Color = dict_['Highlight Fur Color'],
                    Combination_of_Primary_and_Highlight_Color = dict_['Combination of Primary and Highlight Color'],
                    Color_notes = dict_['Color notes'],
                    Location = dict_['Location'],
                    Above_Ground_Sighter_Measurement = dict_['Above Ground Sighter Measurement'],
                    Specific_Location = dict_['Specific Location'],
                    Running = dict_['Running'].capitalize(),
                    Chasing = dict_['Chasing'].capitalize(),
                    Climbing = dict_['Climbing'].capitalize(),
                    Eating = dict_['Eating'].capitalize(),
                    Foraging = dict_['Foraging'].capitalize(),
                    Other_Activities = dict_['Other Activities'],
                    Kuks = dict_['Kuks'].capitalize(),
                    Quaas = dict_['Quaas'].capitalize(),
                    Moans = dict_['Moans'].capitalize(),
                    Tail_flags = dict_['Tail flags'].capitalize(),
                    Tail_twitches = dict_['Tail twitches'].capitalize(),
                    Approaches = dict_['Approaches'].capitalize(),
                    Indifferent = dict_['Indifferent'].capitalize(),
                    Runs_from = dict_['Runs from'].capitalize(),
                    Other_Interactions = dict_['Other Interactions'],
                    Lat_Long = dict_['Lat/Long']

                ))
                a.append(dict_['Unique Squirrel ID'])



        Squirrel.objects.bulk_create(squirrels)
            
