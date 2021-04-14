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
                    Date = dict_['Date'],
                    Hectare_Squirrel_Number = dict_['Hectare Squirrel Number'],
                    Age = dict_['Age'],
                    Primary_Fur_Color = dict_['Primary Fur Color'],
                    Highlight_Fur_Color = dict_['Highlight Fur Color'],
                    Combination_of_Primary_and_Highlight_Color = dict_['Combination of Primary and Highlight Color'],
                    Color_notes = dict_['Color notes'],
                    Location = dict_['Location'],
                    Above_Ground_Sighter_Measurement = dict_['Above Ground Sighter Measurement'],
                
            
